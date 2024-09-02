import threading
import time
import random
from sports import sports


def sport(title):
    tempo = random.uniform(10.0, 40.0)
    time.sleep(tempo)
    print(f'Modalidade {title} iniciada')
    print(f'Duração: {tempo:.2f} minutos.\n')


def start_olympics():
    print('Os Jogos Olímpicos em Paris 2024 foram iniciados!\n')

    threads = []

    for title in sports:
        t = threading.Thread(target=sport, args=(title,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print('Os Jogos Olímpicos em Paris 2024 foram finalizados!\n')


start_olympics()
