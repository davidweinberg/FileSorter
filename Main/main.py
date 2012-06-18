'''
Created on Jun 17, 2012

@author: weinberg
'''
import os
import re
import shutil

DOWNLOADS_PATH = "C:\\Users\\weinberg\\Downloads"
SERVER_PATH = "J:\\tv"
FILE_TYPES = "avi", "mkv", "mp4"

def find_files(path, types, match=''):
    files = os.listdir(path)
    files.sort()
    mylist = []
    
    for f in files:
        if f.endswith(types) and re.search(match, f):
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
        search = show.replace(' ', '.')        
        down_list = find_files(local, types, search)
        for item in down_list:
            dst = os.path.join(server, show)
            print "Moving "+item+" to "+dst
            shutil.move(item, dst)
        
if __name__ == '__main__':
    parse_downloads(SERVER_PATH, DOWNLOADS_PATH, FILE_TYPES)