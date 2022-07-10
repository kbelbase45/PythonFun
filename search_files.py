import os
import numpy as np
import pandas as pd
#import pprint  #pretify print


def initialization():
    print('='*57)
    print('|'+' This program finds any files in the given directory   '+'|')
    print('|'+' Input  = Name of a directory                          '+'|')
    print('|'+' Output = Files and all different extensions of files  '+'|')
    print('|'+'        Output_files.csv and All_extension.csv produce '+'|')       )
    print('='*57)
    print()


def print_current_dir():
    current = os.getcwd()
    print(f' Current directory is \n {current}.')
    print('='*50)
    return current

def get_from_directory(name):
    if name == '.' or name == 'here':
        path_dir = os.getcwd()
    else:
        base_dir = name
        #path_dir = os.path.join(os.getenv('HOME'),base_dir+'/.')
    
    print(f' Files are searched in {path_dir}')
    files = os.listdir(path_dir)    
    return files,path_dir

def make_dataFrame(files,path):    
    file_size = [round(item.stat().st_size/1024,1) for item in os.scandir(path)]     
    files_array = np.array(files)        
    df = pd.DataFrame({'Files_Names':files_array,
                       'File Size (MB)':np.array(file_size)},                      
                      columns=['Files_Names','File Size (MB)'],
                      index=[i for i in range(len(files))]
                      )                    
    return df

def check_file_if_already_exist(file_name,current_directory):
    ''' This function check whether or not a requested csv file already exists.  '''
    
    file_exist = os.path.exists(file_name)
    
    if file_exist == True:
        print(file_name+f' is already in the current working directory. ')
        print()
        answer = input('Do want to replace it? (type yes or no) \n\n')  
        if answer == 'yes':
            os.remove(file_name)
        elif answer == 'no': 
            print(f'\n Old file is kept. ')                
        else:
            print(' Answer is not recognized. ')
    elif file_exist == False:               
        answer = 'yes'        
        
    return answer    

def seperate_file_with_extension(files):
    extension        = [os.path.splitext(item)[-1] for item in files]
    extension        = np.array(extension)        
    total_files      = len(files)
    unique_extension = len(np.unique(np.array(extension)))
    unique_list      = np.unique(np.array(extension))
    print()
    print(f' There are total {total_files} files with the following {unique_extension} different extensions.\n\n')
    print( unique_list )
    print()
    
    counting = dict(zip(list(extension),[list(extension).count(i) for i in list(extension)]) )
    df2 = pd.DataFrame(list(counting.items()),columns=['File Extension','Number of Files'])
    df2.to_csv('All_extension.csv',sep='\t')
        

def results():
    current_directory = print_current_dir()        
    name = input(' Where to search files? Give a full path if it is not the current directory.\n\n ')
    files,path = get_from_directory(name)       
    seperate_file_with_extension(files)
    df = make_dataFrame(files,path)    
    answer = check_file_if_already_exist('Output_files.csv',current_directory)
    if answer == 'yes':df.to_csv('Output_files.csv',sep=',')
    
    print()
    print(f' All files of {path} are listed in Output_files.csv file. ')


if __name__=='__main__':
    initialization()
    results()   



