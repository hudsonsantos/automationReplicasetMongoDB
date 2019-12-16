 
#!/usr/bin/python
# -*- coding: utf-8 -*-
'''#############################################################################
# Title: Program deploy replicaset mongodb					
# Description: program automate deploy of 3 MongoDB replication machines  	
# ------------------------------------------------------------------------------
# Module: downloads.py    					             
# Version: 0.0.1                                                                
#										
# Create Date: 2019/11/03  		                                        
# Modify: Include installMongodb > Include installPyMongo, installpip3                                                             										
# Modify Date: 2019/11/03  >  2019/11/04                                                                                                                                         
#										
# Author: Hudson l. Santos;                                                    
 ###############################################################################'''


class downloadsSystem:
    
### PACKAGE DOWNLOAD CONCENTRATION METHODS

#check version and download mongdb
#download mongodb version CentoOS

    def downloadMongo(operationSystem, version):
        
        import os
        v_centos      = 'centos'
        v_debian      = 'debian'
        v_cv6           = 'VERSION6'
        v_cv7           = 'VERSION7'
        v_cv8           = 'VERSION8'
        v_dv9           = 'VERSION9'
        v_dv10         = 'VERSION10'
        
        print("''")
        print("''")
        print("******** Start download mongoDB ********")
       
        from DeployMongoDB.src.messagens import messagensSystem as ins #import menssagens for output
        ins.startDownload()

#check the version of operation system for mongodb package download
        if (operationSystem == v_centos):
       
            if (version == v_cv6):

               os.system('wget https://www.percona.com/downloads/percona-server-mongodb-LATEST/percona-server-mongodb-4.2.0-1/binary/redhat/6/x86_64/percona-server-mongodb-4.2.0-1-r74f753a-el6-x86_64-bundle.tar')
            
            elif (version == v_cv7):

                os.system('wget https://www.percona.com/downloads/percona-server-mongodb-LATEST/percona-server-mongodb-4.2.0-1/binary/redhat/7/x86_64/percona-server-mongodb-4.2.0-1-r74f753a-el7-x86_64-bundle.tar')
            
            elif (version == v_cv8):
             
                os.system('wget https://www.percona.com/downloads/percona-server-mongodb-LATEST/percona-server-mongodb-4.2.0-1/binary/redhat/8/x86_64/percona-server-mongodb-4.2.0-1-r74f753a-el8-x86_64-bundle.tar')
        
        else:
            
            if (version == v_dv9):
                print('error')
                os.system('wget https://www.percona.com/downloads/percona-server-mongodb-LATEST/percona-server-mongodb-4.2.0-1/binary/debian/stretch/x86_64/percona-server-mongodb-4.2.0-1-r74f753a-stretch-x86_64-bundle.tar')
            elif (version == v_dv10):
                print('error10')
                os.system('wget https://www.percona.com/downloads/percona-server-mongodb-LATEST/percona-server-mongodb-4.2.0-1/binary/debian/buster/x86_64/percona-server-mongodb-4.2.0-1-r74f753a-buster-x86_64-bundle.tar')

        from DeployMongoDB.src.messagens import messagensSystem as ins 
        ins.finishDownload()