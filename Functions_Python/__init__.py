"""Lambda Functions
The creation of anonymous functions at runtime, using a construct called "lambda".
Lambda function doesn't include return statement, it always contains an expression which is returned.
This piece of code shows the difference between a normal function definition ("f") and a lambda function ("g"):
"""
def f (x):
    return x**2
print (f(8))
#Lambda Function
#lambda expressions
times3 = lambda var:var*3
print(times3(10))
#lambda expressions: anoth


##  Map() Function
"""
Map() function is used with two arguments. Just like: r = map(func, seq)
The first argument func is the name of a function and the second a sequence (e.g. a list).
seq. map() applies the function func to all the elements of the sequence seq. It returns a new list with the elements 
changed by func.
"""

s = "it is ranining cats and dogs"
w = s.split()
l = []
for i in w:
    l.append(len(i))
print(l)
l2 = map(lambda w:len(w),w)
print(list(l2))

##  Filter()
fib = [0,1,1,2,3,5,8,13,21,34,55]
result1 = filter(lambda x: x % 2, fib)
list(result1)