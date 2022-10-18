#KELOMPOK 1
#MINIMIZATION OF DFA

#!/usr/bin/env python

#import fungsi floor dan sqrt dari math
from math import floor , sqrt
from secrets import choice 
#import fungsi arange dari numpy
from numpy import arange 
#import fungsi system dari os
from os import system 

# Fungsi untuk mencari kolom dan baris
def find_ab ( counter ):
    #menghitung kolom
    kp = counter - 1
    #kp adalah kolom yang akan dicari

    #menghitung baris
    p = floor (( sqrt ( 1 + 8 * kp ) - 1 ) / 2 )
    # floor adalah fungsi untuk membulatkan ke bawah 
    # sqrt adalah fungsi untuk menghitung akar kuadrat
    #p adalah baris yang akan dicari

    #menghitung kolom
    i = p + 2
    #i adalah kolom yang akan dicari
    # p + 2 adalah rumus untuk mencari kolom

    #menghitung baris
    j = kp - p * ( p + 1 ) / 2 + 1
    #j adalah baris yang akan dicari
    # kp - p * ( p + 1 ) / 2 + 1 adalah rumus untuk mencari baris

    #mengembalikan nilai i dan j
    return int ( i - 1 ), int ( j - 1 )


# Fungsi untuk mencetak tabel
def print_table ( State , Table , listRm , finalState , Simbol ):
# Maksud fungsi ini adalah = Q, Sigma, Start state, final state, delta
# listRm adalah list yang berisi state yang akan dihapus
# finalState adalah list yang berisi state yang merupakan final state
# State adalah list yang berisi state

    #mencetak state
    print ( f"{'state':^10}|" , end = '' )

    #mencetak simbol
    for x in range ( len ( Simbol )): 
    # len(Simbol) adalah panjang dari list Simbol
    # in range adalah fungsi untuk mengulang sesuai dengan panjang dari list Simbol

        print ( f"{Simbol[x]:^10}|" , end = '' ) # mencetak simbol

    print () # mencetak baris baru atau enter

    print("=========================================")

    #mencetak tabel
    for a , b in enumerate ( State ):
    # a adalah index dari state
    # b adalah isi dari state
    # enumerate adalah fungsi untuk mengembalikan index dan isi dari state
    # enumerate(State) adalah fungsi untuk mengembalikan index dan isi dari state

        if ( b not in listRm ): # jika state tidak ada di listRm
        # listRm adalah list yang berisi state yang akan dihapus

            # dan jika state ada di finalState
            if ( b in finalState ): # jika state ada di finalState
            # finalState adalah list yang berisi state yang merupakan final state

                # maka cetak state dengan tanda *
                print ( f"{'*'+b:^10}|" , end = '' ) 
                # cetak state dengan tanda bintang
                # tanda bintang artinya state tersebut merupakan final state

            else: # jika state tidak ada di finalState
                # maka cetak state
                print ( f"{b:^10}|" , end = '' ) # cetak state

            for x in range ( len ( Simbol )): # perulangan sebanyak simbol untuk isi simbol
            # x adalah index dari simbol
            # len(Simbol) adalah fungsi untuk mengembalikan panjang dari simbol
            # range adalah fungsi untuk mengembalikan list dari 0 sampai len(Simbol)

                print ( f"{Table[a*len(Simbol)+x]:^10}|" , end = '' ) 
                # cetak isi tabel dengan index a*len(Simbol)+x
                # a*len(Simbol)+x adalah index dari isi tabel

            print() # cetak enter atau baris baru 
    
    print("=========================================") # cetak garis

    #mencetak state yang akan dihapus
    print('\nQuintuple:\nQ = { ε , ', end='' ) #mencetak Q

    #membuat list state_temp yang berisi state yang akan dihapus dan state yang tidak akan dihapus
    state_temp = list(State) 

    #menghapus state yang akan dihapus dari state_temp
    for a , b in enumerate(listRm): #menghapus state yang akan dihapus
    # a adalah index dari listRm
    # b adalah isi dari listRm
    # enumerate(State) adalah list State yang sudah di enumerate
    # enumerate adalah fungsi yang digunakan untuk mengambil index dan isi dari list

        #jika state yang akan dihapus ada di state_temp
        if(b in state_temp):
        #b adalah isi dari listRm
        #state_temp adalah list state yang akan dihapus dan state yang tidak akan dihapus

            #maka hapus state yang akan dihapus dari state_temp
            #menghapus state yang akan dihapus dari state_temp 
            state_temp.remove(b)
            #b adalah isi dari listRm yang akan dihapus
    
    # mencetak state yang tidak akan dihapus
    print( *state_temp , sep=' , ' , end=' }\n' )
    # state_temp adalah list state yang akan dihapus dan state yang tidak akan dihapus

    # mencetak simbol zigma dari Simbol
    print(f'Σ = {set(Simbol)}')
    # Simbol adalah list simbol yang ada

    # mencetak state awal
    print(f'Start state = {State[0]}')
    # State adalah list state yang ada

    # mencetak final state
    print(f'Final state = {set(finalState)}')
    # finalState adalah list final state yang ada

    print() # mencetak enter atau baris baru

    # mencetak simbol delta
    print(f'Delta : ')
    # mencetak delta

    for a , b in enumerate(State):
    # a adalah index dari State
    # b adalah isi dari State
    # enumerate(State) adalah list State yang sudah di enumerate
    # enumerate adalah fungsi yang digunakan untuk mengambil index dan isi dari list

        if(b not in listRm): #jika state yang akan dihapus tidak ada di listRm
        # b adalah isi dari State
        # listRm adalah list state yang akan dicek

            # maka lakukan perulangan sebanyak simbol
            for c , d in enumerate(Simbol): #mencetak delta
            # c adalah index dari Simbol
            # d adalah isi dari Simbol
            # enumerate(Simbol) adalah list Simbol yang sudah di enumerate
            # enumerate adalah fungsi yang digunakan untuk mengambil index dan isi dari list

                # lalu cetak delta
                print( f"δ( {b} , {c} ) {'=':^5} {Table[a*len(Simbol)+c]}" ) 
                # hasil print adalah δ(state, simbol) = state
                # a adalah index dari State
                # b adalah isi dari State
                # c adalah index dari Simbol
                # Table[a*len(Simbol)+c] adalah isi dari tabel yang akan dicetak
                # len(Simbol) adalah panjang dari Simbol
    
    print("\n========================================= \n") # mencetak garis

