def get_num_words(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return len(file_contents.split())

def get_char_counter(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()
        all_chars = {}
        for char in file_contents:
            if char not in all_chars:
                all_chars[char] = 1
            else:
                all_chars[char] += 1
        return all_chars

def sort_on(items):
    return items["num"]

def sort_chars(all_chars):
    original_list = []
    for key,value in all_chars.items():
        original_list.append({"char":key, "num":value})
        original_list.sort(reverse=True,key=sort_on)
    return original_list

