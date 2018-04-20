def degrees(celsius):
    fahrenheit = 9/5 * celsius + 32
    print('\t  ', celsius, "\t\t|\t", fahrenheit)

def main():
    print("\tCelsius \t- \tFahrenheit")
    print("----------------------------------------------------------")
    for i in range (0,101,10):
        degrees(i)

main()
    

