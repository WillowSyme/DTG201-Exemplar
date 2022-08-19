from Scenarios import scenario1
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
    user_answer = input(situation.get("answers"))
    if user_answer == situation.get("answer"):
        print("You've chosen the most environmentally friendly option.")
        add_score(10)
    elif user_answer == situation.get(""):
        print("You've picked the in-the-middle option.")
    else:
        print("You've chosen the least environmentally friendly option.")
        add_score(-5)


def main():
    start_up()
    situations(scenario1)

main()