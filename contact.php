<?php
header('Content-Type: application/json');

// Check if it's a POST request
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'message' => 'Method not allowed.']);
    exit;
}

// Get JSON input if fetch was used, or standard POST array
$data = json_decode(file_get_contents('php://input'), true);
if (!$data) {
    $data = $_POST;
}

// Required fields mapping
$nome = isset($data['nome']) ? filter_var($data['nome'], FILTER_SANITIZE_STRING) : '';
$empresa = isset($data['empresa']) ? filter_var($data['empresa'], FILTER_SANITIZE_STRING) : '';
$email = isset($data['email']) ? filter_var($data['email'], FILTER_SANITIZE_EMAIL) : '';
$telefone = isset($data['telefone']) ? filter_var($data['telefone'], FILTER_SANITIZE_STRING) : '';
$desafio = isset($data['desafio']) ? filter_var($data['desafio'], FILTER_SANITIZE_STRING) : '';
$detalhes = isset($data['detalhes']) ? filter_var($data['detalhes'], FILTER_SANITIZE_STRING) : '';

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

// Email configuration
$to = 'contact@mobizze.com';
$subject = 'Novo Pedido de Diagnóstico - ' . $empresa;

// Email headers
$headers = "MIME-Version: 1.0" . "\r\n";
$headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";
$headers .= "From: no-reply@mobizze.com" . "\r\n";
$headers .= "Reply-To: " . $email . "\r\n";

// Email body
$message = "
<html>
<head>
<title>Novo Pedido de Diagnóstico</title>
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
    <div class='value'>" . htmlspecialchars($nome) . "</div>
</div>
<div class='field'>
    <div class='label'>Empresa:</div>
    <div class='value'>" . htmlspecialchars($empresa) . "</div>
</div>
<div class='field'>
    <div class='label'>Email:</div>
    <div class='value'>" . htmlspecialchars($email) . "</div>
</div>
<div class='field'>
    <div class='label'>Telefone:</div>
    <div class='value'>" . htmlspecialchars($telefone) . "</div>
</div>
<div class='field'>
    <div class='label'>Maior Desafio:</div>
    <div class='value'>" . htmlspecialchars($desafio) . "</div>
</div>
<div class='field'>
    <div class='label'>Detalhes Adicionais:</div>
    <div class='value'>" . nl2br(htmlspecialchars($detalhes)) . "</div>
</div>
</body>
</html>
";

// Send email
if (mail($to, $subject, $message, $headers)) {
    echo json_encode(['success' => true, 'message' => 'Email sent successfully.']);
} else {
    http_response_code(500);
    echo json_encode(['success' => false, 'message' => 'Failed to send email.']);
}
?>
