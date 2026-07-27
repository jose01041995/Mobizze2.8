<?php
// Carregar .env se existir
if (file_exists(__DIR__ . '/.env')) {
    $lines = file(__DIR__ . '/.env', FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    foreach ($lines as $line) {
        $line = trim($line);
        if (strpos($line, '#') === 0) continue;
        if (strpos($line, '=') !== false) {
            list($name, $value) = explode('=', $line, 2);
            $name = trim($name);
            $value = trim(trim($value), '"\'');
            if (!empty($name)) {
                putenv("$name=$value");
                $_ENV[$name] = $value;
            }
        }
    }
}

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'message' => 'Method not allowed.']);
    exit;
}

$data = json_decode(file_get_contents('php://input'), true);
if (!$data) {
    $data = $_POST;
}

function clean_input($val) {
    return isset($val) ? htmlspecialchars(strip_tags(trim((string)$val)), ENT_QUOTES, 'UTF-8') : '';
}

$nome = clean_input($data['nome'] ?? '');
$empresa = clean_input($data['empresa'] ?? '');
$email = isset($data['email']) ? filter_var(trim($data['email']), FILTER_SANITIZE_EMAIL) : '';
$telefone = clean_input($data['telefone'] ?? '');
$desafio = clean_input($data['desafio'] ?? '');
$detalhes = clean_input($data['detalhes'] ?? '');

if (empty($nome) || empty($empresa) || empty($email) || empty($desafio)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'message' => 'Please fill all required fields.']);
    exit;
}

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'message' => 'Invalid email address.']);
    exit;
}

$from_email = $_ENV['EMAIL_USER'] ?? 'info@mobizze.com';
$to_email = $_ENV['ADMIN_EMAIL'] ?? 'info@mobizze.com';
$email_pass = $_ENV['EMAIL_PASS'] ?? '3056mobizze';
$subject = 'Novo Pedido via IA / Diagnóstico - ' . $empresa;

$headers = "MIME-Version: 1.0" . "\r\n";
$headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";
$headers .= "From: Mobizze Website <" . $from_email . ">" . "\r\n";
$headers .= "Reply-To: " . $email . "\r\n";
$headers .= "X-Mailer: PHP/" . phpversion() . "\r\n";

$message = "
<html>
<head>
<title>Novo Pedido de Contacto</title>
<style>
    body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
    h2 { color: #1e3a8a; }
    .field { margin-bottom: 15px; }
    .label { font-weight: bold; color: #475569; }
    .value { margin-top: 5px; background: #f8fafc; padding: 10px; border-radius: 4px; border: 1px solid #e2e8f0; }
</style>
</head>
<body>
<h2>Novo Pedido de Contacto da Mobizze</h2>
<div class='field'>
    <div class='label'>Nome:</div>
    <div class='value'>" . $nome . "</div>
</div>
<div class='field'>
    <div class='label'>Empresa:</div>
    <div class='value'>" . $empresa . "</div>
</div>
<div class='field'>
    <div class='label'>Email:</div>
    <div class='value'>" . htmlspecialchars($email) . "</div>
</div>
<div class='field'>
    <div class='label'>Telefone:</div>
    <div class='value'>" . ($telefone ?: 'N/A') . "</div>
</div>
<div class='field'>
    <div class='label'>Maior Desafio:</div>
    <div class='value'>" . $desafio . "</div>
</div>
<div class='field'>
    <div class='label'>Detalhes Adicionais:</div>
    <div class='value'>" . nl2br($detalhes) . "</div>
</div>
</body>
</html>
";

function send_smtp_fallback($host, $port, $user, $pass, $from, $to, $subject, $message, $headers) {
    if (empty($pass)) return false;
    $socket = @fsockopen(($port == 465 ? "ssl://" : "") . $host, $port, $errno, $errstr, 10);
    if (!$socket) {
        if ($port == 465) {
            $socket = @fsockopen($host, 587, $errno, $errstr, 10);
        }
        if (!$socket) return false;
    }
    
    stream_set_timeout($socket, 10);
    function get_res($sock) {
        $data = "";
        while ($str = fgets($sock, 515)) {
            $data .= $str;
            if (substr($str, 3, 1) == " ") break;
        }
        return $data;
    }
    
    get_res($socket);
    fputs($socket, "EHLO mobizze.com\r\n");
    get_res($socket);
    fputs($socket, "AUTH LOGIN\r\n");
    get_res($socket);
    fputs($socket, base64_encode($user) . "\r\n");
    get_res($socket);
    fputs($socket, base64_encode($pass) . "\r\n");
    $auth = get_res($socket);
    
    if (strpos($auth, '235') === false) {
        fclose($socket);
        return false;
    }
    
    fputs($socket, "MAIL FROM: <$from>\r\n");
    get_res($socket);
    fputs($socket, "RCPT TO: <$to>\r\n");
    get_res($socket);
    fputs($socket, "DATA\r\n");
    get_res($socket);
    
    $full_msg = "To: $to\r\nSubject: $subject\r\n$headers\r\n\r\n$message\r\n.\r\n";
    fputs($socket, $full_msg);
    $sent_res = get_res($socket);
    
    fputs($socket, "QUIT\r\n");
    fclose($socket);
    
    return (strpos($sent_res, '250') !== false);
}

// 1. Tentar envio por mail() nativo COM o envelope do remetente (-f) para validação Exim
$sent = @mail($to_email, $subject, $message, $headers, "-f" . $from_email);

// 2. Se mail() falhar ou estiver desativado no alojamento, usar ligação SMTP autenticada
if (!$sent && !empty($email_pass)) {
    $sent = send_smtp_fallback("mail.mobizze.com", 465, $from_email, $email_pass, $from_email, $to_email, $subject, $message, $headers);
}

if ($sent) {
    echo json_encode(['success' => true, 'message' => 'Email sent successfully.']);
} else {
    http_response_code(500);
    echo json_encode(['success' => false, 'message' => 'Failed to send email via both mail() and SMTP.']);
}
?>
