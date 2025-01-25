import random
Characters = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+"
Faces = "🥸😏😶‍🌫️😒🙄😬🫣🤫🤔🫡🤐🤨😐😜😛😋🥲😙😚😊😗😘🤩😍🥰😇😀😃😄😁😆😅🤣😂🙂🙃🫠😉😊☹️😟🙁🫤😕🧐🤓😎🥸🥳🤯😵‍💫🤠😮😯😲😳🥺🥹😦😧😨😰😥😢😭😈🤬😠😡😤🥱😫😩😓😞😣😖😱👿💀☠️💩🤡👹👺"
Fruits = "🍄🍇🍈🍉🍊🍋🍌🍍🥭🍎🍏🍐🍑🌶️🌽🥕🥔🍆🥑🥥🫒🍅🥝🫐🍓🍒🫑🥒🥬🥦🧄🧅🥜🫘🌰🍞🥐🍟🍔🥓🥩🍗🍖🧀🧇🥞🥯🫓🥖🍕🌭🥪🌮🌯🫔🥙🧆🥚🍳🥘🍲🫕🍝🍜🍛🍚🍙🍙🍘🧂🧈🍿🥣🥗🍠🍢🍣🍤🥮🍡🥟🥠🦀🦞🦐🍬🍫🥧🧁🍰🎂🍪🍩🍨🍧🍦🦪🦑🍭🍮🍯🍼🥛☕🫖🍵🍶🍾🍷🍸🍹"
length_of_pass = int(input("Please Give the length of the password: "))
All =  Faces + Fruits + Characters

list_of_sets = [Characters,Faces,Fruits,All]


print("---------------------------------------------------------------------------------------------")
print("setA 'Characters', ", Characters)
print("---------------------------------------------------------------------------------------------")
print("setB 'Faces', ", Faces)
print("---------------------------------------------------------------------------------------------")
print("setC 'Fruits', ", Fruits)
print("---------------------------------------------------------------------------------------------")
print("setD 'All', ", All)
print("---------------------------------------------------------------------------------------------")

try: 
 choosen_set = str(input("Please choose one off the sets from above: "))

except ValueError:
    print("Please select a set from Faces, Characters, Fruits, All")

if choosen_set == "Faces":
    choosen_set = Faces
elif choosen_set == "Characters":
    choosen_set = Characters
elif choosen_set == "Fruits":
    choosen_set = Fruits
elif choosen_set == "All":
    choosen_set = All
else:
    print("Please choose one set from above sets.")



def password_func(length_of_pass):
       main_password = []
       for i in range(length_of_pass):
            keys = random.choice(choosen_set)
            main_password.append(keys)
 
            password = "".join(main_password)
            value = "The generated password is: "+ password

       return print(value)

password_func(length_of_pass)