#################################################################################

# fungsi membuat tabel 
def makeTable ( State , secTable ):
# State adalah list state yang ada

    counter = 0 # counter adalah variabel untuk penghitung index
    n = len ( State ) # n adalah panjang dari State
    # len(State) adalah fungsi untuk mengembalikan panjang dari State

    for a in range(1 , n ): # perulangan sebanyak state
    # a adalah index dari State
    # range adalah fungsi untuk mengembalikan list dari 1 sampai n
    # n adalah panjang dari State

        for _ in range( a ): # perulangan sebanyak state
        # _ adalah variabel yang tidak digunakan

            print(secTable[counter] , end = ' ')
            # cetak isi tabel dengan index counter

            counter += 1 # counter ditambah 1

        print() # cetak enter atau baris baru 

#################################################################################

# fungsi untuk mencari letak index tabel menggunakan baris kolom
def find_counter(a,b):
# a adalah baris
# b adalah kolom
        
        return sum(arange(1,a)) + b # mengembalikan hasil dari sum(arange(1,a)) + b
        # sum adalah fungsi untuk menjumlahkan list
        # arrange adalah fungsi untuk mengembalikan list dari 1 sampai a
        # a adalah baris

#################################################################################

#fungsi remove duplicate state
def removeDuplicateState( State , Table , secTable , finalState , Simbol ): 
# State adalah list state yang ada
# finalState adalah list final state yang ada
# Simbol adalah list simbol yang ada

    # membuat list listRm yang berisi state yang akan dihapus
    listRm = []

    # minimisasi state
    for x in range(len( secTable )): #perulangan sebanyak isi dari secTable
    # x adalah index dari secTable
    # len(secTable) adalah panjang dari secTable
    # range adalah fungsi untuk mengembalikan list dari 0 sampai len(secTable)

        if( secTable[x] ==-1 ): # jika isi dari secTable[x] adalah -1
        # x adalah index dari secTable
        # secTable[x] adalah isi dari secTable
            
            # maka mencari a dan b dengan fungsi find_ab
            a , b = find_ab( x + 1) # mencari a dan b dengan fungsi find_ab
            # x adalah index dari secTable
            # a adalah state yang akan dihapus
            # b adalah state yang tidak akan dihapus

            if(b < a): # jika b lebih kecil dari a
            # b adalah state yang tidak akan dihapus
            # a adalah state yang akan dihapus

                # maka a dan b ditukar
                b , a = a , b # menukar a dan b 
            
            # lalu simpan state[a] di variabel temp
            temp = State[a] # menyimpan state yang akan dihapus
            # a adalah state yang akan dihapus
            # temp adalah state yang akan dihapus
            
            State[a] = str( State[a] + '/' + State[b] ) 
            # mengganti state yang akan dihapus dengan state yang tidak akan dihapus
            # a adalah state yang akan dihapus
            # State[a] adalah state yang akan dihapus
            # State[b] adalah state yang tidak akan dihapus
            # output state[a] / state[b]


            # lakukan perulangan sebanyak isi dari Table
            for x , y in enumerate(Table): #minimisasi state pada table
            # x adalah index dari Table
            # y adalah isi dari Table
            # enumerate(Table) adalah list Table yang sudah di enumerate
            # enumerate adalah fungsi yang digunakan untuk mengambil index dan isi dari list

                # jika isi dari Table adalah state yang tidak akan dihapus atau state yang akan dihapus
                if(y == State[b] or y == temp): 
                # y adalah isi dari Table
                # State[b] adalah state yang tidak akan dihapus
                # temp adalah state yang akan dihapus

                    # maka isi dari Table diganti dengan state yang tidak akan dihapus
                    Table[x] = State[a] # mengganti isi dari Table dengan state yang tidak akan dihapus
                    # x adalah index dari Table
                    # State[a] adalah state yang tidak akan dihapus
            
            # end for x , y in enumerate(Table)

            # lalu state yang akan dihapus ditambahkan ke listRm
            listRm.append(State[b]) # menambahkan state yang akan dihapus ke listRm
            # State[b] adalah state yang akan dihapus
            # append adalah fungsi untuk menambahkan isi ke list

            for x , y in enumerate(finalState): #minimisasi state pada final
            # x adalah index dari finalState
            # y adalah isi dari finalState
            # enumerate(finalState) adalah list finalState yang sudah di enumerate
            # enumerate adalah fungsi yang digunakan untuk mengambil index dan isi dari list

                # jika isi dari finalState adalah state yang tidak akan dihapus atau state yang akan dihapus
                if(y == State[b] or y == temp): 
                # y adalah isi dari state[b]
                # State[b] adalah state yang akan dihapus
                # temp adalah state yang akan dihapus

                    # maka isi dari finalState diganti dengan state yang tidak akan dihapus
                    # mengganti isi dari finalState dengan state yang tidak akan dihapus
                    finalState[x] = State[a] 
                    # x adalah index dari finalState
                    # State[a] adalah state yang tidak akan dihapus
                
            # end for x , y in enumerate(finalState):

    # end for x in range(len( secTable )):
                    
    # lakukan perulangan sebanyak isi dari State
    for x in range( len( State ) ): #menghapus state duplikat
    # x adalah index dari State
    # len(State) adalah panjang dari State
    # range adalah fungsi untuk mengembalikan list dari 0 sampai len(State)

        # lalu perulangan lagi sebanyak isi state
        for y in range(len( State ) ): #menghapus state duplikat
        # y adalah index dari State
        # len(State) adalah panjang dari State
        # range adalah fungsi untuk mengembalikan list dari 0 sampai len(State)
            
            if(x == y): continue # continue adalah fungsi untuk melanjutkan perulangan
            # jika x sama dengan y maka lanjutkan
            
            # jika state yang akan dihapus ada di state yang tidak akan dihapus
            if(State[x].find(State[y]) !=- 1): 
            # State[x].find(State[y]) adalah mencari state yang akan dihapus di state yang tidak akan dihapus
            # State[x] adalah state yang akan dihapus
            # State[y] adalah state yang tidak akan dihapus
            # find adalah fungsi untuk mencari string

                # dan jika state yang tidak akan dihapus tidak ada di listRm
                if(State[y] not in listRm): # jika state yang tidak akan dihapus tidak ada di listRm
                # State[y] adalah state yang tidak akan dihapus
                # listRm adalah list yang berisi state yang akan dihapus

                    # dan jika state yang akan dihapus tidak ada di listRm
                    if((Table[x*len(Simbol)] == Table[y*len(Simbol)]) and (Table[x*len(Simbol)+1]==Table[y*len(Simbol)+1])):
                    # jika isi dari Table[x*len(Simbol)] sama dengan isi dari Table[y*len(Simbol)] 
                    # dan isi dari Table[x*len(Simbol)+1] sama dengan isi dari Table[y*len(Simbol)+1]
                    # x adalah index dari State
                    # len(Simbol) adalah panjang dari Simbol
                    # Table[x*len(Simbol)] adalah isi dari Table

                        #maka state yang akan dihapus ditambahkan ke listRm
                        listRm.append( State[y] ) # maka tambahkan state yang akan dihapus ke listRm
                        # State[y] adalah state yang akan dihapus
        
        # end for y

    # end for x
    
    #lalu mengembalikan print_table dan make_table
    return print_table(State, Table, listRm , finalState , Simbol) , makeTable(State , secTable)

