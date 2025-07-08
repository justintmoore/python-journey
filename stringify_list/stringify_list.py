spam = ['apples', 'bananas', 'tofu', 'cats']

def format_list(item_list):
    result_string = "" # Create an empty string
    end_idx = len(item_list) -1 # Create an index that represents the last item

    for idx, item in enumerate(item_list): # Enumerate through list, providing index and values
        if idx == end_idx:
            result_string += f"and {str(item)}" # If it's the last index, concat the string in this format
        elif idx != end_idx: 
            result_string += f"{str(item)}, " # If it's anything besides the last index, concat the string in this format
    return result_string # Return the newly created string


print(format_list(spam)) # Call the function and print out the returned value


# Output
'apples, bananas, tofu, and cats'
