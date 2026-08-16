def prime(n):
    flag = 0
    if(n == 1):
        print("It's not a prime number.")
    else:
        for div in range(2,int(n/2)):
            if n%div == 0:
                flag += 1
                break
        if(flag == 0):
            print("It's a prime number.")
        else:
            print("It's not a primt number.")

number = int(input("Check this number:"))
prime(n = number)