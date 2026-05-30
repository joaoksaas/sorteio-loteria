import subprocess
import platform

def limpar_tela():
    # Detecta o sistema operacional
    sistema_operacional = platform.system()

    # Define o comando a ser usado com base no sistema operacional
    comando = 'cls' if sistema_operacional == 'Windows' else 'clear'

    # Executa o comando para limpar a tela
    subprocess.run([comando], shell=True)


def pedir_inteiro(mensagem, aceitar_negativo=True):
    """
    Fica em loop até o usuário digitar um número válido ou 'q'.
    """
    while True:
        entrada = input(mensagem).strip()
        
        if entrada.lower() == 'q':
            return 'q'
            
        # Dessa forma o usuário não precisa voltar todo o loop para corrigir apenas um input
        try:
            # O int() entende sinais de negativo perfeitamente
            valor = int(entrada)
            
            # Validação específica para a quantidade de números (não pode ser <= 0)
            if not aceitar_negativo and valor <= 0:
                print("\nErro: A quantidade deve ser um número positivo maior que zero.")
                continue
                
            return valor
            
        except ValueError:
            # Cai aqui se digitar letras, símbolos ou apertar Enter vazio
            print("\nErro: Por favor, digite um número inteiro válido.")