import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from data import (patients, archived_patients, professionals, archived_professionals, 
                  procedures, surgeries, admissions, transactions, insurances, atendimentos)
from tkinter import messagebox
from relatorios import gerar_relatorio_txt

# ===============================
# Funções de Cadastro de Pacientes
# ===============================
def cadastrar_paciente_gui():
    window = tk.Toplevel(root)
    window.title("Cadastrar Paciente")
    window.geometry("400x300")

    ttk.Label(window, text="Nome do Paciente:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=0, column=0, padx=10, pady=10)
    entry_nome = ttk.Entry(window)
    entry_nome.grid(row=0, column=1, padx=10, pady=10)
    
    ttk.Label(window, text="Idade:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=1, column=0, padx=10, pady=10)
    entry_idade = ttk.Entry(window)
    entry_idade.grid(row=1, column=1, padx=10, pady=10)
    
    def cadastrar():
        nome = entry_nome.get().strip()
        idade = entry_idade.get().strip()
        if nome == "" or idade == "":
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
        pid = len(patients) + 1
        patient = {"id": pid, "name": nome, "age": idade}
        patients.append(patient)
        messagebox.showinfo("Sucesso", f"Paciente {nome} cadastrado com sucesso com ID {pid}.")
        window.destroy()
    
    ttk.Button(window, text="Cadastrar", command=cadastrar).grid(row=2, column=0, columnspan=2, pady=10)

def atualizar_paciente_gui():
    window = tk.Toplevel(root)
    window.title("Atualizar Paciente")
    window.geometry("600x200")
    
    ttk.Label(window, text="ID do Paciente:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=0, column=0, padx=5, pady=5)
    entry_id = ttk.Entry(window)
    entry_id.grid(row=0, column=1, padx=5, pady=5)
    
    ttk.Label(window, text="Novo Nome (deixe em branco para manter):", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=1, column=0, padx=5, pady=5)
    entry_nome = ttk.Entry(window)
    entry_nome.grid(row=1, column=1, padx=5, pady=5)
    
    ttk.Label(window, text="Nova Idade (deixe em branco para manter):", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=2, column=0, padx=5, pady=5)
    entry_idade = ttk.Entry(window)
    entry_idade.grid(row=2, column=1, padx=5, pady=5)
    
    def atualizar():
        try:
            pid = int(entry_id.get())
        except ValueError:
            messagebox.showerror("Erro", "ID inválido!")
            return
        for p in patients:
            if p["id"] == pid:
                novo_nome = entry_nome.get().strip()
                nova_idade = entry_idade.get().strip()
                if novo_nome:
                    p["name"] = novo_nome
                if nova_idade:
                    p["age"] = nova_idade
                messagebox.showinfo("Sucesso", "Paciente atualizado com sucesso!")
                window.destroy()
                return
        messagebox.showerror("Erro", "Paciente não encontrado!")
    
    ttk.Button(window, text="Atualizar", command=atualizar).grid(row=3, column=0, columnspan=2, pady=10)

def consultar_paciente_gui():
    window = tk.Toplevel(root)
    window.title("Consultar Paciente")
    window.geometry("500x300")
    
    ttk.Label(window, text="Digite o ID do Paciente:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=0, column=0, padx=5, pady=5)
    entry_id = ttk.Entry(window)
    entry_id.grid(row=0, column=1, padx=5, pady=5)
    
    text_area = tk.Text(window, width=50, height=5)
    text_area.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
    def consultar():
        try:
            pid = int(entry_id.get())
        except ValueError:
            messagebox.showerror("Erro", "ID inválido!")
            return
        for p in patients:
            if p["id"] == pid:
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, f"ID: {p['id']}\nNome: {p['name']}\nIdade: {p['age']}")
                return
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, "Paciente não encontrado!")
    
    ttk.Button(window, text="Consultar", command=consultar).grid(row=1, column=0, columnspan=2, pady=5)

def remover_paciente_gui():
    window = tk.Toplevel(root)
    window.title("Remover Paciente")
    window.geometry("400x400")
    
    ttk.Label(window, text="Selecione o Paciente a Remover:", font=("Arial", 12, "bold"), foreground="#2c9192").pack(padx=5, pady=5)
    listbox = tk.Listbox(window, width=50)
    listbox.pack(padx=5, pady=5)
    for p in patients:
        listbox.insert(tk.END, f"ID {p['id']}: {p['name']} - {p['age']} anos")
    
    def remover():
        selection = listbox.curselection()
        if not selection:
            messagebox.showerror("Erro", "Selecione um paciente!")
            return
        index = selection[0]
        removed = patients.pop(index)
        archived_patients.append(removed)
        messagebox.showinfo("Sucesso", f"Paciente {removed['name']} removido e arquivado.")
        window.destroy()
    
    ttk.Button(window, text="Remover", command=remover).pack(pady=10)

# ===============================
# Funções de Cadastro de Profissionais
# ===============================
def cadastrar_profissional_gui():
    window = tk.Toplevel(root)
    window.title("Cadastrar Profissional")
    window.geometry("400x200")
    
    ttk.Label(window, text="Nome do Profissional:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=0, column=0, padx=5, pady=5)
    entry_nome = ttk.Entry(window)
    entry_nome.grid(row=0, column=1, padx=5, pady=5)
    
    ttk.Label(window, text="Especialidade:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=1, column=0, padx=5, pady=5)
    entry_espec = ttk.Entry(window)
    entry_espec.grid(row=1, column=1, padx=5, pady=5)
    
    def cadastrar():
        nome = entry_nome.get().strip()
        especialidade = entry_espec.get().strip()
        if nome == "" or especialidade == "":
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
        pid = len(professionals) + 1
        prof = {"id": pid, "name": nome, "specialty": especialidade}
        professionals.append(prof)
        messagebox.showinfo("Sucesso", f"Profissional {nome} cadastrado com sucesso com ID {pid}.")
        window.destroy()
    
    ttk.Button(window, text="Cadastrar", command=cadastrar).grid(row=2, column=0, columnspan=2, pady=10)

def atualizar_profissional_gui():
    window = tk.Toplevel(root)
    window.title("Atualizar Profissional")
    window.geometry("400x200")
    
    ttk.Label(window, text="ID do Profissional:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=0, column=0, padx=5, pady=5)
    entry_id = ttk.Entry(window)
    entry_id.grid(row=0, column=1, padx=5, pady=5)
    
    ttk.Label(window, text="Novo Nome:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=1, column=0, padx=5, pady=5)
    entry_nome = ttk.Entry(window)
    entry_nome.grid(row=1, column=1, padx=5, pady=5)
    
    ttk.Label(window, text="Nova Especialidade:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=2, column=0, padx=5, pady=5)
    entry_espec = ttk.Entry(window)
    entry_espec.grid(row=2, column=1, padx=5, pady=5)
    
    def atualizar():
        try:
            pid = int(entry_id.get())
        except ValueError:
            messagebox.showerror("Erro", "ID inválido!")
            return
        for p in professionals:
            if p["id"] == pid:
                novo_nome = entry_nome.get().strip()
                nova_espec = entry_espec.get().strip()
                if novo_nome:
                    p["name"] = novo_nome
                if nova_espec:
                    p["specialty"] = nova_espec
                messagebox.showinfo("Sucesso", "Profissional atualizado!")
                window.destroy()
                return
        messagebox.showerror("Erro", "Profissional não encontrado!")
    
    ttk.Button(window, text="Atualizar", command=atualizar).grid(row=3, column=0, columnspan=2, pady=10)

def consultar_profissional_gui():
    window = tk.Toplevel(root)
    window.title("Consultar Profissional")
    window.geometry("500x200")
    
    ttk.Label(window, text="Digite o ID do Profissional:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=0, column=0, padx=5, pady=5)
    entry_id = ttk.Entry(window)
    entry_id.grid(row=0, column=1, padx=5, pady=5)
    
    text_area = tk.Text(window, width=50, height=5)
    text_area.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
    def consultar():
        try:
            pid = int(entry_id.get())
        except ValueError:
            messagebox.showerror("Erro", "ID inválido!")
            return
        for p in professionals:
            if p["id"] == pid:
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, f"ID: {p['id']}\nNome: {p['name']}\nEspecialidade: {p['specialty']}")
                return
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, "Profissional não encontrado!")
    
    ttk.Button(window, text="Consultar", command=consultar).grid(row=1, column=0, columnspan=2, pady=5)

def remover_profissional_gui():
    window = tk.Toplevel(root)
    window.title("Remover Profissional")
    window.geometry("400x300")
    
    ttk.Label(window, text="Selecione o Profissional a Remover:", font=("Arial", 12, "bold"), foreground="#2c9192").pack(padx=5, pady=5)
    listbox = tk.Listbox(window, width=50)
    listbox.pack(padx=5, pady=5)
    for p in professionals:
        listbox.insert(tk.END, f"ID {p['id']}: {p['name']} - {p['specialty']}")
    
    def remover():
        selection = listbox.curselection()
        if not selection:
            messagebox.showerror("Erro", "Selecione um profissional!")
            return
        index = selection[0]
        removed = professionals.pop(index)
        archived_professionals.append(removed)
        messagebox.showinfo("Sucesso", f"Profissional {removed['name']} removido e arquivado.")
        window.destroy()
    
    ttk.Button(window, text="Remover", command=remover).pack(pady=10)

# ===============================
# Funções de Procedimentos (CID)
# ===============================
def cadastrar_procedimento_gui():
    window = tk.Toplevel(root)
    window.title("Cadastrar Procedimento")
    window.geometry("300x150")
    
    ttk.Label(window, text="Código CID:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=0, column=0, padx=5, pady=5)
    entry_cid = ttk.Entry(window)
    entry_cid.grid(row=0, column=1, padx=5, pady=5)
    
    ttk.Label(window, text="Descrição:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=1, column=0, padx=5, pady=5)
    entry_desc = ttk.Entry(window)
    entry_desc.grid(row=1, column=1, padx=5, pady=5)
    
    def cadastrar():
        cid = entry_cid.get().strip()
        desc = entry_desc.get().strip()
        if cid == "" or desc == "":
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
        procedures.append({"cid": cid, "description": desc})
        messagebox.showinfo("Sucesso", "Procedimento cadastrado com sucesso!")
        window.destroy()
    
    ttk.Button(window, text="Cadastrar", command=cadastrar).grid(row=2, column=0, columnspan=2, pady=10)

def atualizar_procedimento_gui():
    window = tk.Toplevel(root)
    window.title("Atualizar Procedimento")
    window.geometry("350x150")
    
    ttk.Label(window, text="Digite o Código CID:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=0, column=0, padx=5, pady=5)
    entry_cid = ttk.Entry(window)
    entry_cid.grid(row=0, column=1, padx=5, pady=5)
    
    ttk.Label(window, text="Nova Descrição:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=1, column=0, padx=5, pady=5)
    entry_desc = ttk.Entry(window)
    entry_desc.grid(row=1, column=1, padx=5, pady=5)
    
    def atualizar():
        cid = entry_cid.get().strip()
        new_desc = entry_desc.get().strip()
        for proc in procedures:
            if proc["cid"] == cid:
                proc["description"] = new_desc
                messagebox.showinfo("Sucesso", "Procedimento atualizado!")
                window.destroy()
                return
        messagebox.showerror("Erro", "Procedimento não encontrado!")
    
    ttk.Button(window, text="Atualizar", command=atualizar).grid(row=2, column=0, columnspan=2, pady=10)

def consultar_procedimento_gui():
    window = tk.Toplevel(root)
    window.title("Consultar Procedimento")
    window.geometry("500x200")
    
    ttk.Label(window, text="Digite o Código CID:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=0, column=0, padx=5, pady=5)
    entry_cid = ttk.Entry(window)
    entry_cid.grid(row=0, column=1, padx=5, pady=5)
    
    text_area = tk.Text(window, width=50, height=5)
    text_area.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
    def consultar():
        cid = entry_cid.get().strip()
        for proc in procedures:
            if proc["cid"] == cid:
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, f"CID: {proc['cid']}\nDescrição: {proc['description']}")
                return
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, "Procedimento não encontrado!")
    
    ttk.Button(window, text="Consultar", command=consultar).grid(row=1, column=0, columnspan=2, pady=5)

def remover_procedimento_gui():
    window = tk.Toplevel(root)
    window.title("Remover Procedimento")
    window.geometry("400x150")
    
    ttk.Label(window, text="Digite o Código CID do procedimento a remover:", font=("Arial", 12, "bold"), foreground="#2c9192").pack(padx=5, pady=5)
    entry_cid = ttk.Entry(window)
    entry_cid.pack(padx=5, pady=5)
    
    def remover():
        cid = entry_cid.get().strip()
        for i, proc in enumerate(procedures):
            if proc["cid"] == cid:
                procedures.pop(i)
                messagebox.showinfo("Sucesso", "Procedimento removido!")
                window.destroy()
                return
        messagebox.showerror("Erro", "Procedimento não encontrado!")
    
    ttk.Button(window, text="Remover", command=remover).pack(pady=10)

# ===============================
# Funções de Cirurgias
# ===============================
def agendar_cirurgia_gui():
    window = tk.Toplevel(root)
    window.title("Agendar Cirurgia")
    window.geometry("400x250")
    
    ttk.Label(window, text="ID do Paciente:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=0, column=0, padx=5, pady=5)
    entry_pid = ttk.Entry(window)
    entry_pid.grid(row=0, column=1, padx=5, pady=5)
    
    ttk.Label(window, text="ID do Profissional:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=1, column=0, padx=5, pady=5)
    entry_prof = ttk.Entry(window)
    entry_prof.grid(row=1, column=1, padx=5, pady=5)
    
    ttk.Label(window, text="Data (dd/mm/aaaa):", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=2, column=0, padx=5, pady=5)
    entry_data = ttk.Entry(window)
    entry_data.grid(row=2, column=1, padx=5, pady=5)
    
    ttk.Label(window, text="Tipo de Cirurgia:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=3, column=0, padx=5, pady=5)
    entry_tipo = ttk.Entry(window)
    entry_tipo.grid(row=3, column=1, padx=5, pady=5)
    
    def agendar():
        try:
            pid = int(entry_pid.get())
            prof = int(entry_prof.get())
        except ValueError:
            messagebox.showerror("Erro", "IDs devem ser números!")
            return
        data = entry_data.get().strip()
        tipo = entry_tipo.get().strip()
        sid = len(surgeries) + 1
        surgery = {"id": sid, "patient_id": pid, "professional_id": prof, "date": data, "type": tipo}
        surgeries.append(surgery)
        messagebox.showinfo("Sucesso", f"Cirurgia agendada com ID {sid}.")
        window.destroy()
    
    ttk.Button(window, text="Agendar", command=agendar).grid(row=4, column=0, columnspan=2, pady=10)

def atualizar_cirurgia_gui():
    window = tk.Toplevel(root)
    window.title("Atualizar Cirurgia")
    window.geometry("500x200")
    
    ttk.Label(window, text="ID da Cirurgia:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=0, column=0, padx=5, pady=5)
    entry_id = ttk.Entry(window)
    entry_id.grid(row=0, column=1, padx=5, pady=5)
    
    ttk.Label(window, text="Nova Data (deixe em branco para manter):", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=1, column=0, padx=5, pady=5)
    entry_data = ttk.Entry(window)
    entry_data.grid(row=1, column=1, padx=5, pady=5)
    
    ttk.Label(window, text="Novo Tipo (deixe em branco para manter):", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=2, column=0, padx=5, pady=5)
    entry_tipo = ttk.Entry(window)
    entry_tipo.grid(row=2, column=1, padx=5, pady=5)
    
    def atualizar():
        try:
            sid = int(entry_id.get())
        except ValueError:
            messagebox.showerror("Erro", "ID inválido!")
            return
        for s in surgeries:
            if s["id"] == sid:
                nova_data = entry_data.get().strip()
                novo_tipo = entry_tipo.get().strip()
                if nova_data:
                    s["date"] = nova_data
                if novo_tipo:
                    s["type"] = novo_tipo
                messagebox.showinfo("Sucesso", "Cirurgia atualizada!")
                window.destroy()
                return
        messagebox.showerror("Erro", "Cirurgia não encontrada!")
    
    ttk.Button(window, text="Atualizar", command=atualizar).grid(row=3, column=0, columnspan=2, pady=10)

def cancelar_cirurgia_gui():
    window = tk.Toplevel(root)
    window.title("Cancelar Cirurgia")
    window.geometry("300x150")
    
    ttk.Label(window, text="Digite o ID da Cirurgia:", font=("Arial", 12, "bold"), foreground="#2c9192").pack(padx=5, pady=5)
    entry_id = ttk.Entry(window)
    entry_id.pack(padx=5, pady=5)
    
    def cancelar():
        try:
            sid = int(entry_id.get())
        except ValueError:
            messagebox.showerror("Erro", "ID inválido!")
            return
        for i, s in enumerate(surgeries):
            if s["id"] == sid:
                surgeries.pop(i)
                messagebox.showinfo("Sucesso", "Cirurgia cancelada!")
                window.destroy()
                return
        messagebox.showerror("Erro", "Cirurgia não encontrada!")
    
    ttk.Button(window, text="Cancelar", command=cancelar).pack(pady=10)

# ===============================
# Funções de Internação
# ===============================
def internar_paciente_gui():
    window = tk.Toplevel(root)
    window.title("Internar Paciente")
    window.geometry("500x200")
    
    ttk.Label(window, text="ID do Paciente:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=0, column=0, padx=5, pady=5)
    entry_pid = ttk.Entry(window)
    entry_pid.grid(row=0, column=1, padx=5, pady=5)
    
    ttk.Label(window, text="Sala/Quarto:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=1, column=0, padx=5, pady=5)
    entry_room = ttk.Entry(window)
    entry_room.grid(row=1, column=1, padx=5, pady=5)
    
    ttk.Label(window, text="Data de Admissão (dd/mm/aaaa):", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=2, column=0, padx=5, pady=5)
    entry_date = ttk.Entry(window)
    entry_date.grid(row=2, column=1, padx=5, pady=5)
    
    def internar():
        try:
            pid = int(entry_pid.get())
        except ValueError:
            messagebox.showerror("Erro", "ID inválido!")
            return
        room = entry_room.get().strip()
        date = entry_date.get().strip()
        aid = len(admissions) + 1
        admission = {"id": aid, "patient_id": pid, "room": room, "date": date, "status": "internado"}
        admissions.append(admission)
        messagebox.showinfo("Sucesso", f"Paciente internado com ID de internação {aid}.")
        window.destroy()
    
    ttk.Button(window, text="Internar", command=internar).grid(row=3, column=0, columnspan=2, pady=10)

def atualizar_internacao_gui():
    window = tk.Toplevel(root)
    window.title("Atualizar Internação")
    window.geometry("500x200")
    
    ttk.Label(window, text="ID da Internação:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=0, column=0, padx=5, pady=5)
    entry_aid = ttk.Entry(window)
    entry_aid.grid(row=0, column=1, padx=5, pady=5)
    
    ttk.Label(window, text="Novo Quarto (deixe em branco para manter):", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=1, column=0, padx=5, pady=5)
    entry_room = ttk.Entry(window)
    entry_room.grid(row=1, column=1, padx=5, pady=5)
    
    ttk.Label(window, text="Nova Data (deixe em branco para manter):", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=2, column=0, padx=5, pady=5)
    entry_date = ttk.Entry(window)
    entry_date.grid(row=2, column=1, padx=5, pady=5)
    
    def atualizar():
        try:
            aid = int(entry_aid.get())
        except ValueError:
            messagebox.showerror("Erro", "ID inválido!")
            return
        for adm in admissions:
            if adm["id"] == aid:
                novo_room = entry_room.get().strip()
                nova_date = entry_date.get().strip()
                if novo_room:
                    adm["room"] = novo_room
                if nova_date:
                    adm["date"] = nova_date
                messagebox.showinfo("Sucesso", "Internação atualizada!")
                window.destroy()
                return
        messagebox.showerror("Erro", "Internação não encontrada!")
    
    ttk.Button(window, text="Atualizar", command=atualizar).grid(row=3, column=0, columnspan=2, pady=10)

def dar_alta_gui():
    window = tk.Toplevel(root)
    window.title("Dar Alta no Paciente")
    window.geometry("200x200")
    
    ttk.Label(window, text="ID da Internação:", font=("Arial", 12, "bold"), foreground="#2c9192").pack(padx=5, pady=5)
    entry_aid = ttk.Entry(window)
    entry_aid.pack(padx=5, pady=5)
    
    def dar_alta():
        try:
            aid = int(entry_aid.get())
        except ValueError:
            messagebox.showerror("Erro", "ID inválido!")
            return
        for adm in admissions:
            if adm["id"] == aid:
                adm["status"] = "alta"
                messagebox.showinfo("Sucesso", "Paciente recebeu alta!")
                window.destroy()
                return
        messagebox.showerror("Erro", "Internação não encontrada!")
    
    ttk.Button(window, text="Dar Alta", command=dar_alta).pack(pady=10)

# ===============================
# Funções do Caixa (Transações)
# ===============================
def registrar_transacao_gui():
    window = tk.Toplevel(root)
    window.title("Registrar Transação")
    window.geometry("400x200")
    
    ttk.Label(window, text="Tipo (particular/convenio):", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=0, column=0, padx=5, pady=5)
    entry_tipo = ttk.Entry(window)
    entry_tipo.grid(row=0, column=1, padx=5, pady=5)
    
    ttk.Label(window, text="Valor:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=1, column=0, padx=5, pady=5)
    entry_valor = ttk.Entry(window)
    entry_valor.grid(row=1, column=1, padx=5, pady=5)
    
    ttk.Label(window, text="Descrição:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=2, column=0, padx=5, pady=5)
    entry_desc = ttk.Entry(window)
    entry_desc.grid(row=2, column=1, padx=5, pady=5)
    
    def registrar():
        tipo = entry_tipo.get().strip().lower()
        try:
            valor = float(entry_valor.get())
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido!")
            return
        desc = entry_desc.get().strip()
        tid = len(transactions) + 1
        transaction = {"id": tid, "type": tipo, "amount": valor, "description": desc}
        transactions.append(transaction)
        messagebox.showinfo("Sucesso", "Transação registrada!")
        window.destroy()
    
    ttk.Button(window, text="Registrar", command=registrar).grid(row=3, column=0, columnspan=2, pady=10)

def consultar_transacoes_gui():
    window = tk.Toplevel(root)
    window.title("Consultar Transações")
    window.geometry("500x250")
    
    text_area = tk.Text(window, width=60, height=15)
    text_area.pack(padx=5, pady=5)
    
    if not transactions:
        text_area.insert(tk.END, "Nenhuma transação registrada.")
    else:
        for t in transactions:
            text_area.insert(tk.END, f"ID {t['id']}: Tipo: {t['type']}, Valor: {t['amount']}, Descrição: {t['description']}\n")

# ===============================
# Funções de Cadastro de Convênios (ANS)
# ===============================
def cadastrar_convenio_gui():
    window = tk.Toplevel(root)
    window.title("Cadastrar Convênio")
    window.geometry("400x150")
    
    ttk.Label(window, text="Nome do Convênio:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=0, column=0, padx=5, pady=5)
    entry_nome = ttk.Entry(window)
    entry_nome.grid(row=0, column=1, padx=5, pady=5)
    
    ttk.Label(window, text="Número ANS:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=1, column=0, padx=5, pady=5)
    entry_ans = ttk.Entry(window)
    entry_ans.grid(row=1, column=1, padx=5, pady=5)
    
    def cadastrar():
        nome = entry_nome.get().strip()
        ans = entry_ans.get().strip()
        if nome == "" or ans == "":
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return
        cid = len(insurances) + 1
        insurance = {"id": cid, "name": nome, "ans_number": ans}
        insurances.append(insurance)
        messagebox.showinfo("Sucesso", f"Convênio {nome} cadastrado com sucesso com ID {cid}.")
        window.destroy()
    
    ttk.Button(window, text="Cadastrar", command=cadastrar).grid(row=2, column=0, columnspan=2, pady=10)

def atualizar_convenio_gui():
    window = tk.Toplevel(root)
    window.title("Atualizar Convênio")
    window.geometry("600x200")
    
    ttk.Label(window, text="ID do Convênio:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=0, column=0, padx=5, pady=5)
    entry_id = ttk.Entry(window)
    entry_id.grid(row=0, column=1, padx=5, pady=5)
    
    ttk.Label(window, text="Novo Nome (deixe em branco para manter):", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=1, column=0, padx=5, pady=5)
    entry_nome = ttk.Entry(window)
    entry_nome.grid(row=1, column=1, padx=5, pady=5)
    
    ttk.Label(window, text="Novo Número ANS (deixe em branco para manter):", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=2, column=0, padx=5, pady=5)
    entry_ans = ttk.Entry(window)
    entry_ans.grid(row=2, column=1, padx=5, pady=5)
    
    def atualizar():
        try:
            cid = int(entry_id.get())
        except ValueError:
            messagebox.showerror("Erro", "ID inválido!")
            return
        for ins in insurances:
            if ins["id"] == cid:
                novo_nome = entry_nome.get().strip()
                novo_ans = entry_ans.get().strip()
                if novo_nome:
                    ins["name"] = novo_nome
                if novo_ans:
                    ins["ans_number"] = novo_ans
                messagebox.showinfo("Sucesso", "Convênio atualizado!")
                window.destroy()
                return
        messagebox.showerror("Erro", "Convênio não encontrado!")
    
    ttk.Button(window, text="Atualizar", command=atualizar).grid(row=3, column=0, columnspan=2, pady=10)

def consultar_convenio_gui():
    window = tk.Toplevel(root)
    window.title("Consultar Convênio")
    window.geometry("500x200")
    
    ttk.Label(window, text="Digite o ID do Convênio:", font=("Arial", 12, "bold"), foreground="#2c9192").grid(row=0, column=0, padx=5, pady=5)
    entry_id = ttk.Entry(window)
    entry_id.grid(row=0, column=1, padx=5, pady=5)
    
    text_area = tk.Text(window, width=50, height=5)
    text_area.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
    def consultar():
        try:
            cid = int(entry_id.get())
        except ValueError:
            messagebox.showerror("Erro", "ID inválido!")
            return
        for ins in insurances:
            if ins["id"] == cid:
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, f"ID: {ins['id']}\nNome: {ins['name']}\nANS: {ins['ans_number']}")
                return
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, "Convênio não encontrado!")
    
    ttk.Button(window, text="Consultar", command=consultar).grid(row=1, column=0, columnspan=2, pady=5)

def remover_convenio_gui():
    window = tk.Toplevel(root)
    window.title("Remover Convênio")
    window.geometry("300x150")
    
    ttk.Label(window, text="Digite o ID do Convênio a remover:", font=("Arial", 12, "bold"), foreground="#2c9192").pack(padx=5, pady=5)
    entry_id = ttk.Entry(window)
    entry_id.pack(padx=5, pady=5)
    
    def remover():
        try:
            cid = int(entry_id.get())
        except ValueError:
            messagebox.showerror("Erro", "ID inválido!")
            return
        for i, ins in enumerate(insurances):
            if ins["id"] == cid:
                insurances.pop(i)
                messagebox.showinfo("Sucesso", "Convênio removido!")
                window.destroy()
                return
        messagebox.showerror("Erro", "Convênio não encontrado!")
    
    ttk.Button(window, text="Remover", command=remover).pack(pady=10)

# ===============================
# Funções de Relatórios
# ===============================
def gerar_relatorios_gui():
    window = tk.Toplevel(root)
    window.title("Relatórios")
    
    text_area = tk.Text(window, width=80, height=25)
    text_area.pack(padx=5, pady=5)
    
    report = "=== Relatórios do Sistema Hospitalar ===\n\n"
    report += f"Total de Pacientes: {len(patients)}\n"
    report += f"Total de Profissionais: {len(professionals)}\n\n"
    
    report += "Procedimentos (CID):\n"
    for proc in procedures:
        report += f"  CID {proc['cid']}: {proc['description']}\n"
    report += "\nMédicos por Especialidade:\n"
    specialty_dict = {}
    for p in professionals:
        spec = p.get("specialty", "Desconhecido")
        specialty_dict.setdefault(spec, []).append(p)
    for spec, profs in specialty_dict.items():
        report += f"\nEspecialidade: {spec}\n"
        for p in profs:
            report += f"  ID {p['id']}: {p['name']}\n"
    
    report += "\nPonto de Presença dos Funcionários:\n"
    for p in professionals:
        report += f"  {p['name']} (ID {p['id']}) - Presença registrada\n"
    
    text_area.insert(tk.END, report)

# ===============================
# Gerar Relatório
# ===============================
def gerar_relatorio_gui():
    file_name = gerar_relatorio_txt()  # Gera o arquivo com o relatório
    messagebox.showinfo("Relatório", f"Relatório gerado com sucesso!\nArquivo: {file_name}")

# ===============================
# Janela Principal
# ===============================
root = tk.Tk()
root.title("Sistema de Gestão Hospitalar")
root.geometry("800x600")

header = ttk.Label(root, text="Bem-vindo ao Sistema de Gestão Hospitalar", font=("Helvetica", 16, "bold"), foreground="blue")
header.pack(pady=15)

frame = ttk.Frame(root)
frame.pack(padx=15, pady=15, fill="both", expand=True)

# Lista de botões (texto, função)
botoes = [
    ("Cadastrar Paciente", cadastrar_paciente_gui),
    ("Atualizar Paciente", atualizar_paciente_gui),
    ("Consultar Paciente", consultar_paciente_gui),
    ("Remover Paciente", remover_paciente_gui),
    ("Cadastrar Profissional", cadastrar_profissional_gui),
    ("Atualizar Profissional", atualizar_profissional_gui),
    ("Consultar Profissional", consultar_profissional_gui),
    ("Remover Profissional", remover_profissional_gui),
    ("Cadastrar Procedimento (CID)", cadastrar_procedimento_gui),
    ("Atualizar Procedimento", atualizar_procedimento_gui),
    ("Consultar Procedimento", consultar_procedimento_gui),
    ("Remover Procedimento", remover_procedimento_gui),
    ("Agendar Cirurgia", agendar_cirurgia_gui),
    ("Atualizar Cirurgia", atualizar_cirurgia_gui),
    ("Cancelar Cirurgia", cancelar_cirurgia_gui),
    ("Internar Paciente", internar_paciente_gui),
    ("Atualizar Internação", atualizar_internacao_gui),
    ("Dar Alta", dar_alta_gui),
    ("Registrar Transação", registrar_transacao_gui),
    ("Consultar Transações", consultar_transacoes_gui),
    ("Cadastrar Convênio", cadastrar_convenio_gui),
    ("Atualizar Convênio", atualizar_convenio_gui),
    ("Consultar Convênio", consultar_convenio_gui),
    ("Remover Convênio", remover_convenio_gui),
    ("Gerar Relatório", gerar_relatorio_gui),
]

cols = 4
for idx, (texto, func) in enumerate(botoes):
    r = idx // cols
    c = idx % cols
    ttk.Button(frame, text=texto, command=func, width=25).grid(row=r, column=c, padx=5, pady=5)

ttk.Button(root, text="Sair", command=root.quit).pack(pady=10)

root.mainloop()
