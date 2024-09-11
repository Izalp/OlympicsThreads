<div style="text-align: center;">
  <img src="https://github.com/user-attachments/assets/fc545583-f9af-4f79-b9ed-df713148e325" alt="img">
</div>

# **Projeto - Olympics Threads** 🏅

Uma simulação em Python que imita vários eventos esportivos olímpicos ocorrendo simultaneamente, usando threads. Este projeto demonstra como lidar com concorrência e paralelismo em Python enquanto simula os diversos eventos que acontecem durante os Jogos Olímpicos.

## **Índice**

- [Visão Geral](#visão-geral)
- [Primeiros Passos](#primeiros-passos)
- [Detalhes do Código](#detalhes-do-código)
- [Autores](#autores)

## **Visão Geral**

Este projeto simula uma variedade de esportes olímpicos usando threads em Python para representar cada evento. Cada esporte possui uma duração aleatória e ocorre dentro de um dia de competição que dura 12 horas, emulando a natureza concorrente dos eventos olímpicos do mundo real. O projeto é estruturado de forma modular, permitindo fácil adição de novos esportes e extensões à simulação.

## **Primeiros Passos**

Para obter uma cópia local e colocá-la em funcionamento, siga estas etapas:

### 1. **Pré-requisitos**

- [Python 3.6 ou superior](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

### 2. **Instalação**

- Clone o repositório:

  ```bash
  git clone https://github.com/Izalp/OlympicsThreads.git
  ```

### 3. **Execução**

- Execute a simulação usando o comando:
  ```bash
  python start_olympics/olympics.py
  ```

## **Detalhes do Código**

### ⚙️ Estrutura do Código

- **Importações Necessárias**
  - `threading`: Para criar threads, possibilitando a execução simultânea de esportes.
  - `time`: Para controlar o tempo de execução de cada esporte.
  - `random`: Para gerar durações aleatórias para cada esporte.
  - `sports`: Lista de esportes importada de um módulo externo.

### 🔧 Funções Principais

- **`sport(title, duration, daily_total_hours)`**: Simula a execução de um esporte por uma duração específica.
- **`start_olympics()`**: Função que gerencia a simulação geral dos Jogos Olímpicos. Ela coordena os dias de competição, executa os esportes usando threads e lida com esportes pendentes que não puderam ser concluídos no dia atual.

### 📊 Fluxo de Execução

1. **Inicialização da Simulação**

   - A função `start_olympics()` é chamada para iniciar a simulação.
   - Exibe uma mensagem indicando o início dos Jogos Olímpicos de Paris 2024.

2. **Configuração Inicial**

   - Definições básicas como a duração de um dia de competição (`day_duration = 12` horas) e o contador de dias (`day_count = 0`) são estabelecidas.
   - Listas de esportes:
     - `all_sports`: Cópia da lista de esportes.
     - `pending_sports`: Esportes que não puderam ser executados no dia anterior.

3. **Execução dos Esportes**

   - Continua enquanto houver esportes a serem executados (`all_sports` ou `pending_sports`).
   - Executa esportes pendentes do dia anterior, se houver tempo suficiente.
   - Executa novos esportes da lista principal, conforme o tempo disponível.
   - Esportes não executados são adicionados à lista `pending_sports` para o dia seguinte.

4. **Gerenciamento de Threads**

   - Cada esporte é executado em uma thread separada, permitindo execuções simultâneas.
   - `t.join()` é utilizado para aguardar a conclusão de todas as threads do dia atual antes de iniciar um novo dia.

5. **Conclusão da Simulação**
   - Exibe uma mensagem final indicando a conclusão dos Jogos Olímpicos após o término de todos os esportes.

### 📊 Exemplo de Saída

```plaintext
Os Jogos Olímpicos em Paris 2024 foram iniciados!

--- Início do dia 1 ---

Modalidade Golfe concluída após 0.036 horas.
Modalidade Natação concluída após 0.138 horas.
Modalidade Futebol concluída após 0.193 horas.
Modalidade Maratona Aquática concluída após 0.537 horas.
Modalidade Basquete concluída após 2.447 horas.
Modalidade Badminton concluída após 3.905 horas.
Modalidade Atletismo concluída após 4.689 horas.

--- Fim do dia 1 ---
Esportes executados: Atletismo, Badminton, Basquete, Futebol, Golfe, Maratona Aquática, Natação

Total de horas de esportes executados no dia 1: 11.944 horas

--- Início do dia 2 ---

Modalidade Basquete 3x3 concluída após 2.362 horas.
Modalidade Breaking concluída após 2.577 horas.
Modalidade Boxe concluída após 2.708 horas.
Modalidade Canoagem de Velocidade concluída após 3.509 horas.

--- Fim do dia 2 ---
Esportes executados: Basquete 3x3, Boxe, Breaking, Canoagem de Velocidade

Total de horas de esportes executados no dia 2: 11.156 horas

Os Jogos Olímpicos em Paris 2024 foram finalizados após 2 dias!
```

## **Autores**

Desenvolvedores que contribuíram para a estruturação e desenvolvimento deste projeto:

- **Iza Lopes Ribeiro**  
  [GitHub: Izalp](https://github.com/Izalp)

- **Wiliane Carolina Silva**  
  [GitHub: wilicarol](https://github.com/wilicarol)
