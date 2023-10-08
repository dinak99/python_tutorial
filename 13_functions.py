###############################################################################################################################
def my_function():
    print("Hello from a function")


my_function()


###############################################################################################################################
def my_function(fname):
    print(fname + " Refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus")


###############################################################################################################################
def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))


###############################################################################################################################
def my_function(country="Norway"):
    '''Default parameter value'''
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


###############################################################################################################################
def my_function(child3, child2, child1):
    '''Keyword arguments'''
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")  # out of order


###############################################################################################################################
def my_function(*kids):
    '''Arbitrary arguments: *args'''
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


###############################################################################################################################
def my_function(**kid):
    '''Arbitrary keyword arguments, **kwargs'''
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")


###############################################################################################################################
def myfunc():
    '''function inside function'''
    x = 300

    def myinnerfunc():
        print(x)
    myinnerfunc()


myfunc()


###############################################################################################################################
def my_function(food):
    '''You can send any data types of argument to a function (string, number, list, dictionary etc.)'''
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]
my_function(fruits)


###############################################################################################################################
def myfunction():
    '''empty function'''
    pass  # you cant' call, it is not defined


###############################################################################################################################
def myRecursion(k):
    '''recursion'''
    if k == 0:
        return 0  # basic case
    result = k + myRecursion(k-1)  # recursion case
    print(result)
    return result


myRecursion(6)
