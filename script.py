import os
from datetime import datetime

os.makedirs("bot_files", exist_ok=True)

now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file = f"bot_files/{now}.txt"

# Escreve data e hora dentro do arquivo
with open(file, "w") as f:
    f.write(f"Executed at: {datetime.now()}\n")

print(f"File generated: {file}")
