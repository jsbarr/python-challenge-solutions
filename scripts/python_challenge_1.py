shift = 2

def char_shift(char, shift):
    code = ord(char) + shift
    if code > ord('z'): code -= 26
    return chr(code)

#text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq gq pcamkkclbcb. lmu ynnjw ml rfc spj."
text = "map"

def shift_cipher(string, shift):
    words = string.split(" ")
    return " ".join(["".join([char_shift(char, shift) for char in word]) for word in words])

print(shift_cipher(text, shift))

# OCR