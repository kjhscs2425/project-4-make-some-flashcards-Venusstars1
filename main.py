import random
flash_card = {
    "ants": "colony", 
    "buffalo": "gang", 
    "crows": "murder", 
    "cheetas": "coalition",
    "donkeys": "drove"
}

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
    return questions_right, questions_wrong
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