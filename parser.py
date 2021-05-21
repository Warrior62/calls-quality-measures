import os, sys

url_repo_github = 'https://github.com/Warrior62/calls-quality-measures.git'
def get_github_repo(url_repo_github):
    if not os.path.exists('calls-quality-measures'):
        os.system('git clone ' + url_repo_github)
    print('get_github_repo')
    
github_folder = 'calls-quality-measures'    
def install_python_modules():
    if not os.path.exists('.\myenv'):
        os.system('py -m venv .\myenv')
    os.system('.\\myenv\\Scripts\\activate')
    os.chdir(github_folder)
    os.system('pip install pandas')
    os.system('pip install selenium')
    os.system('pip install webdriver_manager')
    print('install_python_modules')
    
def download_rainbow_log():
    if os.path.exists('download_log.py'):
        os.system('py download_log.py')
    else:
        print('download_log.py file doesn\'t exist !')
        sys.exit(-1)
    print('download_rainbow_log')
        
def get_quality_values():
    if os.path.exists('get_quality_values_rainbow_log.py'):
        os.system('py get_quality_values_rainbow_log.py')
    else:
        print('get_quality_values_rainbow_log.py file doesn\'t exist !')
        sys.exit(-1)
    print('get_quality_values')
        

get_github_repo(url_repo_github)
install_python_modules()
download_rainbow_log()
get_quality_values()

