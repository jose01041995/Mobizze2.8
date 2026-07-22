import os

legal_entities_pt = """
                <h3>1. Identificação da Entidade</h3>
                <p>A Mobizze (marca operada por Absolutarget Lda., NIF 513360530, com sede em Portugal) compromete-se a proteger a sua privacidade. Esta Política de Privacidade explica como recolhemos, usamos, divulgamos e salvaguardamos as suas informações quando visita o nosso site mobizze.com e utiliza os nossos serviços.</p>
"""

legal_entities_en = """
                <h3>1. Entity Identification</h3>
                <p>Mobizze (a brand operated by Absolutarget Lda., VAT 513360530, headquartered in Portugal) is committed to protecting your privacy. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you visit our website mobizze.com and use our services.</p>
"""

def replace_in_file(filepath, old_text, new_text):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_text in content:
        content = content.replace(old_text, new_text)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

# Update PT Privacy
old_intro_pt = """<h3>1. Introdução</h3>
                <p>A Mobizze ("nós", "nosso") compromete-se a proteger a sua privacidade. Esta Política de Privacidade explica como recolhemos, usamos, divulgamos e salvaguardamos as suas informações quando visita o nosso site mobizze.com e utiliza os nossos serviços.</p>"""

replace_in_file('pt/privacidade.html', old_intro_pt, legal_entities_pt)

# Update EN Privacy
old_intro_en = """<h3>1. Introduction</h3>
                <p>Mobizze ("we", "us", "our") is committed to protecting your privacy. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you visit our website mobizze.com and use our services.</p>"""

replace_in_file('en/privacy.html', old_intro_en, legal_entities_en)

# Do terms as well
terms_pt = """<h3>1. Aceitação dos Termos</h3>
                <p>Ao aceder ao website da Mobizze (operado por Absolutarget Lda., NIF 513360530), concorda em cumprir estes termos de serviço, todas as leis e regulamentos aplicáveis.</p>"""

replace_in_file('pt/termos.html', """<h3>1. Aceitação dos Termos</h3>
                <p>Ao aceder ao website da Mobizze, concorda em cumprir estes termos de serviço, todas as leis e regulamentos aplicáveis.</p>""", terms_pt)

terms_en = """<h3>1. Acceptance of Terms</h3>
                <p>By accessing the website of Mobizze (operated by Absolutarget Lda., VAT 513360530), you agree to comply with these terms of service and all applicable laws and regulations.</p>"""

replace_in_file('en/terms.html', """<h3>1. Acceptance of Terms</h3>
                <p>By accessing the website of Mobizze, you agree to comply with these terms of service and all applicable laws and regulations.</p>""", terms_en)
