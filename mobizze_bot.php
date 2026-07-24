#!/usr/bin/php -q
<?php

/**
 * Mobizze Bot v1.0 (AI Agent for Sales Qualification & Automation)
 * - Integração: OpenAI GPT-4o
 * - Objective: Qualify leads for custom AI systems, virtual employees, and automations.
 * - Extração de Dados: Sector, Pain Points, Desired Integrations, Company Name, Website.
 * - HubSpot Sync: Supported and adapted for Mobizze B2B Leads.
 */

// --- BLOQUEIO DE CONCURRÊNCIA --- //
$lock_file = __DIR__ . '/mobizze_bot.lock';
$f_lock = fopen($lock_file, 'w');
if (!flock($f_lock, LOCK_EX | LOCK_NB)) {
    die("Bot já em execução. A sair.\n");
}

// --- LOAD .ENV VARIABLES NATIVAMENTE --- //
$env_file = __DIR__ . '/.env';
if (file_exists($env_file)) {
    $lines = file($env_file, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    foreach ($lines as $line) {
        $line = trim($line);
        if (empty($line) || strpos($line, '#') === 0) continue;
        if (strpos($line, '=') !== false) {
            list($name, $value) = explode('=', $line, 2);
            $name = trim($name);
            $value = trim($value, " \t\n\r\0\x0B\"'");
            putenv(sprintf('%s=%s', $name, $value));
            $_ENV[$name] = $value;
        }
    }
}

// --- CONFIGURAÇÕES --- //
$TEST_MODE = true; 
$BOT_START_TIME = strtotime('2026-07-24 00:00:00'); 

if ($TEST_MODE) {
    ini_set('display_errors', 1);
    error_reporting(E_ALL);
    echo "<h2>--- MODO MOBIZZE BOT v1.0 ---</h2><br>";
}

set_time_limit(300); 

// Configurações do servidor de Email da Mobizze
// Altere 'mail.mobizze.com' para o servidor correto se necessário
$server_string    = '{mail.mobizze.com:993/imap/ssl/novalidate-cert}';
$email_inbox      = $server_string . 'INBOX';
$email_sent       = $server_string . 'INBOX.Sent'; 

$email_user       = $_ENV['EMAIL_USER'] ?? getenv('EMAIL_USER') ?: 'info@mobizze.com';
$email_pass       = $_ENV['EMAIL_PASS'] ?? getenv('EMAIL_PASS'); 
$openai_api_key   = $_ENV['OPENAI_API_KEY'] ?? getenv('OPENAI_API_KEY'); 
$admin_email      = $_ENV['ADMIN_EMAIL'] ?? getenv('ADMIN_EMAIL') ?: 'info@mobizze.com';

// --- HUBSPOT CONFIGURATION --- //
$hubspot_client_id     = $_ENV['HUBSPOT_CLIENT_ID'] ?? getenv('HUBSPOT_CLIENT_ID');
$hubspot_client_secret = $_ENV['HUBSPOT_CLIENT_SECRET'] ?? getenv('HUBSPOT_CLIENT_SECRET');
$hubspot_initial_refresh_token = $_ENV['HUBSPOT_REFRESH_TOKEN'] ?? getenv('HUBSPOT_REFRESH_TOKEN'); 
$hubspot_token_file    = __DIR__ . '/hubspot_tokens.json';
$hubspot_owner_id = $_ENV['HUBSPOT_OWNER_ID'] ?? getenv('HUBSPOT_OWNER_ID'); 

// Diretorios
$base_dir = __DIR__ . '/conversations_data';
$json_dir = $base_dir . '/json';
$files_dir = $base_dir . '/attachments';

if (!file_exists($json_dir)) @mkdir($json_dir, 0777, true);
if (!file_exists($files_dir)) @mkdir($files_dir, 0777, true);

// Proteção da pasta de anexos
$htaccess_path = $files_dir . '/.htaccess';
if (!file_exists($htaccess_path)) {
    $htaccess_content = "<FilesMatch \"\\.(php|php[0-9]|phtml|pl|py|jsp|asp|htm|html|shtml|sh|cgi|phar)$\">\nOrder allow,deny\nDeny from all\n</FilesMatch>\nOptions -Indexes -ExecCGI\nphp_flag engine off\nRemoveHandler .php .phtml .php3 .php4 .php5 .php8";
    @file_put_contents($htaccess_path, $htaccess_content);
}

function write_log($text) {
    global $TEST_MODE;
    $date = date('Y-m-d H:i:s');
    @file_put_contents('bot_log.txt', "[$date] $text" . PHP_EOL, FILE_APPEND);
    if ($TEST_MODE) { echo "$text <br>"; flush(); }
}

write_log("--- Iniciando verificação Mobizze Bot v1.0 ---");

if (!$email_pass || !$openai_api_key) {
    write_log("ERRO: Faltam credenciais (EMAIL_PASS ou OPENAI_API_KEY) no ficheiro .env");
    die("Configurar credenciais no .env\n");
}

$inbox = imap_open($email_inbox, $email_user, $email_pass);
if (!$inbox) {
    write_log("ERRO FATAL: Falha conexão IMAP. " . imap_last_error());
    die();
}

$emails_uids = imap_search($inbox, 'UNANSWERED', SE_UID);

if ($emails_uids) {
    rsort($emails_uids); 
    
    $max_analises_por_cron = 15;
    $analisados = 0;

    foreach ($emails_uids as $email_uid) {
        $analisados++;
        if ($analisados > $max_analises_por_cron) {
            write_log("LIMITE DE SEGURANÇA atingido.");
            break;
        }
        
        $overview = imap_fetch_overview($inbox, $email_uid, FT_UID);
        if (!$overview) continue;

        $subject = imap_utf8(isset($overview[0]->subject) ? $overview[0]->subject : '(Sem Assunto)');
        
        $auto_reply_keywords = ['automatic reply', 'out of office', 'ausência temporária', 'resposta automática', 'autoreply', 'oof:', 'vacation reply', 'auto-reply','thank you for your email'];
        $is_auto_reply = false;
        foreach ($auto_reply_keywords as $keyword) {
            if (stripos($subject, $keyword) !== false) {
                $is_auto_reply = true;
                break;
            }
        }
        if ($is_auto_reply) {
            imap_setflag_full($inbox, $email_uid, "\\Answered", ST_UID);
            write_log("IGNORADO: Resposta automática detetada no assunto: $subject");
            continue; 
        }
        
        $from_header = imap_utf8(isset($overview[0]->from) ? $overview[0]->from : '');
        $message_id = isset($overview[0]->message_id) ? $overview[0]->message_id : null;
        $email_date = isset($overview[0]->udate) ? $overview[0]->udate : 0;

        if ($email_date < $BOT_START_TIME) continue; 

        preg_match('/(.*)<(.*)>/', $from_header, $matches);
        $client_email = isset($matches[2]) ? trim($matches[2]) : str_replace(['<', '>'], '', $from_header);
        $client_name = isset($matches[1]) ? trim($matches[1], " \"'") : "Cliente";
        
        if (strpos(strtolower($client_email), strtolower($email_user)) !== false) {
            imap_setflag_full($inbox, $email_uid, "\\Answered", ST_UID);
            continue;
        }

        $hubspot_extracted = false;
        $user_message_raw = get_email_body($inbox, $email_uid);

        $hard_blacklist = ['noreply@notifications.hubspot.com', 'jobs-listings@linkedin.com', 'invitations@linkedin.com', 'notification@service.tiktok.com'];
        if (!$hubspot_extracted && in_array(strtolower($client_email), $hard_blacklist)) {
            imap_setflag_full($inbox, $email_uid, "\\Answered", ST_UID);
            continue;
        }

        $client_hash = md5($client_email); 
        $json_file = $json_dir . "/$client_hash.json";
        $client_files_folder = $files_dir . "/$client_hash";
        $is_old_client = file_exists($json_file);

        $address_block = ['hubspot', 'noreply', 'no-reply', 'marketing', 'mailer-daemon', 'newsletter', 'email@', 'info@'];
        foreach ($address_block as $term) {
            if (!$hubspot_extracted && stripos($client_email, $term) !== false && $client_email !== $email_user) {
                // Ignorar se for um email genérico de sistema
                if (stripos($client_email, 'info@') !== false && stripos($client_email, 'mobizze.com') === false) {
                    // Se for um cliente genuíno que usa info@, aceitamos. Mas bloqueamos noreply etc.
                    if (in_array($term, ['noreply', 'no-reply', 'mailer-daemon'])) {
                        imap_setflag_full($inbox, $email_uid, "\\Answered", ST_UID); 
                        continue 2;
                    }
                }
            }
        }

        $user_message_text = clean_reply_text_simple($user_message_raw);
        $full_context = strtolower($subject . " " . $user_message_text);

        if (!$is_old_client) {
            $blacklist = [
                'crypto', 'bitcoin', 'investment', 'casino', 'lottery', 'winner', 'prize', 'viagra', 'weight loss',
                'lead generation', 'backlinks', 'traffic', 'seo boost', 'domain registration', 'renew your domain'
            ];
            foreach ($blacklist as $bad_word) {
                if (stripos($full_context, $bad_word) !== false) {
                    imap_setflag_full($inbox, $email_uid, "\\Answered", ST_UID); 
                    continue 2;
                }
            }
        }

        write_log("PROCESSANDO UID $email_uid: $client_name ($client_email)");

        $conversation_data = [
            'messages' => [], 
            'client_name' => $client_name, 
            'language' => '', 
            'report_sent' => false, 
            'history_archive' => [],
            'project_details' => [
                'sector' => 'Pending',
                'pain_point' => 'Pending',
                'integrations' => 'Pending',
                'company_name' => 'Not Specified',
                'company_website' => 'Not Specified',
                'phone' => ''
            ],
            'last_processed_uid' => 0,
            'retry_count' => 0
        ];
        if ($is_old_client) {
            $json_content = @file_get_contents($json_file);
            if ($json_content) {
                $decoded = json_decode($json_content, true);
                if (is_array($decoded)) {
                    $conversation_data = array_merge($conversation_data, $decoded);
                }
            }
        }

        if (!isset($conversation_data['last_processed_uid'])) $conversation_data['last_processed_uid'] = 0;
        if (!isset($conversation_data['retry_count'])) $conversation_data['retry_count'] = 0;

        if ($conversation_data['last_processed_uid'] == $email_uid) {
            $conversation_data['retry_count']++;
        } else {
            $conversation_data['last_processed_uid'] = $email_uid;
            $conversation_data['retry_count'] = 1;
        }

        @file_put_contents($json_file, json_encode($conversation_data, JSON_PRETTY_PRINT));

        if ($conversation_data['retry_count'] > 3) {
            write_log("⚠️ LIMITE DE TENTATIVAS para UID $email_uid. Saltando.");
            imap_setflag_full($inbox, $email_uid, "\\Answered", ST_UID);
            $conversation_data['retry_count'] = 0;
            @file_put_contents($json_file, json_encode($conversation_data, JSON_PRETTY_PRINT));
            continue; 
        }

        $detected_lang = detect_language_better($user_message_text);
        if (empty($conversation_data['language'])) {
            $conversation_data['language'] = $detected_lang ?? 'Portuguese'; 
        } else {
            if ($detected_lang !== null && $detected_lang !== $conversation_data['language']) {
                $conversation_data['language'] = $detected_lang;
            }
        }
        $locked_language = $conversation_data['language'];

        $internal_message = $user_message_text;

        if (empty(trim($internal_message))) continue;

        if (isset($conversation_data['report_sent']) && $conversation_data['report_sent'] === true) {
            $conversation_data['history_archive'][] = $conversation_data['messages'];
            $conversation_data['messages'] = [];
            $conversation_data['report_sent'] = false;
            $conversation_data['project_details']['sector'] = 'Pending';
        }

        $html_signature = get_signature_html();

        $conversation_data['messages'][] = ['content' => $internal_message, 'role' => 'user'];
        
        $hub_contact_id = null; 
        try {
            $hub_contact_id = sync_hubspot_contact($client_email, $client_name, $conversation_data, 'lead');
            if ($hub_contact_id) {
                log_hubspot_email($hub_contact_id, $subject, $internal_message, 'INCOMING', $client_email, $client_name);
            }
        } catch (Exception $e) {
            write_log("HUBSPOT ERROR: " . $e->getMessage());
        }

        // --- CHAMADA AI (OPENAI GPT-4o) --- //
        $system_prompt = <<<'EOD'
You are the AI Assistant for "Mobizze", a B2B AI Agency based in Portugal.
Your goal is to act as a Virtual Assistant that qualifies incoming business leads interested in implementing AI systems, automated customer support bots, and CRM integrations.

STRICT ROLE BOUNDARY:
You are a commercial assistant. You do NOT write code, you do NOT troubleshoot their existing software, and you do NOT provide free AI consulting. Your job is to gather specific requirements so our technical team can propose a solution and quote.

THE VALUE PROPOSITION:
Mobizze sells "Virtual Employees". We help companies increase sales and reduce administrative work by up to 70% without hiring more people. Our bots respond in under 5 seconds, are available 24/7, and integrate with WhatsApp, Email, CRM, Teams, and Slack.

OBJECTIVE:
Qualify clients using a strict 3-Phase Process. The client must never know this process exists.

PHASE 1: GATHERING (The Filter)
If the client has not already provided this information, you MUST ask:

1. Company & Sector: What is the name of their company, website, and in what sector do they operate? (This helps us understand their industry).
2. Pain Point / Use Case: What is the main problem they want to solve? (e.g., customer support overload, lead generation, booking appointments, internal processes).
3. Integrations: Where do they want the AI to operate? (e.g., WhatsApp, Email, Website, Instagram, CRM).

STRICT PERSISTENCE:
If they avoid answering what their company does or where they want the bot to operate, politely insist. Our team cannot design an architecture without knowing their channels (like WhatsApp) and their sector.

PHASE 2: TERMS & EXPECTATIONS
Trigger: You have gathered Company Name, Sector, Pain Point, and Integrations.
Action: Explain how we work and ask for agreement before passing to the technical team. 

Send this exactly (translated to the client's language):
"Thank you for the details. To give you an idea of how we operate, our implementation process starts with an initial setup fee to build and train your custom Virtual Employee, followed by a flexible monthly maintenance plan that includes server costs, AI API usage, and ongoing optimizations. 

Does this model align with your expectations so I can forward your project to our technical team for a formal proposal?"

PHASE 3: CLOSING
Trigger: Client accepts Phase 2.
Action: 
"Perfect! I have documented your requirements. Our technical team (Paulo, José, or Bruno) will review your use case and contact you shortly to present a tailored solution or schedule a demonstration. Thank you for choosing Mobizze."

BEHAVIOR INSTRUCTIONS:
- Tone: Professional, modern, and tech-savvy, but very human.
- Do NOT schedule meetings directly. Tell them the technical team will reach out.
- Do NOT give prices. Prices depend entirely on the complexity of the integrations and the volume of messages.
- ALWAYS use numbered lists when asking multiple missing questions.
- NEVER sign your messages. The system adds your signature.
- Output ONLY the final email response.

EOD;

        $system_prompt .= "\n\nCRITICAL LANGUAGE LOCK: The conversation language is explicitly locked to " . strtoupper($locked_language) . ". You MUST respond ENTIRELY in " . strtoupper($locked_language) . ".";

        $ai_reply = call_openai_api($conversation_data['messages'], $system_prompt, $openai_api_key);

        if ($ai_reply) {
            $conversation_data['messages'][] = ['content' => $ai_reply, 'role' => 'assistant'];
            
            $sent = send_reply($client_email, $subject, $ai_reply, $email_user, $message_id, $inbox, $email_sent, $html_signature);
            
            if ($sent) {
                $conversation_data['retry_count'] = 0;
                @file_put_contents($json_file, json_encode($conversation_data, JSON_PRETTY_PRINT));
                
                imap_setflag_full($inbox, $email_uid, "\\Answered", ST_UID);
                write_log("OK: Respondido em $locked_language via OpenAI");
                
                if ($hub_contact_id) {
                    log_hubspot_email($hub_contact_id, "Re: " . $subject, $ai_reply, 'OUTGOING', $client_email, $client_name);
                }
                
                sleep(3);

                write_log("-> Verificando qualificação via extração JSON...");
                $extracted = extract_project_details_via_openai($conversation_data['messages'], $openai_api_key, $system_prompt);

                if ($extracted) {
                     if (!empty($extracted['company_name']) && $extracted['company_name'] !== 'Not Specified') {
                         $conversation_data['project_details']['company_name'] = $extracted['company_name'];
                     }
                     if (!empty($extracted['sector']) && $extracted['sector'] !== 'Pending') {
                         $conversation_data['project_details']['sector'] = $extracted['sector'];
                     }
                     if (!empty($extracted['company_website']) && $extracted['company_website'] !== 'Not Specified') {
                         $conversation_data['project_details']['company_website'] = $extracted['company_website'];
                     }
                     
                     if (!empty($extracted['phone'])) $conversation_data['project_details']['phone'] = $extracted['phone'];
                     
                     @file_put_contents($json_file, json_encode($conversation_data, JSON_PRETTY_PRINT));
                     
                     if (!empty($extracted['company_name']) && $extracted['company_name'] !== 'Not Specified') {
                         try { sync_hubspot_contact($client_email, $client_name, $conversation_data, 'lead'); } catch (Exception $e) {}
                     }
                }
                
                $is_standard_qualified = ($extracted && isset($extracted['sector']) && strtolower($extracted['sector']) !== 'pending' && isset($extracted['terms_accepted']) && strtoupper($extracted['terms_accepted']) === 'YES');

                if ($is_standard_qualified && !$conversation_data['report_sent']) {
                    
                    write_log("-> SUCESSO: Lead Qualificada!");
                    
                    $status = "SUCESSO (Lead Qualificada)";
                    
                    $conversation_data['project_details'] = $extracted;
                    $det = $conversation_data['project_details'];
                    $summary_technical = "RELATÓRIO: LEAD QUALIFICADA MOBIZZE\n";
                    $summary_technical .= "CLIENTE: " . $client_name . " ($client_email)\n";
                    $summary_technical .= "EMPRESA: " . ($det['company_name'] ?? 'Not Specified') . "\n";
                    $summary_technical .= "WEBSITE: " . ($det['company_website'] ?? 'Not Specified') . "\n";
                    $summary_technical .= "SECTOR: " . ($det['sector'] ?? 'Not Specified') . "\n\n";
                    $summary_technical .= "-- NECESSIDADES --\n";
                    $summary_technical .= "- **Pain Point:** " . $det['pain_point'] . "\n";
                    $summary_technical .= "- **Integrations:** " . $det['integrations'] . "\n";
                    
                    $conversation_data['report_sent'] = true;
                    @file_put_contents($json_file, json_encode($conversation_data, JSON_PRETTY_PRINT));
                    
                    send_smart_report($admin_email, $client_email, $client_name, $status, $summary_technical, $conversation_data);
                    
                    try {
                        sync_hubspot_contact($client_email, $client_name, $conversation_data, 'marketingqualifiedlead');
                    } catch (Exception $e) {}
                }
            } else {
                write_log("ERRO: Falha ao enviar email via SMTP/Mail().");
            }
        } else {
            write_log("API Failed (Likely 429). Stopping script.");
            break;
        }
        
        break; 
    }
}

if ($inbox) {
    imap_close($inbox);
    write_log("Ligação IMAP fechada.");
}

flock($f_lock, LOCK_UN);
fclose($f_lock);
write_log("--- Fim da Execução v1.0 ---");

// ==========================================================
// FUNÇÕES AUXILIARES
// ==========================================================

function call_openai_api($messages, $system_prompt, $api_key, $response_format = null) {
    $formatted_messages = [];
    $formatted_messages[] = ["role" => "system", "content" => $system_prompt];
    foreach ($messages as $msg) {
        $formatted_messages[] = ["role" => $msg['role'], "content" => $msg['content']];
    }

    $payload = [
        "model" => "gpt-4o",
        "messages" => $formatted_messages,
        "temperature" => 0.1
    ];

    if ($response_format) {
        $payload['response_format'] = $response_format;
    }
    
    $url = "https://api.openai.com/v1/chat/completions";
    
    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Content-Type: application/json',
        'Authorization: Bearer ' . $api_key
    ]);
    curl_setopt($ch, CURLOPT_TIMEOUT, 30);
    $response = curl_exec($ch);
    $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);

    if ($http_code === 200) {
        $result = json_decode($response, true);
        return $result['choices'][0]['message']['content'] ?? false;
    }
    return false;
}

