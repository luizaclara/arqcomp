import memory
from array import array

MPC = 0
MIR = 0

#registradores
MAR = 0
MDR = 0
PC = 0
MBR = 0

X = 0
Y = 0
H = 0
A = 0
B = 0

#saída da ALU
N = 0
Z = 1

#barramentos
BUS_A = 0
BUS_B = 0
BUS_C = 0

firmware = array('Q', [0]) * 512

#main: PC <- PC + 1; MBR <- read_byte(PC); GOTO MBR
firmware[0] =  0b000000000100001100101000010000010001

#goto address
##9: PC <- PC + 1; fetch; GOTO 10
firmware[9] =  0b000001010000001100101000010000010001
##10: PC <- MBR; fetch; GOTO MBR
firmware[10] = 0b000000000100000100100000010000010010

### REGISTRADOR X ###
#X = X + mem[address]
##2: PC <- PC + 1; MBR <- read_byte(PC); GOTO 3
firmware[2] =  0b000000011000001100101000010000010001
##3: MAR <- MBR; read_word; GOTO 4
firmware[3] =  0b000000100000000100100001000000100010
##5: X <- MDR + X; GOTO 0
firmware[4] =  0b000000000000001101100000001000000101  

#X = X - mem[address]
##13: PC <- PC + 1; fetch; goto 14
firmware[13] = 0b000001110000001100101000010000010001
##14: MAR <- MBR; read; goto 15
firmware[14] = 0b000001111000000100100001000000100010
##16: X <- X - MDR; goto 0
firmware[15] = 0b000000000000001101111000001000000101

#X = mem[address]
##17: PC <- PC + 1; MBR <- read_byte(PC); GOTO 18
firmware[17] = 0b000010010000001100101000010000010001
##18: MAR <- MBR; read_word; GOTO 19
firmware[18] = 0b000010011000000100100001000000100010
##19: X <- MDR; GOTO 0
firmware[19] = 0b000000000000000101000000001000000000

#mem[address] = X
##6: PC <- PC + 1; fetch; GOTO 7
firmware[6] =  0b000000111000001100101000010000010001
##7: MAR <- MBR; GOTO 8
firmware[7] =  0b000001000000000100100001000000000010
##8: MDR <- X; write; GOTO 0
firmware[8] =  0b000000000000000100100000100001000011

#if X = 0 then goto address
## 11: X <- X; IF ALU = 0 GOTO 268 (100001100) ELSE GOTO 12(000001100)
firmware[11] = 0b000001100001000100100000001000000011
## 12: PC <- PC + 1; GOTO 0
firmware[12] = 0b000000000000001100101000010000000001
## 268: GOTO 9
firmware[268] =0b000001001000000000000000000000000000



### REGISTRADOR Y ###
#Y = mem[address]
##20: PC <- PC + 1; MBR <- read_byte(PC); GOTO 21
firmware[20] = 0b000010101000001100101000010000010001
##21: MAR <- MBR; read_word; GOTO 22
firmware[21] = 0b000010110000000100100001000000100010
##22: Y <- MDR; GOTO 0
firmware[22] = 0b000000000000000101000000000100000000

#Y = Y - mem[address]
##23: PC <- PC + 1; fetch; goto 24
firmware[23] = 0b000011000000001100101000010000010001
##24: MAR <- MBR; read; goto 25
firmware[24] = 0b000011001000000100100001000000100010
##25: Y <- Y - MDR; goto 0
firmware[25] = 0b000000000000001101111000000100000110

#Y = Y + mem[address]
##23: PC <- PC + 1; fetch; goto 24
firmware[27] = 0b000011100000001100101000010000010001
##24: MAR <- MBR; read; goto 25
firmware[28] = 0b000011101000000100100001000000100010
##25: Y <- Y + MDR; goto 0
firmware[29] = 0b000000000000001101100000000100000110

#mem[address] = Y
##50: PC <- PC + 1; fetch; GOTO 51
firmware[50] =  0b000110011000001100101000010000010001
##51: MAR <- MBR; GOTO 52
firmware[51] =  0b000110100000000100100001000000000010
##52: MDR <- Y; write; GOTO 0
firmware[52] =  0b000000000000000100100000100001000110

