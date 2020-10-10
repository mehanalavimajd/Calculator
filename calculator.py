# Amazing CALCULATOR
# We can't run here...
# function
try:
    from os import system 
    import sys
except Exception:
    system('pip install sys')
    import sys

def finput(running):
    global number1
    global number2
    
    number1 = int(input('\n pleas enter number one: '))
    number2 = int(input(' pleas enter number tow: '))
    
    if (number1 or number2) == (None or ''):
        print(' Go out!')
        running = False
    
def fopration():
    global number_operation
    
    print('''\n
     [01] Total
     [02] Reduce
     [03] Multiplication
     [04] Division\n
    ''')
    
    number_operation = str(input(' Enter number of opration: '))
    
def fdooperation(running):
    global number1
    global number2
    global number_operation
    
    if '1' in number_operation:
        result = str(number1 + number2)
        print(' Your result is: ' + result)
    elif '2' in number_operation:
        result = str(number1 - number2)
        print(' Your result is: ' + result)
    elif '3' in number_operation:
        result = str(number1 * number2)
        print(' Your result is: ' + result)
    elif '4' in number_operation:
        try:
            result = str(number1 / number2)
            print(' Your result is: ' + result)
        except Exception:
            print(' You can\'t division zero...')
            running = False

def fexit(running):
    try:
        a = input('\n Are you want to exit?[y/n]')
        if a == 'y':
            print(' Good luck!')
            sys.exit()
    except Exception:
        print('')
    
# main loop
running = True
while running:
    # I think solo learn can not get tow input.(so bad...)
    finput(running)
    
    fopration()
    
    fdooperation(running)

    fexit(running)