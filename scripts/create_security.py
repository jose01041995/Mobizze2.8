import os

def create_security_page(src_file, dst_file, is_pt=True):
    if not os.path.exists(src_file):
        return
    
    with open(src_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if is_pt:
        content = content.replace('<title>Política de Privacidade | Mobizze</title>', '<title>Segurança e Conformidade | Mobizze</title>')
        content = content.replace('Política de <span class="text-accent">Privacidade</span>', 'Segurança e <span class="text-accent">Conformidade</span>')
        content = content.replace('A sua privacidade é importante para nós.', 'A nossa infraestrutura é construída com foco na segurança e privacidade dos seus dados.')
        
        security_body = """
                <h3>1. Infraestrutura e Encriptação</h3>
                <p>Todos os dados são encriptados em trânsito (TLS 1.2+) e em repouso (AES-256). Utilizamos fornecedores de infraestrutura de topo (ex: AWS, Google Cloud) com certificações ISO 27001 e SOC 2.</p>

                <h3>2. Controlo de Acessos</h3>
                <p>Implementamos autenticação multifator (MFA) e princípio do menor privilégio para todos os sistemas internos. O acesso aos dados de clientes é estritamente limitado e registado em logs de auditoria.</p>

                <h3>3. Inteligência Artificial e Dados</h3>
                <p><strong>Nós NÃO utilizamos os seus dados confidenciais para treinar os nossos modelos base.</strong> Os dados processados através dos nossos agentes e automações são utilizados estritamente para fornecer o serviço à sua empresa, garantindo total isolamento da informação (tenant isolation).</p>

                <h3>4. Retenção de Dados e Backups</h3>
                <p>Efetuamos backups diários. Os dados são retidos apenas pelo período estritamente necessário ou acordado com o cliente. Dispomos de políticas rigorosas de eliminação segura de informação.</p>
                
                <h3>5. Subprocessadores</h3>
                <p>Trabalhamos apenas com parceiros (ex: OpenAI, Anthropic, Supabase) que garantem acordos rigorosos de processamento de dados (DPA) em conformidade com o RGPD europeu, assegurando que os dados não são partilhados publicamente.</p>
"""
        
        # We need to find the content between <div class="max-w-3xl mx-auto legal-content"> and </div> </section>
        import re
        content = re.sub(r'(<div class="max-w-3xl mx-auto legal-content">)(.*?)(</div>\s*</section>)', r'\1' + security_body + r'\3', content, flags=re.DOTALL)
        
    else:
        content = content.replace('<title>Privacy Policy | Mobizze</title>', '<title>Security & Compliance | Mobizze</title>')
        content = content.replace('Privacy <span class="text-accent">Policy</span>', 'Security & <span class="text-accent">Compliance</span>')
        content = content.replace('Your privacy is important to us.', 'Our infrastructure is built with a focus on the security and privacy of your data.')
        
        security_body = """
                <h3>1. Infrastructure and Encryption</h3>
                <p>All data is encrypted in transit (TLS 1.2+) and at rest (AES-256). We use top-tier infrastructure providers (e.g., AWS, Google Cloud) with ISO 27001 and SOC 2 certifications.</p>

                <h3>2. Access Control</h3>
                <p>We implement multi-factor authentication (MFA) and the principle of least privilege for all internal systems. Access to client data is strictly limited and logged in audit trails.</p>

                <h3>3. Artificial Intelligence and Data</h3>
                <p><strong>We DO NOT use your confidential data to train our base models.</strong> The data processed through our agents and automations is strictly used to provide the service to your company, ensuring total data isolation (tenant isolation).</p>

                <h3>4. Data Retention and Backups</h3>
                <p>We perform daily backups. Data is retained only for the strictly necessary period or as agreed with the client. We have strict policies for secure data deletion.</p>
                
                <h3>5. Subprocessors</h3>
                <p>We work only with partners (e.g., OpenAI, Anthropic, Supabase) who guarantee strict Data Processing Agreements (DPA) in compliance with the European GDPR, ensuring that data is not shared publicly.</p>
"""
        import re
        content = re.sub(r'(<div class="max-w-3xl mx-auto legal-content">)(.*?)(</div>\s*</section>)', r'\1' + security_body + r'\3', content, flags=re.DOTALL)
        
    with open(dst_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {dst_file}")

create_security_page('pt/privacidade.html', 'pt/seguranca.html', is_pt=True)
create_security_page('en/privacy.html', 'en/security.html', is_pt=False)
