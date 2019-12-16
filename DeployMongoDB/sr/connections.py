 
#!/usr/bin/python
# -*- coding: utf-8 -*-
'''#############################################################################
# Title: Program deploy replicaset mongodb					
# Description: program automate deploy of 3 MongoDB replication machines  	
# ------------------------------------------------------------------------------
# Module: dependences.py    					             
# Version: 0.0.1                                                                
#										
# Create Date: 2019/11/04  		                                        
# Modify:    Include connectFirstreplic                                                       										
# Modify Date:  2019/11/06                                                                                                                                     
#										
# Author: Hudson l. Santos;                                                    
 ###############################################################################'''

class connectDatabase:

###CONNECTION METHODS IN DATABASE

    def connectNotAutentication():

# connect not authentication - (first connect)
        from pymongo import MongoClient
        client = MongoClient('localhost:27017')
        #client.admin.authenticate('siteRootAdmin', 'Test123')
        return client

 # connect with authentication, new port and host IP 
    def connectNewUser(IP, port ,MDsr, MDwd):
        
        from pymongo import MongoClient
        conn =  IP + ':' + port
        client = MongoClient(conn)
        client.admin.authenticate(MDsr, MDwd)
        return client

 # connect with authentication, new port and host IP 
    def connectReplicSet(IP, port ,MDsr, MDwd):
        
        from pymongo import MongoClient
        conn =  IP + ':' + port
        client = MongoClient(conn, replicaSet='perconaReplic')
        #client = MongoClient(('mongodb://app_percona:MongoDb095#@192.168.163.130:40017,192.168.163.130:40018,192.168.163.130:40018/?replicaSet=perconaReplic'))

        client.admin.authenticate(MDsr, MDwd)
        return client




