from selenium import webdriver
from selenium.webdriver.common.by import By


#entra no site 
driver = webdriver.Chrome()
driver.get('https://contabil-devaprender.netlify.app/')

driver.find_element(By.XPATH,"//input[@type='email']")


input('aperte ENTER para fechar')
