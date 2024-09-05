import threading
import time
import random
from sports import sports


def sport(title, duration):
    time.sleep(duration)
    print(f'Modalidade {title} concluída após {duration:.2f} horas.')


def start_olympics():
    print('Os Jogos Olímpicos em Paris 2024 foram iniciados!\n')

    day_duration = 12
    day_count = 0
    all_sports = sports.copy()
    pending_sports = []

    while all_sports or pending_sports:
        day_count += 1
        print(f'--- Início do dia {day_count} ---')
        day_remaining = day_duration
        executed_today = []

        while pending_sports and day_remaining > 0:
            title, duration = pending_sports.pop(0)
            if duration <= day_remaining:
                t = threading.Thread(target=sport, args=(title, duration))
                executed_today.append((t, title))
                t.start()
                day_remaining -= duration
            else:
                pending_sports.insert(0, (title, duration))
                break

        while all_sports and day_remaining > 0:
            title = all_sports.pop(0)
            duration = random.uniform((1/60), 5)

            if duration <= day_remaining:
                t = threading.Thread(target=sport, args=(title, duration))
                executed_today.append((t, title))
                t.start()
                day_remaining -= duration
            else:
                pending_sports.append((title, duration))

        for t, title in executed_today:
            t.join()

        executed_sports = ', '.join([title for _, title in executed_today])
        print(
            f'--- Fim do dia {day_count}, esportes executados: {executed_sports} ---\n')

    print(
        f'Os Jogos Olímpicos em Paris 2024 foram finalizados após {day_count} dias!')


# Inicia a simulação dos Jogos Olímpicos
start_olympics()
