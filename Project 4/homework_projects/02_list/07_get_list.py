def main():
    
    lst = [] # Defining the Empty List
    elem = input("Enter the number of elements you want to add: ") # User Input
    
    while elem != "": # Loop to add elements to the list
        lst.append(elem)
        elem = input("Enter the number of elements you want to add:")
        
    print(lst)
    

    
    
if __name__ == '__main__':
    main()