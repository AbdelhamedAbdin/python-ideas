def func(n):
    i = 0
    
    while i < n:
        if n < 0:
            return
        else:
            r = i ** 2
            print(r)
        i += 1

func(int(input("enter number: \n")))

i = 0
n = int(input("enter number: \n"))

while i < n:
    if n < 0:
        break
    else:
        if i <= 20:
            r = i ** 2
            print(r)
    i += 1