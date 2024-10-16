import csv
import re
import os.path

# Define function to read file and store data in array
def readFile(filename):
    format_lengths = []
    data = []
    
    # Open file and append to data array
    with open(filename, encoding="utf-8-sig", newline='') as csvfile:
        reader = csv.reader(csvfile, skipinitialspace=True)
        for row in reader:
            data.append(row)

    # Insert longest data lengths for each column into list for formatting
    i = 0
    while i < len(data[0]):
        format_lengths.append(0)
        i += 1
    for row in data:
        i = 0
        while i < len(row):
            if format_lengths[i] < len(row[i]):
                format_lengths[i] = len(row[i]) + 2
            i += 1

    # If ID column length is under 15, force length
    if format_lengths[0] < 15:
        format_lengths[0] = 15

    # Create formatted array
    printarr = [len(format_lengths)]
    printstr = ""
    for row in data:
        i = 0
        while i < len(row):
            printstr += f"{row[i]:{'<' if i == 0 else '>'}{format_lengths[i]}s}"
            i += 1
        printarr.append(printstr)
        printstr = ""
    return printarr

# Runtime loop
while True:
    print("Welcome")
    filename = input("Please enter the file name: ")
    if os.path.isfile(filename) == False:
        print("File not found, please try again")
        continue
    print("1) View data")
    print("2) Add row")
    print("X) Exit program")
    option = input("> ")
    
    # If user chooses to print
    if option == "1":
        printer = readFile(filename)
        # Ignore length item
        for item in printer[1:]:
            print(item)
    # If user chooses to add data
    elif option == "2":
        result = readFile(filename)
        data_to_write = []
        # ALlow unlimited data entry
        while True:
            data_write = input("Please enter your data separated by ',' (or X when done): ")
            # End data entry
            if data_write == "X":
                break
            # Check if enough rows have been entered
            # Use Regex to allow for cells to contain commas
            if len(re.split("(,(?=\S))", data_write)) == result[0]:
                data_to_write.append(re.split("(,(?=\S))", data_write))
            else:
                print("Expected", result[0], "data items. Received", len(data_write.split(",")))
        # Append all rows to file
        with open(filename,'a', encoding="utf-8-sig", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for row in data_to_write:
                writer.writerow(row)
        print("Wrote", len(data_to_write), "rows to file")
    # If user chooses to quit program
    elif option == "X":
        break
    # Unknown option
    else:
        print("Try again")