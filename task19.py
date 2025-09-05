letters = ["h", "e", "l", "l", "o", "w", "O", "r", "l", "d"]
unli_harf = 0
unlilar = ["a", "e", "i", "o", "u"]

for harf in letters:
    if harf.lower() in unlilar:
        unli_harf += 1

print(unli_harf)