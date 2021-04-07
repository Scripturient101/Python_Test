
str = input('Enter your string:')
nix=len(str)
print ("Length of the string entered:",nix)

if nix>7:
    for i in str[0::2] :
        print(i)
else:
    for i in str[1::2] :
        print(i)