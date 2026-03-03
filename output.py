from src.sheets_reader import fetch_pending_rows

rows = fetch_pending_rows()

print("Pending Rows:")
for r in rows:
    print(r)