#if Y = 0 then goto address
## 48: Y <- Y; IF ALU = 0 GOTO 305 (100110001) ELSE GOTO 49(000110001)
firmware[48] = 0b000110001001000100100000000100000100
## 49: PC <- PC + 1; GOTO 0
firmware[49] = 0b000000000000001100101000010000000001
## 305: GOTO 9
firmware[305] =0b000001001000000000000000000000000000



### ATRIBUIÇÕES SIMPLES ###
#X = 0
firmware[34] = 0b000000000000000100000000001000000000

#Y = 0
firmware[35] = 0b000000000000000100000000000100000000

#X = 1
firmware[124] = 0b000000000000001100001000001000000000

#Y = 1
firmware[125] = 0b000000000000001100001000000100000000

#X = X + 1
firmware[113] =  0b000000000000001100101000001000000011

#X = X - 1
firmware[114] =  0b000000000000001100110000001000000011

#Y = Y + 1
firmware[115] =  0b000000000000001100101000000100000100

#Y = Y - 1
firmware[116] =  0b000000000000001100110000000100000100

#Y = X
firmware[37] = 0b000000000000000101000000000100000111

#X = Y
firmware[26] = 0b000000000000000100100000001000000111

#X = X + Y
firmware[30] = 0b000000000000001101100000001000000111

#H = H + 1
firmware[38] = 0b000000000000001101001000000010000001

#H = H - 1
firmware[39] = 0b000000000000001100110000000010000000

#H = X
firmware[61] = 0b000000000000000100100000000010000011

#H = Y
firmware[62] = 0b000000000000000100100000000010000100

#H = 0
firmware[63] = 0b000000000000000100000000000010000000

#H = 1
firmware[129] = 0b000000000000001100001000000010000000


### REGISTRADOR H ###
#H = mem[address]
##64: PC <- PC + 1; MBR <- read_byte(PC); GOTO 18
firmware[64] = 0b001000001000001100101000010000010001 
##65: MAR <- MBR; read_word; GOTO 19
firmware[65] = 0b001000010000000100100001000000100010
##66: H <- MDR; GOTO 0
firmware[66] = 0b000000000000000101000000000010000000

#mem[address] = H
##135: PC <- PC + 1; fetch; GOTO 136
firmware[135] =  0b010001000000001100101000010000010001
##136: MAR <- MBR; GOTO 137
firmware[136] =  0b010001001000000100100001000000000010
##137: MDR <- H; write; GOTO 0
firmware[137] =  0b000000000000000100100000100001000000

#if H = 0 then goto address
##127: H <- H; IF ALU = 0 GOTO 384 ELSE GOTO 49(000110001)
firmware[127] = 0b010000000001000100100000000010000000
##384: GOTO 9 
firmware[384] = 0b000001001000000000000000000000000000
##128 : PC <- PC + 1; GOTO 0
firmware[128] = 0b000000000000001100101000010000000001



### USANDO MAIOR QUE ALU ###
#if not(X > Y) then goto address
## 57: A <- X > Y; IF ALU = 0 GOTO 313 () ELSE GOTO 58(000111010)
firmware[57] = 0b000111010001000011100100000000000111
## 314: GOTO 9
firmware[314] =0b000001001000000000000000000000000000
## 58: PC <- PC + 1; GOTO 0
firmware[58] = 0b000000000000001100101000010000000001

#if A = H > Y; A = 0 then goto address
##132: A <- H > Y; IF ALU = 0 GOTO 384 ELSE GOTO 49(000110001)
firmware[132] = 0b010000101001000011100100000000000100
##384: GOTO 9 
firmware[389] = 0b000001001000000000000000000000000000
##128 : PC <- PC + 1; GOTO 0
firmware[133] = 0b000000000000001100101000010000000001


### USANDO IGUAL ALU ###
#if (X == Y) then goto address
##130: A <- X = Y; IF ALU = 1 GOTO 384 ELSE GOTO 49(000110001)
firmware[130] = 0b010000011010001111100100000000000111
##387: GOTO 9 
firmware[387] = 0b000001001000000000000000000000000000
##131 : PC <- PC + 1; GOTO 0
firmware[131] = 0b000000000000001100101000010000000001


