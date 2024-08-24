import random


#global variables that will remain constant throughout the code and we can use them anywhere in the code.!!!
MAX_LINES = 3    
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,                       #Dictionary
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 5,
    "B" : 4,                      #values
    "C" : 3,
    "D" : 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):    #checking through lines
        symbol = columns[0][line]   # checking the first symbol
        for column in columns:
            symbol_to_check = column[line] 
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines





def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):           # instead of for i we have used for _ because it is an anonymous variable in python. So whenver you need to loop through something we dont care about the count that irriration value then you just put underscore(_) and then you don't have unused variable anymore.
            all_symbols.append(symbol)


    columns = []     # every interior list gives us the value of the items inside of our column. 
    for _ in range(cols):
        # till line 37 code is picking random values for each row in our column
        column = []   
        current_symbols = all_symbols[:]   # Here we have made copy of all_symbols list because once we pick a value we need to remove it from the list so that we can't choose that value again.  
                                           # So if there is 2 'A's we should be able to select only 2 times A not 3. To copy a list we put a colon ':' --> called slice operator
        for _ in range(rows): 
            value = random.choice(current_symbols)    # picks random value from current_symbols list
            current_symbols.remove(value)             # removes the value so that we dont pick it again
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):                  #We are doing transposing of matrix which means rows become columns , columns become rows.
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):       #Enumerate --> it gives you the index and items
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()       #brings us to the new line beacuse it prints a new line character by default at the end of the empty print statement




def deposit():
    while True:
        amount = input("What would you like to deposit?")
        if amount.isdigit():        #isdigit is a string method  , there it is checking whether the amount entered is valid number
            amount = int(amount)           #converting string into interger
            if amount > 0:
                break
            else:
                print("Amount should be greater than 0")
        else: 
            print("Please Enter Number")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():        #isdigit is a string method  , there it is checking whether the amount entered is valid number
            lines = int(lines)           #converting string into interger
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a Valid Number of Lines. ")
        else: 
            print("Please Enter Number")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? ")
        if amount.isdigit():        #isdigit is a string method  , there it is checking whether the amount entered is valid number
            amount = int(amount)           #converting string into interger
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}")
        else: 
            print("Please Enter Number")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet() 
        total_bet = bet * lines

        if total_bet >balance:
            print(
              f"You do not have enough to bet that amount, your current balance is: {balance}"  
            )
        else:
            break
            
    print(f"You are betting {bet} on {lines} lines. Total bet is equal to: {total_bet}")


    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings}")
    print(f"You won on lines:", *winning_lines)    # '*' is called splat operator or the unpack operator and its going to pass every single line from the winning_lines list to this print function
    return winnings - total_bet

def main():  
    balance = deposit() 
    while True:
        print(f"Current balance is {balance}")
        answer = input("Press enter to play (q to quit). ")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with {balance}")
    


main()