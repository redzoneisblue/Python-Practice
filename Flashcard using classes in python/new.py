class flashcard:
    def __init__(self, word,  meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):

        #we will return a string
        return self.word+' : '+self.meaning
    
flash = []
print("Welcome to flashcard application !")

#the following loop will be repeated untill user stops to add the flashcard

while(True):
    word = input("enter the word you want to add to flashcard: ")
    meaning = input("enter the meaning of the word : ")

    flash.append(flashcard(word, meaning))
    with open("flashcards.txt", "a+") as flasher:
        for wordmeaning in flash:
            while flasher.read()!=wordmeaning:
                flasher.write(str(wordmeaning)+"\n")
                break
                
            

    option = input("enter T, if you want to add another flashcard : ")

    if option == "t" or option == "T":
        continue
    else:
        break

#printing all the flashcards
with open("flashcards.txt", "r") as reader:
    flash = reader.readlines()
    print("\n Your flashcards")
    for i in flash: 
        print(">", i)