function extract_project_details_via_openai($messages, $api_key, $system_prompt) {
    $messages[] = ["content" => "COMMAND: Analyze the conversation. Extract 'sector', 'pain_point', 'integrations', 'company_name', 'company_website', 'phone'. Return JSON.", "role" => "user"];

    $extra_sys = "You are a JSON extraction bot. Priority 1: Extract project details. CRITICAL RULES: Set 'terms_accepted' to 'NO' if ANY of the requested data (Sector, Pain Point, Integrations) is missing, vague, or 'Pending'. Set to 'YES' ONLY when the client has provided all requirements and explicitly agreed to the pricing structure mentioned in Phase 2.";

    $combined_sys = $system_prompt . "\n\n" . $extra_sys;

    $response_format = [
        "type" => "json_schema",
        "json_schema" => [
            "name" => "lead_extraction",
            "strict" => true,
            "schema" => [
                "type" => "object",
                "properties" => [
                    "sector" => ["type" => "string"],
                    "pain_point" => ["type" => "string"],
                    "integrations" => ["type" => "string"],
                    "company_name" => ["type" => "string"],
                    "company_website" => ["type" => "string"],
                    "phone" => ["type" => "string"],
                    "terms_accepted" => ["type" => "string", "enum" => ["YES", "NO"]]
                ],
                "required" => ["sector", "pain_point", "integrations", "company_name", "company_website", "phone", "terms_accepted"],
                "additionalProperties" => false
            ]
        ]
    ];
    
    $response_text = call_openai_api($messages, $combined_sys, $api_key, $response_format);
    return $response_text ? json_decode($response_text, true) : false;
}

