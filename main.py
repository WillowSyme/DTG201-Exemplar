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

def main():
    start_up()
    print("Hello, world!")

main()