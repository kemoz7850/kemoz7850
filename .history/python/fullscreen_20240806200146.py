x = 1
total = 0
while x != 0:
    x = int(input())
    total += x
tax = int(input())
after = total * (tax/100)
print(total)