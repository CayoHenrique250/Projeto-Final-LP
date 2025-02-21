from data import admissions

def admit_patient():
    try:
        patient_id = int(input("Digite o ID do paciente a internar: "))
    except ValueError:
        print("ID inválido.")
        return
    room = input("Digite o número da sala/quarto: ").strip()
    date = input("Digite a data de admissão (dd/mm/aaaa): ").strip()
    admission_id = len(admissions) + 1
    admission = {"id": admission_id, "patient_id": patient_id, "room": room, "date": date, "status": "internado"}
    admissions.append(admission)
    print(f"Paciente internado com sucesso. ID da internação: {admission_id}.")

def update_admission():
    try:
        admission_id = int(input("Digite o ID da internação para atualizar: "))
    except ValueError:
        print("ID inválido.")
        return
    for adm in admissions:
        if adm["id"] == admission_id:
            new_room = input("Digite o novo número da sala (deixe em branco para manter): ").strip()
            new_date = input("Digite a nova data (deixe em branco para manter): ").strip()
            if new_room:
                adm["room"] = new_room
            if new_date:
                adm["date"] = new_date
            print("Internação atualizada com sucesso.")
            return
    print("Internação não encontrada.")

def discharge_patient():
    try:
        admission_id = int(input("Digite o ID da internação para alta: "))
    except ValueError:
        print("ID inválido.")
        return
    for adm in admissions:
        if adm["id"] == admission_id:
            adm["status"] = "alta"
            print("Paciente recebeu alta com sucesso.")
            return
    print("Internação não encontrada.")
