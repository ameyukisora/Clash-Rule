import requests
from datetime import datetime
import pytz

url = "https://raw.githubusercontent.com/dler-io/Rules/main/Surge/Surge%203/Provider/AdBlock.list"
response = requests.get(url)
if response.status_code == 200:
    text = response.text.splitlines()
    domain = [rule[7:] for rule in text if rule.startswith('DOMAIN,')]
    domain_suffix = [rule[14:] for rule in text if rule.startswith('DOMAIN-SUFFIX,')]

time = datetime.now(pytz.timezone('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S")

with open('autoupdate/Reject.yaml', 'w') as f:
    f.write(f'''payload:
  # {time}
  # DOMAIN-SUFFIX: {len(domain_suffix)}, DOMAIN: {len(domain)}
  # TOTAL: {len(domain) + len(domain_suffix)}
{'\n'.join(f"  - '{url}'" for url in domain)}
{'\n'.join(f"  - '+.{url}'" for url in domain_suffix)}
''')
