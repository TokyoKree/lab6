def sum(x1, x2):
    return x1 + x2
def mul(x1, x2):
    return x1 * x2
def sub(x1, x2):
    return x1 - x2
def div(x1, x2):
    if x2 != 0:
      return x1/x2


x1 = 0
x2 = 0
F = open("Unit.txt")
p = F.readlines()
for i in range(len(p)):
    str = p[i]
    if (str[1]=="+"):
        print(sum(int(str[0]),int(str[2])))
    if (str[1]=="*"):
        print(mul(int(str[0]),int(str[2])))
    if (str[1]=="-"):
        print(sub(int(str[0]),int(str[2])))
    if (str[1]=="/"):
        print(div(int(str[0]),int(str[2])))

