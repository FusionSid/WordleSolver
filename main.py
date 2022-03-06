from datetime import datetime 
from flask import Flask, render_template
import json

app = Flask(__name__)

def get_word():
    date_format = "%d/%m/%y"

    start_day = "07/03/22"
    today = datetime.now().strftime(date_format)

    a, b = datetime.strptime(start_day, date_format), datetime.strptime(today, date_format)

    delta = b - a

    with open("words.json") as f:
        data = json.load(f)

    answer = data[delta.days]
    
    print(f"\n\033[94m\033[1m\033[4mTodays Word:\u001b[0m\033[92m\n   {answer}\u001b[0m\n")

    return answer
    
@app.route("/")
def home():
    answer = get_word()

    return f"<h1><center>{answer}</center></h1>"

app.run()