<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type, Authorization');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['error' => 'Method not allowed']);
    exit;
}

// Carregar ficheiro .env no servidor
function load_env($path) {
    if (!file_exists($path)) return false;
    $lines = file($path, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
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
                $_SERVER[$name] = $value;
            }
        }
    }
    return true;
}

load_env(__DIR__ . '/.env');

$api_key = $_ENV['OPENAI_API_KEY'] ?? getenv('OPENAI_API_KEY');
if (empty($api_key)) {
    http_response_code(500);
    echo json_encode(['error' => 'OPENAI_API_KEY not configured in .env']);
    exit;
}

$input = json_decode(file_get_contents('php://input'), true);
if (!$input || !isset($input['messages'])) {
    http_response_code(400);
    echo json_encode(['error' => 'Invalid input payload']);
    exit;
}

// Preparar payload para a OpenAI
$payload = [
    'model' => $input['model'] ?? 'gpt-4o-mini',
    'messages' => $input['messages'],
    'temperature' => $input['temperature'] ?? 0.7
];

if (isset($input['max_tokens'])) {
    $payload['max_tokens'] = $input['max_tokens'];
}
if (isset($input['tools'])) {
    $payload['tools'] = $input['tools'];
    $payload['tool_choice'] = $input['tool_choice'] ?? 'auto';
}

$ch = curl_init('https://api.openai.com/v1/chat/completions');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'Authorization: Bearer ' . $api_key
]);
curl_setopt($ch, CURLOPT_TIMEOUT, 30);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, true);

$response = curl_exec($ch);
$http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$curl_error = curl_error($ch);
curl_close($ch);

if ($curl_error) {
    http_response_code(500);
    echo json_encode(['error' => 'cURL Error: ' . $curl_error]);
    exit;
}

http_response_code($http_code);
echo $response;
?>
