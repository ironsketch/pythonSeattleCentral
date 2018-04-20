L = [(170,74),(74,170),(250,48),(250,96)]
def BMI(weight,inches):
    BMI = 720 * (weight / (inches**2))
    return BMI

def compBMI(BMI):
    if (BMI < 19):
        poop = 'This is an arbitrary form of classification of human weight'
        print(poop,BMI)
    elif (19 <= BMI <= 25):
        poop = 'If the teacher has a high BMI, this weight system is FUCKED'
        print(poop,BMI)
    else:
        poop = 'This is an aweful program'
        print(poop,BMI)
    
def main():
##    weight = eval(input('How much do you weigh? (Type int)'))
##    print('State your height:')
##    feet,inches = eval(input('(Type int for both feet and inches seperated by comma) '))
##    height = (feet * 12) + inches
    for item in L:
        weight,inches = item
        print(item)
        compBMI(BMI(weight,inches))
        print('-------------')
        print()

main()
