#a
A, B = map(int, input().split())
print((A-B)/3 + B)
#b
a = 0
b = 0
c = 0
d = 0
for i in range(4):
  h = input()
  if h == "H":
    a =1
  if h == "2B":
    b=1
  if h == "3B":
    c=1
  if h == "HR":
    d=1
if a+b+c+d == 4:
  print("Yes")
else:
  print("No")
