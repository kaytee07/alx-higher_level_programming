for letter in range(97, 123):
    asciiToAlpha = chr(letter)
    if asciiToAlpha == "e" or asciiToAlpha == "q":
        continue
    print(f"{asciiToAlpha}", end="")
