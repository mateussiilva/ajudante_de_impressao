






LEN_PLACAS = 150
MEDIDA = "307 x300".split("x")
width = int(MEDIDA[0])
height = int(MEDIDA[1])




def metros_linear(width,altura):
    x = width / LEN_PLACAS 
    metros_linear = x * altura
    return metros_linear
    


print(metros_linear(1200,2))
# print(width % LEN_PLACAS)