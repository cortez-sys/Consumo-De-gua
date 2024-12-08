import os
# Sistema de Monitoramento de Consumo de Água

# Dados das residências e consumo
residencias = []  # Lista para armazenar as informações das casas
consumo_mensal = []  # Matriz para armazenar o consumo mensal de cada residência


# Função para cadastrar uma nova residência
def cadastrar_casa():
    print("\n--- Cadastro de Casa ---")
    id_casa = input("Digite o ID da residência: ")
    nome = input("Digite o nome do morador principal: ")
    moradores = int(input("Digite a quantidade de moradores: "))
    residencias.append({"id": id_casa, "nome": nome, "moradores": moradores})
    consumo_mensal.append([0] * 12)  # Inicializa consumo com 0 para 12 meses
    print("Residência cadastrada com sucesso!\n")


# Função para registrar o consumo mensal
def registrar_consumo():
    print("\n--- Registrar Consumo Mensal ---")
    id_casa = input("Digite o ID da residência: ")
    mes = int(input("Digite o número do mês (1-12): ")) - 1
    consumo = float(input("Digite o consumo de água (m³): "))

    for i, casa in enumerate(residencias):
        if casa["id"] == id_casa:
            consumo_mensal[i][mes] = consumo
            print("Consumo registrado com sucesso!\n")
            return
    print("Residência não encontrada!\n")


# Função para calcular o consumo médio da comunidade
def calcular_media_comunidade():
    total_consumo = 0
    total_residencias = 0
    for consumo in consumo_mensal:
        total_consumo += sum(consumo)
        total_residencias += 1
    return total_consumo / total_residencias if total_residencias > 0 else 0


# Função para exibir residências acima da média segura
def exibir_acima_media():
    print("\n--- Casas Acima da Média ---")
    media_segura = 15
    media_comunidade = calcular_media_comunidade()
    for i, casa in enumerate(residencias):
        consumo_total = sum(consumo_mensal[i])
        consumo_medio = consumo_total / 12
        if consumo_medio > media_segura:
            print(f"ID: {casa['id']}, Morador: {casa['nome']}, Consumo Médio: {consumo_medio:.2f} m³")
    print()


# Função para exibir residências abaixo da média segura
def exibir_abaixo_media():
    print("\n--- Casas Abaixo da Média ---")
    media_segura = 15
    media_comunidade = calcular_media_comunidade()
    for i, casa in enumerate(residencias):
        consumo_total = sum(consumo_mensal[i])
        consumo_medio = consumo_total / 12
        if consumo_medio <= media_segura:
            print(f"ID: {casa['id']}, Morador: {casa['nome']}, Consumo Médio: {consumo_medio:.2f} m³")
    print()

# Função para alertar consumo excessivo
def alertar_consumo_excessivo():
    print("\n--- Alerta de Consumo Excessivo ---")
    media_segura = 15
    for i, casa in enumerate(residencias):
        consumo_total = sum(consumo_mensal[i])
        consumo_medio = consumo_total / 12
        if consumo_medio > media_segura:
            print(f"ATENÇÃO! ID: {casa['id']}, Morador: {casa['nome']} está com consumo médio de {consumo_medio:.2f} m³, acima da média segura de {media_segura} m³.\n")



# Menu principal
def menu():
    while True:
        print("\n--- Sistema de Consumo de Água ---")
        print("1 – Cadastrar casa")
        print("2 – Registrar consumo mensal")
        print("3 – Exibir casas acima da média")
        print("4 – Exibir casas abaixo da média")
        print("5 – Consulta Consumos Excessivos")
        print("6 – Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            cadastrar_casa()
        elif opcao == "2":
            registrar_consumo()
        elif opcao == "3":
            exibir_acima_media()
        elif opcao == "4":
            exibir_abaixo_media()
        elif opcao == "5":
            alertar_consumo_excessivo()
        elif opcao == "6":
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Executar o programa
menu()
