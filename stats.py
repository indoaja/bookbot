# function accept text as a string and returns the number of words in the text
def count_words(text):
    words = text.split()
    return len(words)


# function to take text from the book and returns the number of times each character including symbols & spaces appears
def count_character(text):
    # start with blank list
    count ={}
    # convert any character to lowercase to prevent duplicates
    text = text.lower()
    # iterate through the text and count each character
    for char in text:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

# dictionary of characters and their counts and returns a sorted list of dictionaries without lambda
def sort_character(count):
    # sort the dictionary by value in descending order
    sorted_count = {}
    for key in sorted(count, key=count.get, reverse=True):
        sorted_count[key] = count[key]
    return sorted_count

# sort character count excluding spaces and symbols
def sort_character_no_spaces(count):
    # sort the dictionary by value in descending order
    sorted_count = {}
    for key in sorted(count, key=count.get, reverse=True):
        if key.isalpha():
            sorted_count[key] = count[key]
    return sorted_count