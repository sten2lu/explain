# Carsten Lueth @ 23.05.2021
import os
import datetime
from argparse import ArgumentParser 
import json
import time

parser = ArgumentParser()
parser.add_argument('name', default=None,type=str )
parser.add_argument('--new', '-n', action="store_true") # Boolean which is true if new one should be created
parser.add_argument('--list', '-l', action="store_true") # Boolean which is true if elemnts should be listed
parser.add_argument('--search', '-s', action="store_true") # searches in database for the correct value
parser.add_argument('--path', '-p', default=None ,type=str) # allows to set new path  

with open('config.json', 'r') as file:
    config = json.load(file)
base_path = config['path']
editor = config['editor']
writer = config['name']

tail = {'tags' : ['tag1', 'tag2']}

def open_text(base_path, name, editor='subl'):
    f_path = os.path.join(base_path, name)
    if not os.path.isfile(f_path):
        create_template(f_path)
    os.system('{} {}'.format(editor, f_path))

def create_template(f_path):
    with open(f_path, 'w') as file:
            file.write('{} @ {}\n\n'.format(writer, str(datetime.datetime.today()).split()[0] ))
            file.write('##')
            for i in range(7):
                file.write('\n')
            file.write('-'*10)
            file.write('\n{} \n'.format(tail))
            file.write('-'*20)
    
    time.sleep(0.01)

def list_files(path):
    for file in os.listdir(path):
        print(file)

def search_files(path, name):
    pass

    
    
if __name__ == '__main__':
    args = parser.parse_args()
    name = args.name
    f_new = args.new 
    f_list = args.list 
    f_search = args.search

    if f_list:
        list_files(base_path)
    elif f_search:
        search_files(base_path, name)
    else:
        open_text(base_path, name, editor=editor)


    
