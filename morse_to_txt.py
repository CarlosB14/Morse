def morse_txt(text_in_morse, lista_morse):
    letra = ''
    palabra = ''
    count = 0
    texto = ''
    for indice, caracter in enumerate(text_in_morse):
        if (caracter == '.') or (caracter == '-'):
            letra += caracter
            count = 0

        elif caracter == ' ':
            count += 1
            for letter in lista_morse:
                if letter[1] == letra:
                    palabra += letter[0]
                    letra = ''
                    break
            if count == 2:
                texto += palabra
                texto += ' '
                palabra = ''
        if len(text_in_morse) == (indice+1):
            for letter in lista_morse:
                if letter[1] == letra:
                    palabra += letter[0]
                    texto += palabra
    return texto