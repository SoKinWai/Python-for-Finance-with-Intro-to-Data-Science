#c. Create one or more Python scripts in each subfolder, at each level.
# Each script should have a unique function (you may reuse previously-created functions and/or create new functions).
# Be sure to name the scripts aptly.


def Fibonacci_iterative(N):
    # return Fibonacci series up to N
    res = []
    a=0
    b=1
    if N<=0:
     print("Please enter a positive integer")
    elif N==1:
     return([0])
    else:
        res.append(a)
        res.append(b)
        while len(res) != N:
            temp = a + b
            res.append(temp)
            a = b
            b = temp

        return(res)