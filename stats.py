def get_num_words(text: str):
    spl = text.split()
    return len(spl)


def get_num_chars(text: str):
    chars_dc = {}
    
    for char in text:
        char = char.lower()

        if char not in chars_dc:
            chars_dc[char] = 0
        chars_dc[char]+=1
    
        
    return chars_dc

def sort_on(e):
        return e['count']

def sort_num_chars(char_dc: dict):
    sorted_dc = []
    
    for i in char_dc.keys():
        sorted_dc.append({'char': i, 'count': char_dc[i]})

    sorted_dc.sort(key=sort_on, reverse=True)

    return sorted_dc


    
