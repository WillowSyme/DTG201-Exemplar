#Import statements to access my scenarios and endings
import scenarios, endings
from time import sleep

#Sets up a global variable that holds the users score - this makes it useable across different functions
SCORE = 0

#Start up screen
#Prints the game name, and informs the user of how the game works
def start_up():
    print(
        "~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n~ Welcome To: Environmental Activists ~\n~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~"
    )
    name = input("To begin, please enter your name: ")
    if name.lower().strip() == "will":
        print(f"Thank you {name.strip()}. Now entering Admin Mode.")
        admin_mode()
    else:
        print(f"Thank you, {name.strip()}.")
        print("Your journey will begin shortly.\n\nYou will be presented with 10 scenarios, each with 3 options for you to choose from.\nYou need to decide which option to choose.\n\nChoose wisely, as your answers will determine if you are fit to be an Environmental Activist, or if you are doomed for all eternity.\n\n")
        print("For each scenario, make sure you input either 'a', 'b', or 'c' relating to which answer you want to pick.\n\n")
        sleep(3)

#This function is for admin purposes - you can update scenarios/add new scenarios/delete scenarios
def admin_mode():
    menu_options = [
        "Add Scenario", "Update Scenario", "Delete Scenario",
        "Print Scenarios", "Exit Admin Mode", "Exit Application"
    ]
    print("Admin Menu:\n")
    print(f"{'Task':<6}{'Operation':<20}")
    for i in range(0, 6):
        print(f"{i:<6}{menu_options[i]:<20}")
    print("\n")
    menu_select = int(input("Which menu item would you like to select?: ").strip())

    if menu_select == 0:
        add_new_scenario()
    elif menu_select == 1:
        update_scenario()
    elif menu_select == 2:
        remove_scenario()
    elif menu_select == 3:
        print_scenarios()
    elif menu_select == 4:
        print("Game starting in 3...", end="")
        sleep(1)
        print("2...", end="")
        sleep(1)
        print("1...", end="")
        sleep(1)
        print("\n")
    elif menu_select == 5:
        print("Thanks for visiting")
        exit()
    else:
        print("Please select a number between 0 - 5:\n")


#This function handles adding new items to scenarios
def add_new_scenario():
    scenario = input("What is the new scenario you'd like to add?\n").strip()
    best_answer = input("Which answer is the positive answer?\n").strip()
    neutral_answer = input("Which answer is the neutral answer?\n").strip()
    negative_answer = input("Which answer is the negative answer?\n").strip()
    next_scenario = len(scenarios.scenarios) + 1
    temp_dict = {
        next_scenario: {
            "scenario": scenario,
            "answers": [best_answer, neutral_answer, negative_answer],
            "best_answer": "a",
            "neutral_answer": "b",
            "negative_answer": "c"
        }
    }
    scenarios.scenarios.update(temp_dict)
    print_scenarios()


#This function handles removing items from scenarios
def remove_scenario():
    scenario_num = int(
        input(
            "Please enter the number of the scenario you are wanting to remove: "
        ).strip())
    scenarios.scenarios.pop(scenario_num)
    print_scenarios()


#This function updates an existing scenario
def update_scenario():
    scenario_number = int(input("Which Scenario are you wanting to update?: ").strip())
    scenario = input("Please enter the new scenario:\n").strip()
    best_answer = input("Please enter the positive answer:\n").strip()
    neutral_answer = input("Please enter the neutral answer:\n").strip()
    negative_answer = input("Please enter the negative answer:\n").strip()
    temp_dict = {
        "scenario": scenario,
        "answers": [neutral_answer, negative_answer, best_answer],
        "best_answer": best_answer,
        "neutral_answer": neutral_answer,
        "negative_answer": negative_answer
    }
    scenarios.scenarios.update({scenario_number: temp_dict})
    print_scenarios()


#This function is used specifically for admin mode to print out the dictionary again to show what has been added or removed
def print_scenarios():
    length = len(scenarios.scenarios)
    if length <= 10:
        length = 11
    else:
        length += 1
    for i in range(1, length):
        scen = scenarios.scenarios.get(i)
        if scen:
            print(f"Scenario {i}")
            print(scen.get("scenario"))
            print(scen.get("answers"))
            print("\n")

    admin_mode()

#each time this function is called, it will add the parameter 'value' to the current SCORE
def add_score(value):
    global SCORE
    SCORE += value


#This function prints out the current scenario from scenarios.py
#It goes through a while loop waiting for a valid input answer from the user and then prints out what their answer was - the best, ok, or worst option they could have picked.
#The neutral answer doesn't call add_score() because the score for a neutral answer is 0 so it won't change the current score
def situations(situation):
    print(situation.get("scenario"))
    answers = situation.get("answers")
    for i in range(0,3):
        print(answers[i])
    valid_input = False
    while valid_input == False:
        user_answer = input("\nWhich option should she choose?\n").lower().strip()
        if user_answer == situation.get("best_answer"):
            print("You've chosen the most environmentally friendly option.")
            add_score(10)
            valid_input = True
        elif user_answer == situation.get("neutral_answer"):
            print("You've picked the in-the-middle option.")
            valid_input = True
        elif user_answer == situation.get("negative_answer"):
            print("You've chosen the least environmentally friendly option.")
            add_score(-5)
            valid_input = True
        else:
            print("Please pick 'a', 'b', or 'c'")


#This function prints out each scenario
def call_scenarios():
    length = len(scenarios.scenarios)
    if length <= 10:
        length = 11
    else:
        length += 1
    for i in range(1, length):
        scen = scenarios.scenarios.get(i)
        if scen:
            print(f"Scenario {i}")
            situations(scen)
            print("\n")


#This function prints out the ending based on the players final score
def print_ending():
    global SCORE
    if 50 <= SCORE <= 100:
        print(endings.endings.get("positive ending"))
    elif 0 <= SCORE < 50:
        print(endings.endings.get("neutral ending"))
    elif -50 <= SCORE < 0:
        print(endings.endings.get("negative ending"))


#This is the main function. It calls all the other functions
def main():
    start_up()
    restart = True
    while restart:
        call_scenarios()
        print(SCORE)
        print_ending()
        print("\n\n")
        repeat = input("Would you like to try again to get a different ending? ")
        while repeat != "yes":
            repeat = repeat.lower().strip()
            if repeat == "yes":
                print("restarting...")
                print("\n\n")
                sleep(3)
            elif repeat == "no":
                print("Thanks for playing!")
                quit()
            else:
                print("hmmm... I don't recognise that word.")
                repeat = input("Would you like to try again to get a different ending? ")
    

#This calls our main function so the code will run
main()
