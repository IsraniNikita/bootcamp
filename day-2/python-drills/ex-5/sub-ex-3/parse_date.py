from datetime import datetime

date_str = "2024-01-01"
date_obj = datetime.strptime(date_str, "%Y-%m-%d")
print("Parsed datetime object:", date_obj)
