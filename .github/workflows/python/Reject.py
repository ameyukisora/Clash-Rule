import re
import requests
from datetime import datetime
from pytz import timezone

# 下载文件
response = requests.get("https://raw.githubusercontent.com/dler-io/Rules/main/Surge/Surge%203/Provider/Reject.list")

# 读取文件内容
lines = response.text.splitlines()

# 定义正则表达式
domain_suffix_regex = re.compile(r"^DOMAIN-SUFFIX,(.*)")
domain_regex = re.compile(r"^DOMAIN,(.*)")

# 提取内容
results = []
domain_suffix_count = 0
domain_count = 0
for line in lines:
    match = domain_suffix_regex.match(line)
    if match:
        domain_suffix_count += 1
        domain = match.group(1)
        results.append("  - '+." + domain + "'")
    else:
        match = domain_regex.match(line)
        if match:
            domain_count += 1
            domain = match.group(1)
            results.append("  - '" + domain + "'")

# 生成统计数据
now = datetime.now(timezone('UTC'))
timestamp = now.astimezone(timezone('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S")
total_count = domain_suffix_count + domain_count

# 写入目标文件
with open("/autoupdate/Reject.yaml", "w") as f:
    f.write("payload:\n")
    f.write("  # " + timestamp + "\n")
    f.write("  # DOMAIN-SUFFIX: " + str(domain_suffix_count) + ", DOMAIN: " + str(domain_count) + "\n")
    f.write("  # TOTAL: " + str(total_count) + "\n")
    f.writelines(results)