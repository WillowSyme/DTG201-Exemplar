#Import statements to access my scenarios and endings
import scenarios, endings

#Sets up a global variable that holds the users score - this makes it useable across different functions
SCORE = 0


#Start up screen
#Prints the game name, and informs the user of how the game works
def start_up():
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    print("~ Welcome To: Environmental Activists ~")
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    name = input("To begin, please enter your name: ")
    print("Thank you, {}.".format(name))
    print("Your journey will begin shortly.")
    print("\n")
    print(
        "You will be presented with 10 scenarios, each with 3 options for you to choose from."
    )
    print("You need to decide which option to choose.")
    print(
        "Choose wisely, as your answers will determine if you are fit to be an Environmental Activist, or if you are doomed for all eternity."
    )
    print("\n")


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


#This is the main function. It calls all the other functions
def main():
    start_up()
    print("Scenario One")
    situations(scenarios.scenario1)
    print("\n")
    print("Scenario Two")
    situations(scenarios.scenario2)
    print("\n")
    print("Scenario Three")
    situations(scenarios.scenario3)
    print("\n")
    print("Scenario Four")
    situations(scenarios.scenario4)
    print("\n")
    print("Scenario Five")
    situations(scenarios.scenario5)
    print("\n")
    print("Scenario Six")
    situations(scenarios.scenario6)
    print("\n")
    print("Scenario Seven")
    situations(scenarios.scenario7)
    print("\n")
    print("Scenario Eight")
    situations(scenarios.scenario8)
    print("\n")
    print("Scenario Nine")
    situations(scenarios.scenario9)
    print("\n")
    print("Scenario Ten")
    situations(scenarios.scenario10)
    print(SCORE)
    

#This calls our main function so the code will run
main()
