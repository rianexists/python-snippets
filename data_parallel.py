import csv, re, os.path, numbers

# Define function to read file and store data in parallel arrays
def updateArray(filename):
    # Global variables for access from runtime and reset to empty for new read
    global columns, format_lengths, printarr
    format_lengths, columns, printarr = [], [], []
    # Open file and append to data array
    with open(filename, encoding="utf-8-sig", newline='') as csvfile:
        reader = csv.reader(csvfile, skipinitialspace=True)
        for _ in next(reader):
            columns.append([])
            format_lengths.append(0)
    # open datastream again to reset reader object (this allows us to include header names in the output)
    with open(filename, encoding="utf-8-sig", newline='') as csvfile:
        reader = csv.reader(csvfile, skipinitialspace=True)
        for row in reader:
            # Set each format_lengths value to match longest data length in column
            for i in range(len(row)):
                if format_lengths[i] < len(row[i]) + 2:
                    format_lengths[i] = len(row[i]) + 2
            # Check value type of data, apply correct data storage to match
            for i in range(len(format_lengths)):
                try:
                    columns[i].append(int(row[i]) if row[i].find(".") == -1 else float(row[i]))
                except:
                    columns[i].append(row[i])

    # If ID column length is under 15, pad extra for separation
    if format_lengths[0] + 5 < 15:
        format_lengths[0] += 5

    # Create formatted array
    printarr = []
    for i in range(len(columns[0])):
        printstr = ""
        for x in range(len(format_lengths)):
            custom = ""
            justify = "<"
            # If data in column is int or float, apply right justification
            if isinstance(columns[x][1], numbers.Number):
                if not isinstance(columns[x + 1][1], numbers.Number):
                    custom = "  "
                justify = ">"
            # Check for ID column, force left justification if so
            if x == 0:
                justify = "<"
            printstr += f"{columns[x][i]:{justify}{format_lengths[x]}}{custom}"
        printarr.append(printstr)

filename, option = "", ""
# Runtime loop 
while option != "X":
    print("Welcome")
    if filename == "":
        filename = input("Please enter the file name: ")
        
        # Check file exists
        if not os.path.isfile(filename):
            print("File not found, please try again")
            filename = ""
            continue
        if filename[-4:] != ".csv":
            print(f"Invalid filetype, expected .csv but saw .{filename.split(".")[1]}. Please try again")
            filename = ""
            continue
    print("1) View data")
    print("2) Add row")
    print("3) Open another file")
    print("X) Exit program")
    option = input("> ")
    
    # If user chooses to print
    if option == "1":
        updateArray(filename)
        # Ignore length item
        for item in printarr:
            print(item)
    # If user chooses to add data
    elif option == "2":
        updateArray(filename)
        data_to_write = []
        # ALlow unlimited data entry
        data_write = ""
        while data_write != "X":
            data_write = input("Please enter your data separated by ',' (or X when done): ")
            # End data entry
            if data_write == "X":
                continue
            # Check if enough rows have been entered
            # Use Regex to allow for cells to contain commas
            if len(re.split(",(?=\\S)", data_write)) == len(format_lengths):
                data_to_write.append(re.split(",(?=\\S)", data_write))
            else:
                print(f"Expected {len(format_lengths)} data column{'s' if len(format_lengths) > 1 else ''}. Received {len(re.split(',(?=\\S)', data_write))}")

        # Add data to columns
        for row in data_to_write:
            for i in range(len(format_lengths)):
                columns[i].append(row[i])

        # Append all rows to file
        with open(filename,'a', encoding="utf-8-sig", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for row in data_to_write:
                writer.writerow(row)
        print(f"Wrote {len(data_to_write)} row{'s' if len(data_to_write) > 1 else ''} to file")
    # If user chooses to change file
    elif option == "3":
        filename = ""
        continue
    # If user chooses to quit program
    elif option == "X":
        continue
    # Unknown option
    else:
        print("Unknown option entered. Please try again")