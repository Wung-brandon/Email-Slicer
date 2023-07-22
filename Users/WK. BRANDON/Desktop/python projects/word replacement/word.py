
def replace_word():
    str = 'hey hey hi hi. How are you my name is brandon'
    word = input('what the word you want to replace:')
    word_replace = input('Enter the word replacement:')
    print(str.replace(word, word_replace))
    
replace_word()