import os

def apply_disclaimers():
    base_dir = "/Users/joseteixeira/Desktop/Antigravity Stuf/Mobizze2.0"
    
    # PT index.html
    pt_index = os.path.join(base_dir, "pt", "index.html")
    if os.path.exists(pt_index):
        with open(pt_index, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add disclaimer below stats
        target_pt = '<div class="text-xs md:text-sm text-slate-500 mt-2 font-medium">Países Com Clientes Ativos</div>\n                </div>'
        replacement_pt = target_pt + '\n            </div>\n            <div class="text-center mt-6 text-[10px] text-slate-400 max-w-2xl mx-auto px-4">\n                Dados agregados de projetos implementados entre 2024 e 2026. Resultados variam consoante os processos, volume e sistemas de cada empresa.\n            </div>'
        
        if "Dados agregados" not in content and target_pt in content:
            content = content.replace(target_pt, replacement_pt)
            with open(pt_index, 'w', encoding='utf-8') as f:
                f.write(content)
            print("Updated pt/index.html with disclaimer")
            
    # EN index.html
    en_index = os.path.join(base_dir, "en", "index.html")
    if os.path.exists(en_index):
        with open(en_index, 'r', encoding='utf-8') as f:
            content = f.read()
            
        target_en = '<div class="text-xs md:text-sm text-slate-500 mt-2 font-medium">Countries With Active Clients</div>\n                </div>'
        replacement_en = target_en + '\n            </div>\n            <div class="text-center mt-6 text-[10px] text-slate-400 max-w-2xl mx-auto px-4">\n                Aggregated data from projects implemented between 2024 and 2026. Results vary depending on the processes, volume, and systems of each company.\n            </div>'
        
        if "Aggregated data" not in content and target_en in content:
            content = content.replace(target_en, replacement_en)
            with open(en_index, 'w', encoding='utf-8') as f:
                f.write(content)
            print("Updated en/index.html with disclaimer")

if __name__ == "__main__":
    apply_disclaimers()
