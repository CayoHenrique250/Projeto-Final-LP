pacientes = []
profissionais = []
consultas = []
prontuarios = {}
estoque = {}
triagens = []

def cadastrar_paciente():
    pid = len(pacientes) + 1
    nome = input("Digite o nome do paciente: ")
    idade = input("Digite a idade do paciente: ")
    paciente = {"id": pid, "nome": nome, "idade": idade}
    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")

def cadastrar_profissional():
    pid = len(profissionais) + 1
    nome = input("Digite o nome do profissional de saúde: ")
    especialidade = input("Digite a especialidade: ")
    profissional = {"id": pid, "nome": nome, "especialidade": especialidade}
    profissionais.append(profissional)
    print("Profissional cadastrado com sucesso!")

def marcar_consulta():
    if not pacientes or not profissionais:
        print("Cadastre pelo menos um paciente e um profissional primeiro!")
        return
    print("\n--- Lista de Pacientes ---")
    for p in pacientes:
        print(f"ID: {p['id']} - Nome: {p['nome']}")
    paciente_id = int(input("Digite o ID do paciente: "))
    
    print("\n--- Lista de Profissionais ---")
    for p in profissionais:
        print(f"ID: {p['id']} - Nome: {p['nome']} - Especialidade: {p['especialidade']}")
    prof_id = int(input("Digite o ID do profissional: "))
    
    data = input("Digite a data da consulta (dd/mm/aaaa): ")
    hora = input("Digite o horário da consulta (hh:mm): ")
    
    consulta = {"paciente_id": paciente_id, "profissional_id": prof_id, "data": data, "hora": hora}
    consultas.append(consulta)
    print("Consulta marcada com sucesso!")
    
    with open("log_consultas.txt", "a") as f:
        f.write(f"Consulta marcada: Paciente {paciente_id}, Profissional {prof_id}, Data {data}, Hora {hora}\n")

def cancelar_consulta():
    if not consultas:
        print("Não há consultas marcadas.")
        return
    print("\n--- Consultas Agendadas ---")
    for idx, c in enumerate(consultas, 1):
        print(f"{idx}. Paciente ID {c['paciente_id']} com Profissional ID {c['profissional_id']} em {c['data']} às {c['hora']}")
    opc = int(input("Digite o número da consulta que deseja cancelar: "))
    
    if 1 <= opc <= len(consultas):
        consulta_cancelada = consultas.pop(opc - 1)
        print("Consulta cancelada com sucesso!")
        with open("log_consultas.txt", "a") as f:
            f.write(f"Consulta cancelada: {consulta_cancelada}\n")
    else:
        print("Opção inválida.")

def atualizar_prontuario():
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return
    paciente_id = int(input("Digite o ID do paciente para atualizar o prontuário: "))
    nota = input("Digite a nova anotação no prontuário: ")
    if paciente_id not in prontuarios:
        prontuarios[paciente_id] = []
    prontuarios[paciente_id].append(nota)
    print("Prontuário atualizado com sucesso!")

def exibir_prontuario():
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return
    paciente_id = int(input("Digite o ID do paciente para exibir o prontuário: "))
    if paciente_id in prontuarios:
        print(f"\n--- Prontuário do Paciente {paciente_id} ---")
        for entry in prontuarios[paciente_id]:
            print(f"- {entry}")
    else:
        print("Prontuário não encontrado para esse paciente.")

def gerenciar_estoque():
    print("\n--- Gerenciar Estoque de Medicamentos ---")
    print("1. Adicionar medicamento")
    print("2. Remover medicamento")
    print("3. Visualizar estoque")
    opc = int(input("Escolha uma opção: "))
    
    if opc == 1:
        med = input("Digite o nome do medicamento: ")
        qtd = int(input("Digite a quantidade a adicionar: "))
        if med in estoque:
            estoque[med] += qtd
        else:
            estoque[med] = qtd
        print("Medicamento adicionado ao estoque.")
    elif opc == 2:
        med = input("Digite o nome do medicamento: ")
        if med in estoque:
            qtd = int(input("Digite a quantidade a remover: "))
            if estoque[med] >= qtd:
                estoque[med] -= qtd
                print("Medicamento removido do estoque.")
            else:
                print("Quantidade insuficiente em estoque.")
        else:
            print("Medicamento não encontrado.")
    elif opc == 3:
        print("\n--- Estoque de Medicamentos ---")
        for med, qtd in estoque.items():
            print(f"{med}: {qtd}")
    else:
        print("Opção inválida.")

def triagem_emergencial():
    print("\n--- Triagem Emergencial ---")
    paciente_id = int(input("Digite o ID do paciente: "))
    print("Classificação de gravidade:")
    print("1. Baixa")
    print("2. Média")
    print("3. Alta")
    gravidade = int(input("Digite a opção de gravidade (1-3): "))
    
    if gravidade == 1:
        prioridade = "Baixa"
    elif gravidade == 2:
        prioridade = "Média"
    elif gravidade == 3:
        prioridade = "Alta"
    else:
        prioridade = "Desconhecida"
    triagem = {"paciente_id": paciente_id, "gravidade": prioridade}
    triagens.append(triagem)
    print(f"Triagem registrada: Paciente {paciente_id} com gravidade {prioridade}.")

def gerar_relatorios():
    print("\n==== Relatórios Administrativos ====")
    print(f"\nTotal de Pacientes cadastrados: {len(pacientes)}")
    print("\nConsultas Agendadas:")
    for c in consultas:
        print(c)
    print("\nEstoque de Medicamentos:")
    for med, qtd in estoque.items():
        print(f"{med}: {qtd}")
    print("\nTriagens Emergenciais:")
    for t in triagens:
        print(t)

def main():
    while True:
        print("\n======== Menu Principal ========")
        print("1. Cadastrar Paciente")
        print("2. Cadastrar Profissional")
        print("3. Marcar Consulta")
        print("4. Cancelar Consulta")
        print("5. Atualizar Prontuário")
        print("6. Exibir Prontuário")
        print("7. Gerenciar Estoque de Medicamentos")
        print("8. Triagem Emergencial")
        print("9. Gerar Relatórios")
        print("0. Sair")
        opc = input("Escolha uma opção: ")
        
        if opc == "1":
            cadastrar_paciente()
        elif opc == "2":
            cadastrar_profissional()
        elif opc == "3":
            marcar_consulta()
        elif opc == "4":
            cancelar_consulta()
        elif opc == "5":
            atualizar_prontuario()
        elif opc == "6":
            exibir_prontuario()
        elif opc == "7":
            gerenciar_estoque()
        elif opc == "8":
            triagem_emergencial()
        elif opc == "9":
            gerar_relatorios()
        elif opc == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()
