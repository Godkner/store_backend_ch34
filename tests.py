def say_hello():
    print("Hello")
    
    

def some_numbers():
    prices = [1.5, 2.5, 3.5, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0,
          11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0]
    
# 1 the sum of all prices
    total = 0
    results = 0
    for num in prices:
        total += num 
        if num < 12:
            results += 1

    print("Total: " + str(total) + " Lower than 12: " + str(results))


# 1 total number of colors
# 2 how many times the color blue appears on the list (case insensitive search)
def some_colors():
    colors = ["red", "Green", "blue", "yellow", "green", "Orange", "Red", "BLUE", 
        "YELLOW", "blue", "purple", "Pink", "brown", "Black", "white", "GREY", "silver", 
        "Gold", "Cyan", "magenta", "BluE"]
    
    print(len(colors))
    count= 0
    for color in colors:
        if color.lower()== 'blue':
            count+= 1
    
    print(f"Blue appears {count} time in the list")
    
    #3 print the list color where
    # - all the colors are in lower case
    # -each color appears only once in the results list
    for i in range(len(colors)):
        colors[i] = colors[i].lower()
    print(set(colors))
    
def  some_ages():
    ages = [24, 35, 18, 46, 29, 51, 22, 33, 40, 27, 55, 19, 31, 37, 43, 25, 49, 20, 23, 26]
    count= 0
    count2=0
    #1 how many are over 30?
    for i in range(len(ages)):
        if ages[i] > 30:
            count+=1
        if ages[i]>=25 and ages[i]<=35:
            count2+=1
        
    print(f"there are {count} ages over 30")
    print(f"there are {count2} ages between 25 and 35")

# call the fns
say_hello()
some_numbers()
some_colors()
some_ages()