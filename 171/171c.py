N = int(input())

# def Base_10_to_n(X, n):
#     alfabet = ["a","b","c","d","e","f","g","h","i","j","k","l","n","m","o","p","q","r","s","t","u","v","w","x","y","z"]
#     X_dumy = X
#     out = ''
#     while X_dumy>0:
#         out = alfabet[X_dumy%n-1]+out
#         X = X_dumy%n
#         X_dumy = int(X_dumy/n)
#         if X == 0:
#             break
#     return out


def num2alpha(num):
    if num<=26:
        return chr(64+num)
    elif num%26==0:
        return num2alpha(num//26-1)+chr(90)
    else:
        return num2alpha(num//26)+chr(64+num%26)


print(num2alpha(N).lower())
