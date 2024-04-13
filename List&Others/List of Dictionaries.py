def add(x,y):
    print(x+y)
# this is keyword arguments

add(y = 2, x=7)


def pizza(name,size,*toppings): # by adding * we can said that all the arbitrary value will be the toppings
    print(name,size,toppings)
    return "Hello"

pizza("Tikka",12,"Olives","Tomatoe","Mushrooms")