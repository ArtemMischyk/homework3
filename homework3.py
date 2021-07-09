def reverse_string1(s):
    return s [:: - 1]

print(reverse_string1("Hello my name is Artem"))


n = 5
for i in range(1, n + 1 ):
    print("*" * i)


print("****")
print("***")
print("**")
print("*")


a = int(input())
b = int(input())
if a < b:
   for i in range(a,b+1):
    print(i)
else:
    for i in range(a,b - 1, -1):
        print(i)





a = int(input())
b = int(input())
for i in range(a,b+1):
    print(i)