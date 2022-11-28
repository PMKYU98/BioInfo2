def PARSE(fInput, delimiter=' '):
    with open(fInput, 'r') as f:
        fThreshold = float(f.readline().strip())
        f.readline()
        Alphabet = [character for character in f.readline().strip().split(delimiter) if character != '']
        f.readline()

        lines = f.readlines()
        lstAlign = [line.strip() for line in lines]

        return fThreshold, Alphabet, lstAlign


inputfile = '221129/221129_Q5_input1.txt'
fThreshold, Alphabet, lstAlign = PARSE(inputfile)
print(fThreshold)
print(Alphabet)
print(lstAlign)