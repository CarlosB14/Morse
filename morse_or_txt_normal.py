from text_to_morse import txt_morse
from morse_to_txt import morse_txt

def ascertain_morse_or_normal_txt(txt, lista_morse):
    count = 0
    for letra in txt:
        if (letra == '.') or (letra == '-') or (letra == ' '):
            count +=1
            if count == 5:
                return morse_txt(txt, lista_morse)
        else:
            return txt_morse(txt, lista_morse)