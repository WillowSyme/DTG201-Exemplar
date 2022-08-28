#Import statements to access my scenarios and endings
import scenarios, endings

#Sets up a global variable that holds the users score - this makes it useable across different functions
SCORE = 0


#Start up screen
#Prints the game name, and informs the user of how the game works
def start_up():
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n~ Welcome To: Environmental Activists ~\n~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    name = input("To begin, please enter your name: ")
    if name.lower() == "will":
        print(f"Thank you {name}. Now entering Admin Mode.")
        admin_mode()
    else:
        print(f"Thank you, {name}.")
        print("Your journey will begin shortly.\n\nYou will be presented with 10 scenarios, each with 3 options for you to choose from.\nYou need to decide which option to choose.\n\nChoose wisely, as your answers will determine if you are fit to be an Environmental Activist, or if you are doomed for all eternity.\n\n")


#This function is for admin purposes - you can update scenarios/add new scenarios/delete scenarios
def admin_mode():
    menu_options = ["Add Scenario", "Update Scenario", "Delete Scenario", "Exit Admin Mode", "Exit Application"]
    print("Admin Menu:")
    print(f"{"Task":<6}{"Operation":<20}")
    for i in range(0, 5):
        print(f"{i:<6}{menu_options[i]:<20}")
    

#each time this function is called, it will add the parameter 'value' to the current SCORE
def add_score(value):
    global SCORE
    SCORE += value


#This function prints out the current scenario from scenarios.py
#It goes through a while loop waiting for a valid input answer from the user and then prints out what their answer was - the best, ok, or worst option they could have picked.
#The neutral answer doesn't call add_score() because the score for a neutral answer is 0 so it won't change the current score
def situations(situation):
    print(situation.get("scenario"))
    valid_input = False
    while valid_input == False:
        user_answer = input(situation.get("answers"))
        if user_answer.lower() == situation.get("best_answer"):
            print("You've chosen the most environmentally friendly option.")
            add_score(10)
            valid_input = True
        elif user_answer.lower() == situation.get("neutral_answer"):
            print("You've picked the in-the-middle option.")
            valid_input = True
        elif user_answer.lower() == situation.get("negative_answer"):
            print("You've chosen the least environmentally friendly option.")
            add_score(-5)
            valid_input = True
        else:
            print("Please pick 'a', 'b', or 'c'")


#This function prints out each scenario
def call_scenarios():
    for i in range(1, len(scenarios.scenarios) + 1):
        print(f"Scenario {i}")
        situations(scenarios.scenarios.get(i))
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
    call_scenarios()
    print(SCORE)
    print_ending()
    print("\n\n")
    restart = ""
    while restart.lower != "no":
        restart = input("Would you like to try again to get a different ending?")
        if restart.lower() == "yes":
            print("restarting...")
            print("\n\n")
            call_scenarios()
        elif restart.lower() == "no":
            print("Thanks for playing!")
            quit()
        else:
            print("hmmm... I don't recognise that word.")

            
#This calls our main function so the code will run
main()
