x=int (input("Enter starting range:"))
w=int (input("Enter ending range:"))
for y in range(x,w+1):
    if y%3==0 and y%5==0:
        print("FizzBuzz")
    elif y%3==0:
        print("Fizz")
    elif y%5==0:
        print("Buzz")
    else:
        print(y)