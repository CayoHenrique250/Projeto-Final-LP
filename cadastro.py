from data import patients, archived_patients, professionals, archived_professionals

def add_patient():
    name = input("Digite o nome do paciente: ").strip()
    age = input("Digite a idade do paciente: ").strip()
    if name == "" or age == "":
        print("Campos obrigatórios não preenchidos.")
        return
    patient_id = len(patients) + 1
    patient = {"id": patient_id, "name": name, "age": age}
    patients.append(patient)
    print(f"Paciente {name} cadastrado com sucesso com ID {patient_id}.")

def update_patient():
    try:
        pid = int(input("Digite o ID do paciente para atualizar: "))
    except ValueError:
        print("ID inválido.")
        return
    for p in patients:
        if p["id"] == pid:
            new_name = input("Digite o novo nome (ou deixe em branco para manter): ").strip()
            new_age = input("Digite a nova idade (ou deixe em branco para manter): ").strip()
            if new_name:
                p["name"] = new_name
            if new_age:
                p["age"] = new_age
            print("Paciente atualizado com sucesso.")
            return
    print("Paciente não encontrado.")

def consult_patient():
    try:
        pid = int(input("Digite o ID do paciente para consulta: "))
    except ValueError:
        print("ID inválido.")
        return
    for p in patients:
        if p["id"] == pid:
            print(f"Paciente ID {p['id']}: Nome: {p['name']}, Idade: {p['age']}")
            return
    print("Paciente não encontrado.")

def delete_patient():
    try:
        pid = int(input("Digite o ID do paciente a excluir: "))
    except ValueError:
        print("ID inválido.")
        return
    for i, p in enumerate(patients):
        if p["id"] == pid:
            removed = patients.pop(i)
            archived_patients.append(removed)
            print(f"Paciente {removed['name']} removido e arquivado.")
            return
    print("Paciente não encontrado.")

def add_professional():
    name = input("Digite o nome do profissional: ").strip()
    specialty = input("Digite a especialidade: ").strip()
    if name == "" or specialty == "":
        print("Campos obrigatórios não preenchidos.")
        return
    prof_id = len(professionals) + 1
    professional = {"id": prof_id, "name": name, "specialty": specialty}
    professionals.append(professional)
    print(f"Profissional {name} cadastrado com sucesso com ID {prof_id}.")

def update_professional():
    try:
        pid = int(input("Digite o ID do profissional para atualizar: "))
    except ValueError:
        print("ID inválido.")
        return
    for p in professionals:
        if p["id"] == pid:
            new_name = input("Digite o novo nome (ou deixe em branco para manter): ").strip()
            new_specialty = input("Digite a nova especialidade (ou deixe em branco para manter): ").strip()
            if new_name:
                p["name"] = new_name
            if new_specialty:
                p["specialty"] = new_specialty
            print("Profissional atualizado com sucesso.")
            return
    print("Profissional não encontrado.")

def consult_professional():
    try:
        pid = int(input("Digite o ID do profissional para consulta: "))
    except ValueError:
        print("ID inválido.")
        return
    for p in professionals:
        if p["id"] == pid:
            print(f"Profissional ID {p['id']}: Nome: {p['name']}, Especialidade: {p['specialty']}")
            return
    print("Profissional não encontrado.")

def delete_professional():
    try:
        pid = int(input("Digite o ID do profissional a excluir: "))
    except ValueError:
        print("ID inválido.")
        return
    for i, p in enumerate(professionals):
        if p["id"] == pid:
            removed = professionals.pop(i)
            archived_professionals.append(removed)
            print(f"Profissional {removed['name']} removido e arquivado.")
            return
    print("Profissional não encontrado.")