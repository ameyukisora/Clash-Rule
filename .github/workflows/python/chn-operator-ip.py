import requests
from datetime import datetime
import pytz

response = requests.get("https://raw.githubusercontent.com/gaoyifan/china-operator-ip/ip-lists/china.txt")
ips = [ip for ip in response.text.splitlines() if ip and ip[0].isdigit()]

timestamp = datetime.now(pytz.timezone('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S")

with open("autoupdate/cnipcidr.yaml", "w") as f:
    f.write(f'''payload:
  # https://github.com/gaoyifan/china-operator-ip
  # {timestamp}
  # TOTAL: {len(ips)}
{'\n'.join(f"  - '{ip}'" for ip in ips)}
''')