function markdown_to_html_simple($text) {
    $text = htmlspecialchars($text);
    $text = preg_replace('/\*\*(.*?)\*\*/s', '<strong>$1</strong>', $text);
    $text = nl2br($text);
    return $text;
}

function send_smart_report($admin_email, $client_email, $client_name, $status, $summary, $conversation_data) {
    $subject = "[MOBIZZE] Lead Qualificada - $client_name";
    $boundary = "----=_Part_" . md5(time());
    $domain = 'mobizze.com';
    $message_id = "<" . md5(uniqid()) . "@" . $domain . ">";

    $headers = "From: Mobizze Bot <$admin_email>\r\n";
    $headers .= "Reply-To: $admin_email\r\n";
    $headers .= "Message-ID: $message_id\r\n";
    $headers .= "MIME-Version: 1.0\r\n";
    $headers .= "Content-Type: multipart/mixed; boundary=\"$boundary\"\r\n";

    $history_html = "";
    foreach ($conversation_data['messages'] as $msg) {
        $role = ($msg['role'] === 'user') ? "CLIENTE" : "MOBIZZE BOT";
        $history_html .= "<strong>--- $role ---</strong><br>" . markdown_to_html_simple($msg['content']) . "<br><br>";
    }

    $body_html = "<html><body style='font-family: Arial, sans-serif; line-height: 1.6;'>";
    $body_html .= "<h3>NOVO LEAD QUALIFICADO (MOBIZZE)</h3>";
    $body_html .= "<hr>";
    $body_html .= "<strong>Status:</strong> $status<br>";
    $body_html .= "<strong>Cliente:</strong> $client_name ($client_email)<br>";
    $body_html .= "<hr><br>";
    $body_html .= "<strong>RESUMO:</strong><br>";
    $body_html .= markdown_to_html_simple($summary);
    $body_html .= "<br><br><strong>HISTÓRICO:</strong><br>";
    $body_html .= "<div style='background: #f9f9f9; padding: 15px; border: 1px solid #ddd;'>" . $history_html . "</div>";
    $body_html .= "</body></html>";

    $message = "--$boundary\r\nContent-Type: text/html; charset=\"UTF-8\"\r\nContent-Transfer-Encoding: 8bit\r\n\r\n" . $body_html . "\r\n";
    $message .= "--$boundary--";
    
    return mail($admin_email, $subject, $message, $headers, "-f$admin_email");
}

