import subprocess
import sys

# Step 1: Run the Node.js login script to refresh cookies
try:
    print("Running login.js to get fresh cookies...")
    result = subprocess.run(
        ["node", "login.js"],
        check=True,
        capture_output=True,
        text=True
    )
    print(result.stdout)
    print("Login complete.\n")
except subprocess.CalledProcessError as e:
    print("Error running login.js:")
    print(e.stderr)
    sys.exit(1)

# Step 2: Fetch tee times and save to tee_times.json
try:
    print("Fetching tee times...")
    result = subprocess.run(
        ["python3", "FetchTimes.py"],  # This script hits the GetAvailableTeeTimes endpoint
        check=True,
        capture_output=True,
        text=True
    )
    print(result.stdout)
    print("Tee times fetched.\n")
except subprocess.CalledProcessError as e:
    print("Error running FetchTimes.py:")
    print(e.stderr)
    sys.exit(1)

# Step 3: Run the Reservation script
try:
    print("Running Reservation.py to attempt bookings...")
    result = subprocess.run(
        ["python3", "Reservation.py"],
        check=True,
        capture_output=True,
        text=True
    )
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print("Error running Reservation.py:")
    print(e.stderr)
    sys.exit(1)
