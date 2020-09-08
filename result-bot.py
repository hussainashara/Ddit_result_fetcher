import pytesseract as tess
from pytesseract import image_to_string
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)
driver.get('https://egov.ddit.ac.in/index.php?r=site/login')


# -----------------------------------------------------------------
username1 = "YOUR USERNAME"  # write your username here
password1 = "YOUR PASSWORD"  # write your password here
# -----------------------------------------------------------------


def login(username, password):
    time.sleep(2)
    driver.find_element_by_xpath('//*[(@id = "yw0")]').screenshot('screenshot.png')
    text = tess.image_to_string(Image.open('screenshot.png'))
    text = text.replace(" ", "")
    username = driver.find_element_by_css_selector('#LoginForm_username').clear()
    username = driver.find_element_by_css_selector('#LoginForm_username').send_keys(username1)
    passs = driver.find_element_by_css_selector('#LoginForm_password').clear()
    passs = driver.find_element_by_css_selector('#LoginForm_password').send_keys(password1)
    captcha = driver.find_element_by_css_selector('#LoginForm_verifyCode').clear()
    time.sleep(2)
    captcha = driver.find_element_by_css_selector('#LoginForm_verifyCode').send_keys(text)
    btn = driver.find_element_by_css_selector('#yw1').click()
    time.sleep(2)
    try:
        exameresults = driver.find_element_by_css_selector('li:nth-child(3) a').click()
    except:
        driver.find_element_by_css_selector('#yw0_button').click()
        login(username1, password1)


login(username1, password1)
time.sleep(2)
inter = driver.find_element_by_css_selector('#yt7').click()
time.sleep(1)
handle = driver.window_handles
driver.switch_to.window(handle[1])
driver.maximize_window()
driver.execute_script("window.scrollBy(0,100)", "")
driver.find_element_by_css_selector('#tblintexamresulttxn-grid , td , .summary').screenshot('result.png')
driver.quit()
