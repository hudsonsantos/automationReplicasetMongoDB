 
#!/usr/bin/python
# -*- coding: utf-8 -*-
'''#############################################################################
# Title: Program deploy replicaset mongodb					
# Description: program automate deploy of 3 MongoDB replication machines  	
# ------------------------------------------------------------------------------
# Module: dependences.py    					             
# Version: 0.0.1                                                                
#										
# Create Date: 2019/11/03  		                                        
# Modify: Include  findIPHost                                                          										
# Modify Date: 2019/11/03  >  2019/11/04                                                                                                                                         
#										
# Author: Hudson l. Santos;                                                    
 ###############################################################################'''
 
class dependencesSystem:

#### DEPENDENCES MANAGEMENT FOR MONGODB INSTALATION

#Installs wget in Centos or Debian
    def installWgetCentos():
       
        import os

        os.system('yum install wget -y')

    def installWgetDebian():
        import os

        os.system('apt-get install wget -y')
    
#find and return host IP
    def findIPHost():
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        IP = s.getsockname()[0]
        s.close()
        
        return IP


        