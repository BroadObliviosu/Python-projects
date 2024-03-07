def count_characters(input_string):
    #will initialise counters
    letter_count = 0
    digit_count = 0

    #iterate through each character in the input string
    for char in input_string:
        if char.isalpha(): #checks if character is a letter
            letter_count += 1 
        elif char.isdigit(): #checks if the character is a diget.
            digit_count += 1 

    #will display the counts for each category
    print(f"letter count {letter_count}")
    print(f"Digit count {digit_count}")
    
#input from the user    
user_input = input("Enter a string: ")

count_characters(user_input)