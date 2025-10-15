def get_book_text(filepath):
    with open(filepath, "r") as file:
        text = file.read()
    return text


def get_num_words(filepath):
    text = get_book_text(filepath)
    return len(text.split())


def get_char_count(text):
    text = text.lower()
    char_dict = {}
    for i in range(len(text)):
        if text[i] not in char_dict:
            char_dict[text[i]] = 0

        char_dict[text[i]] += 1

    return char_dict

def sort_on(items):
    return items["num"]

def get_sorted_char_dict(char_dict):
    sorted_char_dict = []
    for item in char_dict: 
        item = {"char": item, "num": char_dict[item]}
        sorted_char_dict.append(item)
    
    sorted_char_dict.sort(reverse=True, key=sort_on)
    return sorted_char_dict
