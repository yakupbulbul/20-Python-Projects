def main(): 
    print("This program converts US dollars to Pounds Sterling")
    print()


    dollars = eval(input("Enter amount in dollors: "))
    pounds = convert_to_pounds(dollars)


    print("That is", pounds, "pounds.")


convert_to_pounds = lambda dollars: dollars * 0.88



main()