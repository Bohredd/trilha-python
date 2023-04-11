import random
import string

tamanhoSenha = 16

caracteres = string.ascii_letters + string.digits + '!@#$%&*()-+=.;,'

randomVar = random.SystemRandom() # os.urandom() <- para criar gerador a partir de objetos

print(''.join(randomVar.choice(caracteres) for i in range(tamanhoSenha)))
