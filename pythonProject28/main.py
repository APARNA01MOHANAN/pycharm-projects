#stdin input
import sys
# Take input using stdin
print("enter the input")
for inputVal in sys.stdin:
    # Print the input value
    print('The input value is:%s' % inputVal)
    # Ask for the next iteration
    nextInput = input("Do you want to terminate? (Y/N)")
    # Terminate from the loop if 'y/Y' is pressed
    if nextInput.strip().upper() == 'Y':
        break
    else:
        print("Type any text:")

#path
# importing module
import sys
print(sys.path)
# importing module

