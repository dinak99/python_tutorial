try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
finally:
    # good to close/clean/free objects
    print("Executed no matter if the try block raises any errors or not")

try:
    x = 1 / 0
    print(x)
except NameError:
    print("Variable x is not defined")
except ZeroDivisionError as err:
    print('Handling run-time error:', err)
except:
    print("Something else went wrong")

try:
    raise TypeError("Only integers are allowed")
    raise Exception("Sorry, no numbers below zero")
except TypeError as err:
    print("TypeError: {0}".format(err.args))
except:
    print("Something else went wrong")
