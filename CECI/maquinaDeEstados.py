#import numpy as np

arq = open('entrada.txt', 'r')
ler = arq.readlines()
#print(ler)
i = 0
clk = 0
rst = 0
state = 0
while (i < len(ler)):
    string = ler[i]
    opcode = string[2:8]
    #print (opcode)
    funct = string[9:15]
    #print (funct)
    strOpcode = ''

    #Parte do código para saber qual e a operacao
    if(opcode == '100011'):
        strOpcode = "LW"
    elif(opcode == '101011'):
        strOpcode = "SW"
    elif(opcode == '000000'):
        if (funct == '101010'):
            strOpcode = 'SLT'
        elif (funct == '100110'):
            strOpcode = 'XOR'
        elif(funct == '100111'):
            strOpcode = 'NOR'
        elif (funct == '100101'):
            strOpcode = 'OR'
        elif(funct == '100100'):
            strOpcode = 'AND'
        elif(funct == '100010'):
            strOpcode = "SUB"
        elif (funct == "100000"):
            strOpcode = "ADD"
    elif (opcode == '001000'):
        strOpcode = 'ADDI'
    elif (opcode == '001101'):
        strOpcode = 'ORI'
    #elif (opcode = '001110')
    #    strOpcode = 'NORI'
    elif (opcode == '001110'):
        strOpcode = 'XORI'
    elif(opcode == '001010'):
        strOpcode = 'STLI'
    elif (opcode == '000100'):
        strOpcode = 'BEQ'
    elif(opcode == '000101'):
        strOpcode = 'BNE'
    elif(opcode == '000010'):
        strOpcode = 'J'

    #final dessa parte


    if (string[rst] == '1'):
        state = 0
    elif (clk == 1 and string[rst] == '0'):
        state = state + 1
        #if (state == 4):
            #state = 0




    if (clk == 0):  #Parte do clock
        clk = 1
    elif (clk == 1):
        clk = 0

    print ("clock = ", clk, "| reset = ", string[rst], "| opcode = ", strOpcode, "| state = ", state)
    i = i + 1
arq.close()