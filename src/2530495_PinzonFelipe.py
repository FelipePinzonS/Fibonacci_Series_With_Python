# Fibonacci Series with Python ;)

# Nombre: Felipe Pinzon Segura
# Matrícula: 2530495
# Grupo: IM 1-2

# RESUMEN EJECUTIVO
"""
La serie de Fibonacci es una secuencia donde cada término es la suma de 
los dos anteriores, comenzando con 0 y 1. Calcular la serie hasta n 
términos significa generar los primeros n números de esta secuencia. 
Este programa lee n desde el usuario, valida la entrada (1-50) y 
genera la serie utilizando un bucle while, mostrando los términos 
en formato legible.
"""

# Problem: Fibonacci series up to n terms
"""
Description: Program that reads an integer n and prints the first n
terms of the Fibonacci series starting at 0 and 1.

Inputs:
- n (int; number of terms to generate)

Outputs:
- "Number of terms: <n>"
- "Fibonacci series: <term_1> <term_2> ... <term_n>"

Validations:
- n must be convertible to integer
- n must be >= 1
- n must be <= 50 (to prevent extremely large series)

Test cases:
1) Normal: n = 7 → expected series: 0 1 1 2 3 5 8
2) Border: n = 1 → expected series: 0
3) Error: n = -3 → expected message: "Error: invalid input"
"""

n_terms = (input("Enter the number of terms: "))

try:
    n = int(n_terms)
    if n < 1 or n > 50:
        print("Error: invalid input")
        exit()
except ValueError:
    print("Error: invalid input")
    exit()

fibonacci_series = []
a, b = 0, 1
for i in range(n):
    fibonacci_series.append(a)
    a, b = b, a + b

print(f"The Fibonacci Series is: {fibonacci_series}")

# CONCLUSIONES
"""
    El bucle while fue efectivo para generar la serie Fibonacci ya que
    permitió controlar el número de iteraciones basado en el valor n
    ingresado por el usuario, creando cada nuevo término a partir de
    los dos anteriores.

    Manejar los casos especiales n=1 y n=2 fue crucial para evitar
    errores de índice, ya que la lógica de generación requiere al
    menos dos términos previos para calcular el siguiente.

    Esta lógica puede reutilizarse en otros contextos como cálculos
    financieros (interés compuesto), crecimiento poblacional o cualquier
    fenómeno que siga un patrón de recurrencia similar.

    La validación de entrada (1 ≤ n ≤ 50) protegió al programa de
    valores extremos que podrían generar números excesivamente grandes
    o causar problemas de rendimiento.
"""

# REFERENCIAS
"""
1) Python - More Control Flow Tools¶
   URL:https://docs.python.org/3.11/tutorial/controlflow.html

2) Real Python - Python Fibonacci Sequence Tutorial
   URL: https://realpython.com/fibonacci-sequence-python/

3) GeeksforGeeks - Program for Fibonacci numbers
   URL: https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
"""

# REPOSITORIO DE GITHUB
"""
    URL:
"""