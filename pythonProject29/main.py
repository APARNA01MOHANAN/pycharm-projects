'''import sys
# appending a path
sys.path.append("C:/Users/40032118/PycharmProjects/pythonProject26")
# printing all paths
print(sys.path)

import sys
# printing all directories for
# interpreter to search
print(sys.path)'''
import sys
# Take input using stdin
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


