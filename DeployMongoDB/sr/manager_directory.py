 
#!/usr/bin/python
# -*- coding: utf-8 -*-
'''#############################################################################
# Title: Program deploy replicaset mongodb					
# Description: program automate deploy of 3 MongoDB replication machines  	
# ------------------------------------------------------------------------------
# Module: manager_diretorry.py    					             
# Version: 0.0.1                                                                
#										
# Create Date: 2019/11/02   		                                        
# Modify: Include alterGroupUserMongoDirectory                                                                    										
# Modify Date: 2019/11/04                                                                                                                                             
#										
# Author: Hudson l. Santos;                                                    
 ###############################################################################'''

class managerDirectory:
 
 # METHOD FOR MANAGER DIRECTORIES (create, delete, alter user/group, alter permission)
   
#create directory for extract packages the perconaMongodb
    def createDirectoryExtract():
           
           import os

           print("''")
           print("''")
           print("******** start create dir /usr/perconaMongodb/ ********")

           os.system('mkdir /usr/perconaMongodb/')
           print("''")
           print("directory create")


#create directory for replication data store 
    def createDirectoryData():
        
        import os

        print ("''")
        print ("''") 
        print ("******** Alterando grupo e dono diretório mongo_data ********")
        try:
            dir = '/mongodb'            #directory path
            os.mkdir(dir)
            os.mkdir(dir + '/node0')    #children directories
            os.mkdir(dir + '/node1')
            os.mkdir(dir + '/node2')
        
        except:
            print ("''")
            print("Directory exists")

    
#alter group and owner  of replicasets directory 
    def alterGroupUserMongoDirectory():
     
        print ("''")
        print ("''") 
        print ("******** Change group and owner of replicasets directories  ********")

        import pwd
        import grp
        import os
        try:
            uid = pwd.getpwnam("mongod").pw_uid
            gid = grp.getgrnam("mongod").gr_gid
            path = "/mongodb"  
            for root, dirs, files in os.walk(path):  
                  for momo in dirs:  
                    os.chown(os.path.join(root, momo), uid, gid)
                    for momo in files:
                        os.chown(os.path.join(root, momo), uid, gid)

        except ValueError:
            print ("''")
            print("unable to change directory group")
            print ("''")

#create directory for files mongo.conf
    def createDirectoryMongoconf():
           
        import os
        print("''")
        print("''")
        print("******** start create dir ectory:  /etc/mongo_config/ ********")
         
        try:
            path = '/etc/mongo_config/'
            os.system('mkdir ' + path)
        except ValueError:
            print ("''")
            print("Fail: create directory mongo_config")
            print ("''")
        else:
            print ("''")
            print("directory create success")
            print ("''")
            return path
