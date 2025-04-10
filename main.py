import random
import json
import os
flash_card = {
    "ants": "colony", 
    "buffalo": "gang", 
    "crows": "murder", 
    "cheetas": "coalition",
    "donkeys": "drove",
    "emus": "mob", 
    "flamingos": "flamboyance", 
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
    animals = list(flash_card.keys())
    questions_right = []
    questions_wrong = []
    random_questions = random.sample(list(flash_card.keys()), k=len(animals))
    for random_question in random_questions:
        user_response = input("What do you call a group of " + random_question + "? Answer: a ")
        if user_response == flash_card[random_question]:
            print("Correct!")
            questions_right.append(random_question)
        else:
            print("sorry, that is incorrect")
            questions_wrong.append(random_question)
            print(f"the correct answer is a {flash_card[random_question]}")
    with open (data_file, "r") as f:
            sum = json.load(f)
    num_right_total = 0
    for run_of_program in sum["list"]:
        num_right_total += len(run_of_program["questions_right"])
    num_wrong_total = 0
    for run_of_program in sum["list"]:
        num_wrong_total += len(run_of_program["questions_wrong"])
    percentages = {}
    total_right = {}
    total_wrong = {}
    for animal in animals:
        total_right[animal] = 0
        for run_of_program in sum["list"]:
            if animal in run_of_program["questions_right"]:
                total_right[animal] += 1
        total_wrong[animal] = 0
        for run_of_program in sum["list"]:
            if animal in run_of_program["questions_wrong"]:
                total_wrong[animal] += 1
        percentages[animal] = total_right[animal] / (total_right[animal] + total_wrong[animal])*100
    print("\n".join([
        "Here are some summary stats.",
        f"In this round, you answered {len(questions_right)} questions correctly",
        f"and {len(questions_wrong)} questions wrong",
        f"and you got {list(questions_right)} correct and {list(questions_wrong)} wrong"
    ]))
    print(f"""Here are all of the stats from previous runs of the game. Brace yourself, it might be a lot
                      
In total, you got {num_right_total} questions right

and {num_wrong_total} questions wrong. 
          
That's {(num_right_total/(num_wrong_total+num_right_total))*100}% correct!

Across all the runs:""")
    for animal in animals:
        print(f"""you got {animal} correct {total_right[animal]} times and {animal} wrong {total_wrong[animal]} times. That's {percentages[animal]}% correct""")
    save_data(questions_right, questions_wrong)

    def go_again(n):
        restart = input("\nDo you want to play again? (yes/no): ")
        if restart == "yes" or restart == "Yes":
            animals_that_need_practice = []
            for animal, percentage in percentages.items():
                if percentage < 60-n:
                    animals_that_need_practice.append(animal)
                else:
                    pass
            random_questions_new = random.sample(animals_that_need_practice, k=len(animals_that_need_practice))
            for random_question in random_questions_new:
                user_response = input("What do you call a group of " + random_question + "? Answer: a ")
                if user_response == flash_card[random_question]:
                            print("Correct!")
                            questions_right.append(random_question)
                else:
                    print("sorry, that is incorrect")
                    questions_wrong.append(random_question)
                    print(f"the correct answer is a {flash_card[random_question]}")
            go_again(n+5)
        else:
                print("Thanks for playing! See you next time.")
    go_again(0)
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

 