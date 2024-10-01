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

#preenche os campos com os valores extraidos do arquivo
campo_ativo_circulante = driver.find_element(By.ID, 'ativo_circulante')
sleep(1)
campo_ativo_circulante.click()
campo_ativo_circulante.send_keys(ativo_circulante)

campo_caixa_equivalente = driver.find_element(By.ID,'caixa_equivalente')
sleep(1)
campo_caixa_equivalente.click()
campo_caixa_equivalente.send_keys(caixa_equivalente)

campo_contas_receber = driver.find_element(By.ID,'contas_receber')
sleep(1)
campo_contas_receber.click()
campo_contas_receber.send_keys(contas_receber)

campo_estoques = driver.find_element(By.ID,'estoques')
sleep(1)
campo_estoques.click()
campo_estoques.send_keys(estoques)

campo_ativo_nao_circulante = driver.find_element(By.ID,'ativo_nao_circulante')
sleep(1)
campo_ativo_nao_circulante.click()
campo_ativo_nao_circulante.send_keys(ativo_nao_circulante)

campo_imobilizado = driver.find_element(By.ID,'imobilizado')
sleep(1)
campo_imobilizado.click()
campo_imobilizado.send_keys(imobilizado)

campo_intangivel = driver.find_element(By.ID, 'intangivel')
sleep(1)
campo_intangivel.click()
campo_intangivel.send_keys(intangivel)

campo_total_ativo = driver.find_element(By.ID,'total_ativo')
sleep(1)
campo_total_ativo.click()
campo_total_ativo.send_keys(total_ativo)

#clica no botao cadastrar
botao_cadastrar = driver.find_element(By.XPATH,"//button[@class='btn btn-primary']")
sleep(2)
botao_cadastrar.click()




input('aperte ENTER para fechar')
