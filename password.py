# Importa el módulo `random`
import random

# Define la función `generar_contrasena_aleatoria()`
def generar_contrasena_aleatoria():
  # Genera la longitud de la contraseña
  longitud = random.randint(7, 10)

  # Inicializa la contraseña como una cadena vacía
  contrasena = ""

  # Itera sobre la longitud de la contraseña
  for i in range(longitud):
    # Genera un caracter aleatorio
    caracter = chr(random.randint(33, 126))

    # Agrega el caracter a la contraseña
    contrasena += caracter

  # Devuelve la contraseña
  return contrasena

# Define la función `main()`
def main():
  """
  Muestra una contraseña aleatoria.
  """

  # Genera una contraseña aleatoria
  contrasena = generar_contrasena_aleatoria()

  # Imprime la contraseña
  print(f"La contraseña aleatoria es: {contrasena}")

# Ejecuta la función `main()`
if __name__ == "__main__":
  main()
