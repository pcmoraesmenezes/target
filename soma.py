def calcula_soma():
    INDICE = 13
    SOMA = 0
    K = 0

    while K < INDICE:
        K += 1
        SOMA += K
    
    return SOMA

print(f"O valor final de SOMA é: {calcula_soma()}")
