import time
import requests
import webbrowser
from datetime import datetime 

from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController

keyboard = KeyboardController()
mouse = MouseController()

def get_word():
    url = "https://www.nytimes.com/games/wordle/main.3d28ac0c.js"

    resp = requests.get(url).content.decode()

    resp = resp.split("var Ma=")[1]
    resp = resp.split("]")[0]
    resp+="]"

    date_format = "%d/%m/%y"

    start_day = "11/04/22"
    today = datetime.now().strftime(date_format)

    a, b = datetime.strptime(start_day, date_format), datetime.strptime(today, date_format)

    delta = b - a

    data = eval(resp)
    data = data[297:]

    answer = data[delta.days-1]

    return answer

word = get_word()

webbrowser.open("https://www.nytimes.com/games/wordle/index.html")

time.sleep(2)
mouse.click(button=Button.left)
time.sleep(2)
keyboard.type(word)
time.sleep(2)
keyboard.press(Key.enter)