function detect_language_better($text) {
    $text = strtolower($text);
    $pt_keywords = ['olá', 'obrigado', 'obrigada', 'bom dia', 'boa tarde', 'gostaria', 'queria', 'automação', 'bot', 'vendas', 'projeto'];
    $en_keywords = ['hi', 'hello', 'thanks', 'thank you', 'would', 'want', 'automation', 'bot', 'sales', 'project'];
    
    $pt_score = 0; $en_score = 0;
    foreach($pt_keywords as $k) if (preg_match("/\b$k\b/u", $text)) $pt_score++;
    foreach($en_keywords as $k) if (preg_match("/\b$k\b/u", $text)) $en_score++;
    
    if ($en_score > $pt_score) return 'English';
    if ($pt_score > $en_score) return 'Portuguese';
    return null;
}

function send_reply($to, $original_subject, $body, $from_email, $in_reply_to_id = null, $imap_stream = null, $sent_folder = null, $html_signature = "") {
    $domain = 'mobizze.com';
    $new_msg_id = "<" . md5(uniqid()) . "@" . $domain . ">";
    $boundary = "----=_Part_" . md5(uniqid());

    $subject_raw = (stripos($original_subject, 'Re:') === false) ? 'Re: ' . $original_subject : $original_subject;
    $subject = "=?UTF-8?B?" . base64_encode($subject_raw) . "?=";
    
    $clean_body = preg_replace('/(Best regards|Kind regards|Atenciosamente|Cumprimentos|Sincerely).*?Mobizze.*/is', '', $body);
    if(empty(trim($clean_body))) $clean_body = $body; 

    $headers = array();
    $headers[] = "From: Equipa Mobizze <$from_email>";
    $headers[] = "Reply-To: Equipa Mobizze <$from_email>";
    $headers[] = "Organization: Mobizze";
    $headers[] = "Message-ID: $new_msg_id";
    if ($in_reply_to_id) { 
        $headers[] = "In-Reply-To: $in_reply_to_id";
        $headers[] = "References: $in_reply_to_id"; 
    }
    $headers[] = "MIME-Version: 1.0";
    $headers[] = "Content-Type: multipart/alternative; boundary=\"$boundary\"";

    $headers_str = implode("\n", $headers);

    $plain_text = strip_tags($clean_body) . "\n\nCumprimentos,\nAssistente Virtual\nMobizze\ninfo@mobizze.com";
    $html_content = markdown_to_html_simple($clean_body) . $html_signature;

    $message = "--$boundary\n";
    $message .= "Content-Type: text/plain; charset=UTF-8\n";
    $message .= "Content-Transfer-Encoding: 8bit\n\n";
    $message .= $plain_text . "\n\n";
    
    $message .= "--$boundary\n";
    $message .= "Content-Type: text/html; charset=UTF-8\n";
    $message .= "Content-Transfer-Encoding: 8bit\n\n";
    $message .= "<html><body style='font-family: Inter, Arial, sans-serif; font-size: 14px; line-height: 1.6; color:#333;'>$html_content</body></html>\n\n";
    
    $message .= "--$boundary--";

    $sent = mail($to, $subject, $message, $headers_str, "-f$from_email");
    
    if ($sent && $imap_stream && $sent_folder) {
        $full_headers = "Date: " . date("r") . "\r\n";
        $full_headers .= "To: $to\r\n";
        $full_headers .= "Subject: $subject_raw\r\n";
        $full_headers .= str_replace("\n", "\r\n", $headers_str);
        
        $full_msg = $full_headers . "\r\n\r\n" . $message;
        @imap_append($imap_stream, $sent_folder, $full_msg, "\\Seen");
    }
    return $sent;
}

