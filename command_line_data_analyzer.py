print("welcome to command-line data analyzer. Type 'exit' to quit.")

def load_numbers(file_path):
    numbers=[]

    try:
        with open(file_path , "r", encoding= "utf-8") as file :
            #content= file.read()
            #print("file read successfully ")

            for line in file:
                line=line.strip()

                if not line:
                    continue

                try: 
                     number = float(line)
                     numbers.append(number) 
                except ValueError:
                    pass

                #finally:
                 #   file.close()

    except FileNotFoundError :
        print("file not found or cannot be opened")
        return []                      
               
    return numbers


def show_statistics(numbers):
     
    
       #if no number avail
     if not numbers:
         print("no data available")
         return
     
    # count=len(numbers)
    # total = 0
            #mean
     total = 0
     for val in numbers:
         total = total + val
     count = len(numbers)
     mean = total / count
     print(f"mean :{mean}")

          # min/max
     
     current_min = numbers[0]
     current_max = numbers[0]

     for val in numbers:
         if val < current_min:
             current_min = val
         if val > current_max:
             current_max = val


     sorted_numbers = numbers.copy()
     sorted_numbers.sort()
     n = len(sorted_numbers)
     mid = n // 2

     if n % 2 != 0:
         median = sorted_numbers[mid]     
     else:
         median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2


             # standard deviations
     sum_of_squared_diff = 0     
     for val in numbers:
          diff = val - mean 
          sum_of_squared_diff = sum_of_squared_diff + (diff * diff)

     variance = sum_of_squared_diff / count
     standard_deviation = variance ** 0.5

     print("count :", count)
     print("min :", current_min)
     print("max :", current_max)
     print("median :", median)
     print("standard deviation :", standard_deviation)




         

def filter_greater_than (numbers, x):
    try:
        x = float(x)
    except:
        print("error")
        return


    found = False # varaible to keep track of loop history


    for val in numbers:
        if val > x:
            print(val)
            found= True

        if not found   :
            print("no values found")  

def filter_less_than(numbers, x):
    try:
        x= float(x)
    except :
        print("error")
        return
    
    found= False
    
    for val in numbers :
        if val < x :
            print(val)
            found= True

        if not found   :
            print("no values found") 


def main():
    
    file_path = input("Enter file path or 'exit' to quit:").strip()
    if file_path.lower() == "exit":
        print("exiting program")
        return
    number_list = load_numbers(file_path)
    #print("DEBUG:" , number_list)   # temporary - for testing 
    
    if not number_list:
        print("No valid numbers found") 
        return
        
    while True:
        print("\n1. Show statistics")
        print("2. Filter numbers greater than x")
        print("3. Filter numbers less than x")
        print("4. Exit")

        user_choice = input("enter your choice:").strip()

        if user_choice == "1":
             show_statistics(number_list)

        elif user_choice == "2":
            x = input("enter x:").strip()
            filter_greater_than(number_list, x)

        elif user_choice == "3":
            x = input("enter x:").strip()
            filter_less_than(number_list, x)

        elif user_choice == "4":
            print("exiting program")
            break
        else:
            print("invalid choice, try again.")

main()                


           
               




