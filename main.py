import random
import json
import os
flash_card = {
    "ants": "colony", 
    "buffalo": "gang", 
    "crows": "murder", 
    "cheetas": "coalition",
    "donkeys": "drove"
}


data_file = "quiz.json"

def load_data():
    if os.path.exists(data_file):
        with open(data_file, "r") as f:
            return json.load(f)
    else:
            print("Error: quiz.json is corrupted. Resetting file.")
            return {}
    return {}

def save_data(questions_right, questions_wrong):
    data = load_data() 
    data["list"].append({
        "questions_right": questions_right,
        "questions_wrong": questions_wrong
    })
    with open(data_file, "w") as f:
        json.dump(data, f, indent=4)

def flash_card_round():
    questions_right = []
    questions_wrong = []
    random_questions = random.sample(list(flash_card.keys()), k=5)
    for random_question in random_questions:
        user_response = input("What do you call a group of " + random_question + "? Answer: a ")
        if user_response == flash_card[random_question]:
            print("Correct!")
            questions_right.append(random_question)
        else:
            print("sorry, that is incorrect")
            questions_wrong.append(random_question)
            print(f"the correct answer is a {flash_card[random_question]}")
    print(f"Great Job! You answered {len(questions_right)} questions correctly and {len(questions_wrong)} questions wrong")
    print(f"You got {list(questions_right)} correct and {list(questions_wrong)} wrong")
    save_data(questions_right, questions_wrong)
    def go_again():
        restart = input("\nDo you want to play again? (yes/no): ")
        if restart == "yes" or restart == "Yes":
            flash_card_round()
        else:
            with open (data_file, "r") as f:
                sum = json.load(f)
                print(sum)
    go_again()
flash_card_round()



"""
"emus": "mob", 
"flamingos": flamboyance", 
"geese": "gaggle", 
"hyenas": "cackle", 
"jellyfish": "smack",
"kangaroos": "troop",
"lemurs": "conspiracy", 
"moles": "labor",
"nightingales": "watch",
"owls": "parliament",
"ponies": "string", 
"rattlesnakes": "rhumba",
"sharks": "shiver", 
"turkeys": "gang",
"wombats": "wisdom"
"""

"""
data = {"questions_right": questions_right,
     "questions_wrong": questions_wrong}
with open ("d.json", "w") as f:
    json.dump(data, f)

with open ("d.json", "r") as f:
    d = json.load(f)
"""

 #print("Thanks for playing! See you next time.")
                #print(f"""Here are some summary stats. 
#In this round, you answered {len(questions_right)} questions correctly 
#and {len(questions_wrong)} questions wrong 
#and you got {list(questions_right)} correct and {list(questions_wrong)} wrong""")
                #print(f"""Here are all of the stats from previous runs of the game. Brace yourself, it might be a lot
                  #You got {sum[list(len(questions_right))]} questions right 

                  #and {sum[list(len(questions_wrong))]} questions wrong.
                  
                  #The questions you got right were {sum[list(list(questions_right))]}
                  
                  #The questions you got wrong were {sum[list(list(questions_wrong))]}""")