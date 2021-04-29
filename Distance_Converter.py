unit = input("Enter your 1st unit: (mi, km, ft, m, in, mm, cm, yd)").lower()
unit2 = input("Enter your 2nd units: (mi, km, ft, m, in, mm, cm, yd)").lower()
num = float(input("Enter Number you want converted: "))

def miConverter(num, unit):
    if(unit == "km"):
        return num*1.609
    elif(unit == "ft"):
        return num*5280
    elif(unit == "m"):
        return num*1609.34
    elif(unit == "in"):
        return num*63360
    elif(unit == "mm"):
        return num*1609344
    elif(unit == "cm"):
        return num*160934
    elif(unit == "yd"):
        return num*1760
    else:
        print("invalid input")

def kmConverter(num, unit):
    if(unit == "mi"):
        return num*0.62137
    elif(unit == "ft"):
        return num*3280.839895
    elif(unit == "m"):
        return num*1000
    elif(unit == "in"):
        return num*39370.0787
    elif(unit == "mm"):
        return num*1000000
    elif(unit == "cm"):
        return num*100000
    elif(unit == "yd"):
        return num*1093.6
    else:
        print("invalid input")

def ftConverter(num, unit):
    if(unit == "mi"):
        return num/5280
    elif(unit == "km"):
        return num/3281
    elif(unit == "m"):
        return num/3.281
    elif(unit == "in"):
        return num*12
    elif(unit == "mm"):
        return num*304.8
    elif(unit == "cm"):
        return num*30.48
    elif(unit == "yd"):
        return num/3
    else:
        print("invalid input")

def mConverter(num, unit):
    if(unit == "mi"):
        return num/1609
    elif(unit == "km"):
        return num/1000
    elif(unit == "ft"):
        return num*3.28084
    elif(unit == "in"):
        return num*39.37007874
    elif(unit == "mm"):
        return num*1000
    elif(unit == "cm"):
        return num*100
    elif(unit == "yd"):
        return num*1.093613 
    else:
        print("invalid input")

def inConverter(num, unit):
    if(unit == "mi"):
        return num/63360
    elif(unit == "km"):
        return num/39370
    elif(unit == "ft"):
        return num/12
    elif(unit == "m"):
        return num/39.37
    elif(unit == "mm"):
        return num*25.4
    elif(unit == "cm"):
        return num*2.54
    elif(unit == "yd"):
        return num/36
    else:
        print("invalid input")

def mmConverter(num, unit):
    if(unit == "mi"):
        return num*0.00000062137 
    elif(unit == "km"):
        return num*0.000001 
    elif(unit == "ft"):
        return num*0.00328084
    elif(unit == "m"):
        return num/1000
    elif(unit == "in"):
        return num/25.4
    elif(unit == "cm"):
        return num/10
    elif(unit == "yd"):
        return num*0.00109361
    else:
        print("invalid input")

def cmConverter(num, unit):
    if(unit == "mi"):
        return num*0.0000062137119224 
    elif(unit == "km"):
        return num/100000
    elif(unit == "ft"):
        return num/30.48
    elif(unit == "m"):
        return num/100
    elif(unit == "in"):
        return num/2.54
    elif(unit == "mm"):
        return num*10
    elif(unit == "yd"):
        return num/91.44
    else:
        print("invalid input")

def ydConverter(num, unit):
    if(unit == "mi"):
        return num/1760
    elif(unit == "km"):
        return num*0.0009144 
    elif(unit == "ft"):
        return num*3
    elif(unit == "m"):
        return num*0.9144 
    elif(unit == "in"):
        return num*36
    elif(unit == "mm"):
        return num*914.40 
    elif(unit == "cm"):
        return num*91.44
    else:
        print("invalid input")

if(unit == "mi"):
    print(miConverter(num,unit2))
elif(unit == "km"):
    print(kmConverter(num,unit2))
elif(unit == "ft"):
    print(ftConverter(num,unit2))
elif(unit == "m"):
    print(mConverter(num,unit2))
elif(unit == "in"):
    print(inConverter(num,unit2))
elif(unit == "mm"):
    print(mmConverter(num,unit2))
elif(unit == "cm"):
    print(cmConverter(num,unit2))
elif(unit == "yd"):
    print(ydConverter(num,unit2))
else:
    print("invalid input")
