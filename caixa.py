from data import transactions

def record_transaction():
    trans_type = input("Digite o tipo de transação (particular/convenio): ").strip().lower()
    try:
        amount = float(input("Digite o valor da transação: "))
    except ValueError:
        print("Valor inválido.")
        return
    description = input("Digite a descrição da transação: ").strip()
    trans_id = len(transactions) + 1
    transaction = {"id": trans_id, "type": trans_type, "amount": amount, "description": description}
    transactions.append(transaction)
    print("Transação registrada com sucesso.")

def consult_transactions():
    if not transactions:
        print("Nenhuma transação registrada.")
        return
    for t in transactions:
        print(f"ID {t['id']}: Tipo: {t['type']}, Valor: {t['amount']}, Descrição: {t['description']}")
