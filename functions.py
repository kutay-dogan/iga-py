
def say_hello(name:str):
    print(f"{name} says hello")

say_hello("kutay")


def add_items(a:int,b:int) -> int:
    return a+b

summation = add_items(1,2)
print(summation)


abs_list = map(abs, [10,-1,20])

#for num in abs_list:
    #print(num)

def positive(x): return x>0

for x in filter(positive, [10,-1,20]):print(x)



def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1,2,3))


def sum_for(num_list):
    summation = 0

    for i in num_list:
        summation += i
    
    return summation

print(sum_for([1,2,3]))


def fibonacci(n):
    if n <=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

print(fibonacci(1))


