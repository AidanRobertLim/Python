#Aidan Lim
#Letter Inventory

inv = [0] * 27
print("Enter a phrase.")
phrase = input()
for letter in phrase:
    if 97 <= ord(letter) <= 122:
        inv[ord(letter)-97] += 1
print(inv)
    
