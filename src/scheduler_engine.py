from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from src.sender import send_message

scheduler = BackgroundScheduler()
scheduler.start()

def schedule_message(row, parsed_datetime):
    """
    Schedule message sending
    """

    scheduler.add_job(
        send_message,
        'date',
        run_date=parsed_datetime,
        args=[row],
        id=str(row["_row_number"]),
        replace_existing=True
    )

    print(f"Message scheduled for {parsed_datetime}")