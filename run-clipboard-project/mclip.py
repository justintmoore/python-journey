#! python3

import sys, pyperclip

RESPONSES = {'PHISHING': """Incident Classification: Phishing Attempt\n.
Reasoning: Analysis indicates multiple indicators consistent with a phishing attack, including but not limited to: [Enter Reasoning].\n
Recommended Action: [Enter Action].\n
Analyst Notes: [Additional context].\n""",
'SPAM': """Incident Classification: Unsolicited Commercial Email (SPAM/Marketing).\n
Reasoning: This email exhibits characteristics of unsolicited commercial communication or bulk marketing. Indicators include: [Indicators].\n
Recommended Action: [Enter Action].\n
Analyst Notes: This does not appear to be a direct security threat but contributes to mailbox clutter.""",
'SAFE': """Incident Classification: Legitimate Communication.\n
Reasoning: After thorough analysis, no definitive evidence of phishing, malware, or other malicious intent was identified. The email originated from a legitimate source and its content appears benign.\n
Recommended Action: None required; email delivered to user.\n
Analyst Notes: No further action needed at this time.\n"""}

keyword = sys.argv[1].upper()  # Recieve command line argument and capitilize text.

try:
    # If keyword is in RESPONSE Dictionary, copy text to clipboard
    if keyword in RESPONSES: 
        pyperclip.copy(RESPONSES[keyword])
        print(f"{keyword.title()} was copied to the clipboard!")

except KeyError: 
    # If the keyword is not in RESPONSES, print error message
    print("That key does not exist as a valid response!")