function clean_reply_text_simple($text) {
    $text = str_replace(["\r\n", "\r"], "\n", $text);
    $separators = ['/^On.*wrote:\s*$/m', '/^Em.*escreveu:\s*$/m', '/^-----Original Message-----/m', '/^From:.*Sent:.*To:.*Subject:.*/ms'];
    foreach($separators as $sep) {
        $parts = preg_split($sep, $text);
        if (count($parts) > 1) $text = $parts[0];
    }
    return trim($text);
}

function get_email_body($inbox, $email_uid) {
    $s = imap_fetchstructure($inbox, $email_uid, FT_UID);
    if (!isset($s->parts)) {
        $m = imap_fetchbody($inbox, $email_uid, 1, FT_PEEK | FT_UID);
        $encoding = $s->encoding;
    } else {
        $m = imap_fetchbody($inbox, $email_uid, 1.1, FT_PEEK | FT_UID);
        if(empty($m)) $m = imap_fetchbody($inbox, $email_uid, 1, FT_PEEK | FT_UID);
        $encoding = isset($s->parts[0]->encoding) ? $s->parts[0]->encoding : 0;
    }
    if ($encoding == 3) $m = base64_decode($m);
    elseif ($encoding == 4) $m = quoted_printable_decode($m);
    
    $m = mb_convert_encoding($m, 'UTF-8', 'UTF-8'); 
    
    return strip_tags($m);
}

