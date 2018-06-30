import sys
# 翻译的有问题
print("Enter a Number:")
def clozz(num):
    if num == 0:
        sys.exit(0)
    try:
        if num % 2 == 0:
            res = num//2
            print(str(res))
            return clozz(res)
        elif num %2 == 1:
            res = 3 * num + 1
            print(res)
            return clozz(res)
    except ValueError:
            print("The value must be an integer")

while True:
    print("Please enter a number")
    num = input()
    clozz(num)

