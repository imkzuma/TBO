
# Ini merupakan fungsi dari L3 untuk Mencari
# string yang diawali 0 dan jumlah simbol 1 adalah ganjil
def L3(state , string): 
# Fungsi L3 dengan parameter state dan string
# state adalah state awal, string adalah string yang akan diuji
    
    finishState = 'q2'
    #Mendefinisikan finishState dengan nilai q2

    if(string != ''): #Jika string tidak kosong

        print(f'δ({state},{string[0]}) = ',end='')
        #Mencetak δ(state,string[0]) =

        if(state == "q0"): #Jika state awal adalah q0
            if(string[0] == "0"): #Jika string yang akan diuji adalah 0
                print("q1") #Maka akan menampilkan state q1

                return L3("q1" , string[1:]) 
                # Mengembalikan fungsi dengan state awal q1

            else: # Jika string yang akan diuji bukan 0
                print("q0") # Maka akan menampilkan state q0

                print("Dead State = q0") 
                # Maka akan menampilkan dead state

        elif(state=="q1"): #Jika state awal adalah q1
            if(string[0] == "0"): #Jika string yang akan diuji adalah 0
                print(state) #Maka akan menampilkan state q1

                return L3(state, string[1:]) 
                # Mengembalikan fungsi dengan state awal q1

            else: # Jika string yang akan diuji bukan 0
                print(finishState) # Maka akan menampilkan finish state q2

                return L3(finishState , string[1:])
                # Mengembalikan fungsi dengan state awal finish state q2

        elif(state == finishState): #Jika state awal adalah finish state
            if(string[0] == "0"): #Jika string yang akan diuji adalah 0
                print(state) #Maka akan menampilkan finish state q2

                return L3(state , string[1:])
                # Mengembalikan fungsi dengan state awal finish state q2

            else: # Jika string yang akan diuji bukan 0
                print("q1") # Maka akan menampilkan state q1
                
                return L3("q1", string[1:])
                # Mengembalikan fungsi dengan state awal q1

    else: #Jika string kosong
        if state == finishState: #Jika state awal adalah finish state

            # Maka akan menampilkan finish state q2
            print('Finish State = ' + state) 

        else: #Jika state awal bukan finish state

            # Maka akan menampilkan dead state
            print('Dead State = ' + state)
            