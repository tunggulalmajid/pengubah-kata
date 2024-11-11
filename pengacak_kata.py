import os 
import termcolor

def clear():
    os.system("cls")

def garis(a):
    print(a*50)

def cover(a):
    garis("=")
    print(a.center(50))
    garis("=")

def enter ():
    enter = input("Tekan [ENTER] untuk melanjutkan ...")

def exit():
    clear()
    cover(a)
def main():
    while True :
        clear()
        cover(a)
        print ("""
MENU :
            1. PENGUBAH KATA 
            2. EXIT

""")
        garis("=")
        try :
            pilih = int (input ("masukkan opsi yang dipilih >> "))
            if pilih == 1 :
                enter()
                pengubah_kata()
                break
            elif pilih == 2 :
                enter()
                exit ()
                break
            else :
                raise ValueError ("hanya piliih opsi yang tersedia")
        except ValueError as error :
            termcolor.cprint(error,"red")
            enter()
            continue

def pengubah_kata():
    clear()
    cover(a)
    kata = input ("\nmasukkan kata yang ingin diubah >> ")
    operasi = int(input("penambahan atau pengurangan bilangan ASCII ? 1. penambahan, 2. pengurangan >> "))
    bil_ascii = int (input ("ingin sebanyak berapa bilangan ASCII ? >> "))
    if operasi == 1:
        gass = "menambah"
        kata_baru = []
        for i in kata:
            operasi_ascii = chr(ord(i) + bil_ascii)
            kata_baru.append(operasi_ascii)

    elif operasi == 2 :
        gass = "mengurangi"
        kata_baru = []
        for i in kata :
            operasi_ascii = chr(ord(i) + bil_ascii)
            kata_baru.append(operasi_ascii)
    print ("HASIL")
    print ("KATA AWAL :")
    print(kata)
    print ("KATA BARU :")
    for i in kata_baru:
        print (i,end="")
    print(f"""\nDIOPERASIKAN DENGAN {gass.upper()}  sebanyak {bil_ascii} BILANGAN ASCII """)       
    garis("=")
    enter()
    main()



if __name__ == "__main__":
    a = "PROGRAM PENGUBAH KATA"
    main()