str ="mississippi"

def make_dict(x):
    dictionary={}
    for letter in x:
        dictionary[letter]=1+ dictionary.get(letter,0)
    return dictionary

def most_frequent(str):
    letters=[letter.lower() for letter in str if letter.isalpha()]
    dictionary=make_dict(letters)
    result=[]
    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True)
    for count, letter in result:
        print(letter, count)
        
most_frequent(str)
