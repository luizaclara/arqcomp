goto main
wb 0

a ww 4 
b ww 1
c ww 4
r ww 0 # saida retorno

main xmem x, a # x <- mem[a]
     ymem y, c # y <- mem[c]
     hmem h, b # h <- mem[b]
     jzxequalsy x, jump # se (x=y) entao goto jump
     movy y, a # mem[a] <- y // a = c
     hgetone # h <- 1
     movh h, r # mem[r] <- h
     halt # retorno 1
jump movh h, c # mem[c] <- h // c = b
     halt # retorno 0