#############################################################################################################

# fungsi untuk mengecek simbol untuk dimasukkan kedalam table
def cekSimbol( firstState, secondState, Simbols, Table, State, secTable):
# firstState adalah state pertama
# secondState adalah state kedua
# Simbols adalah simbol
# Table adalah table
# State adalah state
# secTable adalah table yang digunakan untuk mengecek state

    simbol = Simbols  # Simbols di simpan ke dalam variabel simbol

    # lalu perulangan sebanyak isi dari simbol
    for b in simbol:
    # b adalah isi dari simbol
    # simbol adalah isi dari simbol

        # jika isi dari simbol adalah epsilon
        if(State.index(Table[State.index( firstState ) * 2 + simbol.index(b)]) < State.index(Table[State.index( secondState ) * len( simbol ) + simbol.index( b ) ] ) ):
        # State.index(Table[State.index( firstState ) * 2 + simbol.index(b)]) adalah mencari isi dari Table 
        # State.index( firstState ) * 2 + simbol.index(b) adalah mencari isi dari Table 
        # State.index( firstState ) adalah mencari isi dari Table
        # 2 adalah jumlah state
        # simbol.index(b) adalah mencari isi dari Table
        # State.index(Table[State.index( firstState ) * 2 + simbol.index(b)]) adalah mencari isi dari Table
        # State.index(Table[State.index( secondState ) * len( simbol ) + simbol.index( b ) ] ) adalah mencari isi dari Table
        # State.index( secondState ) adalah mencari isi dari Table
        # len( simbol ) adalah panjang dari simbol
        # simbol.index( b ) adalah mencari isi dari Table

            # maka x , y diganti dengan firstState dan secondState
            x , y = firstState , secondState #mengganti isi dari x dan y dengan firstState dan secondState
            secondState , firstState = x , y # mengganti isi dari secondState dan firstState dengan x dan y
        
        #Ketika state1 == state2, kondisi tidak valid karna tidak bisa mengecek diri sendiri.
        if( ( Table[ State.index( firstState ) * len( simbol ) + simbol.index( b ) ] == Table[State.index( secondState ) * len( simbol ) + simbol.index( b ) ] ) ):
            continue # continue adalah fungsi untuk melanjutkan perulangan
        
        # jika isi dari simbol tidak ada di table 
        if(secTable[ find_counter(State.index( Table[ State.index( firstState ) * len( simbol ) + simbol.index(b) ] ) ,State.index(Table[ State.index(secondState) * len(simbol)+simbol.index(b) ] ) ) ] != -1):
        # secTable[ find_counter(State.index( Table[ State.index( firstState ) * len( simbol ) + simbol.index(b) ] ) ,State.index(Table[ State.index(secondState) * len(simbol)+simbol.index(b) ] ) ) ] adalah mencari isi dari Table
        # find_counter(State.index( Table[ State.index( firstState ) * len( simbol ) + simbol.index(b) ] ) ,State.index(Table[ State.index(secondState) * len(simbol)+simbol.index(b) ] ) ) adalah mencari isi dari Table
        # State.index( Table[ State.index( firstState ) * len( simbol ) + simbol.index(b) ] ) adalah mencari isi dari Table
        # State.index( firstState ) adalah mencari isi dari Table
        # len( simbol ) adalah panjang dari simbol
        # simbol.index(b) adalah mencari isi dari Table
        # Table[ State.index( firstState ) * len( simbol ) + simbol.index(b) ] adalah mencari isi dari Table
        # State.index(Table[ State.index(secondState) * len(simbol)+simbol.index(b) ] ) adalah mencari isi dari Table
        # State.index(secondState) adalah mencari isi dari Table
        # len(simbol) adalah panjang dari simbol
        # simbol.index(b) adalah mencari isi dari Table
        # Table[ State.index(secondState) * len(simbol)+simbol.index(b) ] adalah mencari isi dari Table
        # -1 adalah nilai yang akan di return jika tidak ada

            return b # maka mengembalikan nilai dari b
    
    #end for b in simbol

    # jika tidak ada yang memenuhi kondisi diatas maka mengembalikan nilai -1
    return -1

