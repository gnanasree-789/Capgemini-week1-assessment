def Celsius_to_Fahrenheit(celsius):
    print(f"Celsius : {celsius} = Fahrenheit:{celsius*(9/5)+32}")
def Celsius_to_kelvin(Celsius):
    print(f"Celsius : {Celsius} = kelvin:{Celsius + 273.15}")
def Fahrenheit_to_celsius(Fahrenheit):
    print(f"Fahrenheit:{Fahrenheit} = celsius={(Fahrenheit - 32)*5/9}")
def Fahrenheit_to_kelvin(Fahrenheit):
    print(f"Fahrenheit:{Fahrenheit} = kelvin={(Fahrenheit-32)*(5/9) + 273.15}")
def kelvin_to_Fahrenheit(kelvin):
    print(f"kevin:{kelvin} = Fahrenheit:{(kelvin-273.15) * 1.8 + 32}")
def kelvin_to_celsius(kelvin):
    print(f"kelvin:{kelvin} = Celsius:{kelvin - 273.15}")
celsius=int(input("Enter celsius"))
Fahrenheit=int(input("ENter Fahrenheit"))
kelvin=int(input("ENter kelvin"))
Celsius_to_Fahrenheit(celsius)
Celsius_to_kelvin(celsius)
Fahrenheit_to_celsius(Fahrenheit)
Fahrenheit_to_kelvin(Fahrenheit)
kelvin_to_Fahrenheit(kelvin)
kelvin_to_celsius(kelvin)