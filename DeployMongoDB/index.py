'''#############################################################################
# Title: Program deploy replicaset mongodb					
# Description: program automate deploy of 3 MongoDB replication machines  	
# ------------------------------------------------------------------------------
# Module: index.py    					             
# Version: 0.0.1                                                                
#										
# Create Date: 2019/11/08   		                                        
# Modify:                                                                 										
# Modify Date:                                                                                                                                              
#										
# Author: Hudson l. Santos;                                                    
 ###############################################################################'''


# CLASS OF SART ALL SYSTEM
class C_index:
    def cor_index():

        from DeployMongoDB.src.cor import coreDeploy as cd
        cd.coreDeployMongodb()
