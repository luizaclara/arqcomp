import sys

fsrc = open(str(sys.argv[1]), 'r')

lines = []
lines_bin = []
names = []

instructions = ['goto',
                'addx',
                'subx',
                'xmem',
                'movx',
                'jzx',
                'ymem',
                'suby',
                'addy',
                'movy',
                'jzy',
                'xgetzero',
                'ygetzero',
                'xgetone', 
                'ygetone',
                'xincone',
                'xdecone',
                'yincone',
                'ydecone',
                'ygetx',
                'xgety',
                'xincy',
                'hincone',
                'hdecone',
                'hgetx',
                'hgety',
                'hgetzero',
                'hgetone',
                'hmem',
                'movh',
                'jzh',
                'xprodmem',
                'yprodmem',
                'xprody',
                'jzxgthany',
                'jzxequalsy',
                'jzhgthany',
                'halt', 
                'wb', 
                'ww'
               ]

instruction_set = {'goto'          : 0x09, # goto address
                   'addx'          : 0x02, # x = x + mem
                   'subx'          : 0x0D, # x = x - mem
                   'xmem'          : 0x11, # x = mem
                   'movx'          : 0x06, # mem = x
                   'jzx'           : 0x0B, # if X = 0 goto address
                   'ymem'          : 0x14, # y = mem 
                   'suby'          : 0x17, # y = y - mem
                   'addy'          : 0x1B, # y = y + mem
                   'movy'          : 0x32, # mem = y 
                   'jzy'           : 0x30, # if Y = 0 then goto address
                   'xgetzero'      : 0x22, # X = 0
                   'ygetzero'      : 0x23, # Y = 0
                   'xgetone'       : 0x7C, # X = 1 
                   'ygetone'       : 0x7D, # Y = 1
                   'xincone'       : 0x71, # X = X + 1
                   'xdecone'       : 0x72, # X = X - 1
                   'yincone'       : 0x73, # Y = Y + 1
                   'ydecone'       : 0x74, # Y = Y - 1
                   'ygetx'         : 0x25, # Y = X
                   'xgety'         : 0x1A, # X = Y 
                   'xincy'         : 0x1E, # X = X + Y 
                   'hincone'       : 0x26, # H = H + 1
                   'hdecone'       : 0x27, # H = H - 1
                   'hgetx'         : 0x3D, # H = X
                   'hgety'         : 0x3E, # H = Y
                   'hgetzero'      : 0x3F, # H = 0
                   'hgetone'       : 0x81, # H = 1
                   'hmem'          : 0x40, # H = mem
                   'movh'          : 0x87, # mem = H 
                   'jzh'           : 0x7F, # if H = 0 then goto address
                   'xprodmem'      : 0x28, # X = X * mem[address]
                   'yprodmem'      : 0x49, # Y = Y * mem[address]
                   'xprody'        : 0x75, # X = X*Y
                   'jzxgthany'     : 0x39, # if not(X > Y) then goto address
                   'jzxequalsy'    : 0x82, # if X == Y goto address
                   'jzhgthany'     : 0x84, # if H > Y goto address
                   'halt'          : 0xFF  # halt
                  }

def is_instruction(str):
   global instructions
   inst = False
   for i in instructions:
      if i == str:
         inst = True
         break
   return inst
   
def is_name(str):
   global names
   name = False
   for n in names:
      if n[0] == str:
         name = True
         break
   return name
   
def encode_2ops(inst, ops):
   line_bin = []
   if len(ops) > 1:
      if ops[0] == 'x' or ops[0] == 'y' or ops[0] == 'h':
         if is_name(ops[1]):
            line_bin.append(instruction_set[inst])
            line_bin.append(ops[1])
   return line_bin

def encode_0ops(inst):
   line_bin = []
   line_bin.append(instruction_set[inst])
   return line_bin

def encode_goto(ops):
   line_bin = []
   if len(ops) > 0:
      if is_name(ops[0]):
         line_bin.append(instruction_set['goto'])
         line_bin.append(ops[0])
   return line_bin
   
def encode_wb(ops):
   line_bin = []
   if len(ops) > 0:
      if ops[0].isnumeric():
         if int(ops[0]) < 256:
            line_bin.append(int(ops[0]))
   return line_bin   

