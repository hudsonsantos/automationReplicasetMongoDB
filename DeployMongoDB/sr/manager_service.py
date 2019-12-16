
'''#############################################################################
# Title: Program deploy replicaset mongodb					
# Description: program automate deploy of 3 MongoDB replication machines  	
# ------------------------------------------------------------------------------
# Module: start_service.py    					             
# Version: 0.0.1                                                                
#										
# Create Date: 2019/11/03   		                                        
# Modify:  Include serviceReplication                                                                										
# Modify Date:   2019/11/05                                                                                                                                            
#										
# Author: Hudson l. Santos;                                                    
 ###############################################################################'''


class managerService:

### START SERVICES:
    
#service mongodb stand alone
    def serviceStartMongo():      

        import os 
        print ("''")
        print ("''")
        print ("******** Restart service mongod********")  
                
        try:
            start = os.system("systemctl restart mongod")
            if (start == 0 ):
                print ("''")
                print("restart success")
        except:
            print ("''")
            print("error: Check if exists service mongod")

#service mongodb stand alone
    def serviceStopMongo():      

        import os 
        print ("''")
        print ("''")
        print ("******** Stop service mongod********")  
                
        try:
            start = os.system("systemctl stop mongod")
            if (start == 0 ):
                print ("''")
                print("stop service success")
        except:
            print ("''")
            print("error: Check if exists service mongod")

#services of replicationset  mongodb
    def serviceReplication():

        import os

        print ("''")
        print ("''")
        print ("******** start service replication ********")  

        try:
            os.system('mongod --config /etc/mongod.conf --fork')
            os.system('mongod --config /etc/mongo_config/mongod1.conf --fork')
            os.system('mongod --config /etc/mongo_config/mongod2.conf --fork')
        except:
            print ("''")
            print("error: Failed start service replication")
        else:
            print ("''")
            print("service start replication success")


