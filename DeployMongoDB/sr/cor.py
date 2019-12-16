#!/usr/bin/python
# -*- coding: utf-8 -*-
'''#############################################################################
# Title: Program deploy replicaset mongodb					
# Description: program automate deploy of 3 MongoDB replication machines  	
# ------------------------------------------------------------------------------
# Module: cor.py    					             
# Version: 0.0.1                                                                
#										
# Create Date: 2019/11/03  		                                        
# Modify: Include methods                                                         										
# Modify Date: 2019/11/08                                                                                                                                   
#										
# Author: Hudson l. Santos;                                                    
 ###############################################################################'''


class coreDeploy:

    def coreDeployMongodb():
        import os
        print("Importando modulos,  aguarde ... ")
        IP_new = ''
        fileDest = ''


        
        # Return on the requeriments of operational system
        # find operational system 
        from DeployMongoDB.src.check_requeriments import checkRequeriments as cr
        operationSystem = cr.checkOperationSystem()
        operationSystem

        # check python version - (requeriment python 3)
        cr.requerimentsPython()

        # install dependences
        from DeployMongoDB.src.install_dependences import installInSystem as ins
        ins.installWget(operationSystem)  

        #search version based on input which is operating system
        version = cr.requerimentsVersion(operationSystem)
        
        #download mongodb based on version
        from DeployMongoDB.src.downloads import downloadsSystem as dls
        dls.downloadMongo(operationSystem, version)

        #create directory extract package 
        from DeployMongoDB.src.manager_directory import managerDirectory as md
        md.createDirectoryExtract()

        #copy file mongodb download for new directory
        from DeployMongoDB.src.manager_packager import manager as mn
        mn.copyFile()

        #extract file mongodb download in new directory
        mn.extractFile()

        #Instalation mongoDB
        ins.installMongodb()

        #start mongod
        from DeployMongoDB.src.manager_service import managerService as ss
        ss.serviceStartMongo()    

        #create directory for replication
        md.createDirectoryData()
         
        #create security file       
        from DeployMongoDB.src.security import security as s
        s.createKeyFile()

        #alter group and owner of replicasets directory
        md.alterGroupUserMongoDirectory()
      
        # Install requeriment pip3 for download pymongo
        ins.installpip3()

        # install requeriment pymongo for connect in mongodb
        ins.installPyMongo()

        #create user in mongodb
        from DeployMongoDB.src.manager_user import managerMongodb as mnm
        MDsr, MDwd = mnm.addUserMongodb()

        # find IP host
        from DeployMongoDB.src.dependences import  dependencesSystem as fip
        IP = fip.findIPHost()
       
        #change mongo.conf for IP host
        from DeployMongoDB.src.mongo_conf import managerMongoConf as cp
        port = cp.reconfigureMongoConf(IP)
        
        # restart service mongod
        ss.serviceStartMongo() 

        #testing new user
        mnm.testNewUser(IP, port, MDsr, MDwd )

        #create directory for mongo.conf of replicaset
        pathDirConf = md.createDirectoryMongoconf()

        #copy mongo.conf for path
        path_destination, file_package = mn.copyMongoconf(pathDirConf)

        #create copy config files replicaset
        mn.copyReplicationMongoconf(path_destination, file_package)
       
        #configure mongo.conf dbpath replicasets
        cp.reconfigureDbpath(path_destination)

        #configure mongo.conf port replicasets
        cp.reconfigureMongoPorts(path_destination)
        
        # stop services  mongodb
        ss.serviceStopMongo()

        # start services  replication mongodb
        ss.serviceReplication()
           
        #start replication and add members
        from  DeployMongoDB.src.replic_config import  managerReplicConfig as mrc 
        mrc.startReplics(IP, port , MDsr, MDwd)

        #insert 1000 rows in mongodb replic
        from DeployMongoDB.src.querys import querys as q
        q.insert1000(IP, port , MDsr, MDwd)

        
        print ("'*****************************************'")
        print ("* IP: " + IP)
        print ("* PORT: " + port)
        print ("* USER :" + MDsr)
        print ("* PASSWORD :" + MDwd)
        print ("'*****************************************'")

        


        
