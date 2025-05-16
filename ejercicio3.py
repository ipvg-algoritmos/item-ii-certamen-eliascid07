# 📝 ejercicio3.py
# 🔁 Verificador de palíndromos
# Puntaje: 15 puntos

# Instrucciones:
# 1. Solicita al usuario una palabra o frase.
# 2. Crea una función llamada es_palindromo(texto) que:
#    - Convierta el texto a minúsculas
#    - Elimine los espacios
#    - Compare el texto con su reverso
# 3. Muestra si es o no un palíndromo con un mensaje claro.

# 👇 Aquí comienza tu código
def es_palindromo(palabra):
    
    palabra = palabra.replace("", "").lower()
    
    if palabra == palabra [::-1]:
        return True
    return False

entrada = input("Introduce una palabra para verificar si es un palindromo: ")    

if es_palindromo(entrada):
    print(f"La Palabra: '{entrada}' es un palindromo")
else:
    print(f"la palabra: '{entrada}' no es un palindromo")
    
