import threading
import time
import random
from sports import sports


# Função para simular a execução do esporte, com título e duração específica
def sport(title, duration):
    time.sleep(duration)
    print(f'Modalidade {title} concluída após {duration:.2f} horas.')


# Simula o início dos Jogos Olímpicos, distribuindo os esportes ao longo dos dias
def start_olympics():
    print('\nOs Jogos Olímpicos em Paris 2024 foram iniciados!\n')

    day_duration = 12  # Duracao maxima de um dia (12 horas)
    day_count = 0  # Contador de dias
    all_sports = sports.copy()  # Lista de todos os esportes
    pending_sports = []  # Lista dos esportes pendentes para o próximo dia

    # Executa enquanto houver esportes a serem realizados
    while all_sports or pending_sports:
        day_count += 1

        print(f'--- Início do dia {day_count} ---\n')

        day_remaining = day_duration  # Tempo restante do dia
        executed_today = []  # Esportes executados no dia

        # Executa os esportes pendentes, se houver tempo no dia
        while pending_sports and day_remaining > 0:

            # Remove o primeiro esporte da lista de pendentes
            title, duration = pending_sports.pop(0)

            # Verifica se há tempo suficiente para executar o esporte
            if duration <= day_remaining:
                # Cria uma thread para o esporte
                t = threading.Thread(target=sport, args=(title, duration))
                executed_today.append((t, title))

                t.start()  # Inicializa a Thread
                day_remaining -= duration  # Decrementa o tempo do dia a cada esporte executado
            else:
                # Reinsere o esporte na lista de pendentes se não houver tempo suficiente
                pending_sports.insert(0, (title, duration))
                break

        # Executa novos esportes, se houver tempo restante no dia
        while all_sports and day_remaining > 0:
            # Remove o primeiro esporte da lista de todos os esportes
            title = all_sports.pop(0)

            # Duração aleatória (em horas)
            duration = random.uniform((1/60), 5)

            # Verifica se há tempo suficiente para executar o esporte
            if duration <= day_remaining:
                t = threading.Thread(target=sport, args=(title, duration))
                executed_today.append((t, title))

                t.start()  # Inicializa as Threads
                day_remaining -= duration  # Decrementa o tempo do dia a cada esporte executado
            else:
                pending_sports.append((title, duration))

        # Espera que todos os esportes do dia sejam concluídos
        for t, title in executed_today:
            t.join()

        # Exibe o resumo dos esportes executados no dia
        executed_sports = ', '.join([title for _, title in executed_today])
        print(
            f'\n--- Fim do dia {day_count} ---\nEsportes executados: {executed_sports}\n')

     # Exibe mensagem de finalização dos Jogos Olímpicos
    print(
        f'Os Jogos Olímpicos em Paris 2024 foram finalizados após {day_count} dias!\n')


# Inicia a simulação dos Jogos Olímpicos
start_olympics()
