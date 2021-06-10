# Imports Here
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import wget
import os

def instagram_profile_post_downloader():
    # Remember that you can also use Chrome webdriver! so its up to you ;)
    driver = webdriver.Firefox()
    driver.get("https://www.instagram.com/")

    accept_cookies = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//button[text()="Accept All"]'))).click()

    username = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input[name="username"]')))
    password = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'input[name="password"]')))
    username.clear()
    password.clear()
    # your IG username here!
    username.send_keys("HERE")
    # your IG password here!
    password.send_keys("HERE")

    time.sleep(5)

    login_button = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button[type="submit"]'))).click()

    save_info = WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(text(), "Save Info")]'))).click()
    # if you don't want to save your information
    # not_now = WebDriverWait(driver,60).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(text(), "Not Now")]'))).click()

    time.sleep(3)

    # if you want to enable notification
    # turn_on_notif = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(text(),"Turn On")]'))).click()
    turn_off_notif = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(text(),"Not Now")]'))).click()

    # to load posts
    time.sleep(5)

    click_on_profile = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'span[class="_2dbep qNELH"]'))).click()
    profile = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'//div[contains(text(),"Profile")]'))).click()

    time.sleep(4)

    # scroll down to load all components
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    # get posts url
    posts = driver.find_elements_by_tag_name('img')
    posts = [post.get_attribute('src') for post in posts]

    # save them all into the computer
    path = os.getcwd()
    foldername = "myposts"
    path = os.path.join(path,f"{foldername}")
    os.mkdir(path)
    # this is the path your pics will save
    print(path)

    counter = 0
    for post in posts:
        save_as = os.path.join(path,str(counter) + ".jpg")
        wget.download(post,save_as)
        counter += 1

if __name__ == "__main__":
    instagram_profile_post_downloader()

# A Simple Code By ThisMahdi | Telegram : @Thisismahdi
