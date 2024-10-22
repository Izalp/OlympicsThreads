import threading
import time
import random
from sports import sports


# Função para simular a execução do esporte, com título e duração específica
def sport(title, duration, daily_total_hours, lock):
    start_time = time.perf_counter()  # Captura o tempo inicial
    print(f'Modalidade {title} iniciada - tempo inicio: {start_time:.3f}')

    elapsed_time = 0
    time_count = 0.1

    while elapsed_time < duration:
        elapsed_time += time_count

    end_time = time.perf_counter()  # Captura o tempo final
    print(f'Modalidade {title} finalizada - tempo final: {end_time:.3f}')
    
    with lock:
        daily_total_hours[0] += duration

    print(f'Modalidade {title} concluída após {duration:.3f} horas. '
          f'Espera: {end_time - start_time:.3f} segundos.')


# Simula o início dos Jogos Olímpicos, distribuindo os esportes ao longo dos dias
def start_olympics():
    print('\nOs Jogos Olímpicos em Paris 2024 foram iniciados!\n')

    day_duration = 12  
    day_count = 0 
    all_sports = sports.copy()  
    pending_sports = []  

    lock = threading.Lock()

    while all_sports or pending_sports:
        day_count += 1

        print(f'--- Início do dia {day_count} ---\n')

        day_remaining = day_duration  
        executed_today = []  
        daily_total_hours = [0]

        # Executa os esportes pendentes, se houver tempo no dia
        while pending_sports and day_remaining > 0:
            title, duration = pending_sports.pop(0)

            if duration <= day_remaining:
                t = threading.Thread(target=sport, args=(
                    title, duration, daily_total_hours, lock))
                executed_today.append((t, title))

                t.start()  
                day_remaining -= duration 
            else:
                pending_sports.insert(0, (title, duration))
                break

        # Executa novos esportes, se houver tempo restante no dia
        while all_sports and day_remaining > 0:
            title = all_sports.pop(0)
            duration = random.uniform((1/60), 5)

            if duration <= day_remaining:
                t = threading.Thread(target=sport, args=(
                    title, duration, daily_total_hours, lock))
                executed_today.append((t, title))

                t.start()  
                day_remaining -= duration 
            else:
                pending_sports.append((title, duration))

        for t, title in executed_today:
            t.join()

        executed_sports = ', '.join([title for _, title in executed_today])
        print(
            f'\n--- Fim do dia {day_count} ---\nEsportes executados: {executed_sports}\n')

        print(
            f'Total de horas de esportes executados no dia {day_count}: {daily_total_hours[0]:.3f} horas\n')
        
    print(
        f'Os Jogos Olímpicos em Paris 2024 foram finalizados após {day_count} dias!\n')


# Inicia a simulação dos Jogos Olímpicos
start_olympics()
