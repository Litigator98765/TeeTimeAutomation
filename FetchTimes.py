import json
import requests
from datetime import datetime, timedelta

date = (datetime.today() + timedelta(days=7)).strftime("%Y%m%d")
courses = "143"
url = f"https://ohiostategolfclub.clubhouseonline-e3.com/api/v1/teetimes/GetAvailableTeeTimes/{date}/{courses}/0/null/false"

# Load cookies
with open("cookies.json", "r") as f:
    raw_cookies = json.load(f)
cookies = {c['name']: c['value'] for c in raw_cookies}

# Make request
response = requests.get(url, cookies=cookies)

if response.status_code == 200:
    data = response.json()
    with open("tee_times.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Tee times saved to tee_times.json")
else:
    print(f"Failed to fetch tee times. Status code: {response.status_code}")
    print(response.text)
