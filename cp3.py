temperaturas = [[28, 31, 34, 33],
                [25, 27, 29, 28],
                [32, 35, 36, 34],
                [24, 26, 25, 27]
                ]

sala_mais_critica = 0

max_registros_criticos = -1

for i in range(len(temperaturas)):
    salaAtual = temperaturas[i]
    numSala = i + 1
    somaTemperatura = 0
    contCritico = 0

    for temperatura in salaAtual:
        somaTemperatura += temperatura
        if temperatura >= 33:
            contCritico += 1

    mediaTemperatura = somaTemperatura / len(salaAtual)

    print(f"Sala {numSala} \nMédia: {mediaTemperatura:.2f}°C  \nRegistros críticos: {contCritico}\n")

    if contCritico > max_registros_criticos:
        max_registros_criticos = contCritico
        sala_mais_critica = numSala

print(f"Sala com maior risco: {sala_mais_critica}")