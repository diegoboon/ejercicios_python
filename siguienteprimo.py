# Importa la función `es_primo()` del esprimo
import esprimo

# Define la función `nextPrime()`
def nextPrime(n):
  """
  Devuelve el primer número primo mayor que n.

  Args:
    n: El número inicial.

  Returns:
    El primer número primo mayor que n, o None si no existe.
  """

  # Inicializa la variable `i` a `n + 1`
  i = n + 1

  # Mientras `i` no sea primo, incrementa `i` en 1
  while not ejercicio1.es_primo(i):
    i += 1

  # Devuelve `i` si es primo
  return i

# Define la función `main()`
def main():
  """
  Lee un número del usuario y llama a la función `nextPrime()` para encontrar el primer número primo mayor que ese número.
  """

  # Lee el número del usuario
  n = int(input("Introduce un número: "))

  # Llama a la función `nextPrime()`
  next_prime = nextPrime(n)

  # Si la función `nextPrime()` devuelve un valor, imprime el número
  if next_prime is not None:
    print(f"El primer número primo mayor que {n} es {next_prime}.")
  else:
    # Si la función `nextPrime()` devuelve `None`, imprime un mensaje de error
    print("No existe un número primo mayor que {n}.")

# Ejecuta la función `main()`
if __name__ == "__main__":
  main()
