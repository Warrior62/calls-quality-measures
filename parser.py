import os, sys, platform, pathlib, glob

url_repo_github = 'https://github.com/Warrior62/calls-quality-measures.git'
def get_github_repo(url_repo_github):
    if not os.path.exists('calls-quality-measures'):
        os.system('git clone ' + url_repo_github)
    print('get_github_repo')
    
def check_os():
    my_os = platform.system()
    if my_os == 'Windows':
        print('Running on a Windows system...')
    elif my_os == 'Darwin':
        print('Running on a MacOS system...')
    elif my_os == 'Linux':
        print('Running on a Linux system...')
    return my_os
        
github_folder = 'calls-quality-measures'    
def install_python_modules():
    if check_os() == 'Windows':
        if not os.path.exists('.\myenv'):
            os.system('py -m venv .\myenv')
        os.system('.\\myenv\\Scripts\\activate')
    else:
        if not os.path.exists('myenv'):
            os.system('python -m venv myenv')
        os.system('myenv/bin/activate')
    os.system('pip install platform')
    os.system('pip install pandas')
    os.system('pip install selenium')
    os.system('pip install webdriver_manager')
    print('install_python_modules')
    
def download_rainbow_log():
    if os.path.exists('download_log.py'):
        if check_os() == 'Windows':
            os.system('py download_log.py')
        else: 
            os.system('python download_log.py')
    else:
        print('download_log.py file doesn\'t exist !')
        sys.exit(-1)
    print('download_rainbow_log')
        
def get_quality_values():
    if os.path.exists('get_quality_values_rainbow_log.py'):
        if check_os() == 'Windows':
            os.system('py get_quality_values_rainbow_log.py')
        else: 
            os.system('python get_quality_values_rainbow_log.py')
    else:
        print('get_quality_values_rainbow_log.py file doesn\'t exist !')
        sys.exit(-1)
    print('get_quality_values')
    
def delete_last_downloaded_log():
    current_dir_path = str(pathlib.Path().absolute())
    list_of_files = glob.glob(current_dir_path) 
    latest_file = max(list_of_files, key=os.path.getctime)
    os.remove(latest_file)
    print("Latest Log : ", latest_file, 'has been deleted!')

        

get_github_repo(url_repo_github)
install_python_modules()
download_rainbow_log()
get_quality_values()
