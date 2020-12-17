from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

contatos = ['Helena']
#Nome dos Grupos/Contatos desejados devem estar identicos a no seu Whatsapp
mensagem = str(input(':'))
#Você pode trocar esse input por uma str ou até uma proporção matemática 

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)
#Se quiser aumentar esse tempo, vai do seu processamento

def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    #Ambos os Xpath's servem para encontrar as caixas de busca e mensagem do whatsapp
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    #Pelo dois Xpath's terem o mesmo titulo você os coloca numa lista e busca o desejado, no primeiro caso queremos o primeiro campo que aparece na busca, porém nesse queremos o segundo
    # campo_mensagem[0] == Buscar contatos ; campo_mensagem[1] == escrever a mensagem
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)

for contato in contatos:
    buscar_contato(contato)
    for i in range(2000):
        enviar_mensagem(2 ** i)
