'''
Created on Jun 17, 2012

@author: weinberg

Purpose of this script is to move files from a local storage to a server (ex: media server).
The script will read a listing of directory names from the server then try to find files
matching the name in the local folder.  If some are found it will upload them to the 
appropriate location on the server.
'''
import os, re, shutil, ConfigParser


'''
find a list of files given a path, file types and a regex match
'''
def find_files(path, types, match=''):
    files = os.listdir(path)
    files.sort()
    mylist = []
    
    for f in files:
        if f.endswith(types) and re.search(match, f, re.IGNORECASE):
            src = os.path.join(path, f)
            mylist.append(src)   
    return mylist

'''
find a list of directories given a path
'''            
def find_directories(path):
    dirs =  [ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ]
    return dirs

'''
 generate a list of folders from the server dir, then
 search the temp directorie for any files with those names
 and filetypes
 '''
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
        
'''
main
'''     
if __name__ == '__main__':
    # read config
    config = ConfigParser.RawConfigParser()
    config.read('settings.cfg')
        
    # sort the downloads 
    parse_downloads(config.get('app','server_dir'), config.get('app', 'temp_dir'), tuple(config.get('app', 'file_types').split(',')))
    print "done!"