def add (*nums):
    sum = 0
    for num in nums:
        sum = sum + num

    return sum

print(add(2,3,6))


def intro(**data):
    print("\nData type of argument:",type(data))
    for key, value in data.items():
        print("{} is {} ".format(key,value))
intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)