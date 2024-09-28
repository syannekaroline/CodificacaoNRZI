def nrzi(bits: str) -> str:
    """
    Este método Codifica sequências binárias conforme o esquema de codificação NRZI.
    No NRZI a mudança ou a falta de mudança no nível de tensão determina o valor do bit a ser trasmitido.
    - Nenhuma Inversão: O próximo bit é 0
    - Inversão: O próximo bit é 1

    Entrada: Os sinais binários para transmissão.
    Retorno: Elementos de sinal conforme a codificação NRZI.
    """

    # Representação dos níveis de tensão
    nivelAlto = '¯'
    nivelBaixo = '_'
    transicao = '|'

    #verificação de erro
    if not bits or any(bit not in '01' for bit in bits):
        raise Exception('A entrada deve ser uma sequência de bits binários contendo apenas 0 e 1.')

    # Padrão de inicialização do sinal - nível baixo de tensão
    elemSinal = sinalAtual = nivelBaixo

    # Processa cada bit a partir do segundo
    for i in range(1, len(bits)):
        if bits[i] == '1':
            # Se o bit é 1, inverte o sinal (transição)
            elemSinal += transicao
            sinalAtual = nivelBaixo if sinalAtual == nivelAlto else nivelAlto
            elemSinal += sinalAtual
        else:
            # Se o bit é 0, mantém o mesmo sinal
            elemSinal += sinalAtual

    return elemSinal

def NRZIbyUser():
    """Função de codificação NRZI com interação com usuário"""

    print("\033[92m" + "-=-=-= Esquema de Codificação NRZI -=-=-=-" + "\033[0m")

    # Solicita ao usuário que insira uma sequência de bits
    bits = input("Insira uma sequência de bits (ex.: 01101000): ")

    try:
        resultado = nrzi(bits)
        print(f"Sequência de bits: {bits} \n Elementos de sinal: {resultado}")

    except Exception as e:
        # Se ocorrer um erro, exibe a mensagem de erro
        print(f"Erro: {e}")

def main():
    """Programa que processa uma lista de sequências de bits com o esquema de codificação NRZI e exibie graficamente, tanto as sequências originais quanto os resultados obtidos após cada codificação"""
    
    bitsList = ["01001100011","11111","1000000001010011", "1110100101000010"]

    print("\033[92m" + "-=-=-= Esquema de Codificação NRZI -=-=-=-" + "\033[0m \n")


    for i,bits in enumerate(bitsList):

        print(f"- {i+1}ª Sequência -=-=-=-=-=")
        elemSinal=nrzi(bits)
        print(f" Sequência de bits: {bits} \n Elementos de sinal: {elemSinal}\n")


# Executa a função principal
if __name__ == "__main__":
    main()
