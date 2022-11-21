from textwrap import indent


message = ' Hello There. My name is Mustafa Aydoğmuş'

# message = message.upper()
# message = message.lower()
# message = message.title()
# message = message.capitalize()

# message = message.strip() # Cümle başındaki boşluğu kaldırı.

# message = message.split()
# # message = message.split('.')
# message = '---'.join(message)

# index = message.find('Mustafa')
# print(index)

isFound = message.startswith('H') # Cümlenin içinde H harfi ile mi başlıyor ?
print(isFound)

isFound = message.endswith('ş') # Cümmle ş harfi ile mi bitiyor ?
print(isFound)

message = message.replace('Mustafa', 'Aydoğmuş')
message = message.replace(' ', '*')
print(message)
print(message)

message = message.center(100,'*')
print(message)
# print(message[1])
