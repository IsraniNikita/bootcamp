from datetime import datetime, timedelta

today = datetime.now()
future = today + timedelta(days=7)
print("Today:", today)
print("7 days later:", future)
