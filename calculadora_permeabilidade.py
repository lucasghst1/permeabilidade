import tkinter as tk
from tkinter import messagebox, ttk
import math

# Função para verificar a permeabilidade com base no tipo de solo
def verificar_permeabilidade(K_m_s, tipo_solo):
    # Mapeamento do tipo de solo para suas condições de permeabilidade
    condicoes = {
        "Areia fina": ('10^-4 a 10^-5', 1e-4 >= K_m_s >= 1e-5),
        "Areia grossa": ('10^-2 a 10^-3', 1e-2 >= K_m_s >= 1e-3),
        "Areia média": ('10^-3 a 10^-4', 1e-3 >= K_m_s >= 1e-4),
        "Areia siltosa": ('10^-5 a 10^-6', 1e-5 >= K_m_s >= 1e-6),
        "Siltes": ('10^-6 a 10^-8', 1e-6 >= K_m_s >= 1e-8),
        "Argilas": ('< 10^-8', K_m_s < 1e-8),
    }
    faixa, _ = condicoes[tipo_solo]
    return faixa

def calcular_permeabilidade():
    try:
        H = 300  # Altura do solo (cm)
        r = 0.09113321515115849  # Raio do cilindro (cm)
        T = 1785  # Tempo fixo (s)

        # Obtém valores do usuário
        H1 = float(entrada_H1.get())
        H2 = float(entrada_H2.get())
        tipo_solo = tipo_solo_var.get()

        # Cálculos
        R = math.pi * r**2  # Área da seção transversal do cilindro
        Q = (H2 - H1) * R  # Volume de água percolado (cm3)
        K = Q / (T * H)  # Permeabilidade do solo (cm/s)
        K_m_s = K / 100  # Conversão de permeabilidade para m/s

        # Formata a string de permeabilidade
        K_string = f"{K:.2e}".replace('e', '×10^')
        
        # Obter a faixa de permeabilidade com base no tipo de solo escolhido
        faixa = verificar_permeabilidade(K_m_s, tipo_solo)
        
        # Mostrar resultados
        mostrar_resultados(tipo_solo, Q, K_string, K_m_s, faixa)
        
    except ValueError:
        messagebox.showerror("Erro", "Insira apenas números.")

def mostrar_resultados(tipo_solo, Q, K_string, K_m_s, faixa):
    # Cria uma nova janela para os resultados
    janela_resultados = tk.Toplevel()
    janela_resultados.title("Resultados")
    janela_resultados.geometry('400x250')
    janela_resultados.configure(bg='#f0f0f0')
    
    # Adiciona texto com os resultados
    texto_resultados = tk.Text(janela_resultados, height=10, width=50, font=('Helvetica', 12))
    texto_resultados.insert(tk.END, f"Tipo de solo: {tipo_solo}\n")
    texto_resultados.insert(tk.END, f"Faixa de permeabilidade esperada: {faixa}\n")
    texto_resultados.insert(tk.END, f"Volume de água percolado: {Q:.2f} cm³\n")
    texto_resultados.insert(tk.END, f"Permeabilidade do solo: {K_string} cm/s\n")
    texto_resultados.insert(tk.END, f"Permeabilidade do solo em m/s: {K_m_s:.2e} m/s")
    texto_resultados.config(state=tk.DISABLED)  # Desativa a edição do texto
    texto_resultados.pack(padx=10, pady=10)

# Configuração da janela principal
app = tk.Tk()
app.title("Tecnosolo - Permeabilidade do Solo")
app.geometry('400x300')

# Estilos
fonte_titulo = ('Helvetica', 14, 'bold')
fonte_texto = ('Helvetica', 12)
cor_botao = '#0052cc'
cor_texto_botao = '#ffffff'
padding = {'padx': 5, 'pady': 5}

# Título
titulo = tk.Label(app, text="Permeabilidade do Solo - Tecnosolo", font=fonte_titulo)
titulo.grid(row=0, column=0, columnspan=2, **padding)

# Entrada para altura inicial
label_H1 = tk.Label(app, text="Altura inicial (cm):", font=fonte_texto)
label_H1.grid(row=1, column=0, **padding)
entrada_H1 = tk.Entry(app, font=fonte_texto)
entrada_H1.grid(row=1, column=1, **padding)

# Entrada para altura final
label_H2 = tk.Label(app, text="Altura final (cm):", font=fonte_texto)
label_H2.grid(row=2, column=0, **padding)
entrada_H2 = tk.Entry(app, font=fonte_texto)
entrada_H2.grid(row=2, column=1, **padding)

# Escolha do tipo de solo
label_tipo_solo = tk.Label(app, text="Tipo de solo:", font=fonte_texto)
label_tipo_solo.grid(row=3, column=0, **padding)
tipos_solo = ["Areia grossa", "Areia média", "Areia fina", "Areia siltosa", "Siltes", "Argilas"]
tipo_solo_var = ttk.Combobox(app, values=tipos_solo, font=fonte_texto, state="readonly")
tipo_solo_var.grid(row=3, column=1, **padding)
tipo_solo_var.set(tipos_solo[0])  # Valor padrão

# Botão de cálculo
botao_calcular = tk.Button(app, text="Calcular", command=calcular_permeabilidade, bg=cor_botao, fg=cor_texto_botao, font=fonte_texto)
botao_calcular.grid(row=4, column=0, columnspan=2, **padding)

app.mainloop()
