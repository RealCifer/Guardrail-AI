from src.sheets_reader import update_status

def send_message(row):
    """
    Simulate sending SMS/WhatsApp message
    """

    try:
        print(f"\nSending message to {row['Mobile']}")
        print(f"Message: {row['Message']}")

        # Simulated sending success
        update_status(row["_row_number"], "Status", "Sent")

        print("Message Sent Successfully")

    except Exception as e:
        update_status(row["_row_number"], "Status", "Failed")
        print("Message Failed:", e)