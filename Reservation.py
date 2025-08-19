import json
import requests
import GetTimes

# Get the 5 earliest available tee time IDs from GetTimes.py
tee_time_ids = GetTimes.get_earliest_tee_time_ids(limit=5)
print(f"Earliest available tee time IDs: {tee_time_ids}")

# Load cookies from cookies.json
with open("cookies.json", "r") as f:
    raw_cookies = json.load(f)

# Convert to a dict usable by requests
cookies = {c['name']: c['value'] for c in raw_cookies}

# Base URL
base_url = "https://ohiostategolfclub.clubhouseonline-e3.com/api/v1/teetimes"

# Step 1: ProceedBooking (GET)
def proceed_booking(tee_time_id):
    url = f"{base_url}/ProceedBooking/{tee_time_id}"
    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        print(f"ProceedBooking successful for tee time {tee_time_id}")
        return response.json()
    else:
        print(f"ProceedBooking failed for {tee_time_id}: {response.status_code}")
        return None

# Step 2: CommitBooking (POST)
def commit_booking(tee_time_id):
    url = f"{base_url}/CommitBooking/{tee_time_id}"
    
    payload = {
        "Mode": "Booking",
        "BookingId": 0,
        "OwnerId": 1006706841,  # Primary member
        "editingBookingId": None,
        "AllowJoinUs": False,
        "Holes": 18,
        "Notes": "",
        "Reservations": [
            {
                "ReservationId": 0,
                "ReservationType": 0,
                "FullName": "Max Miller",
                "MemberId": 1006706841,
                "Transport": "0",
                "Caddy": "false",
                "Rentals": ""
            },
            {
                "ReservationId": 0,
                "ReservationType": 0,
                "FullName": "Jack McDonnell",
                "MemberId": 1006663264,
                "Transport": "0",
                "Caddy": "false",
                "Rentals": ""
            },
            {
                "ReservationId": 0,
                "ReservationType": 0,
                "FullName": "Gavin Weis",
                "MemberId": 1006695970,
                "Transport": "0",
                "Caddy": "false",
                "Rentals": ""
            },
            {
                "ReservationId": 0,
                "ReservationType": 0,
                "FullName": "Alexander Bruncak",
                "MemberId": 1006695972,
                "Transport": "0",
                "Caddy": "false",
                "Rentals": ""
            }
        ]
    }
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://ohiostategolfclub.clubhouseonline-e3.com",
        "Referer": "https://ohiostategolfclub.clubhouseonline-e3.com/"
    }

    response = requests.post(url, cookies=cookies, headers=headers, json=payload)
    if response.status_code == 200:
        print(f"✅ CommitBooking successful for tee time {tee_time_id}")
        return response.json()
    else:
        print(f"❌ CommitBooking failed for {tee_time_id}: {response.status_code}")
        print(response.text)
        return None

# --- Main execution ---
for tee_time_id in tee_time_ids:
    print(f"\n--- Trying tee time {tee_time_id} ---")
    proceed_booking(tee_time_id)
    commit_response = commit_booking(tee_time_id)
    print("Booking response:", commit_response)
