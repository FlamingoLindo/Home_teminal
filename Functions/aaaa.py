import subprocess
import time

last = ''
# Comando PowerShell a ser executado
command = "Get-Date -Format 'dddd MM/dd/yyyy HH:mm'"

while True:
    try:
        # Executando o comando PowerShell
        result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)

        # Verificar se a saída atual é diferente da última saída armazenada
        if result.stdout.strip() != last:
            print(result.stdout.strip())
            last = result.stdout.strip()

        # Aguarda um pouco antes de repetir o loop
        time.sleep(1.0)

    except OSError as e:
        print(f"Error: {e}. Could not read image!")
        time.sleep(1.5)
