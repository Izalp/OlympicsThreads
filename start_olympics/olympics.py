# A duração dos esportes variam de 1 minuto até 5 horas (300  minutos)
# Os esportes podem ocorrem entre as 9h ás 21h no dia = 12 horas
# tempo máximo de ocorrer os esportes é 12 horas = 720 minutos
# Os esportes que não ocorrerem até esses 720 minutos, ficam para o próximo dia
# O proximo dia também tera 12 horas e os esportes irão ocorrer nesse tempo
# Só vai terminar quando todos os esportes acontecerem
# os esportes são threads

import threading
import time
import random
from sports import sports

# Função que simula a duração de cada esporte


def sport(title, duration):
    time.sleep(duration)
    print(f'Modalidade {title} concluída após {duration:.2f} horas.')

# Função


def start_olympics():
    print('Os Jogos Olímpicos em Paris 2024 foram iniciados!\n')

    day_duration = 12  # Duração máxima
    day_count = 0  # Contador de dias
    all_sports = sports.copy()  # Copia a lista de esportes
    pending_sports = []  # Esportes que não puderam ser executados no dia anterior

    while all_sports or pending_sports:
        day_count += 1
        print(f'--- Início do dia {day_count} ---')
        day_remaining = day_duration
        executed_today = []

        # Começa o próximo dia com esportes pendentes do dia anterior
        while pending_sports and day_remaining > 0:
            title, duration = pending_sports.pop(0)
            if duration <= day_remaining:
                t = threading.Thread(target=sport, args=(title, duration))
                executed_today.append((t, title))
                t.start()
                day_remaining -= duration
            else:
                # Reinsere na frente se não couber
                pending_sports.insert(0, (title, duration))
                break

        # Começa os esportes restantes
        while all_sports and day_remaining > 0:
            title = all_sports.pop(0)
            # Duração do evento entre 1 e 300 segundos
            duration = random.randint(0.0167, 5)

            if duration <= day_remaining:
                t = threading.Thread(target=sport, args=(title, duration))
                executed_today.append((t, title))
                t.start()
                day_remaining -= duration
            else:
                pending_sports.append((title, duration))

        # Aguarda todas as threads do dia terminarem
        for t, title in executed_today:
            t.join()

        print(
            f'--- Fim do dia {day_count}, esportes executados: {[title for _, title in executed_today]} ---\n')

    print(
        f'Os Jogos Olímpicos em Paris 2024 foram finalizados após {day_count} dias!')


start_olympics()
