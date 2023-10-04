import ejercicio1

def nextPrime(n):


  i = n + 1
  while not ejercicio1.es_primo(i):
    i += 1
  return i

def main():

  n = int(input("Introduce un número: "))
  next_prime = nextPrime(n)

  if next_prime is not None:
    print(f"El primer número primo mayor que {n} es {next_prime}.")
  else:
    print("No existe un número primo mayor que {n}.")

if __name__ == "__main__":
  main()
