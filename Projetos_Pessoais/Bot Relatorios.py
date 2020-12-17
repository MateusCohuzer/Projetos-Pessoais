from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

escolha = int(input('[0]- A1\n[1] - A2\n[2] - A3\n[3] - A4\n[4] - A5\n[5] - A6\n[6] - Internos\n[7] - Proj Internos\n[8] - IFR\nR = '))

if escolha < 6:
    seu_nome = input('Seu nome: ')
    clube = input('Clube: ')
    data = int(input('Data: '))
    assunto = input('Assunto: ')
    numero_associados = int(input('Associados: '))
    realizou_projetos = input('Realização de projetos: ')
    associados_projetos = input('Associados Projeto: ')

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://rdaic4630.000webhostapp.com/')
time.sleep(20)
envio_relatorio = driver.find_element_by_xpath('//a[contains(@title, "Envio de Relatório")]')
envio_relatorio.click()
time.sleep(10)

def busca_relatorio(escolha):
    campo_pesquisa = driver.find_elements_by_xpath('//a[contains(@class, "wp-block-button__link has-background")]')
    if escolha == 0:
        campo_pesquisa[0].click()
        senha(escolha)
    elif escolha == 1:
        campo_pesquisa[1].click()
        senha(escolha)
    elif escolha == 2:
        campo_pesquisa[2].click()
        senha(escolha)
    elif escolha == 3:
        campo_pesquisa[3].click()
        senha(escolha)
    elif escolha == 4:
        campo_pesquisa[4].click()
        senha(escolha)
    elif escolha == 5:
        campo_pesquisa[5].click()
        senha(escolha)
    elif 5 < escolha <= 8:
        campo_pesquisa = driver.find_elements_by_xpath('//a[contains(@class, "wp-block-button__link has-text-color has-white-color has-background has-black-background-color")]')
        if escolha == 6:
            campo_pesquisa[0].click()
            senha(escolha)
        elif escolha == 7:
            campo_pesquisa[1].click()
            senha(escolha)
        elif escolha == 8:
            campo_pesquisa[2].click()
            senha(escolha)

def senha(escolha):
    time.sleep(5)
    campo_senha = driver.find_element_by_xpath('//input[contains(@name, "post_password")]')
    if escolha == 0:
        campo_senha.click()
        campo_senha.send_keys('relatorioarea14630')
        campo_senha.send_keys(Keys.ENTER)
    elif escolha == 1:
        campo_senha.click()
        campo_senha.send_keys('relatorioarea24630')
        campo_senha.send_keys(Keys.ENTER)
    elif escolha == 2:
        campo_senha.click()
        campo_senha.send_keys('relatorioarea34630')
        campo_senha.send_keys(Keys.ENTER)
    elif escolha == 3:
        campo_senha.click()
        campo_senha.send_keys('relatorioarea44630')
        campo_senha.send_keys(Keys.ENTER)
    elif escolha == 4:
        campo_senha.click()
        campo_senha.send_keys('relatorioarea54630')
        campo_senha.send_keys(Keys.ENTER)
    elif escolha == 5:
        campo_senha.click()
        campo_senha.send_keys('relatorioarea64630')
        campo_senha.send_keys(Keys.ENTER)
    elif escolha == 6:
        campo_senha.click()
        campo_senha.send_keys('internos4630relatorio')
        campo_senha.send_keys(Keys.ENTER)
    elif escolha == 7:
        campo_senha.click()
        campo_senha.send_keys('relatorioprojetosinternos4630')
        campo_senha.send_keys(Keys.ENTER)
    elif escolha == 8:
        campo_senha.click()
        campo_senha.send_keys('relatorioatividades4630ifr')
        campo_senha.send_keys(Keys.ENTER)
    time.sleep(10)

def enviar_relatorio(escolha):
    if escolha < 6:
        campo_respostas = driver.find_element_by_xpath('//input[contains(@name, "your-name")]')
        campo_respostas.send_keys(seu_nome)

busca_relatorio(escolha)
enviar_relatorio(escolha)
