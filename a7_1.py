import random
from colorama import Fore

boys = ['ali', 'reza', 'yasin', 'benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']
girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']
result=[]

for i in range(len(boys)):
    b = random.choice(boys)
    g = random.choice(girls)
    boys.remove(b)
    girls.remove(g)
    m=[b,g]
    result.append(m)

for j in range(len(result)):
    print(Fore.LIGHTGREEN_EX+'new family 👪:\n')
    print(Fore.BLACK+'Groom 🤵: '+Fore.BLUE+result[j][0])
    print(Fore.RED+'          &')
    print(Fore.WHITE+'Bride 👰: '+Fore.BLUE+result[j][1]+'\n')

