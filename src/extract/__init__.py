def get_input(filename):
    rows = []
    try:
        with open(filename, 'r') as f:
            for line in f.readlines():
                rows.append(line.strip().split(','))
    except OSError as e:
        print(f"unable to open {filename}: {e}")
    return rows

# Add function to remove duplicates from a list based on first column needing to be unique.  Assume any duplicates are sorted together in sequential rows and we want to retain the first of any 'batch'

def remove_duplicates(list):
    # loop through a list and add to a new list if the item has a unique user ID
    deduped_list = []
    for i in list:
        # is the first element of the row in the input list in the deduped list
        if i[0] not in [r[0] for r in deduped_list]:
            deduped_list.append(i)


    return deduped_list

# Add function to remove empty lines

def remove_empty_lines(list):
    # loop through a list where each element is also a list retaining only lines where the first element of the line is not blank
    no_empty_lines = []
    for i in list:
        if i[0] != '':
            no_empty_lines.append(i)

    return no_empty_lines

def capitalise_names(list):
    # loop through a list where each element is also a list capitalizing elements 1 and 2
    # Initialise new list we will append to
    newlist = []

    for i in list:
        i[1] = i[1].capitalize()
        i[2] = i[2].capitalize()
        newlist.append(i)
    
    return newlist

def validate_answer_3(list):
     # loop through a list where each element is also a 'sublist' retaining only sublists where element 5 is between 1 and 10 inclusive
     # Assume first siblist is headers, so ignore
    newlist = []
    # Append the header row unchanged
    newlist.append(list[0])
    # Consider all the remaining rows for the test
    for i in list[1:]:
        if i[5] != '' and (int(i[5]) >=1 and int(i[5]) <= 10):
            newlist.append(i)

    return newlist


