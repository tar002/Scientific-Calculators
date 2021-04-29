unit = input("Enter your 1st unit: (f, c, k, n)").lower()
unit2 = input("Enter your 2nd units: (f, c, k, n)").lower()
temp = float(input("Enter Temperature: "))

def fConverter(temp, unit):
    if(unit == "c"):
        return 5/9*(temp-32)
    elif(unit == "k"):
        return 5/9*(temp-32)+273.15
    elif(unit == "k"):
        return (temp-32)*11/60
    else:
        print("invalid input")

def cConverter(temp, unit):
    if(unit == "f"):
        return (9/5)*temp+32
    elif(unit == "k"):
        return temp+273.15
    elif(unit == "n"):
        return temp*0.33
    else:
        print("invalid input")

def kConverter(temp, unit):
    if(unit == "f"):
        return 9/5*(temp-273.15)+32
    elif(unit == "c"):
        return temp-273.15
    elif(unit == "n"):
        return (temp-273.15)*0.33000
    else:
        print("invalid input")

def nConverter(temp, unit):
    if(unit == "f"):
        return (temp*60)/11+32
    elif(unit == "c"):
        return temp/0.33
    elif(unit == "k"):
        return temp*(100/33)+273.15
    else:
        print("invalid input")

if(unit == "f"):
    print(fConverter(temp,unit2))
elif(unit == "c"):
    print(cConverter(temp,unit2))
elif(unit == "n"):
    print(nConverter(temp,unit))
elif(unit == "k"):
    print(kConverter(temp,unit2))
else:
    print("invalid input")






