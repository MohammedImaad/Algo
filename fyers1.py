from fyers_api import accessToken
from fyers_api import fyersModel
from fyers_api import accessToken
from pyotp import TOTP
from selenium import webdriver
import time
client_id='TAZ287TZUA-100'
secret_id='PPZ5ZG1YAR'
url='https://www.google.com/'
response_type = "code"
grant_type = "authorization_code"
totp='dsadsadsdasa'
pin1='1'
pin2='1'
pin3='1'
pin4='1'
session=accessToken.SessionModel(
    client_id=client_id,
    secret_key=secret_id,
    redirect_uri=url, 
    response_type=response_type,
    grant_type=grant_type
)

response = session.generate_authcode()
print(response)
driver=webdriver.Chrome()
driver.get(response)
driver.find_element("xpath",'//*[@id="mobile-code"]').send_keys('9591461984');
driver.find_element("xpath",'//*[@id="mobileNumberSubmit"]').click();
time.sleep(4)
t=TOTP(totp).now()
print(t)
driver.find_element("xpath",'//*[@id="first"]').send_keys(t[0])
driver.find_element("xpath",'//*[@id="second"]').send_keys(t[1])
driver.find_element("xpath",'//*[@id="third"]').send_keys(t[2])
driver.find_element("xpath",'//*[@id="fourth"]').send_keys(t[3])
driver.find_element("xpath",'//*[@id="fifth"]').send_keys(t[4])
driver.find_element("xpath",'//*[@id="sixth"]').send_keys(t[5])
driver.find_element("xpath",'//*[@id="confirmOtpSubmit"]').click()
time.sleep(3)

