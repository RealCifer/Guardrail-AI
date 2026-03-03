from src.sheets_reader import fetch_pending_rows, update_status
from src.validator import validate_row
from src.compliance import classify_message

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

    if classification == "Approved":
        print("Message Approved")
        update_status(row["_row_number"], "Status", "Pending_Compliance_Approved")
    else:
        print("Message Blocked")
        update_status(row["_row_number"], "Status", "Blocked")