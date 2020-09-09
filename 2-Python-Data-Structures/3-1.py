
fname = input("Enter file name: ")
fh = open(fname)
print(fh.read().upper().strip())