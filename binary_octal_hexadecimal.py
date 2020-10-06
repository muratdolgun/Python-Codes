print("""
            Girdiğiniz sayının
            ikili, sekizli ve onaltılı
            sayı sistemlerindeki karşılığını bulacağım.\n   """)
binary=[]
binary_son=[]
binary_octal_gecis=[]
octal=[]
binary_hex_gecis=[]
hexadecimal=[]
sayi=int(input("Bir sayı giriniz:"))
while sayi>3:
    binary.append(sayi%2)
    sayi=sayi//2
if sayi==3 or sayi==2:
    binary.append(sayi%2)
    binary.append(sayi//2)
print("İkili Sayı Sistemindeki karşılığı:",end="")
for i in binary[::-1]:
    binary_son.append(i)
    print(i,end="")
a=len(binary_son)
print("\nSekizli Sayı Sistemindeki karşılığı:",end="")
if a<3:
    if a==2:
        octal[0]=binary_son[1]+binary_son[0]*2
    elif a==1:
        octal[0]=binary_son[0]
    print(octal[0])
else:
    if a%3==0:
        for k in range(0,a,3):
            binary_octal_gecis.append(binary_son[a-(k+1)]+binary_son[a-(k+2)]*2+binary_son[a-(k+3)]*4)
    elif a%3==2:
        for k in range(0,a-2,3):
           binary_octal_gecis.append(binary_son[a-(k+1)]+binary_son[a-(k+2)]*2+binary_son[a-(k+3)]*4)
        binary_octal_gecis.append(binary_son[1]+binary_son[0]*2)
    elif a%3==1:
        for k in range(0,a-1,3):
            binary_octal_gecis.append(binary_son[a-(k+1)]+binary_son[a-(k+2)]*2+binary_son[a-(k+3)]*4)
        binary_octal_gecis.append(binary_son[0])
    for j in binary_octal_gecis[::-1]:
        octal.append(j)
        print(j,end="")



print("\nOnaltılı Sayı Sistemindeki karşılığı:",end="")
if a<4:
    if a==3:
        hexadecimal[0]=binary_son[2]+binary_son[1]*2+binary_son[0]*4
    if a==2:
        hexadecimal[0]=binary_son[1]+binary_son[0]*2
    elif a==1:
        hexadecimal[0]=binary_son[0]
    print(hexadecimal[0])
else:
    if a%4==0:
        for k in range(0,a,4):
            binary_hex_gecis.append(binary_son[a-(k+1)]+binary_son[a-(k+2)]*2+binary_son[a-(k+3)]*4+binary_son[a-(k+4)]*8)
    elif a%4==3:
        for k in range(0,a-3,4):
           binary_hex_gecis.append(binary_son[a-(k+1)]+binary_son[a-(k+2)]*2+binary_son[a-(k+3)]*4+binary_son[a-(k+4)]*8)
        binary_hex_gecis.append(binary_son[2]+binary_son[1]*2+binary_son[0]*4)
    elif a%4==2:
        for k in range(0,a-2,4):
            binary_hex_gecis.append(binary_son[a-(k+1)]+binary_son[a-(k+2)]*2+binary_son[a-(k+3)]*4+binary_son[a-(k+4)]*8)
        binary_hex_gecis.append(binary_son[1]+binary_son[0]*2)
    elif a%4==1:
        for k in range(0,a-1,4):
            binary_hex_gecis.append(binary_son[a-(k+1)]+binary_son[a-(k+2)]*2+binary_son[a-(k+3)]*4+binary_son[a-(k+4)]*8)
        binary_hex_gecis.append(binary_son[0])
    for j in binary_hex_gecis[::-1]:
        hexadecimal.append(j)
        #print(j,end="")
for i in range(0,len(hexadecimal),1):
    if hexadecimal[i]>9:
        if hexadecimal[i]==10:
            hexadecimal[i]="A"
        elif hexadecimal[i]==11:
            hexadecimal[i]="B"
        elif hexadecimal[i]==12:
            hexadecimal[i]="C"
        elif hexadecimal[i]==13:
            hexadecimal[i]="D"
        elif hexadecimal[i]==14:
            hexadecimal[i]="E"
        elif hexadecimal[i]==15:
            hexadecimal[i]="F"
    else:
        pass
for i in hexadecimal:
    print(i,end="")
