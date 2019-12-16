 
#!/usr/bin/python
# -*- coding: utf-8 -*-
'''#############################################################################
# Title: Program deploy replicaset mongodb					
# Description: program automate deploy of 3 MongoDB replication machines  	
# ------------------------------------------------------------------------------
# Module: check_requeriments.py    					             
# Version: 0.0.1                                                                
#										
# Create Date: 2019/11/03  		                                        
# Modify:                                                          										
# Modify Date:                                                                                                                                      
#										
# Author: Hudson l. Santos;                                                    
 ###############################################################################'''


class checkRequeriments:

### CHECK WHICH OPERATION SYSTEM

    def checkOperationSystem():

        print("''")
        print("''")
        print("******** Start check  Operation System ********")

 #find info system operation   
        path = '/etc/os-release'
        file = open(path, 'r')
        SO = file.readlines()[2]        

#treatment variable OS
        b = '="ID'
        for i in range(0, len(b)):
            SO = SO.replace(b[i], "")
            SO = SO.replace('\n', '')
        
        SO = SO.lower()

#condition for check CentOS or Debian version
        if SO.find("centos") == 0:
            print("''")
            print("Your system is " + SO)
            

        elif SO.find("debian") == 0:
            
            print("''")
            print("Your system is " + SO)
            
        else:
            print("''")
            print("<<<< Your system not compatible with roboth >>>>")
            print(SO)

        return SO

#check Version of operation system
    def requerimentsVersion(operationSystem):

        print("''")
        print("''")
        print("******** Start check version Operation System ********")

#find version info system operation
        path = '/etc/os-release'
        file = open(path, 'r')
        version = file.readlines()[1]

#treatment variable OS
        b = '="(Core)'
        for i in range(0, len(b)):
            version = version.replace(b[i], "")
            version = version.replace('\n', '')
            version = version.strip(" ")

        print("''")     
        print(version)    
        
        return version

#check version Python
    def requerimentsPython():

        print("''")
        print("''")
        print("******** Start check version PYTHON ********")

        import subprocess
    
        version = subprocess.getoutput('python -V')

        if version.find("Python 3") == 0:
            
            print("''")
            print("Python 3 is OK") 

        else:
            print("''")
            print("<<<< Please, check if you in sistem install Python or update the  Python 3 and return the robot start >>>>")
            
            print("<< FINISH >>")
