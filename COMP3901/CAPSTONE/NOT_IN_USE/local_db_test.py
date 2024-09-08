from local_sql import CaptureDatabase

capture_db = CaptureDatabase(host="localhost", user="robin", password="password123", database="Capture")
capture_db.create_table()
ids = capture_db.get_ids()
print("IDs:", ids)
# Perform other operations as needed
capture_db.close_connection()