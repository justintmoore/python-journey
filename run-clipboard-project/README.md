# Run Based Clipboard Script

## Description  
This Python script uses the `sys` and `pyperclip` modules to create a simple clipboard tool I can launch from the Run dialog box. I call it "run based" because you trigger it by typing the script name into Run (Windows + R), along with a keyword.

I set up a dictionary called `RESPONSES` with three options: PHISHING, SPAM, and SAFE. These are just examples I use for classifying suspicious emails, but you can change them to whatever you want.

The script grabs the first argument after the script name using `sys.argv[1]`, converts it to uppercase (so it always matches the keys in the dictionary), and then checks if that keyword exists. If it does, the corresponding value gets copied to the clipboard using `pyperclip.copy()`. If it doesn’t, the script throws an error message.

Each response includes newline characters so it pastes neatly into documentation or email replies.

## Why I Built It  
As a Desktop Support Tech, I frequently deal with the investigation and analyzing of suspicious emails. Writing out the same kind of detailed response over and over wastes time. I made this script so I can quickly copy standard responses with just a couple of keystrokes. It saves time, keeps my responses consistent, and lets me move on to the next task faster.



## How to Use
1. Save the Python script
2. Press, `Win + R` to open your Run dialog box
3. Type `python C:\Location\of\your\pythonscript.py` followed by an argument defined in the Python dictionary
4. Run box should read, `python C:\Location\of\mclip.py spam` + Enter
5. You will immediately have the SPAM key text value copied to your keyboard where it will read:

### Output
Incident Classification: Unsolicited Commercial Email (SPAM/Marketing).

Reasoning: This email exhibits characteristics of unsolicited commercial communication or bulk marketing. Indicators include: [Indicators].

Recommended Action: [Enter Action].

Analyst Notes: This does not appear to be a direct security threat but contributes to mailbox clutter.
