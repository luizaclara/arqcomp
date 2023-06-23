goto main
wb 0

r ww 0 # saida resultado
n ww 7 # entrada

main xmem x, n # x <- mem[n]
     jzx x, return0 # se x=0 entao goto return0
     ymem y, n # y <- mem[n]
     ydecone # y <- y - 1
     jzy y, return0 # se y=0 entao goto return0

 fat xprody # x <- x*y
     ydecone # y <- y - 1
     jzy y, return1 # se y=0 entao goto return1
     goto fat # loop

return0 hgetone # h <- 1
        movh h, r # mem[r] <- h
        halt # resultado 1 (quando n eh 0 ou 1)
return1 movx x, r # mem[r] <- x
        halt # resultado calculado n!