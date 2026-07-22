import os
import shutil
import glob

def replace_in_file(file_path, replacements):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# 1. Rename files
pt_old = 'pt/financiamento.html'
pt_new = 'pt/planos-implementacao.html'
en_old = 'en/financing.html'
en_new = 'en/flexible-implementation-plans.html'

if os.path.exists(pt_old):
    shutil.move(pt_old, pt_new)

if os.path.exists(en_old):
    shutil.move(en_old, en_new)

# 2. Update global links and menu text
all_html_files = glob.glob('pt/*.html') + glob.glob('en/*.html')

global_replacements = [
    ('"financiamento.html"', '"planos-implementacao.html"'),
    ('>Financiamento<', '>Planos Flexíveis<'),
    ('../pt/financiamento.html', '../pt/planos-implementacao.html'),
    ('"financing.html"', '"flexible-implementation-plans.html"'),
    ('>Financing<', '>Flexible Plans<'),
    ('../en/financing.html', '../en/flexible-implementation-plans.html')
]

for file_path in all_html_files:
    replace_in_file(file_path, global_replacements)

# 3. Update specific content in PT page
if os.path.exists(pt_new):
    pt_specific = [
        ('<title>Financiamento para Projetos de IA | Mobizze</title>', '<title>Planos de Implementação Flexíveis | Mobizze</title>'),
        ('Financiamento Flexível', 'Planos Flexíveis'),
        ('Financie a Sua <span class="text-accent">Transformação Digital</span>.', 'Viabilize a Sua <span class="text-accent">Transformação Digital</span>.'),
        ('A falta de orçamento já não é um obstáculo. Com o nosso programa de financiamento, pode começar a implementar a IA na sua empresa hoje e pagar de forma flexível.', 'A falta de orçamento já não é um obstáculo. Oferecemos planos de pagamento por fases, projeto piloto e mensalidade de suporte, com implementação progressiva. Condições sujeitas à dimensão do projeto.'),
        ('Plano de Financiamento', 'Plano de Implementação'),
        ('Vantagens do Financiamento', 'Vantagens dos Planos Flexíveis'),
        ('Pedir Diagnóstico e Plano de Financiamento', 'Pedir Diagnóstico e Plano de Implementação')
    ]
    replace_in_file(pt_new, pt_specific)

# 4. Update specific content in EN page
if os.path.exists(en_new):
    en_specific = [
        ('<title>Financing for AI Projects | Mobizze</title>', '<title>Flexible Implementation Plans | Mobizze</title>'),
        ('Flexible Financing', 'Flexible Plans'),
        ('Finance Your <span class="text-accent">Digital Transformation</span>.', 'Make Your <span class="text-accent">Digital Transformation</span> Viable.'),
        ('Lack of budget is no longer an obstacle. With our financing program, you can start implementing AI in your company today and pay flexibly.', 'Lack of budget is no longer an obstacle. We offer phased payment plans, pilot projects, and support retainers with progressive implementation. Conditions are subject to project size.'),
        ('Financing Plan', 'Implementation Plan'),
        ('Financing Advantages', 'Advantages of Flexible Plans'),
        ('Request Diagnosis and Financing Plan', 'Request Diagnosis and Implementation Plan')
    ]
    replace_in_file(en_new, en_specific)

print("Financing page updated successfully.")
