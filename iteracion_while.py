contador_interno = 0
contador_externo = 0

while contador_externo < 5:

    while contador_interno < 8:
        print(contador_externo, contador_interno)
        contador_interno += 1

        if contador_interno >= 4:
            break

    contador_externo += 1
    contador_interno = 0
