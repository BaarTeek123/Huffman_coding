import os


class Node:
    # contructor
    def __init__(self, char: str, freq=0, huffman=''):
        self.__character = char
        self.__frequency = freq
        self.__huffman_code = huffman

    def set_huffman_code(self, node: bool):
        if node:
            self.__huffman_code += '1'
        else:
            self.__huffman_code += '0'

    def get_character(self):
        return self.__character

    def get_freq(self):
        return self.__frequency

    def get_huffman(self):
        return self.__huffman_code

    def __eq__(self, other):
        return self.__character == other.get_character()

    def __str__(self): #print(node)
        return 'Character: ' + str(self.__character) + '\n\tFrequency: ' + str(
            self.__frequency) + '\n\tBit code: ' + self.__huffman_code


def read_text_from_file(source_path_to_file: str) -> str:
    if os.path.isfile(source_path_to_file) and os.path.getsize(source_path_to_file) > 0:
        with open(source_path_to_file) as f:
            text = f.read()
            return text


def count_letters(text: str) -> list:
    dictionary = {}
    nodes = []
    for letter in text:
        if letter in dictionary.keys():
            dictionary[letter] += 1
        else:
            dictionary[letter] = 1
    dictionary = {key: val for key, val in sorted(dictionary.items(), key=lambda item: item[1])}
    for k in list(dictionary.keys()):
        nodes.append(Node(k, dictionary[k]))
    return nodes


def choose_min_path(sorted_nodes):
    sorted_nodes[0].set_huffman_code(True)
    sorted_nodes[1].set_huffman_code(False)


def update_node(sorted_nodes, huffman_code):
    node = Node(sorted_nodes[0].get_character() + sorted_nodes[1].get_character(),
                sorted_nodes[0].get_freq() + sorted_nodes[1].get_freq(), sorted_nodes[0].get_huffman())
    if len(sorted_nodes[0].get_character()) == 1:
        huffman_code.append(sorted_nodes[0])
    else:
        for char in huffman_code:
            if char.get_character() in sorted_nodes[0].get_character():
                char.set_huffman_code(True)

    if len(sorted_nodes[1].get_character()) == 1:
        huffman_code.append(sorted_nodes[1])
    else:
        for char in huffman_code:
            if char.get_character() in sorted_nodes[1].get_character():
                char.set_huffman_code(False)
    del sorted_nodes[:2]
    sorted_nodes.append(node)
    return sorted(sorted_nodes, key=lambda node: node.get_freq())


def find_huffman_by_character(nodes, character):
    for node in nodes:
        if node.get_character() == character:
            return node


if __name__ == '__main__':
    source_path_to_file = 'C:/Users/user/Desktop/tmp_praca/tmp.txt'
    text_from_file = read_text_from_file(source_path_to_file)
    huffman = count_letters(text_from_file)
    huffman_code_list = []

    while len(huffman) != 1:
        choose_min_path(huffman)
        huffman = update_node(huffman, huffman_code_list)

    ##################################################################################

    compressed_text = ''
    for char in text_from_file:
        compressed_text += find_huffman_by_character(huffman_code_list, char).get_huffman()
    print("Original text: ", text_from_file)
    print("Text size: ", len(text_from_file) * 8, 'bits')
    print("Compressed text: ", compressed_text)
    print("Compressed text size: ", len(compressed_text), 'bits')
    for node in sorted(huffman_code_list, key=lambda node: node.get_freq(), reverse=True):
        print(node)
