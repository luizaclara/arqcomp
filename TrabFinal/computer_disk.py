import ufc2x as cpu
import sys
import memory as mem
import clock as clk 
import disk

questao = str(sys.argv[1])
disk.read(questao)
clk.start([cpu])

if questao == 'q1.bin':
    print("Resultado da Potencia: ", mem.read_word(1))

elif questao == 'q3.bin':
    print("a: ", mem.read_word(1))
    print("b: ", mem.read_word(2))
    print("c: ", mem.read_word(3))
    print("r: ", mem.read_word(4))

elif questao == 'q4.bin':
    print("Resultado do Fatorial: ", mem.read_word(1))


