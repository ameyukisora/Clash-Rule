import requests
import re
from pathlib import Path

# 将正则表达式预编译为模块级常量，避免每次调用函数都重新编译
IP_PATTERN = re.compile(r'^\d{1,3}(\.\d{1,3}){3}/\d{1,2}$')

def generate_chroutes_yaml(url: str, output_file: str):
    """下载 IP 列表并生成 YAML 文件。"""
    # 1. 下载文件
    response = requests.get(url)
    response.raise_for_status()
    
    # 2. 处理文本并构建 YAML 内容
    lines = response.text.splitlines()
    
    # 使用生成器表达式过滤 IP
    filtered_ips = (line for line in lines if IP_PATTERN.match(line))
    
    yaml_content = [
        "payload:",
        "  # https://github.com/misakaio/chnroutes2",
        # 保留源文件前两行
        *[f"  {line}" for line in lines[:2]],
        # 添加过滤后的 IP
        *[f"  - '{ip}'" for ip in filtered_ips]
    ]
    
    # 3. 写入文件 (使用 pathlib)
    output_path = Path(output_file)
    # 自动创建父目录
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # write_text 是一个便捷方法，自动处理文件打开和关闭
    output_path.write_text("\n".join(yaml_content), encoding='utf-8')

if __name__ == "__main__":
    generate_chroutes_yaml(
        "https://raw.githubusercontent.com/misakaio/chnroutes2/master/chnroutes.txt",
        "autoupdate/chnroutes.yaml"
    )
