import requests
import os
from datetime import datetime
import pytz
from typing import List, Optional, Callable

# 常量定义
BASE_URL = "https://raw.githubusercontent.com/gaoyifan/china-operator-ip/ip-lists"
CONFIGURATIONS = [
    {
        "url_suffix": "china.txt",
        "filename": "autoupdate/cn.yaml",
        "filter_func": lambda line: line and line[0].isdigit(),  # IPv4地址过滤
    },
    {
        "url_suffix": "china6.txt",
        "filename": "autoupdate/cn_v6.yaml",
        "filter_func": lambda line: line and line[0].isalnum(),  # IPv6地址过滤
    },
]
TIMEOUT = 10
TIMEZONE = pytz.timezone("Asia/Shanghai")


def fetch_ips(url: str, filter_func: Callable[[str], bool]) -> Optional[List[str]]:
    """从指定URL获取并过滤IP地址列表"""
    try:
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()
        return [line for line in response.text.splitlines() if filter_func(line)]
    except requests.exceptions.RequestException as e:
        print(f"请求失败 {url}: {str(e)}")
        return None


def generate_yaml_content(ips: List[str], timestamp: str) -> str:
    """生成YAML文件内容"""
    total = len(ips)
    ip_lines = '\n'.join(f'  - "{ip}"' for ip in ips)
    return f"""payload:
  # https://github.com/gaoyifan/china-operator-ip
  # 更新时间: {timestamp}
  # 条目总数: {total}
{ip_lines}
"""


def ensure_directory_exists(filepath: str) -> None:
    """确保文件所在目录存在"""
    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)


def write_yaml_file(filepath: str, content: str) -> None:
    """安全写入文件"""
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"成功生成 {filepath}，包含 {len(content.splitlines()) - 4} 个IP条目")
    except IOError as e:
        print(f"写入文件失败 {filepath}: {str(e)}")


def main():
    """主处理逻辑"""
    timestamp = datetime.now(TIMEZONE).strftime("%Y-%m-%d %H:%M:%S")

    for config in CONFIGURATIONS:
        full_url = f"{BASE_URL}/{config['url_suffix']}"
        print(f"正在获取: {full_url}")
        
        if (ips := fetch_ips(full_url, config["filter_func"])) is not None:
            ensure_directory_exists(config["filename"])
            yaml_content = generate_yaml_content(ips, timestamp)
            write_yaml_file(config["filename"], yaml_content)


if __name__ == "__main__":
    main()
