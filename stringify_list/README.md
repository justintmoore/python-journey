# Automate The Boring Stuff By Al Sweigart

## Description  
This Python script takes a list of strings and returns a new string with commas separating each item, and the word 'and' before the final item.  
For example, `['apples', 'bananas', 'tofu', 'cats']` becomes `'apples, bananas, tofu, and cats'`.  
This is helpful for cleanly formatting list output for users or display.

## How It Works  
The `format_list()` function takes a list as input and processes it as follows:
Initializes an empty string `result_string` to build the final output.
Calculates the index of the last item in the list (`end_idx`) to know where to place `"and"`.
Uses `enumerate()` to loop through each item in the list along with its index.
If the current index equals the last index, it appends `'and <item>'` without a comma.
Otherwise, it appends `'<item>, '` with a comma and space.
Returns the final formatted string.

Finally, the function is called with a list of sample strings (`spam`), and the result is printed to the console.
