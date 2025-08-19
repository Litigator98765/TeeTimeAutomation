import json

def get_earliest_tee_time_ids(file_path="tee_times.json", course_id=143, required_slots=4, limit=5):
    # Load the JSON file
    with open(file_path, "r") as f:
        data = json.load(f)

    tee_times = []

    # Loop through the teeSheet entries
    for entry in data.get("data", {}).get("teeSheet", []):
        entry_course_id = entry.get("teeSheetBank", {}).get("teeSheetKey", {}).get("courseId")
        avail_players = entry.get("availPlayers", 0)

        if entry_course_id == course_id and avail_players >= required_slots:
            tee_time_id = entry.get("teeSheetTimeId")
            tee_times.append(tee_time_id)
            print(f"Found tee time ID with {required_slots}+ slots on course {course_id}: {tee_time_id}")

            if len(tee_times) >= limit:
                break

    if not tee_times:
        print(f"No tee times with {required_slots}+ available slots found on course {course_id}.")
    else:
        print(f"Returning first {len(tee_times)} tee time IDs: {tee_times}")

    return tee_times


# Example usage:
# tee_time_ids = get_earliest_tee_time_ids()
