N = int(input())
l = list(input())



R_c = l.count("R")
w_count = l[:R_c].count("W")

print(min(R_c,N-R_c,w_count))


#https://note.com/nanigashi/n/n509d0d9b757c
