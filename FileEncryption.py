codes = {
    'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '0', 'c': '!', 'D': '$', 'd': '2',
    'E': '&', 'e': '*', 'F': '3', 'f': '1', 'G': '(', 'g': '7', 'H': ')', 'h': '4',
    'I': '+', 'i': '-', 'J': '/', 'j': '=', 'K': '5', 'k': '8', 'L': '?', 'l': '6',
    'M': '^', 'm': '[', 'N': ']', 'n': '~', 'O': '<', 'o': '>', 'P': '{', 'p': '}',
    'Q': '|', 'q': ':', 'R': ';', 'r': ',', 'S': '.', 's': '_', 'T': '`', 't': '"',
    'U': 'Z', 'u': 'J', 'V': 'C', 'v': 'V', 'W': 'B', 'w': 'N', 'X': 'M', 'x': 'P',
    'Y': 'L', 'y': 'K', 'Z': 'X', 'z': 'H'
}

def encrypt_file(input_filename, output_filename):
    infile = open(input_filename, 'r')
    outfile = open(output_filename, 'w')

    for line in infile:
        encrypted_line = ""
        for char in line:
            encrypted_line += codes.get(char, char)
        outfile.write(encrypted_line)

    infile.close()
    outfile.close()

input_file = 'info_security.txt'
output_file = 'encrypted.txt'
encrypt_file(input_file, output_file)

print("File has been encrypted and saved as 'encrypted.txt'.")
