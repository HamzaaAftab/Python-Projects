def main():
   # Defining the speed of Light C as Constant
   
   c = 299792458  # meters per second
   
   while True:
       try:
           # Input the Mass
           mass = float(input("Enter the mass (in kilograms) of an object: "))
           
           if mass < 0:
               print("Mass Cannot be Negative, Enter a Positive Value..!")
               break
           
           # Calculate the Energy using E = mc^2
           
           E = mass * c**2  # Corrected Exponentiation Operator
           
           print(f"Mass of the Object: {mass} Kg ")
           print(f"C of the Object: {c} m/s ")
           print(f"The Energy of the object is: {E} Joules")
           
       except Exception as e:
           print(e) 
    
if __name__ == "__main__":
    main()