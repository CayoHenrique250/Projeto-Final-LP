from data import insurances

def add_insurance():
    name = input("Digite o nome do convênio: ").strip()
    ans_number = input("Digite o número ANS: ").strip()
    if name == "" or ans_number == "":
        print("Campos obrigatórios não preenchidos.")
        return
    ins_id = len(insurances) + 1
    insurance = {"id": ins_id, "name": name, "ans_number": ans_number}
    insurances.append(insurance)
    print(f"Convênio {name} cadastrado com sucesso com ID {ins_id}.")

def update_insurance():
    try:
        ins_id = int(input("Digite o ID do convênio para atualizar: "))
    except ValueError:
        print("ID inválido.")
        return
    for ins in insurances:
        if ins["id"] == ins_id:
            new_name = input("Digite o novo nome (deixe em branco para manter): ").strip()
            new_ans = input("Digite o novo número ANS (deixe em branco para manter): ").strip()
            if new_name:
                ins["name"] = new_name
            if new_ans:
                ins["ans_number"] = new_ans
            print("Convênio atualizado com sucesso.")
            return
    print("Convênio não encontrado.")

def consult_insurance():
    try:
        ins_id = int(input("Digite o ID do convênio para consulta: "))
    except ValueError:
        print("ID inválido.")
        return
    for ins in insurances:
        if ins["id"] == ins_id:
            print(f"Convênio ID {ins['id']}: Nome: {ins['name']}, ANS: {ins['ans_number']}")
            return
    print("Convênio não encontrado.")

def delete_insurance():
    try:
        ins_id = int(input("Digite o ID do convênio a excluir: "))
    except ValueError:
        print("ID inválido.")
        return
    for i, ins in enumerate(insurances):
        if ins["id"] == ins_id:
            insurances.pop(i)
            print("Convênio excluído com sucesso.")
            return
    print("Convênio não encontrado.")
