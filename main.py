s=input("Enter the string :")
if len(s) == 0:
  print(0)
elif s[0] == '-':
  print("negative numbers or strings not allowed")
else:
  print("Reverse of the string ",s," is ",s[::-1])
