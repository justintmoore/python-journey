import pyperclip

# Get the text from clipboard
# Add a star and space as prefix
# copy the text in the clip board

text = pyperclip.paste()  # Returns text in one big string

prefix = "* " 
lines = text.split('\n')  # seperate text by splitting them at the delimitter "\n"

for idx, value in enumerate(lines):  # Get the index and value of the text
    lines[idx] = prefix + value  # As you loop through new string indexes of text, add prefix to each value.

text = '\n'.join(lines)  # Join your new string of text by adding a newline between each text
pyperclip.copy(text)  # Copy the text string to clipboard

