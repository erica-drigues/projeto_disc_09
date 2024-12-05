import tkinter as tk
from tkinter import messagebox
from imc import IMC

def calcular():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc_calculado = IMC(peso, altura)
        imc_valor = imc_calculado.calcular_imc()
        print(f"{imc_valor}")
        classificacao = imc_calculado.classificar_imc()

        resultado.set(f"Seu IMC: {imc_valor:.2f}\nClassificação: {classificacao}")
    except ValueError as e:
        messagebox.showerror("Erro", f"Entrada inválida(Ultilize a altura em metros (1.65)): {e}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("300x300")

# Entrada para peso
tk.Label(janela, text="Peso (kg):").pack(pady=5)
entry_peso = tk.Entry(janela)
entry_peso.pack(pady=5)

# Entrada para altura
tk.Label(janela, text="Altura (m):").pack(pady=5)
entry_altura = tk.Entry(janela)
entry_altura.pack(pady=5)

# Botão para calcular
tk.Button(janela, text="Calcular IMC", command=calcular).pack(pady=10)

# Label para mostrar o resultado
resultado = tk.StringVar()
label_resultado = tk.Label(janela, textvariable=resultado, wraplength=280, justify="center")
label_resultado.pack(pady=10)

# Loop principal
janela.mainloop()
