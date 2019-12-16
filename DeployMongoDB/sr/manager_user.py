#!/usr/bin/python
# -*- coding: utf-8 -*-

'''#############################################################################
# Title: Program deploy replicaset mongodb					
# Description: program automate deploy of 3 MongoDB replication machines  	
# ------------------------------------------------------------------------------
# Module: manager_user.py    					             
# Version: 0.0.1                                                                
#										
# Create Date: 2019/11/04   		                                        
# Modify:                                                                      										
# Modify Date:                                                                                                                                              
#										
# Author: Hudson l. Santos;                                                    
 ###############################################################################'''

class managerMongodb:

### METHODS FOR MANAGE USERS IN SISTEM
### Create user in mongoDB
### Test user in mongoDB

    def addUserMongodb():
        
 #create user in mongodb for autentication
        print ("''") 
        print ("''")
        print ("******** Create user in mongodb********")
        print ("''") 

        try:
            from DeployMongoDB.src.connections import connectDatabase as cd    
            conn = cd.connectNotAutentication()  #this is method for log in on mongodb first time

            MDsr = 'app_percona'
            MDwd = 'MongoDb095#'
  
            conn.admin.add_user(MDsr, MDwd, roles=[{'role':'root','db':'admin'}]) #create user in mongodb

        except:
            print ("''")
            print("failed to create user")
        
        else:
            print ("''")
            print ("create user success")

        return MDsr, MDwd

 #this is method for testing connection in mongodb authentication and list all databases 
    def testNewUser(IP, port, MDsr, MDwd ):
     
        print ("''") 
        print ("''")
        print ("******** testing new user ********")
        print ("''") 

        from DeployMongoDB.src.connections import connectDatabase as cd  
        conn = cd.connectNewUser(IP, port, MDsr, MDwd) #method log in on mongodb using autentication, Ip host and new port set in mongo.conf
        
        listDatabases = conn.list_databases()  

        for db in listDatabases:    

            print (db)
                       
        print ("''")
        print ("'connection success'")
        print ("''")