function get_signature_html() {
    return '<br><br>
    <div style="font-family: Inter, Arial, sans-serif; color: #1e293b; line-height: 1.5; max-width: 500px; border-top: 1px solid #e2e8f0; padding-top: 15px; margin-top: 20px;">
        <div style="font-size: 11pt; font-weight: bold; color: #0f172a;">Assistente de IA</div>
        <div style="font-size: 10pt; margin-bottom: 10px; color: #64748b;">Triagem e Atendimento B2B</div>
        <div style="font-size: 9pt; margin-top: 10px; color: #475569;">
            email: <a href="mailto:info@mobizze.com" style="color: #2563eb; text-decoration: none;">info@mobizze.com</a><br>
            site: <a href="https://mobizze.com" style="color: #2563eb; text-decoration: none;">mobizze.com</a><br>
        </div>
        <div style="margin-top: 15px; font-weight: bold; font-size: 14px; letter-spacing: -0.5px; color: #0f172a;">
            Mobizze
        </div>
    </div>';
}

function get_hubspot_token() {
    global $hubspot_client_id, $hubspot_client_secret, $hubspot_initial_refresh_token, $hubspot_token_file;
    if (!$hubspot_client_id || !$hubspot_client_secret) return false;
    
    $tokens = [];
    if (file_exists($hubspot_token_file)) {
        $tokens = json_decode(file_get_contents($hubspot_token_file), true);
    }
    if (isset($tokens['access_token']) && isset($tokens['expires_at']) && $tokens['expires_at'] > time()) {
        return $tokens['access_token'];
    }
    $refresh_token = $tokens['refresh_token'] ?? $hubspot_initial_refresh_token;
    if (empty($refresh_token)) return false;

    $ch = curl_init('https://api.hubapi.com/oauth/v1/token');
    $fields = ['grant_type' => 'refresh_token', 'client_id' => $hubspot_client_id, 'client_secret' => $hubspot_client_secret, 'refresh_token' => $refresh_token];
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($fields));
    curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/x-www-form-urlencoded']);
    $response = curl_exec($ch);
    $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    
    if ($http_code == 200) {
        $data = json_decode($response, true);
        $data['expires_at'] = time() + ($data['expires_in'] * 0.95);
        file_put_contents($hubspot_token_file, json_encode($data));
        return $data['access_token'];
    }
    return false;
}

