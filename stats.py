def get_num_words(text):
    return len(text.split())

def char_instances(text):
    char_dict = {}

    for char in text:
        lower_char = char.lower()
        if lower_char in char_dict:
            char_dict[lower_char] += 1
        else:
            char_dict[lower_char] = 1

    return char_dict

def kv_instances(text):
    char_dict = char_instances(text)
    kv_dict = []

    for char in char_dict:
        kv_dict.append({ "char" : char, "num" : char_dict[char]})

    return sorted(kv_dict, key=lambda x: x['num'], reverse=True)