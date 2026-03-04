from src.sheets_reader import fetch_pending_rows, update_status
from src.validator import validate_row
from src.compliance import classify_message
from src.scheduler_engine import schedule_message

rows = fetch_pending_rows()

for row in rows:
    print(f"\nProcessing row: {row['_row_number']}")

    is_valid, parsed_dt, errors = validate_row(row)

    if not is_valid:
        print("Validation Errors:", errors)
        update_status(row["_row_number"], "Status", "Invalid")
        continue

    print("Validation Passed")

    classification = classify_message(row["Message"])
    print("Compliance Classification:", classification)

    update_status(row["_row_number"], "Compliance_flag", classification)

    if classification != "Approved":
        update_status(row["_row_number"], "Status", "Blocked")
        print("Message Blocked")
        continue

    print("Message Approved")

    schedule_message(row, parsed_dt)

    update_status(row["_row_number"], "Status", "Scheduled")