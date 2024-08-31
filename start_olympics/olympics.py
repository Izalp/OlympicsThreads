import threading
import time
import random
from sports import sports


def sport(title):
    print(f'Modalidade iniciada: {title}')
    tempo = random.uniform(1.0, 15.0)
    time.sleep(tempo)
    print(f'Duração: {tempo:.2f} minutos.\n')


def start_olympics():
    print('\nOs Jogos Olímpicos em Paris 2024 foram iniciados!\n')

    threads = []

    for title in sports:
        t = threading.Thread(target=sport, args=(title,))
        threads.append(t)
        t.start()
        t.join()

    print('Os Jogos Olímpicos em Paris 2024 foram finalizados!\n')


start_olympics()
