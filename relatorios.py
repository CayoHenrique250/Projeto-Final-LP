from datetime import datetime
from data import patients, professionals, procedures, archived_patients, archived_professionals

def gerar_relatorio_txt():
    report = "=== Relatório do Sistema Hospitalar ===\n\n"
    report += f"Total de Pacientes: {len(patients)}\n"
    report += f"Total de Profissionais: {len(professionals)}\n\n"
    report += f"Total de Pacientes Arquivados: {len(archived_patients)}\n"
    report += f"Total de Profissionais Arquivados: {len(archived_professionals)}\n\n"
    
    report += "Procedimentos (CID):\n"
    for proc in procedures:
        report += f"  CID {proc['cid']}: {proc['description']}\n"
    
    now = datetime.now()
    timestamp_str = now.strftime("%Y%m%d_%H%M%S")
    file_name = f"relatorio_{timestamp_str}.txt"
    
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"Relatório gerado: {file_name}")
    return file_name
