from threading import Thread
def carro1(velocidade):
    trajeto = 0
    while trajeto <= 100:
        print('Carro1: ',trajeto)
        trajeto += velocidade

def carro2(velocidade):
    trajeto = 0
    while trajeto <= 100:
        print('Carro1: ',trajeto)
        trajeto += velocidade


t_carro1 = Thread(target=carro1, args=[2])
t_carro2 = Thread(target=carro2, args=[1])

t_carro1.start()
t_carro2.start()