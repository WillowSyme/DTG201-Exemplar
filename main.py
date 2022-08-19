from scenario1 import scenario1
global SCORE

def start_up():
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")
    print("~ Welcome To: Environmental Activists ~")
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~")

    name = input("To begin, please enter your name: ")
    print("Thank you, {}.".format(name))
    print("Your journey will begin shortly.")
    print("\n")
    print("You will be presented with 10 scenarios, each with 3 options for you to choose from.")
    print("You need to decide which option to choose.")
    print("Choose wisely, as your answers will determine if you are fit to be an Environmental Activist, or if you are doomed for all eternity.")


def add_score(value):
    SCORE += value


def situations(situation):
    print(type(situation))
    print(situation.get("scenario"))
    valid_input = False
    while valid_input == False:
        user_answer = input(situation.get("answers"))
        if user_answer.lower() == situation.get("best_answer"):
            print("You've chosen the most environmentally friendly option.")
            #add_score(10)
            valid_input = True
        elif user_answer.lower() == situation.get("neutral_answer"):
            print("You've picked the in-the-middle option.")
            valid_input = True
        elif user_answer.lower() == situation.get("negative_answer"):
            print("You've chosen the least environmentally friendly option.")
            #add_score(-5)
            valid_input = True
        else:
            print("Please pick 'a', 'b', or 'c'")


def main():
    start_up()
    situations(scenario1)

main()