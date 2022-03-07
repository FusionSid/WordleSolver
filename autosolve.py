from datetime import datetime 
import webbrowser
import json
import time
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController

keyboard = KeyboardController()
mouse = MouseController()

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

word = get_word()

webbrowser.open("https://www.nytimes.com/games/wordle/index.html")
time.sleep(2)
mouse.click(button=Button.left)

keyboard.type(word)
time.sleep(1)
keyboard.press(Key.enter)