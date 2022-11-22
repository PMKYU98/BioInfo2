def PARSE(fInput):
    with open(fInput, 'r') as f:
        sInput = f.readline().strip()

    return sInput

inputfile = '221122/221122_Q2_input1.txt'
sInput = PARSE(inputfile)
print(sInput)