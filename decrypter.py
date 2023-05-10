def generate_lexicon():
    file = open('lexicon.txt','r')
    lexicon = file.readlines()
    file.close()
    for i in range(58110):
        word = lexicon[0].strip()
        lexicon.pop(0)
        lexicon.append(word)
    return lexicon

def sentence_to_words(sentence):
    word = ""
    words = []
    for character in sentence:
        if character != ' ':
            word = word + character
        else:
            words.append(word)
            word = ""
    words.append(word)
    return words

def find_message_structure(message):
    structure = []
    characters_index = {}
    for character in message:
        if character in decrypted_characters:
            structure.append(character)
        elif character in characters_index.keys():
            structure.append(characters_index[character])
        else:
            characters_index.update({character : len(characters_index.keys())+1})
            structure.append(characters_index[character])
    return structure

def find_structure_match(structure):
    matched_words = []
    for word in lexicon:
        if find_message_structure(word) == structure:
            matched_words.append(word)
    return matched_words

def generate_message(word_lists, message = ''):
    if not word_lists:
        message = message.rstrip()
        if find_message_structure(message) == message_structure:
            print(message)
        return
    first = word_lists[0]
    rest = word_lists[1:]
    for word in first:
        generate_message(rest, message + word + ' ')

print("Enter encrypted message:")
encrypted_message = input()
print("Which of these characters are correct?")
decrypted_characters = input()

lexicon = generate_lexicon()
message_structure = find_message_structure(encrypted_message)
encrypted_words = sentence_to_words(encrypted_message)
word_structures = []
for encrypted_word in encrypted_words:
    word_structures.append(find_message_structure(encrypted_word))
possible_words = []
for word_structure in word_structures:
    possible_words.append(find_structure_match(word_structure))
generate_message(possible_words)