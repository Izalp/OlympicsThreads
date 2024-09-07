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

- **`sport(title, duration)`**: Simula a execução de um esporte por uma duração específica.
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

Modalidade Handebol concluída após 0.11 horas.
Modalidade Rugby Sevens concluída após 0.13 horas.
Modalidade Ciclismo Bmx Racing concluída após 0.26 horas.
Modalidade Atletismo concluída após 0.59 horas.
Modalidade Basquete 3x3 concluída após 3.48 horas.
Modalidade Badminton concluída após 3.57 horas.
Modalidade Basquete concluída após 3.80 horas.

--- Fim do dia 1 ---
Esportes executados: Atletismo, Badminton, Basquete, Basquete 3x3, Ciclismo Bmx Racing, Handebol, Rugby Sevens

--- Início do dia 2 ---

Modalidade Breaking concluída após 1.38 horas.
Modalidade Canoagem de Velocidade concluída após 1.88 horas.
Modalidade Canoagem Slalom concluída após 2.28 horas.
Modalidade Boxe concluída após 3.70 horas.

--- Fim do dia 2 ---
Esportes executados: Boxe, Breaking, Canoagem de Velocidade, Canoagem Slalom

Os Jogos Olímpicos em Paris 2024 foram finalizados após 2 dias!
```

## **Autores**

Desenvolvedores que contribuíram para a estruturação e desenvolvimento deste projeto:

- **Iza Lopes Ribeiro**  
  [GitHub: Izalp](https://github.com/Izalp)

- **Wiliane Carolina Silva**  
  [GitHub: wilicarol](https://github.com/wilicarol)