### MULTIPLICAÇÃO ###
#X = X * mem[address]
##40: PC <- PC + 1; fetch; goto 41
firmware[40] = 0b000101001000001100101000010000010001
##41: MAR <- MBR; read; goto 42
firmware[41] = 0b000101010000000100100001000000100010
##42: B <- (MDR > X); IF Y != 0 GO TO 299 (100101011); ELSE GO TO 43
firmware[42] = 0b000101011010000011100010000000000101
##299: B <- X; GO TO 300 (100101100)
firmware[299] =0b100101100000000101000010000000000111
##299: X <- MDR; GO TO 44 
firmware[300] =0b000101100000000101000000001000000101
##43: B <- MDR; goto 44
firmware[43] = 0b000101100000000101000010000000000110
##44: A <- X; goto 45
firmware[44] = 0b000101101000000100100100000000000011 
##45: X <- 0; goto 46
firmware[45] = 0b000101110000000100000000001000000011
##46: IF B != 0 GO TO 303(100110000); ELSE GOTO 47 (HAULT)
firmware[46] = 0b000101111010000100100010000000000100
#47: GOTO MAIN;
firmware[47] = 0b000000000000000100100000001000000011
##303: X <- X + A; goto 304
firmware[303] =0b100110000000001101100000001000001010
##304: B <- B - 1; goto 45
firmware[304] =0b000101110000001100110010000000001001

#Y = Y * mem[address]
##73: PC <- PC + 1; fetch; goto 74
firmware[73] =  0b001001010000001100101000010000010001
##74: MAR <- MBR; read; goto 75
firmware[74] =  0b001001011000000100100001000000100010
##75: A <- (MDR > Y); IF X != 0 GO TO 332 (101001100); ELSE GO TO 76
firmware[75] =  0b001001100010000011100100000000000110
##332: A <- Y; GO TO 300 (100101100)
firmware[332] = 0b101001101000000100100100000000000111
##333: Y <- MDR; GO TO 77 
firmware[333] = 0b001001101000000101000000000100000110
##76: A <- MDR; goto 77
firmware[76] =  0b001001101000000101000100000000000101
##77: B <- Y; goto 78
firmware[77] =  0b001001110000000100100010000000000100 
##78: Y <- 0; goto 79
firmware[78] =  0b001001111000000100000000000100000100
##79: IF A == 0 GO TO 336(100110000); ELSE GOTO 80 (HALT)
firmware[79] =  0b001010000010000100100100000000001000
#80: GOTO MAIN;
firmware[80] =  0b000000000000000100100000000100000100
##336: Y <- Y + B; goto 337
firmware[336] = 0b101010001000001101100000000100001101
##337: A <- A - 1; goto 79
firmware[337] = 0b001001111000001100110100000000001000

#X = X * Y
##117: A = X > Y; IF A = 1 GOTO 374; ELSE GOTO 118
firmware[117] = 0b001110110001000011100100000000000111
##374: A = Y GO TO 375
firmware[374] = 0b101110111000000100100100000000000100
##375: B = X; GO TO 120
firmware[375] = 0b001111000000000101000010000000000111
##118: A = X; goto 119
firmware[118] = 0b001110111000000100100100000000000011
##119: B = Y; goto 120
firmware[119] = 0b001111000000000100100010000000000100 
##119: X = 0; goto 121
firmware[120] = 0b001111001000000100000000001000000011 
##120: B = B; IF Y = 0; goto 377 ELSE GOTO 122
firmware[121] = 0b001111010001000100100010000000001001
##377 X = X; GO TO 0
firmware[378] = 0b000000000000000100100000001000000011
##121 B = B - 1; GO TO 123
firmware[122] = 0b001111011000001100110010000000001001
##122 X = A + X
firmware[123] = 0b001111001000001101100000001000001010

#halt:
firmware[255] = 0b000000000000000000000000000000000000 

