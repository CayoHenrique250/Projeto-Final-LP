from data import procedures, professionals

def report_procedures():
    print("Relatório de Procedimentos Médicos (CID):")
    for proc in procedures:
        print(f"CID {proc['cid']}: {proc['description']}")

def report_professionals_by_specialty():
    specialty_dict = {}
    for prof in professionals:
        spec = prof.get("specialty", "Desconhecido")
        specialty_dict.setdefault(spec, []).append(prof)
    print("Relatório de Médicos por Especialidade:")
    for spec, profs in specialty_dict.items():
        print(f"\nEspecialidade: {spec}")
        for p in profs:
            print(f" - ID {p['id']}: {p['name']}")

def report_employee_presence():
    print("Relatório de Ponto de Presença dos Funcionários:")
    for prof in professionals:
        print(f"Profissional: {prof['name']} (ID {prof['id']}) - Presença registrada")
