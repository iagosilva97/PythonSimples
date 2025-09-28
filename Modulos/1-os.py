import os

# 1 - Retornar a pasta atual
print("Pasta atual:", os.getcwd())

# 2 - Listar arquivos e pastas na pasta atual
print("Arquivos e pastas na pasta atual:", os.listdir())

#3 - versão do sistema operacional
os.system('ver')  # No Windows
# os.system('uname -a')  # No Linux ou MacOS
print("Sistema operacional:", os.name)
print("Versão do Python:", os.sys.version)

# 4 - configurações da máquina
print("Nome do usuário:", os.getlogin())
os.system('systeminfo')

# 5 - limpar a tela
os.system('cls') # No Windows
# os.system('clear') # No Linux ou MacOS
print("Tela limpa!")

# 6 - desligar o computador
# Cuidado ao usar este comando, ele desligará o computador!
# os.system('shutdown /s /t 1') # No Windows
# os.system('shutdown /a') # Para o desligamento no Windows
# os.system('shutdown -h now') # No Linux ou MacOS

# 7 - função para desligar o computador após um tempo
def turn_off_one_hour():
    os.system('shutdown /s /t 3600') # No Windows
    # os.system('shutdown -h +60') # No Linux ou MacOS
    print("O computador será desligado em 1 hora.")
    
def turn_off_half_hour():
    os.system('shutdown /s /t 1800') # No Windows
    # os.system('shutdown -h +30') # No Linux ou MacOS
    print("O computador será desligado em 30 minutos.")

def cancel_turn_off():
    os.system('shutdown /a') # No Windows
    # os.system('shutdown -c') # No Linux ou MacOS
    print("Desligamento cancelado.")

