def print_upper_words(words):
    """
    Prints every word in the list uppercased.
    """
    for word in words:
      print( word.upper() )


def only_prints_words_that_start_with_e_or_E(words):
    """
    Only uppercase and prints words that start with e or E.
    """
    for word in words:
        if word.startswith("E") or word.startswith('e'):
            print(word.upper())
    
    

def print_words_that_start_with_args_to_uppercased(words, params): 
    """
    Print each word uppercased if it starts with one of the given agruments.
    """
    for word in words:
        for letter in params:
            if word.startswith(letter):
                print(word.upper())
