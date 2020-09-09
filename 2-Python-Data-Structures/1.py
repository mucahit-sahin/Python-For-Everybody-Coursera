text = "X-DSPAM-Confidence:    0.8475"
a=text.find(":")
sayi=text[a+1:]
sayi=sayi.strip()
sayi=float(sayi)
print(sayi)
