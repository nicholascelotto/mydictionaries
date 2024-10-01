codes = {
    'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '0', 'c': '!', 'D': '$', 'd': '2',
    'E': '&', 'e': '*', 'F': '3', 'f': '1', 'G': '(', 'g': '7', 'H': ')', 'h': '4',
    'I': '+', 'i': '-', 'J': '/', 'j': '=', 'K': '5', 'k': '8', 'L': '?', 'l': '6',
    'M': '^', 'm': '[', 'N': ']', 'n': '~', 'O': '<', 'o': '>', 'P': '{', 'p': '}',
    'Q': '|', 'q': ':', 'R': ';', 'r': ',', 'S': '.', 's': '_', 'T': '`', 't': '"',
    'U': 'Z', 'u': 'J', 'V': 'C', 'v': 'V', 'W': 'B', 'w': 'N', 'X': 'M', 'x': 'P',
    'Y': 'L', 'y': 'K', 'Z': 'X', 'z': 'H'
}

reverse_codes = {v: k for k, v in codes.items()}

def decrypt_file(input_filename):
    infile = open(input_filename, 'r')
    for line in infile:
        decrypted_line = ""
        for char in line:
            decrypted_line += reverse_codes.get(char, char)
        print(decrypted_line)
    infile.close()

encrypted_file = 'encrypted.txt'
decrypt_file(encrypted_file)