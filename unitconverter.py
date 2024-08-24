#Defining Intro
def intro():
    x = input("What's your name?")
    print("Hello,", x)

#defining main function
def main():
    #defining all conversions
    def massinkgtogm():
        massinkg = float(input("Mass in KG?"))
        massingm = round(massinkg * 1000, 2)
        print(massinkg, "KG is",massingm, "Gram")
    
    def massingmtokg():
        massingm = float(input("Mass in gm?"))
        massinkg = round(massingm / 1000, 2)
        print(massingm, "Gram is", massinkg, "Kilogram")
    
    def tempinktoc():
        tempink = float(input("What's temeperature in Kelvin"))
        tempinc = round(tempink - 273, 2)
        print(tempink, "Kelvin is", tempinc, "Celsius")

    def tempinctok():
        tempinc = float(input("What's temperature in Celsius?"))
        tempink = round(tempinc + 273, 2)
        print(tempinc, "celsius is", tempink, "Kelvin")

    def volumeinLtom3():
        volumeinL = float(input("What's the volume in Litre?"))
        volumeinm3 = round(volumeinL / 10, 2)
        print(volumeinL, "Litre is ", volumeinm3, "Cubic Metre")
    
    def volumeinm3toL():
        volumeinm3 = float(input("What's volume in Cubic Metre?"))
        volumeinL = volumeinm3 * 10

    #now the input parts
    x = int(input("What you Want to convert today1)mass 2)Temperature 3)Volume"))

    if x == 1:
        
        massinput = int(input("1)KG to GM 2)GM to KG"))
        
        if massinput == 1:
            massinkgtogm()
        elif massinput == 2:
            massingmtokg()
        else:
            print("Invalid Input")

    elif x == 2:
         
         tempinput = int(input("1)Temperature in Kelvin to Celsius 2)Temperature in Celsius to Kelvin"))

         if tempinput == 1:
             tempinktoc()

         elif tempinput == 2:
            tempinctok()

         else: 
             print("Input Invalid")

    elif x == 3:

        volumeinput = int(input("1)Volume in Litre to Cubic Metre 2)Volume in Cubic Metre to Litre"))
        
        if volumeinput == 1:
            volumeinLtom3()

        elif volumeinput == 2:
            volumeinm3toL()

        else: 
             print("Input Invalid")
    
    else: 
        print("Input Invalid")
intro()
main()
