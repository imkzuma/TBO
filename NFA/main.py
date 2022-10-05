# KELOMPOK 1

from FunctionL1 import SameString 
from FunctionL2 import L2
from FunctionL3 import L3

# Ini merupakan fungsi main menu 
# yang akan memanggil fungsi sesuai dengan menu yang dipilih
def mainMenu():
    print("\n\n1. L1 string yang diawali dan diakhiri dengan simbol yang sama")
    print("2. L2 string yang diawali simbol 1 dan jumlah simbol 0 adalah kelipatan 3")
    print("3. L3 string yang diawali 0 dan jumlah simbol 1 adalah ganjil")
    print("4. Exit")
    print("Pilih Menu: ", end = '')
    menu = int(input())

    if menu == 1: #Jika menu yang dipilih adalah 1
        SameString("q0", input("Masukkan string: ")) #Maka akan memanggil fungsi L1
    
    elif menu == 2: #Jika menu yang dipilih adalah 2
        L2("q0", input("Masukkan string: ")) #Maka akan memanggil fungsi L2
    
    elif menu == 3: #Jika menu yang dipilih adalah 3
        L3("q0", input("Masukkan string: ")) #Maka akan memanggil fungsi L3
    
    elif menu == 4: #Jika menu yang dipilih adalah 4
        exit() #Maka akan keluar dari program
    
    else: #Jika menu yang dipilih bukan 1, 2, 3, atau 4
        print("Menu tidak tersedia")

    mainMenu() #Mengulang fungsi main menu


# Fungsi main
if __name__ == "__main__":
    mainMenu() #Memanggil fungsi main menu