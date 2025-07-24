import math

# Abre el archivo binario en modo lectura
with open('your_file', 'rb') as f:
    data = f.read()

# Inicializa una lista para contar la frecuencia de cada byte (0-255)
frequencies = [0] * 256

# Cuenta la frecuencia de cada byte
for byte in data:
    frequencies[byte] += 1

# Calcula la entropía
entropy = 0
total_bytes = len(data)
for freq in frequencies:
    if freq > 0:
        p = freq / total_bytes
        entropy -= p * math.log2(p)

# Imprime el resultado con 6 decimales
print(f"Entropía: {entropy:.6f}")
