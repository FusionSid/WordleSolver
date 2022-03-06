from datetime import datetime 
import json

date_format = "%d/%m/%y"

start_day = "07/03/22"
today = datetime.now().strftime(date_format)

a, b = datetime.strptime(start_day, date_format), datetime.strptime(today, date_format)

delta = b - a

with open("words.json") as f:
    data = json.load(f)

print(f"\n\033[94m\033[1m\033[4mTodays Word:\u001b[0m\033[92m\n   {data[delta.days]}\u001b[0m\n")