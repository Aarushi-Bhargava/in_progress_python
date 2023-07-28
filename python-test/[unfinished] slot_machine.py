#slot machine
import random #bc we need to have the slot machine be random

MAX_LINES = 3 #caps bc constant val
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

#making a dictionary
symbol_count = {
   #key , value 
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

#generates the outcome of the slot machine (the results from the slot machine spin)
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): #.items gives you the key and the value associated within the dictionary
       #A     , 2 etc    
        for _ in range(symbol_count): #if you wanna loop thru smth but you dont care abt how many times it loops thru (like tehre isnt a set amount of times you want it to loop), you just put an underscore symbol
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #[:] makes a copy of the list called all_symbols

        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
    
        columns.append(column)
    
    return columns
        

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit(): #to determine if input = digit
            amount= int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ") ? ")
        if lines.isdigit(): 
            lines= int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit(): 
            amount= int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}") #the f and () makes the value contained by the contant, automatically convert to string. this coding feature is only available in python 3.6 and above. we added the $ just as part of the string, it's not part of the syntax that converts numbers to strings.
        else:
            print("Please enter a number.")

    return amount


#to re run entire code if user ever wants to play again
#and, we're calling the functions here
def main(): 
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Your current betting amount is ${total_bet}")
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")

        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

main()
