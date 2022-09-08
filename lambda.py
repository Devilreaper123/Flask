# add = lambda x,y : x+y
# print(add(5,6))

def double(x):
    return x * 2

seq = [1,3,5,7,9]

# doubled = [double(x) for x in seq]
# doubled = map(double , seq)
doubled = map(lambda x : x*3 , seq)
print(list(doubled))