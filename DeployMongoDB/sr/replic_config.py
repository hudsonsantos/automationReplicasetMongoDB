'''#############################################################################
# Title: Program deploy replicaset mongodb                  
# Description: program automate deploy of 3 MongoDB replication machines    
# ------------------------------------------------------------------------------
# Module: replic_config.py                                   
# Version: 0.0.1                                                                
#                                       
# Create Date: 2019/11/07                                                   
# Modify:                                                                                                         
# Modify Date:                                                                                                                                              
#                                       
# Author: Hudson l. Santos;                                                    
 ###############################################################################'''

class managerReplicConfig:

    def startReplics(IP, port, MDsr, MDwd):

        from DeployMongoDB.src.connections import connectDatabase as cd  
        conn = cd.connectNewUser(IP, port, MDsr, MDwd) #method log in on mongodb using autentication, Ip host and new port set in mongo.conf

        print ("''")
        print ("''")
        print ("******** start configuration replication mongodb ********")  

        config = {'_id': 'perconaReplic'}
        port ='47017'
        #y=7
        members = []

        #for x in range (0,3):
        host = {'_id' : 0, 'host': IP + ':' + port}
        host.update(host)
            #y+=1
        members.append(host)
        config["members"] = members

        conn.admin.command('replSetInitiate', config)
        
        #conf = conn.admin.command({'replSetGetConfig': 1})
        #print(conf['config']['members'])
        
        import pymongo
        #conn = pymongo.MongoClient()
        conf = conn.admin.command({'replSetGetConfig': 1})
        

        port ='4701'
        y=8
        members = []           

        for x in range (1,3):
            host = {'_id' : x, 'host': IP + ':' + port + str(y) }#, "hidden": True , "priority": 0}
            host.update(host)
            conf['config']['members'].append(host)          

            conf['config']['version'] += 1  # Bump the config version          

            conn.admin.command({'replSetReconfig': conf['config']})
            y += 1         

        conf = conn.admin.command({'replSetGetConfig': 1})
        print(conf['config']['members'])

        conn.close()
        