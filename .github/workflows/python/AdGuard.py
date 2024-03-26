import requests

# 下载文件
url = "https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt"
response = requests.get(url)
if response.status_code == 200:
    text = response.text.splitlines()
    adguard = [adg[2:-1] for adg in text if adg.startswith('||') and '*' not in adg and adg.endswith('^')]
    whitelist = [adgw[4:-2] for adgw in text if adgw.startswith('@@||') and '*' not in adgw and adgw.endswith('^|')]

# 输出新文件
with open('autoupdate/AdGuard.yaml', 'w') as f:
    f.write(f'''payload:
{'\n'.join(f'  # {description[2:]}' for description in text[1:6])}
  # Total: {len(adguard)}
{'\n'.join(f"  - '+.{rule}'" for rule in adguard)}
''')

with open('autoupdate/AdGuardWhitelist.yaml', 'w') as f:
    f.write(f'''payload:
  # Use with AdGuard.yaml
{'\n'.join(f'  # {description[2:]}' for description in text[1:6])}
  # Total: {len(whitelist)}
{'\n'.join(f"  - '+.{rule}'" for rule in whitelist)}
''')
