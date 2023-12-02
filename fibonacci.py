def fibonacci(n):
    a=0
    b=1
    my_list = []
    while a < n:
        my_list.append(a)

        a,b=b,a+b
    return my_list
print(fibonacci(100))