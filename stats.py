def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    chars_dict = {}
    for char in text.lower():

        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def sort_on(items):
    return items["num"]

def sorted_dicts(dict_input):
    dict_list = []
    for char in dict_input:
        num = dict_input[char]
        dict_rev = {"char": char, "num": num}
        if char.isalpha() == True:
            dict_list.append(dict_rev) 
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
