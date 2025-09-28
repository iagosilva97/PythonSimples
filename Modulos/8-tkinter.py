import tkinter as tk

# Criar a janela principal
window = tk.Tk()
window.geometry("300x200")
window.title("Exemplo Tkinter")

# Adicionar um frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill="x", expand=True)

# Adicionar um label
label = tk.Label(frame, text="Olá, Tkinter!")
label.pack(fill="x", expand=True)

# Adicionar um inpout de texto
frase_labe = tk.Label(frame, text="Frase")
frase_labe.pack(fill="x", expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill="x", expand=True)

# Função para alterar o texto do label
def click():
    label.config(text=frase_inp.get())
    
# Adicionar um botão
button = tk.Button(frame, text="Enviar", command=click)
button.pack()

window.mainloop()