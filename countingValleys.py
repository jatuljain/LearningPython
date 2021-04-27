def countingValleys(n, s):
    a,b = 0,0
    d = {"U":1, "D":-1}
    for i in s:
        if not a+d[i] and a<0:
            b+=1
        a+=d[i]
    return b
n,s = input(),input()
print(countingValleys(n, s))