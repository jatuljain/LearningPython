def fizzBuzz(n):
    # Write your code here
    for i in list(range(n)):
        # print (i,"outside of if condition" )
        if int(i%3) == 0:
            print ("Fizz")
        elif int(i%5) == 0:
            print("Buzz")
        elif int(i%3) == 0 and int(i%5) == 0:
            print("FizzBuzz")
        else:
            print(i)
        

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)