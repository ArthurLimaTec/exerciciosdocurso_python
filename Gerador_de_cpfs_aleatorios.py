#GERANDO CPF's ALEATÓRIOS:

# import random
# import sys

# onze_digitos = ''
# for i in range(11):
#     onze_digitos += str(random.randint(0, 9))

# print(onze_digitos)
# sys.exit()


#GERANDO 100 CPF's DE UMA VEZ:

import random
import sys

for _ in range(100):
    onze_digitos = ''
    for i in range(11):
        onze_digitos += str(random.randint(0, 9))

    print(onze_digitos)

sys.exit()