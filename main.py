import os
import enum


def read_text_from_file(source_path_to_file):
    if os.path.isfile(source_path_to_file) and os.path.getsize(source_path_to_file) > 0:
        with open(source_path_to_file) as f:
            text = f.read()
            return text





def count_letters(dictionary: dict, text: str):
    for letter in text:
        if letter in dictionary.keys():
            dictionary[letter] += 1
        else:
            dictionary[letter]= 1
    return {key: val for key, val in sorted(dictionary.items(), key=lambda item: item[1], reverse=True)}

# class PATHS():


def choose_min_path(dictionary):
    tmp = dictionary
    while len(tmp.keys()) > 2:
        key = "".join(tmp.keys())[-2:]
        value = sum(list(tmp.values())[-2:])
        del tmp[list(tmp.keys())[-2]]
        del tmp[list(tmp.keys())[-1]]
        tmp[key] = value
        print(tmp, key)
        tmp = {key: val for key, val in sorted(tmp.items(), key=lambda item: item[1], reverse=True)}
    return tmp


def hamming (dictionary):
    tmp = {}
    for k in dictionary.keys():
        tmp=[k] = ''





if __name__ == '__main__':
    source_path_to_file = ''
    text_from_file = read_text_from_file(source_path_to_file)
    dictionary = {}
    dictionary = count_letters(dictionary, text_from_file)
    for k in dictionary:
        print(k, dictionary[k])
    tmp = choose_min_path(dictionary)
    print('\n\n\n\n',  tmp)
    for k in tmp.keys():
        print(k)

    # print(dictionary)
    # print(dictionary.keys())
    # print(dictionary.values())
    # sum_of_chars = sum(dictionary.values())
    # print(sum_of_chars)






