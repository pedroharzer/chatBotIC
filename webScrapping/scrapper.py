from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
a = True
firefox = webdriver.Firefox()
firefox.get('https://computacao.ufba.br/')
htmls = []
first_time = True

def getAllMenus():
    menus = firefox.find_elements_by_xpath("//li[contains(@class, 'expanded dropdown')]")
    return menus

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
    

def navegarMenuHover(first_time, i,menu_number, class_name, class_name2): #navegar pelos menus, first_time = var de controle pois as classes dos menus mudam i=index de submenus, menu_number = qual menu acessar, class_name e class_name2: diferentes metódos de selecionar menu
    if first_time:
        menu = firefox.find_elements_by_xpath(f"//li[contains(@class, '{class_name}')]")
        if menu_number > 0:
            selectedMenu = menu[menu_number - 1]
        else: selectedMenu = menu[menu_number]
        print('try1')
    else:
        menu = firefox.find_element_by_xpath(f"//li[contains(@class, '{class_name2}')]")
        selectedMenu = menu
        print('execpetd')
    subMenus = selectedMenu.find_elements_by_xpath(".//*")
    hover = ActionChains(firefox).move_to_element(selectedMenu).click()
    hover.perform()
    ul = subMenus[2]
    li = ul.find_elements_by_xpath(".//*")
    li[i].click()
    return li
def getHTML(): #pega o html de cada submenu
    first_time = True
    for index,menu in enumerate(getAllMenus()):
        print(f"index: {index}")
        first_time = True
        li = navegarMenuHover(first_time, 0,index,'expanded dropdown', 'expanded active-trail dropdown')
        step = range(0, len(li), 2)
        print(len(li))
        for i in step:
            print(f"i: {i}")
            first_time = False
            navegarMenuHover(first_time, i, index,'expanded dropdown', 'expanded active-trail dropdown')
            WebDriverWait(firefox,50).until(
                EC.element_to_be_clickable((
                    By.CLASS_NAME, 'page-header'
                ))
            )
            html = firefox.page_source
            infos = getTextFromHTML(html)
            if infos != {}:
                htmls.append()
getHTML()
print(htmls)

