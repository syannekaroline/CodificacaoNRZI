# Esquema de codificação NRZI

Este repositório contém uma implementação da codificação NRZI (Non-Return to Zero Inverted) em Python. A codificação NRZI é utilizada na comunicação de dados, onde a presença ou ausência de transições de sinal determina o valor do bit a ser transmitido.

## Descrição

### Função `nrzi(bits: str) -> str`

A função `nrzi` recebe uma sequência de bits como entrada e retorna uma representação de níveis de tensão conforme o esquema NRZI.

#### Entrada:
- `bits`: Uma string de bits binários (ex.: `"010011"`).

#### Retorno:
- Uma string que representa os elementos de sinal de acordo com a codificação NRZI.

#### Regras de Codificação:
- **Nenhuma Inversão**: O próximo bit é `0`.
- **Inversão**: O próximo bit é `1`.

### Função `NRZIbyUser()`

Esta função permite ao usuário interagir com o programa, solicitando uma sequência de bits para codificação e exibindo o resultado correspondente.

### Função `main()`

A função `main` processa uma lista de sequências de bits predefinidas e exibe graficamente as sequências originais e os resultados obtidos após cada codificação.


## Exemplos de Uso


### 1. Processamento de Múltiplas Sequências de Bits
A função main() processa uma lista de sequências de bits predefinidas e exibe os resultados para cada uma delas. Exemplo:

```plaintext
-=-=-= Esquema de Codificação NRZI -=-=-

- 1ª Sequência -=-=-=-=-=
Sequência de bits: 01001100011 
Elementos de sinal: _|¯¯¯|_|¯¯¯¯|_|¯

- 2ª Sequência -=-=-=-=-=
Sequência de bits: 11111 
Elementos de sinal: _|¯|_|¯|_

- 3ª Sequência -=-=-=-=-=
Sequência de bits: 1000000001010011 
Elementos de sinal: _________|¯¯|___|¯|_

- 4ª Sequência -=-=-=-=-=
Sequência de bits: 1110100101000010 
Elementos de sinal: _|¯|__|¯¯¯|__|¯¯¯¯¯|__

```

### 2. Codificação de uma Sequência de Bits pelo Usuário

Quando o usuário executa a função `NRZIbyUser()`, ele pode inserir uma sequência de bits e receber a representação da codificação NRZI. Veja um exemplo:

```plaintext
-=-=-= Esquema de Codificação NRZI -=-=-

Insira uma sequência de bits (ex.: 01101000): 11111
Sequência de bits: 11111
Elementos de sinal: _|¯|_|¯|_
