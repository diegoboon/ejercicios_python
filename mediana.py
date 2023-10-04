# Declara la variable `mediana` y la inicializa a `None`
mediana = None

# Define la función `mediana()`
def mediana(a, b, c):


  # Comprueba si `a` es el valor central.
  if a <= b <= c:
    return b

  # Comprueba si `a` es el valor más grande.
  elif a <= c <= b:
    return c

  # Por defecto, `a` es el valor más pequeño.
  else:
    return a


# Lee los tres valores del usuario.
a = int(input("Introduce el primer valor: "))
b = int(input("Introduce el segundo valor: "))
c = int(input("Introduce el tercer valor: "))

# Asigna el valor de la función `mediana()` a la variable `mediana`.
mediana = mediana(a, b, c)

# Imprime la mediana de los tres valores.
print(f"La mediana de los valores {a}, {b} y {c} es {mediana}.")
