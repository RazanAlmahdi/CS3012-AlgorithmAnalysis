#return maximum number of non overlapping intervals
def nonOverlappingInterval(arr):
    end = float('-inf')

    nonOverlappingInterval = 0

    #sort the list of time intervals according to their end time
    arr.sort(key = lambda x: x[1])

    #loop through the sorted time intervals
    for subList in arr:

        #if start time of the current interval is >= than the highest end time so far
        if subList[0] >= end:

            #increment the number of non-overlapping intervals
            nonOverlappingInterval += 1

            #update the max end time to the end time of the current interval
            end = subList[1]

    #return the max number of non overlapping intervals
    return nonOverlappingInterval

#main driver
def main():
    print('---------------\tInterval scheduling Program\t-----------------')

    #prompt user for file name
    filename = input('\nPlease provide text file name: ') + '.txt'
    print()
    #loop through file and store all elements as a list of sublist of intervals, each with start and end time
    try:
        with open(filename, 'r') as file:
            timeList = [list(map(int, line.strip().split(','))) for line in file]
            print("Current number of time intervals: ", len(timeList))
            #print original number of intervals
            print()
        print("Maximum number of non overlapping intervals: ", nonOverlappingInterval(timeList))
        #print non-overlapping time intervals
    except FileNotFoundError:
        msg = "Sorry, the file "+ filename + " is nonexistent."
        print(msg)

#this function call the main and repeat it as long as answer=yes
def repeat():

    print('\nWould you like to create a schedule? ')
    answer = input('Y/y: ')

    while answer == 'y' or answer == 'Y':

        main()

        print('\nWould you like to create another schedule? ')
        answer = input('Y/y: ')

    if answer != 'y' or answer != 'Y':

        print('\n------------\tInterval Scheduling Program has terminated.\t-------------\n')

repeat()
