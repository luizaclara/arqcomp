goto main
wb 0

r ww 0
base ww 4
exp ww 5

main xmem x, base # x <- mem[base]
     ymem y, exp # y <- mem[exp]
     hgetone # h <- 1
     jzy y, return0 # se y=0 entao goto return0
     hgety # h <- y
     ygetx # y <- x
 pot hdecone # h <- h - 1
     jzh h, return1 # se h=0 entao goto return1
     xprody # x <- x*y
     goto pot # loop
return0 movh h, r # mem[r] <- h
        halt # retorno expoente zero
return1 movx x, r # mem[r] <- x
        halt # retorno calculado da potencia
    