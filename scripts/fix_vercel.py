import json

# 1. Update vercel.json
with open('vercel.json', 'r') as f:
    data = json.load(f)

# Change trailingSlash to false and add cleanUrls
data['trailingSlash'] = False
data['cleanUrls'] = True

# Change default redirect from /en/ to /pt/
for rule in data.get('redirects', []):
    if rule.get('source') == '/' and 'has' not in rule:
        rule['destination'] = '/pt/'

# Change default rewrite from /en/:path to /pt/:path
for rule in data.get('rewrites', []):
    if rule.get('source') == '/:path((?!en|pt|api|_next|favicon|assets|images|css|js).*)':
        rule['destination'] = '/pt/:path'

with open('vercel.json', 'w') as f:
    json.dump(data, f, indent=2)

# 2. Update index.html
with open('index.html', 'r') as f:
    content = f.read()

content = content.replace("lang.toLowerCase().startsWith('pt') ? 'pt/index.html' : 'en/index.html'", "lang.toLowerCase().startsWith('en') ? 'en/index.html' : 'pt/index.html'")
content = content.replace('<meta http-equiv="refresh" content="0;url=en/index.html">', '<meta http-equiv="refresh" content="0;url=pt/index.html">')

with open('index.html', 'w') as f:
    f.write(content)

print("Fixed Vercel configuration and root index.html fallback")