function sync_hubspot_contact($email, $name, $conversation_data, $lifecycle_stage = 'lead') {
    global $hubspot_owner_id;
    $token = get_hubspot_token();
    if (!$token) return false; 

    $details = $conversation_data['project_details'] ?? [];
    
    if (!empty($details['company_name']) && $details['company_name'] !== 'Not Specified') {
        $name = $details['company_name'] . ' Contact'; // Just a fallback if no actual name
    }

    $properties = [
        "email" => $email,
        "lifecyclestage" => strtolower($lifecycle_stage), 
        "hs_lead_status" => ($lifecycle_stage === 'marketingqualifiedlead') ? 'OPEN' : 'NEW',
    ];

    $parts = explode(' ', trim($name));
    $properties['firstname'] = array_shift($parts);
    $properties['lastname'] = !empty($parts) ? implode(' ', $parts) : ''; 

    if (!empty($details['company_name']) && $details['company_name'] != 'Not Specified') {
        $properties['company'] = $details['company_name'];
    }
    if (!empty($details['company_website']) && $details['company_website'] != 'Not Specified') {
        $properties['website'] = $details['company_website'];
    }
    if (!empty($details['phone'])) {
        $properties['phone'] = $details['phone'];
    }
    
    $properties['sales_phase'] = 'Mobizze AI Bot';
    if ($hubspot_owner_id) $properties['hubspot_owner_id'] = $hubspot_owner_id;

    $desc = "--- BOT UPDATE ---\nStatus: " . ($lifecycle_stage == 'marketingqualifiedlead' ? "QUALIFIED" : "Talking") . "\n";
    if (isset($details['sector'])) $desc .= "Sector: " . $details['sector'] . "\n";
    if (isset($details['pain_point'])) $desc .= "Pain: " . $details['pain_point'] . "\n";
    if (isset($details['integrations'])) $desc .= "Integrations: " . $details['integrations'] . "\n";
    $properties['jobtitle'] = $desc; 

    $ch = curl_init("https://api.hubapi.com/crm/v3/objects/contacts/search");
    $search_query = ["filterGroups" => [["filters" => [["propertyName" => "email", "operator" => "EQ", "value" => $email]]]]];
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($search_query));
    curl_setopt($ch, CURLOPT_HTTPHEADER, ["Authorization: Bearer $token", "Content-Type: application/json"]);
    $result = curl_exec($ch);
    $info = curl_getinfo($ch);
    curl_close($ch);

    $contact_id = null;
    if ($info['http_code'] == 200) {
        $data = json_decode($result, true);
        if ($data['total'] > 0) $contact_id = $data['results'][0]['id'];
    }

    if ($contact_id) {
        $url = "https://api.hubapi.com/crm/v3/objects/contacts/$contact_id";
        $method = "PATCH";
    } else {
        $url = "https://api.hubapi.com/crm/v3/objects/contacts";
        $method = "POST";
    }

    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, $method);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode(["properties" => $properties]));
    curl_setopt($ch, CURLOPT_HTTPHEADER, ["Authorization: Bearer $token", "Content-Type: application/json"]);
    $final_res = curl_exec($ch);
    $http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    
    if ($http_code >= 200 && $http_code < 300) {
        $json = json_decode($final_res, true);
        return $json['id'] ?? $contact_id;
    }
    return false;
}

