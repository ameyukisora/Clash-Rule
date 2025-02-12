import requests
from datetime import datetime
import pytz

url = "https://raw.githubusercontent.com/dler-io/Rules/main/Surge/Surge%203/Provider/AdBlock.list"
response = requests.get(url)

# 初始化防止 NameError
domain = []
domain_suffix = []

if response.status_code == 200:
    text = response.text.splitlines()
    # 单次遍历同时提取两类规则
    for rule in text:
        if rule.startswith('DOMAIN,'):
            domain.append(rule[7:])
        elif rule.startswith('DOMAIN-SUFFIX,'):
            domain_suffix.append(rule[14:])

time = datetime.now(pytz.timezone('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S")

with open('autoupdate/Reject.yaml', 'w') as f:
    # 用高效方式组织模板减少字符串操作
    f.write(
        f"payload:\n"
        f"  # {time}\n"
        f"  # DOMAIN-SUFFIX: {len(domain_suffix)}, DOMAIN: {len(domain)}\n"
        f"  # TOTAL: {len(domain) + len(domain_suffix)}\n"
        + '\n'.join(f"  - '{url}'" for url in domain) + '\n'
        + '\n'.join(f"  - '+.{url}'" for url in domain_suffix)
    )
