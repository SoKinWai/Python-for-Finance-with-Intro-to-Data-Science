#c. Create one or more Python scripts in each subfolder, at each level.
# Each script should have a unique function (you may reuse previously-created functions and/or create new functions).
# Be sure to name the scripts aptly.


def Fibonacci_recursive(N):
    res = [0, 1]
    if N <= 0:
        print("Please enter a positive integer")
    elif N == 1:
        return([0])
    else:
     for i in range(2, N):
        res.append(res[i - 1] + res[i - 2])
     return (res)