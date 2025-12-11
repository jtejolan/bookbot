def count_words(text):
    words_list = text.split()
    num = len(words_list)
    return num

def count_characters(text):
    char_count = {}
    lowered_text = text.lower()

    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


        
def sort_dict(char_count_dict):
    dictionaries = []
    for char, count in char_count_dict.items():
        new_dict = {"char": char, "num": count}
        dictionaries.append(new_dict)

    def sort_on(items):
        return items["num"]

    dictionaries.sort(reverse=True, key=sort_on)
    return dictionaries
