 
#!/usr/bin/python
# -*- coding: utf-8 -*-
'''#############################################################################
# Title: Program deploy replicaset mongodb					
# Description: program automate deploy of 3 MongoDB replication machines  	
# ------------------------------------------------------------------------------
# Module: install_dependences.py    					             
# Version: 0.0.1                                                                
#										
# Create Date: 2019/11/03  		                                        
# Modify: Include installMongodb > Include installPyMongo, installpip3                                                             										
# Modify Date: 2019/11/03  >  2019/11/04                                                                                                                                         
#										
# Author: Hudson l. Santos;                                                    
 ###############################################################################'''

class installInSystem:

### METHOD FOR INSTALATION OF DEPENDENCÊS 
### Installs wget, mongoDB, PyMongo

    def installWget(operationSystem):        
        
        centos = 'centos'
        debian = 'debian'
        from DeployMongoDB.src.messagens import messagensSystem as ms        #import methods for messagen output
        from DeployMongoDB.src.dependences import dependencesSystem as ds    #import dependênces of system

        if (operationSystem == centos):
             
            ms.loadRequeriments()      # messagen output
 
            ds.installWgetCentos()      #call the method for Wget install in Centos
 
            ms.okRequeriments()         # messagen output

        elif (operationSystem == debian):
            print("DEBIAN")

            ms.loadoperationSystem()    # messagen output

            ds.installWgetDebian()      #call the method for Wget install in Debian

            ms.okRequeriments()         # messagen output



#installs mongod
    def installMongodb():

        import os
        from DeployMongoDB.src.messagens import messagensSystem as ms   #import methods for messagen output
        
        ms.startInstalation()

#start of installation mongodb  
        m_shell = os.system("yum install -y /usr/perconaMongodb/percona-server-mongodb-shell* ")
        m_server = os.system("yum install -y /usr/perconaMongodb/percona-server-mongodb-server*")
        
        if (m_shell == 0 ):
            print("Install mongoShell sucess")
        else: 
            print("error: Check if not exists service mongod")
        
        if (m_server == 0 ):
            print("Install mongoServer sucess")   
        else: 
            print("error: Check if not exists service mongod")
        
            ms.startInstalation()       # messagen output

    def installPyMongo():
        
        import os
        from DeployMongoDB.src.messagens import messagensSystem as ms  #import methods for messagen output
       
        ms.loadRequeriments()     # messagen output
        
 #start of installation pymongo        
        try:
            os.system('python -m pip install pymongo')
        
        except ValueError:
            print("Error installing pymongo")
        else:
            ms.okRequeriments()      # messagen output

    
    def installpip3():

        import os
        from DeployMongoDB.src.messagens import messagensSystem as ms 
        ms.loadRequeriments()     # messagen output

#start of installation pip 
        try:
            os.system('yum install -y python34-setuptools')
            os.system('yum install -y python34-pip')
        
        except:
            print("Error install pip3")
        else:
            ms.loadRequeriments()     # messagen output











