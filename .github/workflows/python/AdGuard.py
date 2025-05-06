import requests
import re
import os

url = "https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt"
response = requests.get(url, timeout=10)
response.raise_for_status()  # 自动处理HTTP错误

text = response.text.splitlines()

# 使用正则表达式一次性匹配黑白名单
ad_rules = {"adguard": re.compile(r'^\|\|([^*]+?)\^$'), 
            "whitelist": re.compile(r'^@@\|\|([^*]+?)\^\|$')}

filters = {"adguard": [], "whitelist": []}
for line in text:
    for rule_type, pattern in ad_rules.items():
        if match := pattern.match(line):
            filters[rule_type].append(match.group(1))
            break

# 提取公共描述部分
descriptions = [f"  # {line[2:]}" for line in text[1:6]]

# 确保输出目录存在
os.makedirs("autoupdate", exist_ok=True)

# 统一输出逻辑
for rule_type in filters:
    with open(f"autoupdate/AdGuard{['','Whitelist'][rule_type=='whitelist']}.yaml", "w") as f:
        f.write(f"payload:\n")
        if rule_type == "whitelist":
            f.write("  # Use with AdGuard.yaml\n")
        f.write("\n".join(descriptions) + "\n")
        f.write(f"  # Total: {len(filters[rule_type])}\n")
        f.write("\n".join(f"  - '+.{rule}'" for rule in filters[rule_type]))
