def txt_morse(txt, lista_morse):
    txt = txt.lower()
    text_to_morse = ''
    for caracter in txt:
        for letra in lista_morse:
            if caracter == letra[0]:
                text_to_morse += letra[1]
                text_to_morse += ' '
                break
            elif caracter == ' ':
                text_to_morse += ' '
                break
    return text_to_morse