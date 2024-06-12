import requests
from datetime import datetime
import pytz

response = requests.get("https://raw.githubusercontent.com/gaoyifan/china-operator-ip/ip-lists/china.txt")
ips = [ip for ip in response.text.splitlines() if ip and ip[0].isdigit()]

response6 = requests.get("https://raw.githubusercontent.com/gaoyifan/china-operator-ip/ip-lists/china6.txt")
ips6 = [ip6 for ip6 in response6.text.splitlines() if ip6 and ip6[0].isalnum()]

timestamp = datetime.now(pytz.timezone('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S")

with open("autoupdate/cnipcidr.yaml", "w") as f:
    f.write(f'''payload:
  # https://github.com/gaoyifan/china-operator-ip
  # {timestamp}
  # TOTAL: {len(ips)}
{'\n'.join(f"  - '{ip}'" for ip in ips)}
''')

with open("autoupdate/cnipcidr6.yaml", "w") as f:
    f.write(f'''payload:
  # https://github.com/gaoyifan/china-operator-ip
  # {timestamp}
  # TOTAL: {len(ips6)}
{'\n'.join(f"  - '{ip6}'" for ip6 in ips6)}
''')