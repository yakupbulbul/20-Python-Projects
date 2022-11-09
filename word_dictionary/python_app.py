# have a python dictionary that has a key/value that represent a word and it's defination
# collect input from the user, input is word
# check if the word is in the dictionary 

from PyDictionary import PyDictionary 


dictionary = PyDictionary("eyes", "glass", "head")

print(dictionary.getMeanings())


# while True:
#     word  = input("Enter your word: ")
#     if word =="":
#         break
#     print(dictionary.meaning(word))



















# def main():
#     word_dictionary = {
#         "hi": "a way of gretting",
#         "eyes": "an organ for seeing",
#         "earth": "planet in space",

#     }



#     while True:
#         word = input("Enter a word: ")
#         if word == "":
#             break
#         if word in word_dictionary: 
#             print(word, ":", word_dictionary[word])



    

# main()