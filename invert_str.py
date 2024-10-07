def inverter_string(texto):
    invertida = ''
    for i in range(len(texto) - 1, -1, -1):
        invertida += texto[i]
    return invertida

texto = input("Informe uma string para ser invertida: ")
print(f"String invertida: {inverter_string(texto)}")
