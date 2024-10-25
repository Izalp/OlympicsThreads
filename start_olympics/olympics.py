import threading
import time
import random
from collections import deque
from sports import sports


# Função para simular a execução do esporte, com título e duração específica
def sport(title, duration, results, lock, quantum=None):
    start_time = time.perf_counter()  # Captura o tempo inicial
    print(f'Modalidade {title} - TEMPO INICIO: {start_time:.3f}')
    
    # Se for RR, usa o quantum
    if quantum:
        time_count = min(duration, quantum)
        while duration > 0:
            time.sleep(time_count)
            duration -= time_count
            if duration > 0:
                print(f"{title} - Pausado, {duration:.2f}h restantes...")
    else:
        time.sleep(duration)

    end_time = time.perf_counter()  # Captura o tempo final
    elapsed_time = end_time - start_time

    print(f'Modalidade {title} - TEMPO FINAL: {end_time:.3f}')

    with lock:
        results.append((title, duration, elapsed_time))


# Função para executar FCFS 
def fcfs(sports_queue, results, lock):
    while sports_queue:
        title, duration = sports_queue.popleft()
        sport(title, duration, results, lock)


# Função para executar RR
def rr(sports_queue, results, lock, quantum):
    while sports_queue:
        title, duration = sports_queue.popleft()
        sport(title, duration, results, lock, quantum=quantum)
        if duration > 0:  # Se não foi finalizado, volta ao final da fila
            sports_queue.append((title, duration))


def start_olympics(algorithm="FCFS", quantum=0.5):
    print('\nOs Jogos Olímpicos em Paris 2024 foram iniciados!\n')

    day_count = 0
    all_sports = sports.copy()  
    lock = threading.Lock()

    results = [] 

    if algorithm == "FCFS":
        sports_queue = deque([(title, random.uniform((1/60), 5)) for title in all_sports])
        fcfs(sports_queue, results, lock)

    elif algorithm == "RR":
        sports_queue = deque([(title, random.uniform((1/60), 5)) for title in all_sports])
        rr(sports_queue, results, lock, quantum)

    day_count += 1

    total_time = sum([elapsed_time for title, duration, elapsed_time in results])
    print(f'\nOs Jogos Olímpicos em Paris 2024 foram finalizados após {day_count} dias!\n')
    print(f'Tempo total de processamento: {total_time:.2f} segundos')

    return total_time

def compare_algorithms():
    print("Executando FCFS...")
    fcfs_time = start_olympics("FCFS")

    print("Executando RR...")
    rr_time = start_olympics("RR", quantum=1)  # 1 hora

    # Comparar tempos
    print(f"Tempo total com FCFS: {fcfs_time:.2f} segundos")
    print(f"Tempo total com RR: {rr_time:.2f} segundos")

    if fcfs_time < rr_time:
        print("FCFS foi mais rápido.")
    else:
        print("RR foi mais rápido.")


compare_algorithms()
