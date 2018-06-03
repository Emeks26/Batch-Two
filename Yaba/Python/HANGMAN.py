#class project
import random

word_list = ["Holiday","Vacation","Lagos","Justice","League","Barbecue","Beyonce"]
username = str(input("PLEASE ENTER YOUR NAME == "))
limit = 3
random_value = random.randint(0, len(word_list) - 1)
word_length = len(word_list[random_value])
hidden_word = word_list[random_value].lower()
sub_word = ""
#create space for word
for i in hidden_word:
    sub_word += i + " "

output = "_ " * word_length
print(output)

def update(letter):
    global sub_word
    global output
    result = ""

    for i in range(len(sub_word)):
        if(letter == sub_word[i]):
            result += letter.lower()
        elif(output[i] != "_"):
             result += output[i]
        elif(output[i] == " "):
            result += " "
        else:
            result += "_"


    return result

while limit > 0:
    guess = input("GUESS A LETTER == ").lower()

    if guess in hidden_word:
        output = update(guess)
        print(output)
    else:
        print ("LETTER NOT AVAILABLE")
        limit -= 1

    #check if you finished and won
    if(output.find("_") == -1):
        print("\n ======= " + sub_word.upper() + " ========")
        print("======  WELL DONE " + username.upper() + " ========")
        break

#check if fail to complete
if limit < 1:
    print("\n ======= " + sub_word.upper() + " ========")
    print(" ======= SORRY " + username.upper() + " , YOU RAN OUT OF CHANCES =======") 

        

