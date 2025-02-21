import sys
from cadastro import (add_patient, update_patient, consult_patient, delete_patient,
                      add_professional, update_professional, consult_professional, delete_professional)
from procedimentos import add_procedure, update_procedure, consult_procedure, delete_procedure
from cirurgias import schedule_surgery, update_surgery, cancel_surgery
from internacao import admit_patient, update_admission, discharge_patient
from caixa import record_transaction, consult_transactions
from convenios import add_insurance, update_insurance, consult_insurance, delete_insurance
from relatorios import gerar_relatorio_txt

def main_menu():
    while True:
        print("\n=== Sistema de Gestão Hospitalar ===")
        print("1. Cadastro de Pacientes")
        print("2. Cadastro de Profissionais")
        print("3. Cadastro de Procedimentos Médicos (CID)")
        print("4. Cirurgias")
        print("5. Internação")
        print("6. Caixa (Transações)")
        print("7. Cadastro de Convênios (ANS)")
        print("8. Gerar relatório TXT")
        print("0. Sair")
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            patient_menu()
        elif choice == "2":
            professional_menu()
        elif choice == "3":
            procedure_menu()
        elif choice == "4":
            surgery_menu()
        elif choice == "5":
            admission_menu()
        elif choice == "6":
            cash_menu()
        elif choice == "7":
            insurance_menu()
        elif choice == "8":
            reports_menu()
        elif choice == "0":
            print("Encerrando o sistema...")
            sys.exit()
        else:
            print("Opção inválida. Tente novamente.")

def patient_menu():
    while True:
        print("\n--- Cadastro de Pacientes ---")
        print("1. Incluir Paciente")
        print("2. Alterar Paciente")
        print("3. Consultar Paciente")
        print("4. Excluir Paciente")
        print("0. Voltar")
        opt = input("Escolha uma opção: ")
        if opt == "1":
            add_patient()
        elif opt == "2":
            update_patient()
        elif opt == "3":
            consult_patient()
        elif opt == "4":
            delete_patient()
        elif opt == "0":
            break
        else:
            print("Opção inválida.")

def professional_menu():
    while True:
        print("\n--- Cadastro de Profissionais ---")
        print("1. Incluir Profissional")
        print("2. Alterar Profissional")
        print("3. Consultar Profissional")
        print("4. Excluir Profissional")
        print("0. Voltar")
        opt = input("Escolha uma opção: ")
        if opt == "1":
            add_professional()
        elif opt == "2":
            update_professional()
        elif opt == "3":
            consult_professional()
        elif opt == "4":
            delete_professional()
        elif opt == "0":
            break
        else:
            print("Opção inválida.")

def procedure_menu():
    while True:
        print("\n--- Cadastro de Procedimentos Médicos (CID) ---")
        print("1. Incluir Procedimento")
        print("2. Alterar Procedimento")
        print("3. Consultar Procedimento")
        print("4. Excluir Procedimento")
        print("0. Voltar")
        opt = input("Escolha uma opção: ")
        if opt == "1":
            add_procedure()
        elif opt == "2":
            update_procedure()
        elif opt == "3":
            consult_procedure()
        elif opt == "4":
            delete_procedure()
        elif opt == "0":
            break
        else:
            print("Opção inválida.")

def surgery_menu():
    while True:
        print("\n--- Cirurgias ---")
        print("1. Agendar Cirurgia")
        print("2. Alterar Cirurgia")
        print("3. Cancelar Cirurgia")
        print("0. Voltar")
        opt = input("Escolha uma opção: ")
        if opt == "1":
            schedule_surgery()
        elif opt == "2":
            update_surgery()
        elif opt == "3":
            cancel_surgery()
        elif opt == "0":
            break
        else:
            print("Opção inválida.")

def admission_menu():
    while True:
        print("\n--- Internação ---")
        print("1. Internar Paciente")
        print("2. Alterar Internação")
        print("3. Dar Alta no Paciente")
        print("0. Voltar")
        opt = input("Escolha uma opção: ")
        if opt == "1":
            admit_patient()
        elif opt == "2":
            update_admission()
        elif opt == "3":
            discharge_patient()
        elif opt == "0":
            break
        else:
            print("Opção inválida.")

def cash_menu():
    while True:
        print("\n--- Caixa (Transações) ---")
        print("1. Registrar Transação")
        print("2. Consultar Transações")
        print("0. Voltar")
        opt = input("Escolha uma opção: ")
        if opt == "1":
            record_transaction()
        elif opt == "2":
            consult_transactions()
        elif opt == "0":
            break
        else:
            print("Opção inválida.")

def insurance_menu():
    while True:
        print("\n--- Cadastro de Convênios (ANS) ---")
        print("1. Incluir Convênio")
        print("2. Alterar Convênio")
        print("3. Consultar Convênio")
        print("4. Excluir Convênio")
        print("0. Voltar")
        opt = input("Escolha uma opção: ")
        if opt == "1":
            add_insurance()
        elif opt == "2":
            update_insurance()
        elif opt == "3":
            consult_insurance()
        elif opt == "4":
            delete_insurance()
        elif opt == "0":
            break
        else:
            print("Opção inválida.")

def reports_menu():
    gerar_relatorio_txt()
    print("Relatório gerado com sucesso!")

if __name__ == "__main__":
    main_menu()
