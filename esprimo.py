def es_primo(n):
  """
  Determina si un número es primo.

  Args:
    n: El número a comprobar.

  Returns:
    True si el número es primo, False en caso contrario.
  """

  # Si el número es menor o igual a 1, no es primo.

  if n <= 1:
    return False

  # Para cada número entre 2 y la raíz cuadrada de n,
  # si n es divisible por ese número, no es primo.

  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False

  # Si no se ha encontrado ningún divisor, el número es primo.

  return True


def main():
 
 
  # Lee el número del usuario.

  n = int(input("Introduce un número: "))

  # Llama a la función `es_primo()` para comprobar si el número es primo.

  if es_primo(n):
    print(f"El número {n} es primo.")
  else:
    print(f"El número {n} no es primo.")


if __name__ == "__main__":
  main()
