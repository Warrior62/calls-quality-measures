import sys, os, csv, glob, time, shutil, pathlib

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

<<<<<<< HEAD


mail_login = input('Rainbow mail adress: ')
pwd_login = input('Rainbow password: ')
=======
mail_login = input("Rainbow mail address: ")
pwd_login = input("Rainbow password: ")
>>>>>>> 3837048ab7f5f75e99e40fe3ce5ba9dacd3f4738

rainbow_url = "https://web.openrainbow.com"

#object of ChromeOptions
op = webdriver.ChromeOptions()
current_dir_path = str(pathlib.Path().absolute())
#set download directory path
p = {"download.default_directory": current_dir_path,"safebrowsing.enabled":"false"}
#adding preferences to ChromeOptions
op.add_experimental_option("prefs", p)

driver = webdriver.Chrome(executable_path="chromedriver.exe", options=op)
driver.get(rainbow_url)


                         
def watchdog():
    can_continue = "N"
    while can_continue == "N":
        can_continue = input("Est-ce qu'au moins 1 appel a été passé depuis l'exécution du programme ? [y/N]")
    return True

def login():
    mail_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="username"]'))
            )
    mail_input.send_keys(mail_login)
    time.sleep(1)
    go_on_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="form"]/footer/square-button'))
            )
    go_on_btn.click()
    time.sleep(1)
    pwd_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="authPwd"]'))
            )
    pwd_input.send_keys(pwd_login)
    time.sleep(1)
    login_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="form"]/footer/square-button'))
            )
    login_btn.click()
    time.sleep(1)
    print("Authenticated!")
    
def get_home_page():
    try:
        close_new_features_window_btn = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="popup"]/userwindow/userwindow-footer/square-button'))
                )
        close_new_features_window_btn.click()
        time.sleep(1)
        print("Home page displayed!")
    except Exception as e:
        print(e)
        print("Home page not displayed!")
        exit(-1)
        
def get_profile_list():
    pic_profile = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/header/section/user-menu/div'))
                )
    pic_profile.click()
    time.sleep(1)
    print("Profile list displayed!")
    
def get_about_rainbow_page():
    about_rainbow = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="userAreaMenu"]/dropdown-item[7]/div'))
                )
    about_rainbow.click()
    time.sleep(1)
    print("About Rainbow page displayed!")
    
def download_log():
    #driver = webdriver.Chrome(executable_path="chromedriver.exe", options=op)
    save_log_btn = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="popup"]/userwindow/userwindow-content/div[2]/settingsabout/div/square-button'))
                )
    save_log_btn.click()
    time.sleep(2)
    print("Log was downloaded!")



if __name__ == "__main__":
    login()
    get_home_page()
    can_start_flag = watchdog()
    if can_start_flag == True:
        get_profile_list()
        get_about_rainbow_page()
        download_log()
        time.sleep(3)
        driver.close()
        print("--> PLEASE RUN get_quality_values_rainbow_log.py")
