from data import surgeries

def schedule_surgery():
    try:
        patient_id = int(input("Digite o ID do paciente: "))
        professional_id = int(input("Digite o ID do profissional responsável: "))
    except ValueError:
        print("IDs devem ser números.")
        return
    date = input("Digite a data da cirurgia (dd/mm/aaaa): ").strip()
    surgery_type = input("Digite o tipo de cirurgia: ").strip()
    surgery_id = len(surgeries) + 1
    surgery = {"id": surgery_id, "patient_id": patient_id, "professional_id": professional_id, "date": date, "type": surgery_type}
    surgeries.append(surgery)
    print(f"Cirurgia agendada com sucesso com ID {surgery_id}.")

def update_surgery():
    try:
        sid = int(input("Digite o ID da cirurgia a atualizar: "))
    except ValueError:
        print("ID inválido.")
        return
    for s in surgeries:
        if s["id"] == sid:
            new_date = input("Digite a nova data (deixe em branco para manter): ").strip()
            new_type = input("Digite o novo tipo (deixe em branco para manter): ").strip()
            if new_date:
                s["date"] = new_date
            if new_type:
                s["type"] = new_type
            print("Cirurgia atualizada com sucesso.")
            return
    print("Cirurgia não encontrada.")

def cancel_surgery():
    try:
        sid = int(input("Digite o ID da cirurgia a cancelar: "))
    except ValueError:
        print("ID inválido.")
        return
    for i, s in enumerate(surgeries):
        if s["id"] == sid:
            surgeries.pop(i)
            print("Cirurgia cancelada com sucesso.")
            return
    print("Cirurgia não encontrada.")
