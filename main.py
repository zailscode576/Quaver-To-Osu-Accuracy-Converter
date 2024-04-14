import decimal

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def calculate_accuracy():
    # Set the precision for Decimal calculations
    decimal.getcontext().prec = 10  # Adjust the precision as needed

    # Collect user input for the variables
    print("Make sure to use the custom quaver judgements to setup a profile for whicher OD you are trying to convert to. OD9: marv = 16.5ms, perf = 37.5ms great = 70.5ms, good = 100.5ms, meh = 124.5ms ")
    m = get_integer_input("Enter the number of marvelous: ")
    p = get_integer_input("Enter the number of perfects: ")
    g = get_integer_input("Enter the number of greats: ")
    o = get_integer_input("Enter the number of goods: ")
    b = get_integer_input("Enter the number of bads: ")
    mi = get_integer_input("Enter the number of misses: ")

    # Calculate the total 't'
    t = m + p + g + o + b + mi

    print("Total Judgements (this includes LN tails):", t)

    # Use Decimal for calculations
    mc = decimal.Decimal(m) * 1
    pc = decimal.Decimal(p) * 1
    gc = decimal.Decimal(g) * decimal.Decimal('0.6667')
    oc = decimal.Decimal(o) * decimal.Decimal('0.3333')
    bc = decimal.Decimal(b) * decimal.Decimal('0.1667')
    mi = decimal.Decimal(m) * 0  # Using Decimal for consistency

    ALLc = mc + pc + gc + oc + bc + mi

    Acc = ALLc / t
    Acc = round(Acc, 5)  # Round 'Acc' to 5 decimal places

    Acc_percentage = Acc * 100
    print("Accuracy:", Acc_percentage,"%")

    print("Converter made by zailscode576, let me know if there is any bugs.")

    # Ask the user if they want to run the code again or exit
    while True:
        choice = input("Do you have more scores to convert? (re-runs program): ").lower()
        if choice in ['yes', 'y']:
            calculate_accuracy()
            break
        elif choice in ['dan']:
            print("You think this is a game? i oughtta ban you from using this converter.")
            calculate_accuracy()
            break
        elif choice in ['amogus']:
            print("Sending the imposter to this location....")
            calculate_accuracy()
            break
        elif choice in ['sussy']:
            print("https://www.youtube.com/watch?v=j5a0jTc9S10")
            calculate_accuracy()
            break
        elif choice in ['no', 'n']:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 'yes', 'no'.")

# Initial call to the function
calculate_accuracy()
