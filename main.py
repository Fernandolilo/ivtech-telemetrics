import asyncio

from services.enums.connection_type import ConnectionType

def selecionar_conexao():
    print("\n--- Selecione o tipo de equipamento ---")
    for i, tipo in enumerate(ConnectionType, start=1):
        print(f"{i} - {tipo.name}")
    
    while True:
        try:
            escolha = int(input("\nDigite o número da opção desejada: "))
            return list(ConnectionType)[escolha - 1]
        except (ValueError, IndexError):
            print("Opção inválida. Tente novamente.")
            
async def main():
    tipo = selecionar_conexao()
    
    # Instanciação direta
    if tipo == ConnectionType.BLUETOOTH:
        print("Conexao Bluetooth")
    elif tipo == ConnectionType.SERIAL:
         print("Conexao Serial")
    else:
        print("Tipo de conexão não suportado.")
        return

    
   

if __name__ == "__main__":
    asyncio.run(main())