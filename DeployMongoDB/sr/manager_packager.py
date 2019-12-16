#!/usr/bin/python
# -*- coding: utf-8 -*-
'''#############################################################################
# Title: Program deploy replicaset mongodb					
# Description: program automate deploy of 3 MongoDB replication machines  	
# ------------------------------------------------------------------------------
# Module: manager_packager.py    					             
# Version: 0.0.1                                                                
#										
# Create Date: 2019/11/03   		                                        
# Modify:     copyReplicationMongoconf                                                                 										
# Modify Date:  2019/11/06                                                                                                                                            
#										
# Author: Hudson l. Santos;                                                    
 ###############################################################################'''


class manager:

# METHODS FOR MANAGER FILES IN SYSTEM OPERATION

#copy download package for directory /usr/perconaMongodb
    def copyFile():
        try:
            print("''")
            print("''")
            print("******** start transfer package for /usr/perconaMongodb/ ********")
            print("''")

            import shutil
            import os
            import fnmatch

            file_package = "percona-server*"
            path_destination = ("/usr/perconaMongodb/percona.tar")

            listOfFiles = os.listdir('.')                   #function for find package name
            for package in listOfFiles:
                if fnmatch.fnmatch(package, file_package):

                    path_target = os.path.dirname(os.path.realpath(
                        file_package))                       #function find directory
                    path_target = path_target + '/' + package
                                                             #function copy file for path_destination
                    shutil.copyfile(package, path_destination)

        except ValueError:
            print("''")
            print("''")
            print("Unable to back up file, please check user permissions on folder")
            print("After hit, kindly rotate the robot again.")

        else:
            print("''")
            print(path_destination)
            print("''")
            print("copy file success")
            

#extract package of download
    def extractFile():
        
        print("''")
        print("''")
        print("******** extract file in /usr/perconaMongodb/ ********")
        import tarfile

        path_destination = "/usr/perconaMongodb/"    
        path_file = "/usr/perconaMongodb/percona.tar"

        tar = tarfile.open(path_file)           #extract file in path_destination
        tar.extractall(path_destination)
        tar.close()

        print("''")
        print("file extract with sucess")


#security copy file mongo.conf to directory of replication the file conf
    def copyMongoconf(pathDirConf):
        try:
            print("''")
            print("''")
            print("******** start backup file mongo.conf  ********")
            print("''")

            import shutil
            import os
            import fnmatch

            file_package = "mongod.conf"
            path = '/etc/'
            path_destination = pathDirConf   
            
            listOfFiles = os.listdir(path)     #function for find package or file name
            for package in listOfFiles:
                if fnmatch.fnmatch(package, file_package):
  
                    path_target = path + package                                    #variable indicate source directory + name mongod.conf
                    path_destination2 = path_destination + file_package  #variable indicate destination directory for monogod.conf
                                         
                    shutil.copyfile(path_target, path_destination2)                 #function copy file for path_destination

        except:
            print("''")
            print("''")
            print("Unable to back up file, please check user permissions on folder")
            print("After hit, kindly rotate the robot again.")

        else:
            print("''")
            print("copy file success")
        
        return path_destination, file_package



#replication copy files  mongo.conf to set configure replics
    def copyReplicationMongoconf( path_source, file_package):


        import shutil
        import os
        import fnmatch

        try:
            print("''")
            print("''")
            print("******** start replication the files mongo.conf  ********")
            print("''")

            path_file = path_source        #path and name file mongod.conf
            file_package = path_file + file_package         #name file

            #file breaking and extension
            for p, _, files in os.walk(os.path.abspath(path_file)):

                for file in files:
                    #path_full= os.path.join(p, file)               #full path    
                    path = os.path.join(p)              
                    explod_file = file.split('.')                    #delimitator
                    only_name = '.'.join(explod_file[:-1])  #file name
                    extension = explod_file[-1]                 #extension name

                    for x in range(1,3):                               # concat name file, number file and extension and create config files replicaset
                                            
                        shutil.copyfile(file_package, path + '/' + only_name + str(x) + '.' + extension)

        except:
            print("''")
            print("''")
            print("Unable to copy file, please check user permissions on folder")
            print("After hit, kindly rotate the robot again.")

        else:
            print("''")
            print("copy file success")



 



'''
    def extractFile():
        import zipfile
        path_destination = ("/usr/perconaMongodb/percona.tar" )   # directory destination
        mongo_zip = zipfile.ZipFile(path_destination
        fmongo_zip.extractall(path_destination + '/percona')
 
        fantasy_zip.close() 

'''