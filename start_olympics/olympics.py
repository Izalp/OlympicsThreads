import threading
import time
import random
from sports import sports


def sport(title, duration): # titulo e tempo de duracao da Thread
    time.sleep(duration)
    print(f'Modalidade {title} concluída após {duration:.2f} horas.')


def start_olympics():
    # Inicialização da funcao 
    print('Os Jogos Olímpicos em Paris 2024 foram iniciados!\n') 

    day_duration = 12 # Duracao maxima
    day_count = 0
    all_sports = sports.copy()
    pending_sports = [] # Lista dos esportes pendentes

    # Executa os esportes de all_sports ate ter o limite do dia atingido e os outros esportes ficam na variavel pending_sports
    while all_sports or pending_sports:
        # Inicia a contagem dos dias
        day_count += 1 
        print(f'--- Início do dia {day_count} ---') 
        # O restante do tempo limite do dia e igualado com a duracao maxima
        day_remaining = day_duration  
        # Lista dos dias
        executed_today = [] 

        # Executa os esportes pendentes enquando tiver tempo de duracao
        while pending_sports and day_remaining > 0:
            # Inicio da pilha
            title, duration = pending_sports.pop(0) 
            # Enquanto tiver tempo irá executar esse bloco
            if duration <= day_remaining: 
                t = threading.Thread(target=sport, args=(title, duration))
                executed_today.append((t, title)) 
                # Inicia a Thread
                t.start()
                # Decrementa o tempo de duracao a cada esporte executado
                day_remaining -= duration 
            else: # Os esportes pendentes serao executados no proximo dia
                pending_sports.insert(0, (title, duration)) 
                break

        # Verifica qual esporte ainda nao foi executado e se tem tempo suficiente para execucao
        while all_sports and day_remaining > 0: 
            title = all_sports.pop(0)
            # A duracao e de forma aleatoria e colocada em formato de hora
            duration = random.uniform((1/60), 5) 
            # Enquanto tiver tempo ira executar esse bloco
            if duration <= day_remaining: 
                t = threading.Thread(target=sport, args=(title, duration))
                executed_today.append((t, title))
                # Inicia a Thread
                t.start()
                # Decrementa o tempo de duração a cada esporte executado
                day_remaining -= duration
            else:
                pending_sports.append((title, duration))

        # Printa as informacoes
        for t, title in executed_today:
            t.join()

        # Finaliza o dia e mostra os esportes executados 
        executed_sports = ', '.join([title for _, title in executed_today])
        print(
            f'--- Fim do dia {day_count}, esportes executados: {executed_sports} ---\n')

    # Finalização da funcao
    print(
        f'Os Jogos Olímpicos em Paris 2024 foram finalizados após {day_count} dias!')


# Inicia a simulação dos Jogos Olímpicos
start_olympics()
