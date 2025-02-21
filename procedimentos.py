from data import procedures

def add_procedure():
    cid = input("Digite o código CID: ").strip()
    description = input("Digite a descrição do procedimento: ").strip()
    if cid == "" or description == "":
        print("Campos obrigatórios não preenchidos.")
        return
    procedure = {"cid": cid, "description": description}
    procedures.append(procedure)
    print("Procedimento adicionado com sucesso.")

def update_procedure():
    cid = input("Digite o código CID do procedimento a atualizar: ").strip()
    for proc in procedures:
        if proc["cid"] == cid:
            new_description = input("Digite a nova descrição: ").strip()
            if new_description:
                proc["description"] = new_description
            print("Procedimento atualizado com sucesso.")
            return
    print("Procedimento não encontrado.")

def consult_procedure():
    cid = input("Digite o código CID para consulta: ").strip()
    for proc in procedures:
        if proc["cid"] == cid:
            print(f"Procedimento: CID {proc['cid']} - {proc['description']}")
            return
    print("Procedimento não encontrado.")

def delete_procedure():
    cid = input("Digite o código CID do procedimento a excluir: ").strip()
    for i, proc in enumerate(procedures):
        if proc["cid"] == cid:
            procedures.pop(i)
            print("Procedimento excluído com sucesso.")
            return
    print("Procedimento não encontrado.")
