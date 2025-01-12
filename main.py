
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    character_dicts = list_of_character_dicts(num_characters)
    print(f"-- Begin report of {book_path} --")
    print(f"{num_words} words found in the document")
    for dicts in character_dicts: 
        for key, value in dicts.items():
            print(f"The {key} character was found {value} times")
    print("--- End report ---")

def sort_on(dict):
    for key in dict: 
        return dict[key]

def list_of_character_dicts(character_dict): 
    character_dicts = []
    for key, value in character_dict.items(): 
        character_dicts.append({key: value})
    character_dicts.sort(reverse=True, key=sort_on)
    return character_dicts


def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_characters(text):
    characters = {}
    lowered_text = text.lower()
    for character in lowered_text: 
        if character not in characters: 
            characters[character] = 0 
        characters[character] += 1  
    return characters


def get_book_text(path):
    with open(path) as f:
        return f.read() 


main()



