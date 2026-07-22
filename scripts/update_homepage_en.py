import os

def update_file(path, replacements):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
        else:
            print(f"Warning: Could not find '{old[:50]}...' in {path}")
            
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

en_index_replacements = [
    (
        '<h2 class="font-display font-bold text-dark leading-[1.08] tracking-tight animate-fade-in-up delay-100" style="font-size:clamp(2.2rem, 5.5vw, 5rem);">\n                    Reclaim Up To 70% Of Your Team\'s Time <span class="text-accent">With AI & Automation</span>\n                </h2>',
        '<h2 class="font-display font-bold text-dark leading-[1.08] tracking-tight animate-fade-in-up delay-100" style="font-size:clamp(2.2rem, 5.5vw, 5rem);">\n                    Custom AI Systems for Businesses\n                </h2>'
    ),
    (
        '<p class="max-w-xl mt-6 text-base md:text-lg text-slate-600 leading-relaxed animate-fade-in-up delay-200">\n                    We build AI agents, automate processes, and give hours back to your team — for decisions that make a difference.\n                </p>',
        '<p class="max-w-xl mt-6 text-base md:text-lg text-slate-600 leading-relaxed animate-fade-in-up delay-200">\n                    We analyze your processes and build custom agents, automations, and tools to reduce costs, reclaim time, and accelerate growth.\n                </p>'
    ),
    (
        '<span class="hidden sm:inline">Free Diagnostic — See how much I can save</span>',
        '<span class="hidden sm:inline">Discover opportunities for my business</span>'
    ),
    (
        '<a href="#problem" class="inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-full text-sm font-medium transition-all duration-300 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 hover:border-slate-300 shadow-sm">\n                            Discover more\n                            <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M8 3L8 13M8 13L4 9M8 13L12 9" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg>\n                        </a>',
        '<a href="case-studies.html" class="inline-flex items-center justify-center gap-2 px-6 py-3.5 rounded-full text-sm font-medium transition-all duration-300 bg-white border border-slate-200 text-slate-700 hover:bg-slate-50 hover:border-slate-300 shadow-sm">\n                            View real cases\n                            <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M8 3L8 13M8 13L4 9M8 13L12 9" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg>\n                        </a>'
    ),
    (
        '<a href="chatbot.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Chatbot</a>\n                            <a href="emailbot.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Emailbot</a>\n                            <a href="qualify-leads-crm.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Qualify Leads CRM</a>\n                            <a href="schedule-meetings.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Schedule Meetings</a>\n                            <a href="voice-agents.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Voice Agents</a>\n                            <a href="text-agents.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Text Agents</a>\n                            <a href="social-media.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Social Media</a>',
        '<a href="conversational-agents.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Conversational Agents</a>\n                            <a href="emailbot.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Emailbot</a>\n                            <a href="qualify-leads-crm.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Qualify Leads CRM</a>\n                            <a href="schedule-meetings.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Schedule Meetings</a>\n                            <a href="voice-agents.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Voice Agents</a>\n                            <a href="custom-tools.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Custom Tools</a>\n                            <a href="social-media.html" class="px-4 py-2.5 rounded-xl hover:bg-blue-50 text-xs text-slate-600 hover:text-accent font-medium transition-colors">Social Media</a>'
    ),
    (
        '<a href="chatbot.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Chatbot</a>\n                    <a href="emailbot.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Emailbot</a>\n                    <a href="qualify-leads-crm.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Qualify CRM</a>\n                    <a href="schedule-meetings.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Schedule Meetings</a>\n                    <a href="voice-agents.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Voice Agents</a>\n                    <a href="text-agents.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Text Agents</a>\n                    <a href="social-media.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Social Media</a>',
        '<a href="conversational-agents.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Conversational Agents</a>\n                    <a href="emailbot.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Emailbot</a>\n                    <a href="qualify-leads-crm.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Qualify CRM</a>\n                    <a href="schedule-meetings.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Schedule Meetings</a>\n                    <a href="voice-agents.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Voice Agents</a>\n                    <a href="custom-tools.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Custom Tools</a>\n                    <a href="social-media.html" class="mobile-link text-lg font-medium text-slate-700 hover:text-accent">Social Media</a>'
    )
]

update_file('/Users/joseteixeira/Desktop/Antigravity Stuf/Mobizze2.0/en/index.html', en_index_replacements)

# Add disclaimer after stats bar in en/index.html
with open('/Users/joseteixeira/Desktop/Antigravity Stuf/Mobizze2.0/en/index.html', 'r', encoding='utf-8') as f:
    en_content = f.read()

disclaimer_en = '            </div>\n            <div class="max-w-5xl mx-auto mt-6 text-center">\n                <p class="text-xs text-slate-400">Aggregated data from projects implemented between 2024 and 2026. Results vary depending on the processes, volume, and systems of each company.</p>\n            </div>'
if 'Aggregated data from projects' not in en_content:
    en_content = en_content.replace('            </div>\n        </div>\n\n        <!-- Clients and Partners -->', disclaimer_en + '\n        </div>\n\n        <!-- Clients and Partners -->')
    with open('/Users/joseteixeira/Desktop/Antigravity Stuf/Mobizze2.0/en/index.html', 'w', encoding='utf-8') as f:
        f.write(en_content)
        
print("Updated en/index.html")