function log_hubspot_email($contact_id, $subject, $body, $direction, $client_email, $client_name) {
    global $hubspot_owner_id, $admin_email; 
    $token = get_hubspot_token();
    if (!$token || !$contact_id) return;

    if ($direction === 'INCOMING') {
        $from_email = $client_email; $to_email = $admin_email;
        $from_name = $client_name; $to_name = "Mobizze AI";
    } else {
        $from_email = $admin_email; $to_email = $client_email;
        $from_name = "Mobizze AI"; $to_name = $client_name;
    }

    $from_parts = explode(' ', trim($from_name));
    $from_first = array_shift($from_parts);
    $from_last = !empty($from_parts) ? implode(' ', $from_parts) : '';
    $to_parts = explode(' ', trim($to_name));
    $to_first = array_shift($to_parts);
    $to_last = !empty($to_parts) ? implode(' ', $to_parts) : '';

    $url = "https://api.hubapi.com/engagements/v1/engagements";
    $timestamp_ms = time() * 1000;
    
    $post_data = [
        "engagement" => ["active" => true, "ownerId" => $hubspot_owner_id ? (int)$hubspot_owner_id : null, "type" => "EMAIL", "timestamp" => $timestamp_ms],
        "associations" => ["contactIds" => [(int)$contact_id], "companyIds" => [], "dealIds" => [], "ownerIds" => []],
        "metadata" => [
            "from" => ["email" => $from_email, "firstName" => $from_first, "lastName" => $from_last],
            "to" => [["email" => $to_email, "firstName" => $to_first, "lastName" => $to_last]],
            "sender" => ["email" => $from_email],
            "cc" => [], "bcc" => [],
            "subject" => $subject ?: "(Sem Assunto)",
            "html" => nl2br(htmlspecialchars($body)),
            "text" => strip_tags($body)
        ]
    ];
    
    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($post_data));
    curl_setopt($ch, CURLOPT_HTTPHEADER, ["Authorization: Bearer $token", "Content-Type: application/json"]);
    curl_exec($ch);
    curl_close($ch);
}
?>
