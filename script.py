import os
from datetime import datetime

# Cria a pasta se não existir
os.makedirs("arquivos", exist_ok=True)

# Gera nome do arquivo com data e hora
agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
arquivo = f"arquivos/{agora}.txt"

# Escreve data e hora dentro do arquivo
with open(arquivo, "w") as f:
    f.write(f"Execução em: {datetime.now()}\n")

print(f"Arquivo criado: {arquivo}")