#leitura registradores nos barramentos A e B
def read_regs(reg_num):

	global MDR, PC, MBR, X, Y, H, A, B, BUS_A, BUS_B
	
	BUS_A = H

	if reg_num == 0:
		BUS_A = MDR
		BUS_B = H
	elif reg_num == 1:
		BUS_B = PC
	elif reg_num == 2:
		BUS_B = MBR
	elif reg_num == 3:
		BUS_B = X
	elif reg_num == 4:
		BUS_B = Y
	elif reg_num == 5:
		BUS_A = MDR
		BUS_B = X
	elif reg_num == 6:
		BUS_A = MDR
		BUS_B = Y	
	elif reg_num == 7:
		BUS_A = X
		BUS_B = Y
	elif reg_num == 8:
		BUS_B = A
	elif reg_num == 9:
		BUS_B = B
	elif reg_num == 10:
		BUS_A = X
		BUS_B = A
	elif reg_num == 11:
		BUS_A = X
		BUS_B = B
	elif reg_num == 12:
		BUS_A = Y
		BUS_B = A
	elif reg_num == 13:
		BUS_A = Y
		BUS_B = B
	elif reg_num == 14:
		BUS_A = MDR
		BUS_B = A
	elif reg_num == 15:
		BUS_A = MDR
		BUS_B = B
	else:
		BUS_B = 0

	# global MDR, PC, MBR, X, Y, H, BUS_A, BUS_B
	
	# BUS_A = H
	
	# if reg_num == 0:
	# 	BUS_B = MDR
	# elif reg_num == 1:
	# 	BUS_B = PC
	# elif reg_num == 2:
	# 	BUS_B = MBR
	# elif reg_num == 3:
	# 	BUS_B = X
	# elif reg_num == 4:
	# 	BUS_B = Y
	# else:
	# 	BUS_B = 0

#escrita nos registradores pelo barramento C		
def write_regs(reg_bits):
	global MAR, MDR, PC, X, Y, H, A, B, BUS_C
	if reg_bits & 0b10000000:
		A = BUS_C
	if reg_bits & 0b01000000:
		B = BUS_C
	if reg_bits & 0b00100000:
		MAR = BUS_C
	if reg_bits & 0b00010000:
		MDR = BUS_C
	if reg_bits & 0b00001000:
		PC = BUS_C
	if reg_bits & 0b00000100:
		X = BUS_C
	if reg_bits & 0b00000010:
		Y = BUS_C
	if reg_bits & 0b00000001:
		H = BUS_C

	# global MAR, MDR, PC, X, Y, H, BUS_C

	# if reg_bits & 0b100000:
	# 	MAR = BUS_C
	# if reg_bits & 0b010000:
	# 	MDR = BUS_C
	# if reg_bits & 0b001000:
	# 	PC = BUS_C
	# if reg_bits & 0b000100:
	# 	X = BUS_C
	# if reg_bits & 0b000010:
	# 	Y = BUS_C
	# if reg_bits & 0b000001:
	# 	H = BUS_C

