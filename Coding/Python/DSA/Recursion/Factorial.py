import sys
print(sys.getrecursionlimit)
sys.setrecursionlimit(100)
def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

print(factorial(5)) 