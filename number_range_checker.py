#Function to iterate through the given range and check whether each number is a multiple of 3, 5 or both 3 and 5 and print the respective output depending on the result..
def number_range_checker(start, end):
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("rayroy")
        elif num % 3 == 0:
            print("ray")
        elif num % 5 == 0:
            print("roy")
        else:
            print(num)

if __name__ == "__main__":
    # Get user input for the start and end range
    try:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))

    #The if else block below ensures the smallest number of the two inputs is passed first to the range checker function regardless of whether the user entered the smallest or largest first
    #The block also handles the potential error of the user entering two equal numbers instead of a range.
        if start > end:
            min = end
            max = start
        elif start < end:
            min = start
            max = end
        elif start == end:
            print("Error! The numbers entered are the same. Provide a range by entering two different numbers!")
            exit()
    
    #Error handling for invalid or non integer input
    except ValueError:
        print("Error: Please enter valid integer values for start and end.")
        exit(1)
    
    #Finaly, the function call.
    number_range_checker(min, max)
