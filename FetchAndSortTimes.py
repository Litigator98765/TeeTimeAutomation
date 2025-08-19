import json
import requests
from datetime import datetime, timedelta

def get_earliest_tee_time_ids(days_ahead=5, course_id=143, required_slots=4, limit=5):
    # Build date string
    date = (datetime.today() + timedelta(days=days_ahead)).strftime("%Y%m%d")
    print(date)
    url = f"https://ohiostategolfclub.clubhouseonline-e3.com/api/v1/teetimes/GetAvailableTeeTimes/{date}/{course_id}/0/null/false"

    # Load cookies
    with open("cookies.json", "r") as f:
        raw_cookies = json.load(f)
    cookies = {c['name']: c['value'] for c in raw_cookies}

    # Fetch tee times
    response = requests.get(url, cookies=cookies)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch tee times. Status: {response.status_code} | {response.text}")

    data = response.json()
    tee_times = []

    # Parse teeSheet for matching course and available slots
    for entry in data.get("data", {}).get("teeSheet", []):
        entry_course_id = entry.get("teeSheetBank", {}).get("teeSheetKey", {}).get("courseId")
        avail_players = entry.get("availPlayers", 0)

        if entry_course_id == course_id and avail_players >= required_slots:
            tee_times.append(entry.get("teeSheetTimeId"))

            if len(tee_times) >= limit:
                break

    if not tee_times:
        print(f"No tee times with {required_slots}+ slots found on course {course_id}.")
    else:
        print(f"Returning first {len(tee_times)} tee time IDs: {tee_times}")

    return tee_times


