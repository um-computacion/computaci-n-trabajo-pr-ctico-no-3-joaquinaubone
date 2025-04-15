# src/calculo_numeros.py

from src.exceptions import ingrese_numero, NumeroDebeSerPositivo

def main():
    while True:
        try:
            numero = ingrese_numero()
            print(f"Número válido: {numero}")
        except NumeroDebeSerPositivo:
            print("Error: El número debe ser positivo")
        except ValueError:
            print("Error: La entrada debe ser un número válido")
        except KeyboardInterrupt:
            print("\nSaliendo del programa...")
            break

if __name__ == "__main__":
    main()
