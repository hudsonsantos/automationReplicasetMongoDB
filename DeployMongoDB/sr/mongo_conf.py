#!/usr/bin/python
# -*- coding: utf-8 -*-

'''#############################################################################
# Title: Program deploy replicaset mongodb					
# Description: program automate deploy of 3 MongoDB replication machines  	
# ------------------------------------------------------------------------------
# Module: mongo.conf.py    					             
# Version: 0.0.1                                                                
#										
# Create Date: 2019/11/03   		                                        
# Modify:   reconfigureMongoConfReplics                                                          										
# Modify Date:   2019/11/06                                                                                                                                            
#										
# Author: Hudson l. Santos;                                                    
 ###############################################################################'''


class managerMongoConf:  

### METHOD TO CONFIGURE IP, PORT AND SECURITY IN mongo.conf  
 
    def reconfigureMongoConf(IP_new): 
        
        import socket
        try:
            print ("''")
            print ("''")
            print ("******** start of file configuration security mongo.conf ********")  
       
            #IP_new =  input("INSIRA O IP PARA mongod.conf:")

            IP_old  = "127.0.0.1"  
            Port_old = "27017"
            Port_new = "47017"
            file_target = '/etc/mongod.conf'
            Security_old = '#security:'
            Security_new = 'security: \n  authorization: "enabled" \n  keyFile: /mongodb/mongodb.key'
            Replication_old = '#replication:'
            Replication_new = 'replication: \n  replSetName: "perconaReplic"'

            
# find old IP and modify to host IP in mongo.conf
            with open(file_target,"r") as f:         
                newIP=[]

                for bindIP in f.readlines():            # set variable bindIP with read of file mongo.confs for replace old IP to new IP
                    newIP.append(bindIP.replace(IP_old, IP_new))    # replace old IP to new IP

                    with open(file_target,"w") as f:    # open the mongo.config for write a new IP set                       
                        for lineIP in newIP:
                            f.writelines(lineIP)
                            
                            #file_target.close()

 # find old Port and modify mongo.conf to port indicated in variable Port_new
            with open(file_target,"r") as f:       
                newPort=[]

                for port in f.readlines():                  # read file mongo.confs for replace old port to new port
                    newPort.append(port.replace(Port_old, Port_new))  # replace old port to new port

                    with open(file_target,"w") as f:    # open mongo.config and replace for new port set
                        for linePort in newPort:
                            f.writelines(linePort)

# modify the variable security in mongo.conf for: security "enable"
            with open(file_target,"r") as f:    
                newSecurity=[]

                for security in f.readlines():          # read file mongo.confs for replace old security to new security
                    newSecurity.append(security.replace(Security_old, Security_new)) # replace old security to new security
                    
                    with open(file_target,"w") as f:        # open mongo.config and replace for new security set
                        for lineSecurity in newSecurity:
                            f.writelines(lineSecurity)

#modify the variable replication in mongo.conf for: replication replSetname "perconaReplic"
            with open(file_target,"r") as f:
                newReplication=[]

                for replication in f.readlines():       # read file mongo.confs for replace old replication to new replication
                    newReplication.append(replication.replace(Replication_old, Replication_new)) #  replace old replication to new replication
                    
                    with open(file_target,"w") as f:            # open mongo.config and replace for new replication set
                        for lineReplication in newReplication:
                            f.writelines(lineReplication)                           
          
        except:
        
            print ("''")         
            print ("<< Unable to change settings security in mongo.conf >>")
 
        else:
        
            print ("''")     
            print ("change IP, port, security of mongo.conf success")
               
        return Port_new  



   
# reconfigure the files replicasets mongo.confs for new port to replication set 
    def reconfigureMongoPorts(path_file):

        import os
        
        print ("''")
        print ("''")
        print ("******** start of file configuration port mongo.conf ********")  
        files = []
        Port_old= "47017"
        x = 7
        try:
            for p, _, files in os.walk(os.path.abspath(path_file)):     # find all files in directory path_file: /etc/mongo_config

                    for file in files:
                        path_full= os.path.join(p, file)               # concat name directory with name file 

                        with open(path_full,"r") as f:                  # set port with range (x) - increment(1)                     
                            newPort=[]
                            port_new = '4701' + str(x)      

                            for port in f.readlines():                          # open and read files in directory mongo_config and find port old
                                newPort.append(port.replace(Port_old, port_new))

                                with open(path_full,"w") as f:          #open files in mongo_config and change port old for port new
                                    for linePort in newPort:
                                        f.writelines(linePort)      

                        x += 1
        except:
        
            print ("''")         
            print ("<< Unable to change settings port in mongo.confs >>")
 
        else:
        
            print ("''")     
            print ("change port mongo.confs success")



#reconfigure files replicasets mongo.confs
    def reconfigureDbpath(path_file):

        import os
        
        print ("''")
        print ("''")
        print ("******** start of file configuration dbpath in mongo.conf ********")  
        files = []
        import os
        try:
            files = []
            dbPath_old =  '/var/lib/mongo'   # variable default in mongo.conf
            x = 0
        
            for p, _, files in os.walk(os.path.abspath(path_file)):     # find files in directory path_file: /etc/mongo_config

                    for file in files:
                        path_full= os.path.join(p, file)               # concat name directory with name file

                        with open(path_full,"r") as f:                  # set new dbpath with name of new directory  and range (x) - increment(1)
                            newdbPath = []
                            dbPath_new = '/mongodb/node' + str(x)      

                            for dbpath in f.readlines():                          # open and read files in directory /etc/mongo_config and  find dbpath old
                                newdbPath.append(dbpath.replace(dbPath_old, dbPath_new))  # replace dbpath old for dbpath new

                                with open(path_full,"w") as f:          # open and write files in directory /etc/mongo_config and change dbpath old for dbpath new
                                    for linedbPath in newdbPath:
                                        f.writelines(linedbPath)      

                        x += 1
        except:
        
            print ("''")         
            print ("<< Unable to change settings dbpath in mongo.confs >>")
 
        else:
        
            print ("''")     
            print ("change dbpath mongo.confs success")

        
