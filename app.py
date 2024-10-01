from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from docx import Document

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

# extraindo os dados do arquivo word
caminho_arquivo_word = r'C:\Users\Luiz\Documents\GitHub\RemotoContabilidade\relatorios\Relatorio_Contabilidade_Delícias_Foodie.docx'
arquivo_word = Document(caminho_arquivo_word)

ativo_circulante = ''
caixa_equivalente = ''
contas_receber = ''
estoques = ''
ativo_nao_circulante = ''
imobilizado = ''
intangivel = ''
total_ativo = ''

for tabela in arquivo_word.tables:
    for linha in tabela.rows:
        if 'Ativo Circulante' in linha.cells[0].text.strip():
            ativo_circulante = linha.cells[1].text.strip()
        elif 'Caixa e Equivalentes' in linha.cells[0].text.strip():
            caixa_equivalente = linha.cells[1].text.strip()
        elif 'Contas a Receber' in linha.cells[0].text.strip():
            contas_receber = linha.cells[1].text.strip()
        elif 'Estoques' in linha.cells[0].text.strip():
            estoques= linha.cells[1].text.strip()
        elif 'Ativo Não Circulante' in linha.cells[0].text.strip():
            ativo_nao_circulante= linha.cells[1].text.strip()
        elif 'Imobilizado' in linha.cells[0].text.strip():
            imobilizado= linha.cells[1].text.strip()
        elif 'Intangível' in linha.cells[0].text.strip():
            intangivel= linha.cells[1].text.strip()
        elif 'Total do Ativo' in linha.cells[0].text.strip():
            total_ativo= linha.cells[1].text.strip()

input('aperte ENTER para fechar')
