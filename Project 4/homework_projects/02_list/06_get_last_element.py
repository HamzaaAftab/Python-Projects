def get_first_element(lst):
    if lst:  # Check if list is not empty
        return lst[0]
    return "List is empty"

def get_last_element(lst):
    if lst:  # Check if list is not empty
        return lst[-1]
    return "List is empty"

def get_list():
    lst = []  # Empty List
    elem = input("Enter an Element of the List or Press Enter to Stop: ")  # User Input
    
    while elem != "":
        lst.append(elem)  # Add element to list
        elem = input("Enter an Element of the List or Press Enter to Stop: ")  # Next input
        
    return lst

def main():
    lst = get_list()
    
    first_element = get_first_element(lst)
    print("First Element:", first_element)
    
    last_element = get_last_element(lst)
    print("Last Element:", last_element)

if __name__ == '__main__':
    main()
