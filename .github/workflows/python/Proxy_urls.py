import requests
from datetime import datetime
from pytz import timezone

response = requests.get("https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/gfw.txt")
urls = response.text.splitlines()[1:]

now = datetime.now(timezone('UTC'))
timestamp = now.astimezone(timezone('Asia/Shanghai')).strftime("%Y-%m-%d %H:%M:%S")

with open("autoupdate/Proxy_urls.yaml", "w") as f:
    f.write(f'''payload:
  # {timestamp}
  # TOTAL: {len(urls)} urls
{'\n'.join(urls)}
''')