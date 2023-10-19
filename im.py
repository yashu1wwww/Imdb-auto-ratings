from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time


driver = webdriver.Chrome()
driver.get("https://www.imdb.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.imdb.com%2Fregistration%2Fap-signin-handler%2Fimdb_us&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=imdb_us&openid.mode=checkid_setup&siteState=eyJvcGVuaWQuYXNzb2NfaGFuZGxlIjoiaW1kYl91cyIsInJlZGlyZWN0VG8iOiJodHRwczovL3d3dy5pbWRiLmNvbS90aXRsZS90dDc0Nzk5MDIvcmF0aW5ncy8_cmVmXz1sb2dpbiJ9&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&tag=imdbtag_reg-20") #open your required movie in imdb then click on 
time.sleep(3)

#driver.find_element_by_css_selector('#signin-options > div:nth-child(1) > a:nth-child(1) > span.auth-provider-text').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys('yashu^&*@gmail.com') #enterb your imdb acc mail

time.sleep(3)

driver.find_element_by_xpath('//*[@id="ap_password"]').send_keys('veeru$%^')  #enter your imdb acc pass

time.sleep(2)

driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()

time.sleep(3)

driver.find_element_by_css_selector('#main > section > div > div.subpage_title_block > div > div.ipl-rating-widget > div.ipl-rating-interactive.ipl-rating-interactive--no-rating > label > div.ipl-rating-star.ipl-rating-interactive__star--empty > span.ipl-rating-star__star > svg').click()

time.sleep(3)

driver.find_element_by_css_selector('#ipl-rating-selector-tt7479902 > div.ipl-rating-selector__selector.ipl-rating-selector__wrapper > form > a:nth-child(10) > div.ipl-rating-star.ipl-rating-interactive__star--empty > span.ipl-rating-star__star > svg').click()

time.sleep(5)

#if you want auto review also means below is the code remove the # of starting lines in down 

driver.find_element_by_css_selector('#sidebar > div.aux-content-widget-2.links.subnav > ul > li:nth-child(3) > a').click()

time.sleep(4)

driver.find_element_by_xpath('//*[@id="main"]/section/div[1]/div/a').click()

time.sleep(10)

driver.find_element_by_css_selector('#react-entry-point > div > div > div:nth-child(1) > div.a-section.klondike-contribution-field-section > div:nth-child(1) > input').send_keys("amazing one")

time.sleep(4)

driver.find_element_by_css_selector('#react-entry-point > div > div > div:nth-child(1) > div.a-section.klondike-contribution-field-section > div:nth-child(2) > textarea').send_keys("A character can living in the movie one of the best movie ever watched in my life")

time.sleep(5)

driver.find_element_by_css_selector('#react-entry-point > div > div > div:nth-child(1) > div.a-section.klondike-contribution-field-section > div:nth-child(3) > div > ul > li:nth-child(1) > span.ice-icon-radio-unselected').click()

time.sleep(5)

driver.find_element_by_xpath('//*[@id="react-entry-point"]/div/div/div[2]/span/span/input').click()

time.sleep(30)

driver.close()





