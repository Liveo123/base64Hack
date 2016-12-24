# Description: Convert base64 to ASCII based on the RFC 3528 scheme
# Author: Paul Livesey
# Usage: base64.py filename
import pdb

# Function to convert a single base64 character to it's
# numeric equivalent
def cnvtToAsc(letter):
    for i in range(0, len(b64Table)-1):
        if b64Table[i] == letter:
            return i
    # if letter is not found, return -1
    return -1

# Create base64 character data structure
charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
pad = '='

# Take each character and add to array.
b64Table = []
counter = 0
pdb.set_trace()
for letter in charset:
    b64Table.append(letter)
    counter += 1

pdb.set_trace()
print('b64Table[63] = ' + b64Table[63])

# Loop through characters 4 letters at a time...
# For now just get 1st 4
quartet = 'abdr' 

# Take 1st of 4, get base 64 conversion, and shift left 2.
letter1Code = cnvtToAsc(quartet[0])
letter1Code = letter1Code << 2
pdb.set_trace()

# Take 2nd of 4, get base64 conversion, AND final 2 bits out, shift to lowest places and OR with 1st
temp = cnvtToAsc(quartet[1])
twoBits = temp & 192     #11000000
twoBits = twoBits >> 6
letter1Code = letter1Code | twoBits


# Take 2nd conversion again, AND out lowest 4 bits and shift 4 to the left
# Take 3rd of 4, get base64 conversion, AND final 4 bits out,  shift to lowest places and OR with 2nd
# Take 3rd conversion again, AND out lowest 4 bits and shift