#operações da ALU
def alu(control_bits):
	global N, Z, BUS_A, BUS_B, BUS_C
	
	a = BUS_A
	b = BUS_B
	o = 0
	
	shift_bits = control_bits & 0b110000000
	shift_bits = shift_bits >> 7
	
	control_bits = control_bits & 0b001111111
	
	if control_bits == 	 0b0101000:
		o = a
	elif control_bits == 0b0100100:
		o = b
	elif control_bits == 0b0101010:
		o = ~a
	elif control_bits == 0b1001100:
		o = ~b
	elif control_bits == 0b1101100:
		o = a + b
	elif control_bits == 0b1101101:
		o = a + b + 1
	elif control_bits == 0b1101001:
		o = a + 1
	elif control_bits == 0b1100101:
		o = b + 1
	elif control_bits == 0b1101111:
		o = b - a
	elif control_bits == 0b1100110:
		o = b - 1
	elif control_bits == 0b1101011:
		o = -a
	elif control_bits == 0b0001100:
		o = a & b
	elif control_bits == 0b0101100:
		o = a | b
	elif control_bits == 0b0100000:
		o = 0
	elif control_bits == 0b1100001:
		o = 1
	elif control_bits == 0b1100010:
		o = -1
	elif control_bits == 0b0011100:
		o = int(a>b) 
	elif control_bits == 0b1111100:
		o = int(a == b)
	
	if o == 0:
		N = 0
		Z = 1
	else:
		N = 1
		Z = 0
	
	if shift_bits == 0b01:
		o = o << 1
	elif shift_bits == 0b10:
		o = o >> 1
	elif shift_bits == 0b11:
		o = o << 8
		
	BUS_C = o
	
	# global N, Z, BUS_A, BUS_B, BUS_C
	
	# a = BUS_A
	# b = BUS_B
	# o = 0
	
    # #bits de deslocamento
	# shift_bits = control_bits & 0b11000000
	# shift_bits = shift_bits >> 6
	
    # #bits de operação da ALU
	# control_bits = control_bits & 0b00111111
	
	# if control_bits == 0b011000:
	# 	o = a
	# elif control_bits == 0b010100:
	# 	o = b
	# elif control_bits == 0b011010:
	# 	o = ~a
	# elif control_bits == 0b101100:
	# 	o = ~b
	# elif control_bits == 0b111100:
	# 	o = a + b
	# elif control_bits == 0b111101:
	# 	o = a + b + 1
	# elif control_bits == 0b111001:
	# 	o = a + 1
	# elif control_bits == 0b110101:
	# 	o = b + 1
	# elif control_bits == 0b111111:
	# 	o = b - a
	# elif control_bits == 0b110110:
	# 	o = b - 1
	# elif control_bits == 0b111011:
	# 	o = -a
	# elif control_bits == 0b001100:
	# 	o = a & b
	# elif control_bits == 0b011100:
	# 	o = a | b
	# elif control_bits == 0b010000:
	# 	o = 0
	# elif control_bits == 0b110001:
	# 	o = 1
	# elif control_bits == 0b110010:
	# 	o = -1
		
	# if o == 0:
	# 	N = 0
	# 	Z = 1
	# else:
	# 	N = 1
	# 	Z = 0
	
	# if shift_bits == 0b01:
	# 	o = o << 1
	# elif shift_bits == 0b10:
	# 	o = o >> 1
	# elif shift_bits == 0b11:
	# 	o = o << 8
		
	# BUS_C = o
	
#definindo a prox instrução no MPC
def next_instruction(next, jam):
	global MPC, MBR, N, Z
	
	if jam == 0b000:
		MPC = next 
		return
		
	if jam & 0b001: #JAMZ
		next = next | (Z << 8)
	
	if jam & 0b010: #JAMN
		next = next | (N << 8)
		
	if jam & 0b100: #JMPC
		next = next | MBR
		
	MPC = next

#manipulação de memória	
def memory_io(mem_bits):
	global PC, MBR, MDR, MAR
	
	if mem_bits & 0b001: #fetch
		MBR = memory.read_byte(PC)

	if mem_bits & 0b010: #leitura
		MDR = memory.read_word(MAR)
		
	if mem_bits & 0b100: #escrita
		memory.write_word(MAR, MDR)
		
def step():
	global MIR, MPC
	
	MIR = firmware[MPC]
	
	if MIR == 0:
		return False
		
	read_regs       ( MIR & 0b000000000000000000000000000000001111)
	alu             ((MIR & 0b000000000000111111111000000000000000) >> 15)
	write_regs      ((MIR & 0b000000000000000000000111111110000000) >> 7)
	memory_io       ((MIR & 0b000000000000000000000000000001110000) >> 4)
	next_instruction((MIR & 0b111111111000000000000000000000000000) >> 27, (MIR & 0b000000000111000000000000000000000000) >> 24)
	
	# read_regs       ( MIR & 0b00000000000000000000000000000111)
	# alu             ((MIR & 0b00000000000011111111000000000000) >> 12)
	# write_regs      ((MIR & 0b00000000000000000000111111000000) >> 6)
	# memory_io       ((MIR & 0b00000000000000000000000000111000) >> 3)
	# next_instruction((MIR & 0b11111111100000000000000000000000) >> 23, (MIR & 0b00000000011100000000000000000000) >> 20)
	
	return True