def maquina_turing(cinta_input):
    cinta = list(cinta_input) + ['□']
    cabeza = 0
    estado = 'q0'

    transiciones = {
        ('q0', '0'): ('q1', '□', 'R'),
        ('q0', '1'): ('q4', '□', 'R'),
        ('q0', '□'): ('q6', '□', 'R'),
        ('q1', '0'): ('q1', '0', 'R'),
        ('q1', '1'): ('q1', '1', 'R'),
        ('q1', '□'): ('q2', '□', 'L'),
        ('q2', '0'): ('q3', '□', 'L'),
        ('q2', '□'): ('q6', '□', 'R'),
        ('q3', '0'): ('q3', '0', 'L'),
        ('q3', '1'): ('q3', '1', 'L'),
        ('q3', '□'): ('q0', '□', 'R'),
        ('q4', '0'): ('q4', '0', 'R'),
        ('q4', '1'): ('q4', '1', 'R'),
        ('q4', '□'): ('q5', '□', 'L'),
        ('q5', '1'): ('q3', '□', 'L'),
        ('q5', '□'): ('q6', '□', 'R'),
        ('q6', '□'): ('ACEPTACION', '□', 'R')
    }

    paso = 0
    while estado != 'ACEPTACION':
        simbolo = cinta[cabeza]
        clave = (estado, simbolo)
        print(f"Paso {paso}: Estado = {estado}, Cabeza = {cabeza}, Cinta = {''.join(cinta)}")

        if clave not in transiciones:
            print("Transición no definida. Cadena rechazada.")
            return False

        estado_siguiente, simbolo_escrito, direccion = transiciones[clave]
        cinta[cabeza] = simbolo_escrito

        if direccion == 'R':
            cabeza += 1
            if cabeza >= len(cinta):
                cinta.append('□')
        elif direccion == 'L':
            cabeza -= 1
            if cabeza < 0:
                cinta.insert(0, '□')
                cabeza = 0

        estado = estado_siguiente
        paso += 1

    print(f"Cadena aceptada. Estado final: {estado}")
    return True

cadena_a_leer = input("Escribe la cadena a leer: ")
maquina_turing(cadena_a_leer)