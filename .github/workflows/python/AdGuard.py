import requests
import re
import os

url = "https://adguardteam.github.io/AdGuardSDNSFilter/Filters/filter.txt"

# 添加错误处理，增强健壮性
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # 自动处理HTTP错误
except requests.exceptions.RequestException as e:
    print(f"下载过滤文件时发生错误: {e}")
    exit() # 下载失败则退出

text = response.text.splitlines()

# 使用正则表达式一次性匹配黑白名单
# adguard 规则以 || 开头，^ 结尾，提取中间的域名部分
# whitelist 规则以 @@|| 开头，^ 结尾，提取中间的域名部分
ad_rules = {"adguard": re.compile(r'^\|\|([^*]+?)\^$'),
            "whitelist": re.compile(r'^@@\|\|([^*]+?)\^\|$')}

filters = {"adguard": [], "whitelist": []}
for line in text:
    # 尝试匹配 AdGuard 规则
    if match := ad_rules["adguard"].match(line):
        filters["adguard"].append(match.group(1))
    # 尝试匹配白名单规则
    elif match := ad_rules["whitelist"].match(line):
        filters["whitelist"].append(match.group(1)) # 白名单也先收集起来

# 将白名单转换为集合，方便快速查找
whitelist_set = set(filters["whitelist"])

# 过滤 AdGuard 规则，移除白名单中的元素
# 创建一个新的列表存放过滤后的 AdGuard 规则
filtered_adguard_rules = [rule for rule in filters["adguard"] if rule not in whitelist_set]

# 提取公共描述部分
descriptions = [f"  # {line[2:]}" for line in text[1:6]]

# 确保输出目录存在
os.makedirs("autoupdate", exist_ok=True)

# 只输出过滤后的 AdGuard 规则到 AdGuard.yaml
output_file_path = "autoupdate/AdGuard.yaml"
with open(output_file_path, "w", encoding='utf-8') as f:
    f.write("payload:\n")

    # 写入描述信息
    if descriptions:
        f.write("\n".join(descriptions) + "\n")

    # 写入过滤后的规则总数
    f.write(f"  # Total: {len(filtered_adguard_rules)}\n")

    # 写入过滤后的 AdGuard 规则列表
    # 保持原 AdGuard 输出的格式: - '+.规则'
    for rule in filtered_adguard_rules:
        f.write(f"  - '+.{rule}'\n")

print(f"过滤后的 AdGuard 规则已生成到: {output_file_path}")
print(f"原始 AdGuard 规则数量: {len(filters['adguard'])}")
print(f"白名单规则数量: {len(filters['whitelist'])}")
print(f"过滤后 AdGuard 规则数量: {len(filtered_adguard_rules)}")