#############################################################################################################

# fungsi iterasi
#iterasi untuk pengisian epsilon dan simbol lainnya di fungsi cekSimbol
def iteration( State , finalState , Table , Simbol): 
# State adalah state
# finalState adalah final state
# Table adalah table
# Simbol adalah simbol
    
    panjang = sum( arange( 1 , len( State ) ) ) # variabel ini digunakan untuk menghitung panjang dari state
    # panjang adalah panjang dari state
    # arange( 1 , len( State ) ) adalah mencari isi dari state
    # sum( arange( 1 , len( State ) ) ) adalah mencari isi dari state

    sectable = [ -1 for x in range(panjang) ] 
    # sectable adalah table yang digunakan untuk mengecek state
    # -1 adalah nilai yang akan di return jika tidak ada
    # range(panjang) adalah mencari isi dari panjang

    isThere = True # variabel ini digunakan untuk mengecek apakah ada epsilon atau tidak
    counter = 0 # variabel ini digunakan untuk menghitung epsilon

    for a in range( 1 , len( State ) ): #iterasi pertama untuk mencari epsilon
    # a adalah isi dari state
    # range( 1 , len( State ) ) adalah mencari isi dari state

        # lalu perulangan kedua untuk mencari epsilon
        for b in range(a):
        # b adalah isi dari state
        # range(a) adalah mencari isi dari state
        
            if((State[a] in finalState and State[b] not in finalState) or (State[a] not in finalState and State[b] in finalState)): 
            # jika state a ada di final state dan state b tidak ada di final state atau state a tidak ada di final state dan state b ada di final state
            # State[a] adalah mencari isi dari state
            # State[b] adalah mencari isi dari state
            # finalState adalah final state
                
                # maka isi dari sectable adalah epsilon
                sectable[counter] = 'ε' # maka isi dari sectable adalah epsilon
                # counter adalah epsilon
            
            counter+=1 # counter ditambah 1

        #end for b

    #end for a

    # lalu perulangan untuk mencari simbol lainnya
    while(isThere): #iterasi selanjutnya untuk mencari simbol-simbol pada tabel
    # isThere adalah kondisi untuk perulangan

        isThere = False # isThere adalah kondisi untuk perulangan
        # isThere menjadi false

        counter = 0 # counter 

        for a in range( 1 , len( State ) ): # iterasi untuk mencari simbol lainnya sebanyak state
        # a adalah isi dari state
        # range( 1 , len( State ) ) adalah mencari isi dari state

            for b in range(a): # iterasi untuk mencari simbol lainnya sebanyak a
            # b adalah isi dari state
            # range(a) adalah mencari isi dari state

                 # jika sectable adalah -1 dan cekSimbol adalah -1
                if(sectable[counter] == -1 and (cekSimbol(State[a] , State[b] , Simbol , Table , State , sectable) !=-1 ) ):
                # sectable adalah table yang digunakan untuk mengecek state
                # counter adalah epsilon
                # cekSimbol adalah mencari isi dari Table
                # State[a] adalah mencari isi dari state
                # State[b] adalah mencari isi dari state
                # Simbol adalah simbol
                
                    # maka isi dari sectable adalah cekSimbol
                    sectable[counter] = cekSimbol(State[a] , State[b] , Simbol , Table , State , sectable)
                    # sectable adalah table yang digunakan untuk mengecek state
                    # counter adalah epsilon
                    # cekSimbol adalah mencari isi dari Table
                    # State[a] adalah mencari isi dari state
                    # State[b] adalah mencari isi dari state
                    # Simbol adalah simbol

                    # maka isThere adalah true
                    isThere = True

                counter+=1 # counter ditambah 1

            #end for b

        # end for a

    # end while(isThere)

    # mengembalikan nilai dari fungsi removeDuplicateState
    return removeDuplicateState(State , Table , sectable , finalState , Simbol) 

