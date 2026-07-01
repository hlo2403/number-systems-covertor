print("TO COVERT NUMBER")
def bin_to_dec(a):
    a =input("ENTER THE BINARY NUMBER:")
    print(bin(int(a,16))[2:])
    return
def oct_to_dec(b):
    b =input("enter the decimal number:")
    print(int(b ,8))
    return
def hex_to_dec(c):
    c =input("enter the decimal number:")
    print(int(c,16))
    return
def dec_to_bin(d):
    dec=input("enter the decimal number:")
    print(bin(int(dec,16))[2:])
    return
def dec_to_oct(e):
    dec=input("enter the decimal number:")
    print(oct(int(dec))[2:])
    return
def dec_to_hex(f):
    dec=input("enter the decimal number:")
    print(hex(int(dec))[2:])
    return
def oct_to_bin(g):
    oct=input("enter the octal number:")
    print(bin(int(oct,8))[2:])
    return
def hex_to_bin(h):
    hexa=input("enter the hexadecimal number:")
    print(bin(int(hexa,16))[2:])
    return
def bin_to_octal(i):
    binary=input("enter the binary number:")
    print(oct(int(binary,2))[2:])
    return
def bin_to_hex(j):
    binary=input("enter the binary number:")
    print(hex(int(binary,2))[2:])
    return
def main():
    count=0
    while count<=10000000:
        print("==============================")
        print("CHOOSE THE FOLLOWING OPERATION")
        print("==============================")
        print("(a) TO CONVERT BINARY TO DECIMAL")
        print("(b) TO CONVERT OCTAL TO DECIMAL")
        print("(c) TO CONVERT HEXADECIMAL TO DECIMAL")
        print("(d) TO CONVERT DECIMAL TO BINARY")
        print("(e) TO CONVERT DECIMAL TO OCTAL")
        print("(f) TO CONVERT DECIMAL TO HEXADECIMAL")
        print("(g) TO COVERT OCTAL TO BINARY")
        print("(h) TO  CONVERT HEXADECIMAL TO BINARY")
        print("(i) TO CONVERT BINARY TO OCTAL")
        print("(j) TO CONVERT BINARY TO HEXADECIMAL")
        print("(q) TO EXIT THE OPERATION")
        choice=input("ENTER THE CHOICE:")
        if choice=='a':bin_to_dec(" ")
        elif choice=='b':oct_to_dec(" ")
        elif choice=='c':hex_to_dec(" ")
        elif choice=='d':dec_to_bin(" ")
        elif choice=='e':dec_to_oct(" ")
        elif choice=='f':dec_to_hex(" ")
        elif choice=='g':oct_to_bin(" ")
        elif choice=='h':hex_to_bin(" ")
        elif choice=='i':bin_to_octal(" ")
        elif choice=='j':bin_to_hex(" ")
        else:
            print("NO OPERATION")
            break
        count+=1
main()