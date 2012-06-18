'''
Created on Jun 17, 2012

@author: weinberg
'''
import os, re, shutil, ConfigParser

def find_files(path, types, match=''):
    files = os.listdir(path)
    files.sort()
    mylist = []
    
    for f in files:
        if f.endswith(str(types)) and re.search(match, f, re.IGNORECASE):
            src = os.path.join(path, f)
            mylist.append(src)   
    return mylist
            
def find_directories(path):
    dirs =  [ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ]
    return dirs

def parse_downloads(server, local, types):    
    shows = find_directories(server)
    for show in shows:
        print "Looking for "+show        
        search = "^"+show.replace(' ', '.');       
        down_list = find_files(local, types, search)
        for item in down_list:
            dst = os.path.join(server, show)
            print "Moving "+item+" to "+dst
            shutil.move(item, dst)
        
if __name__ == '__main__':
    config = ConfigParser.RawConfigParser()
    config.read('settings.cfg')    
    parse_downloads(config.get('app','server_dir'), config.get('app', 'temp_dir'), config.get('app', 'file_types').split(','))