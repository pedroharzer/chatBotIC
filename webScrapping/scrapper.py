from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

firefox = webdriver.Firefox()
firefox.get('https://computacao.ufba.br/')
htmls = []

def cleanHTML(html): #limpar HTML
    cleanText = html.replace("\n", " ")
    cleanText2 = cleanText.replace("\t", "")
    cleanText3 = cleanText2.replace("\xa0", "")
    return cleanText3
        
            
def getTextFromHTML(html): #converter o html limpo para um dict separado em topico e texto
    try:
        soup = BeautifulSoup(html, 'html.parser')
        topico = soup.find(class_ = 'page-header').get_text()
        text = soup.find(class_ = 'field-item').get_text()
        dict = {
            'topico' : topico,
            'texto' : cleanHTML(text)
        }
        return dict
    except:
        dict = {}
        return dict
    

def navegarMenuHover(i,menu_number, class_name, class_name2): #navegar pelos menus, i=index de submenus, menu_number = qual menu acessar, class_name e class_name2: diferentes metódos de selecionar menu
    try:
        menu = firefox.find_elements_by_xpath(f"//li[contains(@class, '{class_name}')]")
        selectedMenu = menu[menu_number]
    except:
        menu = firefox.find_element_by_xpath(f"//li[contains(@class, '{class_name2}')]")
        selectedMenu = menu
    subMenus = selectedMenu.find_elements_by_xpath(".//*")
    hover = ActionChains(firefox).move_to_element(selectedMenu).click()
    hover.perform()
    ul = subMenus[2]
    li = ul.find_elements_by_xpath(".//*")
    li[i].click()
    return li
def getHTML(): #pega o html de cada submenu
    li = navegarMenuHover(0,1,'expanded dropdown active', 'expanded active-trail dropdown')
    step = range(0, len(li), 2)
    for i in step:
        navegarMenuHover(i, 1,'expanded dropdown active', 'expanded active-trail dropdown')
        WebDriverWait(firefox,50).until(
            EC.element_to_be_clickable((
                By.CLASS_NAME, 'page-header'
            ))
        )
        html = firefox.page_source
        htmls.append(getTextFromHTML(html))
getHTML()
print(htmls)
