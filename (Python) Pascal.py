#Aidan Lim
#Pascal's Triangle

def pascal(row, num):
   if num == 0:
      return 1
   elif num == row - 1:
      return 1
   else:
      return pascal(row - 1, num - 1) + pascal(row - 1, num)

for row in range(6):
   for space in range(6-row):
      print(end = " ")
   for num in range(row):
      print(pascal(row, num), end = " ")
   print()