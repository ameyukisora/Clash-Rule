import requests
import os
import re

def download_and_filter_ips(url, output_file):
    # 下载文件并检查状态
    response = requests.get(url)
    response.raise_for_status()
    
    # 处理文本内容
    lines = response.text.splitlines()
    ip_pattern = re.compile(r'^\d{1,3}(\.\d{1,3}){3}/\d{1,2}$')
    filtered_ips = (line for line in lines if ip_pattern.match(line))
    
    # 构建YAML内容
    yaml_content = [
        "payload:",
        "  # https://github.com/misakaio/chnroutes2",
        *[f"  {line}" for line in lines[:2]],  # 保留源文件前两行
        *[f"  - '{ip}'" for ip in filtered_ips]
    ]
    
    # 写入文件
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w") as f:
        f.write("\n".join(yaml_content))

if __name__ == "__main__":
    download_and_filter_ips(
        "https://raw.githubusercontent.com/misakaio/chnroutes2/master/chnroutes.txt",
        "autoupdate/chnroutes.yaml"
    )
