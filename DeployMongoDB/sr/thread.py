
class querys:

    def insert1000(IP, port , MDsr, MDwd):
        
        from threading import Thread

        THREAD_COUNT = 400
        
        from DeployMongoDB.src.connections import connectDatabase as cd  
        conn = cd.connectNewUser(IP, port, MDsr, MDwd) #method log in on mongodb using autentication, Ip host and new port set in mongo.conf


        print ("''")
        print ("''")
        print ("******** start insert 1000 rows ********")  

        mydb = conn["percona"]
        mycol = mydb["test"]

        try:
            for x in range(10):
                print(x)
                data = {"DadosAutomaticos - " : x}

                mycol.insert(data)

        except :
            print ("''")
            print("Fail: insert rows")
            print ("''")
        else:
            print ("''")
            print("Insert rows success")
            print ("''")
            print ("'*****************************************'")
            print ("* IP: " + IP)
            print ("* PORT: " + port)
            print ("* USER :" + MDsr)
            print ("* PASSWORD :" + MDwd)
            print ("'*****************************************'")



        

