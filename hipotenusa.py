# Importa el módulo `math`
import math

# Define la función `calcular_hipotenusa()`
def calcular_hipotenusa(a, b):
  """
  Calcula la longitud de la hipotenusa de un triángulo rectángulo.

  Args:
    a: La longitud del primer lado más corto.
    b: La longitud del segundo lado más corto.

  Returns:
    La longitud de la hipotenusa.
  """

  # Calcula la longitud de la hipotenusa usando el teorema de Pitágoras.
  hipotenusa = math.sqrt(a**2 + b**2)

  # Devuelve la longitud de la hipotenusa.
  return hipotenusa

# Define la función `main()`
def main():
  """
  Calcula la longitud de la hipotenusa de un triángulo rectángulo.

  Args:
    a: La longitud del primer lado más corto.
    b: La longitud del segundo lado más corto.

  Returns:
    La longitud de la hipotenusa.
  """

  # Lee la longitud del primer lado más corto.
  a = float(input("Introduce la longitud del primer lado más corto: "))

  # Lee la longitud del segundo lado más corto.
  b = float(input("Introduce la longitud del segundo lado más corto: "))

  # Calcula la longitud de la hipotenusa.
  hipotenusa = calcular_hipotenusa(a, b)

  # Imprime la longitud de la hipotenusa.
  print(f"La longitud de la hipotenusa del triángulo rectángulo es: {hipotenusa}")

# Ejecuta la función `main()`
if __name__ == "__main__":
  main()
