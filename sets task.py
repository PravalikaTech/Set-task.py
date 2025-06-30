
# 1) From the list nums = [10, 25, 30, 45, 50, 60], create a set of numbers where the number is divisible by 5 but not divisible by 10 using set comprehension.
n=[10, 25, 30, 45, 50, 60]
res={i for i in n if i%5==0 and i%10!=0}
print(res)

# Output:-
# {25, 45}

# 2) Write a program to sum the digits of all numbers in a list.
#     Example: [12, 34, 5] ➞ 1+2 + 3+4 + 5 = 15
n=[12, 34, 5]
sum=0
for i in n:
    for digit in str(i):
        sum+=int(digit)
print("Sum of all digits:", sum)

# Output:-
# Sum of all digits: 15

# 3) Create a new list by repeating elements of a list n times.
#      Example: [1, 2, 3], n = 2 ➞ [1, 2, 3, 1, 2, 3]
a=[1, 2, 3]
n=2
res=a*n
print(res)

# Output:-
# [1, 2, 3, 1, 2, 3]

# 4) Write a function to count frequency of each element in a list (return as dictionary).
def fun(a):
    res={}
    for i in a:
        if i in res:
            res[i]+=1
        else:
            res[i]=1
    return res
print(fun([1, 2, 2, 3, 1, 4, 2]))

# Output:-
# {1: 2, 2: 3, 3: 1, 4: 1}

# 5) Write a function to count how many prime numbers exist in a given range.
def fun(start, end):
    count=0
    for x in range(start, end+1):
        if x<2:
            continue
        is_prime=True
        for i in range(2,x):
            if x%i==0:
                is_prime=False
                break
        if is_prime:
            count+=1
    return count
print(fun(10,20))

# Output:-
# 4             #(11,13,17,19)

# 6) Write a function to calculate the sum of digits of a number until a single-digit result is obtained.
#   Example: 9875 ➞ 9+8+7+5=29 ➞ 2+9=11 ➞ 1+1=2
def digit_sum(n):
    while n>=10:
        n=sum(int(x) for x in str(n))
    return n
print(digit_sum(9875))

# Output:-
# 2
