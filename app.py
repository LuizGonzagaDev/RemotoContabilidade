from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#entra no site 
driver = webdriver.Chrome()
driver.get('https://contabil-devaprender.netlify.app/')

#preenche email, senha e entrar

#campo email
campo_email = driver.find_element(By.XPATH,"//input[@type='email']")
sleep(2)
campo_email.click()
campo_email.send_keys('emailfake@hotmail.com')
sleep(2)

#campo senha
campo_senha = driver.find_element(By.XPATH,"//input[@type='password']")
sleep(2)
campo_senha.click()
campo_senha.send_keys('123456')
sleep(2)

#botao entrar
botao_entrar = driver.find_element(By.XPATH,"//button[@class='btn btn-primary w-100']")
botao_entrar.click()
sleep(3)

#cadastra balanço patrimonial
botoes_sistemas = driver.find_elements(By.XPATH,"//a[@class='btn btn-primary mt-auto']")
sleep(2)
botoes_sistemas[0].click()

input('aperte ENTER para fechar')
