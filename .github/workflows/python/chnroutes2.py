import requests
import os

url = "https://raw.githubusercontent.com/misakaio/chnroutes2/master/chnroutes.txt"
response = requests.get(url)
lines = response.text.split("\n")

# filter out empty elements
lines = list(filter(None, lines))

# create file
os.makedirs("autoupdate", exist_ok=True)
output_file = "autoupdate/chnroutes.yaml"

output_content = f'''payload:
    # https://github.com/misakaio/chnroutes2"
    {lines[0]}"
    {lines[1]}"
'''

with open(output_file, "w") as f:
    f.write(output_content)
    for line in lines[2:]:
        f.write(f"  - '{line}'\n")