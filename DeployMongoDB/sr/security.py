
'''#############################################################################
# Title: Program deploy replicaset mongodb					
# Description: program automate deploy of 3 MongoDB replication machines  	
# ------------------------------------------------------------------------------
# Module: security.py    					             
# Version: 0.0.1                                                                
#										
# Create Date: 2019/11/06   		                                        
# Modify:                                                                    										
# Modify Date:                                                                                                                                             
#										
# Author: Hudson l. Santos;                                                    
 ###############################################################################'''


class security:


    def createKeyFile():
# generation keyfile for authentication in mongodb replicaset and members

        import os

        print("''")
        print("''")
        print("******** start generate  keyfile  ********")
        print("''")
        try:
            os.system("openssl rand -base64 756 > /mongodb/mongodb.key") #create file mongodbkey for shared password for authenticating other members in the deployment 
            os.system("chmod 400  /mongodb/mongodb.key")  # add permission read in file mongodb.key
        except:
            print("''")
            print("''")
            print("Unable to generation keyfile")
            print("After hit, kindly rotate the robot again.")

        else:
            print("''")
            print("success keyfile generation ")