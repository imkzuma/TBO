
# Ini merupakan fungsi dari L2 untuk mencari
# string yang diawali simbol 1 dan jumlah simbol 0 adalah kelipatan 3
def L2(state , string):
# state adalah state awal, string adalah string yang akan diuji

    finishState = ['q4']
    # FINISH STATE YAITU q4

    if(string!=""): # Jika string tidak kosong

        print(f'δ({ state },{ string[0] }) = ', end = '')
        # Menampilkan delta-topi dari state dan string yang akan diuji

        if(state == "q0"): # Jika state awal adalah q0
            if(string[0] == "1"): # Jika string yang akan diuji adalah 1
                print(state)
                return L2('q1', string[1:] )  
                # Mengembalikan fungsi dengan state awal q1 dan string yang akan diuji adalah string yang akan diuji tanpa karakter pertama

            else: # Jika string yang akan diuji bukan 1
                print("Dead State") # Maka akan menampilkan dead state

        elif(state == "q1"): # Jika state awal adalah q1
            if(string[0]=="1"): # Jika string yang akan diuji adalah 1
                print(state) # Maka akan menampilkan state q1

                return L2(state,string[1:]) 
                # Mengembalikan fungsi dengan state awal q1

            else: # Jika string yang akan diuji bukan 1
                print("q2") # Maka akan menampilkan state q2

                return L2("q2",string[1:]) 
                # Mengembalikan fungsi dengan state awal q2

        elif(state == "q2"): # Jika state awal adalah q2
            if(string[0]=="1"): # Jika string yang akan diuji adalah 1
                print(state) # Maka akan menampilkan state q2

                return L2(state,string[1:])
                # Mengembalikan fungsi dengan state awal q2

            else: # Jika string yang akan diuji bukan 1
                print("q3") # Maka akan menampilkan state q3

                return L2("q3",string[1:])
                # Mengembalikan fungsi dengan state awal q3

        elif(state == "q3"): # Jika state awal adalah q3
            if(string[0] == "1"): # dan Jika string yang akan diuji adalah 1
                print(state) # Maka akan menampilkan state q3

                return L2(state,string[1:]) 
                # Mengembalikan fungsi dengan state awal q3

            else: # Jika string yang akan diuji bukan 1
                print(finishState[0]) # Maka akan menampilkan finish state q4

                return L2(finishState[0],string[1:])
                # Mengembalikan fungsi dengan state awal finish state q4

        elif(state == finishState[0]): # Jika state awal adalah finish state q4
            if(string[0]=="1"): # dan Jika string yang akan diuji adalah 1
                print(state) # Maka akan menampilkan state q4

                return L2(state,string[1:])
                # Mengembalikan fungsi dengan state awal q4

            else: # Jika string yang akan diuji bukan 1
                print("q2") # Maka akan menampilkan state q2

                return L2("q2",string[1:])
                # Mengembalikan fungsi dengan state awal q2

    else: # Jika string sudah kosong atau kosong dari awal
        if state in finishState: 
            # Jika state awal adalah finish state

            print('Finish State = ', state) 
            # Maka akan menampilkan finish state

        else:  # Jika state awal bukan finish state
            print('Dead State = ', state)
            # Maka akan menampilkan dead state
