from morse_or_txt_normal import ascertain_morse_or_normal_txt

lista_morse = [
    ['a', '.-'],
    ['b', '-...'],
    ['c', '-.-.'],
    ['d', '-..'],
    ['e', '.'],
    ['f', '..-.'],
    ['g', '--.'],
    ['h', '....'],
    ['i', '..'],
    ['j', '.---'],
    ['k', '-.-'],
    ['l', '.-..'],
    ['m', '--'],
    ['n', '-.'],
    ['ñ', '--.--'],
    ['o', '---'],
    ['p', '.--.'],
    ['q', '--.-'],
    ['r', '.-.'],
    ['s', '...'],
    ['t', '-'],
    ['u', '..-'],
    ['v', '...-'],
    ['w', '.--'],
    ['x', '-..-'],
    ['y', '-.--'],
    ['z', '--..'],
    ['0', '-----'],
    ['1', '.----'],
    ['2', '..---'],
    ['3', '...--'],
    ['4', '....-'],
    ['5', '.....'],
    ['6', '-....'],
    ['7', '--...'],
    ['8', '---..'],
    ['9', '----.'],
    ['.', '.-.-.-'],
    [',', '--..--'],
    ['?', '..--..'],
    ['"', '.-..-.']]

txt = input('Introduce el texto que quieres convertir a morse, o introduce un texto de morse directamente, separando las letras por un espacio y las palabras por dos espacios ')

# Comprueba si es código morse o texto normal y lo convierte en el otro
converted_text = ascertain_morse_or_normal_txt(txt, lista_morse)
print(converted_text)
