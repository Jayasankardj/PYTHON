#string w/o vowels

s="we can play the game"
new_line=" "
vowels="AaEeIiOoUu"
for i in s:
    if i not in vowels:
        new_line=new_line+i
print(new_line)
