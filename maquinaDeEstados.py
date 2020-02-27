arq = open('entrada.txt', 'r')
ler = arq.readlines()
# print(ler)
i = 0
clk = 1
rst = 0
state = 0


limparRes = open('maquinaDeEstados.tv', 'w')
inicio = limparRes.write('RST_OPCODE_FUNCT_STATE\n')
limparRes.close()

'''def imprimir():  # Funcao para imprimir
    print("clock = ", clk, "| reset = ",
          string[rst], "| opcode = ", strOpcode, "| state = ", state)'''


# Funcao para adicionar no arquivo maquinaDeEstados.tv os resultados esperados
def resultados(rst, opcode, funct, state):
    # s = 'clock = {}| reset = {}| operacao = {}| state = {}\n'.format(
    #    clk, rst, opcode, state)
    s = '{}_{}_{}_{}\n'.format(
        rst, opcode, funct, state)
    adicionar = open('maquinaDeEstados.tv', 'a')
    esc = adicionar.write(s)


while (i < len(ler)):

    string = ler[i]
    opcode = string[2:8]
    funct = string[9:15]
    strOpcode = ''
    if (state == 0):  # Passa do estado 0 pro 1
        state = 1
    if (clk == 0):  # Parte do clock
        clk = 1
    else:
        clk = 0
    # Parte do código para saber qual e a operacao
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
    # elif (opcode = '001110')
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

    # final dessa parte

    if (string[rst] == '1'):
        state = 0
        resultados(rst, opcode, funct, state)
        state = 1
    elif (clk == 1 and string[rst] == '0'):
        if (opcode[0:2] == '10' or opcode[0:3] == '001' or opcode[0:4] == '0001'):  # LW ou SW
            # Instrucao do tipo I
            state = 2
            if (strOpcode == 'LW'):
                state = 3
                resultados(rst, opcode, funct, state)
                state = 4
                resultados(rst, opcode, funct, state)
                state = 0
            elif (strOpcode == 'SW'):
                state = 5
                resultados(rst, opcode, funct, state)
                state = 0
            elif (strOpcode == 'BEQ'):
                state = 8
                resultados(rst, opcode, funct, state)
                state = 0
            elif (strOpcode == 'ADDI'):
                state = 9
                resultados(rst, opcode, funct, state)
                state = 10
        elif (opcode == '000000'):
            # Instrucao do tipo R
            state = 6
            resultados(rst, opcode, funct, state)
            state = 7
        elif (opcode == '000010'):
            # Instrucao do tipo J
            state = 11
            resultados(rst, opcode, funct, state)
            state = 0
    #resultados(rst, opcode, funct, state)
    resultados(rst, opcode, funct, state)
    i = i + 1
arq.close()