def encode_ww(ops):
   line_bin = []
   if len(ops) > 0:
      if ops[0].isnumeric():
         val = int(ops[0])
         if val < pow(2,32):
            line_bin.append(val & 0xFF)
            line_bin.append((val & 0xFF00) >> 8)
            line_bin.append((val & 0xFF0000) >> 16)
            line_bin.append((val & 0xFF000000) >> 24)
   return line_bin
      
def encode_instruction(inst, ops):
   if (inst == 'addx' or 
       inst == 'addy' or 
       inst == 'movx' or
       inst == 'movy' or
       inst == 'xmem' or
       inst == 'ymem' or
       inst == 'hmem' or
       inst == 'suby' or
       inst == 'subx' or
       inst == 'xprodmem' or
       inst == 'yprodmem' or
       inst == 'jzy' or
       inst == 'jzxgthany'or
       inst == 'jzh' or
       inst == 'jzx' or 
       inst == 'movh' or
       inst == 'jzxequalsy' or
       inst == 'jzhgthany'):
       return encode_2ops(inst, ops)
   elif (inst == 'xgety' or
         inst == 'ygetx' or
         inst == 'xincy' or
         inst == 'xgetzero' or
         inst == 'ygetzero' or
         inst == 'hincone' or
         inst == 'hdecone' or
         inst == 'hgetx' or
         inst == 'hgety' or
         inst == 'hgetzero' or
         inst == 'ydecone' or 
         inst == 'xdecone' or
         inst == 'yincone' or
         inst == 'xincone' or
         inst == 'xprody' or
         inst == 'xgetone' or
         inst == 'ygetone' or
         inst == 'hgetone'):
         return encode_0ops(inst) 
   elif inst == 'goto':
      return encode_goto(ops)
   elif inst == 'halt':
      return encode_0ops('halt') 
   elif inst == 'wb':
      return encode_wb(ops)
   elif inst == 'ww':
      return encode_ww(ops)
   else:
      return []
   
   
def line_to_bin_step1(line):
   line_bin = []
   if is_instruction(line[0]):
      line_bin = encode_instruction(line[0], line[1:])
   else:
      line_bin = encode_instruction(line[1], line[2:])
   
   return line_bin
   
def lines_to_bin_step1():
   global lines
   for line in lines:
      line_bin = line_to_bin_step1(line)
      if line_bin == []:
         print("Erro de sintaxe na linha ", lines.index(line))
         return False
      lines_bin.append(line_bin)
   return True

def find_names():
   global lines
   for k in range(0, len(lines)):
      is_label = True
      for i in instructions:
          if lines[k][0] == i:
             is_label = False
             break
      if is_label:
         names.append((lines[k][0], k))
         
def count_bytes(line_number):
   line = 0
   byte = 1
   while line < line_number:
      byte += len(lines_bin[line])
      line += 1
   return byte

def get_name_byte(str):
   for name in names:
      if name[0] == str:
         return name[1]
         
def resolve_names():
   for i in range(0, len(names)):
      names[i] = (names[i][0], count_bytes(names[i][1]))
   for line in lines_bin:
      for i in range(0, len(line)):
         if is_name(line[i]):
            if (line[i-1] == instruction_set['addx'] or 
                line[i-1] == instruction_set['addy'] or 
                line[i-1] == instruction_set['movx'] or
                line[i-1] == instruction_set['movy'] or
                line[i-1] == instruction_set['xmem'] or
                line[i-1] == instruction_set['ymem'] or
                line[i-1] == instruction_set['hmem'] or
                line[i-1] == instruction_set['movh'] or
                line[i-1] == instruction_set['subx'] or
                line[i-1] == instruction_set['suby']):
               line[i] = get_name_byte(line[i])//4
            else:
               line[i] = get_name_byte(line[i])

for line in fsrc:
   tokens = line.replace('\n','').replace(',','').lower().split(" ")
   i = 0
   while i < len(tokens):
      if tokens[i] == '':
         tokens.pop(i)
         i -= 1
      i += 1
   if len(tokens) > 0:
      lines.append(tokens)
   
find_names()
if lines_to_bin_step1():
   resolve_names()
   byte_arr = [0]
   for line in lines_bin:
      for byte in line:
         byte_arr.append(byte)
   fdst = open(str(sys.argv[2]), 'wb')
   fdst.write(bytearray(byte_arr))
   fdst.close()

fsrc.close()