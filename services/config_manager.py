import json
import os

# Define o caminho do arquivo na pasta do projeto
CONFIG_FILE = "config.json"

def save_config(tipo, target_name):
    config = {"tipo": tipo, "target_name": target_name}
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)
    print(f"Configuração salva em: {os.path.abspath(CONFIG_FILE)}")

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return None
    return None