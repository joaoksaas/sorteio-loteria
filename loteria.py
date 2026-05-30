import random
from utils import limpar_tela, pedir_inteiro

# Dicionário para armazenar as modalidades de loteria
MODALIDADES = {
    "1": {"nome": "Megasena", "qtd": 6, "limite": 60},
    "2": {"nome": "Lotofácil", "qtd": 15, "limite": 25},
    "3": {"nome": "Quina", "qtd": 5, "limite": 80},
}


def realizar_sorteio(nome, maior, qte_num):
    limpar_tela()

    # Retorna uma lista de tamanho e limites de acordo com a opção escolhida
    sorteio = random.sample(range(1, maior+1), qte_num)
    sorteio.sort()
    print(f"\nOs números sorteados da {nome} foram: {sorteio}")
    print("\n********************************************************************")
    input("\nPressione Enter para voltar ao menu...")
    limpar_tela()


def person():
    limpar_tela()
    while True:
        # 1. Pede a quantidade (repassa aceitar_negativo=False)
        qte_num = pedir_inteiro("Digite a quantidade de números a serem sorteados ('q' para sair): ", aceitar_negativo=False)
        if qte_num == 'q':
            return

        # 2. Pede o menor número (aceita negativo por padrão)
        menor = pedir_inteiro("Digite o menor número do intervalo ('q' para sair): ")
        if menor == 'q':
            return

        # 3. Pede o maior número (aceita negativo por padrão)
        maior = pedir_inteiro("Digite o maior número do intervalo ('q' para sair): ")
        if maior == 'q':
            return

        # --- VALIDAÇÕES DE REGRAS DE NEGÓCIO ---
        
        if menor >= maior:
            print("\nErro: O menor número deve ser estritamente menor que o maior número.")
            print("Vamos recomeçar a configuração do sorteio.\n")
            continue # Aqui faz sentido voltar tudo, pois os limites estão inconsistentes

        if qte_num > (maior - menor + 1):
            print(f"\nErro: O intervalo entre {menor} e {maior} possui apenas {maior - menor + 1} números.")
            print(f"Não é possível sortear {qte_num} números únicos sem repetição.")
            print("Vamos recomeçar a configuração do sorteio.\n")
            continue


        # Retorna uma lista de tamanho e limites definidos pelo usuário
        sorteio = random.sample(range(menor, maior + 1), qte_num)

        sorteio.sort()

        print("\nOs números sorteados foram: ", sorteio)
        print("\n********************************************************************")
        input("\nPressione Enter para voltar ao menu...")
        limpar_tela()

        # Retorna para o menu principal
        return

def main():
    limpar_tela()
    print("********************************************************************")
    print("Sorteio de loteria automático")
    print("********************************************************************")

    while True:
        print("\nOpções:")
        print("1 - Megasena (6 números entre 1 e 60)")
        print("2 - Lotofácil (15 números entre 1 e 25)")
        print("3 - Quina (5 números entre 1 e 80)")
        print("4 - Personalizado (defina a quantidade de números e o intervalo)")
        print("0 - Sair")
        print("********************************************************************")

        opcao = input("\nEscolha uma opção (1, 2, 3 ou 4): ")


        # Verificação da escolha do usuáro
        if not opcao.isdigit() or int(opcao) not in [1, 2, 3, 4, 0]:
            print("\nOpção inválida. Por favor, escolha 1, 2, 3 ou 4.")

        elif opcao == '0':
            print("\nSaindo do programa... Obrigado e boa sorte!")
            break

        elif opcao in MODALIDADES:
            cfg = MODALIDADES[opcao]
            realizar_sorteio(cfg["nome"], cfg["limite"], cfg["qtd"])

        elif opcao == '4':
            person()

        else:
            print("\nOpção inválida. Por favor, escolha 1, 2, 3 ou 4.")

if __name__ == "__main__":
    main()