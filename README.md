# WordleSolver
Goes to chrome and types in the correct answer to wordle

If you right click and click inspect on [wordle](https://www.nytimes.com/games/wordle/index.html) and then go to sources you will see a file named `main.bfba912f.js`

I downloaded the file then formatted it.

After a quick google search of yesterday's answer i typed cmd-f and put in yesterdays answer. What pops up in a word which is in a list of words. So i typed the next word in the list (after yesterdays word) and it worked.

So this script basicaly just gets the difference of days between that day and the current day and then uses that to word.

In autosolve/autosolve.py It will open chrome, got to the website, click to move the tutorial thing away and then it will type in the word and hit enter

In web/main.py it just shows the word of the day on a basic flask site. Also prints it to terminal.


