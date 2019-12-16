'''#############################################################################
# Title: Program deploy replicaset mongodb                  
# Description: program automate deploy of 3 MongoDB replication machines    
# ------------------------------------------------------------------------------
# Module: querys.py                                   
# Version: 0.0.1                                                                
#                                       
# Create Date: 2019/11/03                                                   
# Modify:  Include serviceReplication                                                                                                       
# Modify Date:   2019/11/05                                                                                                                                            
#                                       
# Author: Hudson l. Santos;                                                    
 ###############################################################################'''


# METHOD INSERT 1000 ROWS IN MONGODB REPLIC
class querys:

    def insert1000(IP, port , MDsr, MDwd):
        
        from DeployMongoDB.src.connections import connectDatabase as cd  
        conn = cd.connectReplicSet(IP, port, MDsr, MDwd) #method log in on mongodb using autentication, Ip host and new port set in mongo.conf


        print ("''")
        print ("''")
        print ("******** start insert 1000 rows ********")  

        mydb = conn["percona"]
        mycol = mydb["test"]

    
        try:
            for x in range(0, 1001):
    
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




        

