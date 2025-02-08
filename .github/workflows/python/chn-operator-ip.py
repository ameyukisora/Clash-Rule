import requests
from datetime import datetime
import pytz
from typing import List, Optional, Callable

# 常量定义
BASE_URL = "https://raw.githubusercontent.com/gaoyifan/china-operator-ip/ip-lists"
CONFIGURATIONS = [
    {
        "url_suffix": "china.txt",
        "filename": "autoupdate/cn.yaml",
        "filter_func": lambda line: line and line[0].isdigit(),
    },
    {
        "url_suffix": "china6.txt",
        "filename": "autoupdate/cn_v6.yaml",
        "filter_func": lambda line: line and line[0].isalnum(),
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
        print(f"Error fetching {url}: {str(e)}")
        return None


def generate_yaml_content(ips: List[str], timestamp: str) -> str:
    """生成YAML文件内容"""
    return f"""payload:
  # https://github.com/gaoyifan/china-operator-ip
  # {timestamp}
  # TOTAL: {len(ips)}
{'\n'.join(f'  - "{ip}"' for ip in ips)}
"""


def main():
    """主处理逻辑"""
    timestamp = datetime.now(TIMEZONE).strftime("%Y-%m-%d %H:%M:%S")

    for config in CONFIGURATIONS:
        full_url = f"{BASE_URL}/{config['url_suffix']}"
        if (ips := fetch_ips(full_url, config["filter_func"])) is not None:
            try:
                with open(config["filename"], "w", encoding="utf-8") as f:
                    f.write(generate_yaml_content(ips, timestamp))
                print(f"Successfully generated {config['filename']} with {len(ips)} IPs")
            except IOError as e:
                print(f"Error writing to {config['filename']}: {str(e)}")


if __name__ == "__main__":
    main()