#############################################################################################################

def mainMenu(): #Pilihan menu

    listState = ['q0','q1','q2','q3','q4','q5'] # variabel ini digunakan untuk menyimpan state

    system('cls')
    print("Tugas Programming Minimisasi DFA")
    print("================================\n")

    print("Menu Program DFA\n")
    print("1. L1 \n2. L2 \n3. L3")

    userInput = int(input("\nPilih Menu : "))

    print("================================\n")

    if(userInput == 1): # jika userInput adalah 1 yaitu menu L1
        # maka akan menampilkan menu L1
        print("Sebelum minimisasi:\n") # menampilkan Sebelum minimisasi:
        print_table(listState[:5] , ['q1','q2','q1','q3','q1','q2','q1','q4','q1','q2'] , [] , listState[4] , ['a', 'b'] )
        # print_table adalah mencetak tabel yang sudah diisi dengan state, final state, dan simbol

        print("Setelah minimisasi: \n") # menampilkan Setelah minimisasi:
        iteration(listState[:5] , listState[4] , ['q1','q2','q1','q3','q1','q2','q1','q4','q1','q2'] , ['a', 'b'] )
        # iteration adalah mencetak tabel yang sudah diisi dengan state, final state, dan simbol

    elif(userInput == 2): # jika userInput adalah 2 yaitu menu L2
        # maka akan menampilkan menu L2
        print("Sebelum minimisasi:") # menampilkan Sebelum minimisasi:
        print_table(listState[:] , ['q3','q1','q2','q5','q2','q5','q0','q4','q2','q5','q5','q5'] , [] , ['q1','q2'] , [0 , 1]) 
        # print_table adalah mencetak tabel yang sudah diisi dengan state, final state, dan simbol
        
        print("Setelah minimisasi: \n") # menampilkan Setelah minimisasi:
        iteration(listState[:] , ['q1','q2'] , ['q3','q1','q2','q5','q2','q5','q0','q4','q2','q5','q5','q5'] , [0 , 1])
        # iteration adalah mencetak tabel yang sudah diisi dengan state, final state, dan simbol

    elif(userInput == 3): # jika userInput adalah 3 yaitu menu L3
        # maka akan menampilkan menu L3
        print("Sebelum minimisasi:") # menampilkan Sebelum minimisasi:
        print_table(listState[:] , ['q1','q3','q0','q3','q1','q4','q5','q5','q3','q3','q5','q5'], [], ['q3','q5'], [0 , 1] )
        # print_table adalah mencetak tabel yang sudah diisi dengan state, final state, dan simbol

        print("Setelah minimisasi: \n") # menampilkan Setelah minimisasi:
        iteration(listState[:] , ['q3','q5'] , ['q1','q3','q0','q3','q1','q4','q5','q5','q3','q3','q5','q5'] , [0 , 1] )
        # iteration adalah mencetak tabel yang sudah diisi dengan state, final state, dan simbol

    else: # jika userInput adalah selain 1, 2, dan 3
        print("inputan tidak ditemukan!") # menampilkan inputan tidak ditemukan!
  
    # mengembalikan nilai dari fungsi mainMenu
    print("\nApakah ingin mengulang?\n1. Yes\n2. No\n")

    choice = int(input("Pilihan : ")) # inputan pilihan 

    if choice == 1 : mainMenu() # jika choice adalah 1 maka akan kembali ke menu utama


# main program
if __name__ == "__main__": # jika __name__ adalah __main__
    mainMenu() # maka akan menampilkan menu utama