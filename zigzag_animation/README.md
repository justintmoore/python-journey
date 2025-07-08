# Automate The Boring Stuff By. Al Sweigart

## Description
This is a simple Python script that creates a terminal based zig zag animation, using a bouncing row of asterisks ('********"). 
The stars shift, back and forth simulating a horizonal "bounce" effect using indentation.
The animation will continue to run until a user interrupts using the `Ctrl+ C` command

## How It Works
The script uses an 'indent' counter to control how many spaces are printed before each line of asterisks. It is controlled through the use of 'if' conditional statements when the indentations reach a max, and min.
A conditional statement is set using the flag (`indentIncreasing`) which determines whether the indent is increasing or decreasing.
The `time.sleep(0.1)` creates a short pause between each frame to control animation speed.
I tried my hand at `try/except` blocks to gracefully exit the loop when `Ctrl+C` is pressed.

