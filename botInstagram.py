'''
Titulo: Criar BOT Inscritos Instagram
Autor: Igor do Espírito Santo
Linguagem: Python
'''

#IMPORTA DEPENDENCIAS NECESSARIAS
from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
import time;

#CRIA CLASSE QUE CONTEM A LOGICA DO SISTEMA.
class InstagramBot:
    #CRIA FUNCAO CONSTRUTOR
    def __init__(self, username, password):
        #DECLARA DADOS NECESSARIOS EM VARIAVEIS
        self.username = username;
        self.password = password;

        #REFERENCIA O EDGE COMO NAVEGADOR E EXECUTA O DRIVER NELE
        #COM O EDGE ESTÁ DANDO PROBLEMA. POR ISSO USEI O FIREFOX
        #DEPENDENCIA DO EDGE FOI BAIXADA DO SITE https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
        #self.driver = webdriver.Edge(executable_path=r'C:\Users\igorb\Documents\GitHub\Bot-Inscritos-Instagram\geckodriver\geckodriver.exe');
        self.driver = webdriver.Firefox(executable_path=r'C:\Users\igorb\Documents\GitHub\Bot-Inscritos-Instagram\geckodriver\geckodriver.exe');
    #FECHA __init__

    '''
    # DADOS NECESSARIOS E PROPRIEDADE UNICA

    # //div(@class='Igw0E IwRSH eGOV_ _4EzTm')

    # //submit(@type='submit')
    # //input(@name='username')
    # //input(@name='password')
    '''

    #CRIA METODO login
    def login(self):
        #PASSA A REFERENCIA DO EDGE COM SELENIUM
        driver = self.driver;
        #COMANDO QUE ABRE O SITE (PRECISA DO LINK)
        driver.get('https://www.instagram.com/');
        #PARA O BOT POR 2 SEG
        time.sleep(2);
        '''
        #REFERENCIA BOTAO SUBMIT DO LOGIN
        login_button = driver.find_element_by_xpath("//submit(@type='submit')");
        login_button.click();
        '''

        #REFERENCIA ELEMENTO INPUT-USERNAME
        #LIMPA O CAMPO
        #ENVIA O VALOR PARA O CAMPO
        user_element = driver.find_element_by_xpath("//input[@name='username']");
        user_element.clear();
        user_element.send_keys(self.username);

        # REFERENCIA ELEMENTO INPUT-PASSWORD
        # LIMPA O CAMPO
        # ENVIA O VALOR PARA O CAMPO
        pass_element = driver.find_element_by_xpath("//input[@name='password']");
        pass_element.clear();
        pass_element.send_keys(self.password);
        #SIMULA CLICK DO BOTÃO ENTER DO TECLADO
        pass_element.send_keys(Keys.RETURN);
        time.sleep(5);
        self.curtirFotos("memesbr");
        #FECHA login

    #CRIA FUNCAO curtirFotos
    def curtirFotos(self, hashtag):
        driver = self.driver;
        #CONCATENA VARIAVEIS E TEXTO
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/');
        time.sleep(5);

        #COMANDO PARA DESCER A PAGINA
        for i in range(1,3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);");
            time.sleep(5);
        #COMANDO PARA PEGAR ALGO PELA TAG_NAME
        hrefs = driver.find_element_by_tag_name('a');
        #EXTRAI APENAS A URL QUE QUEREMOS PARA CURTIR A FOTO
        picHrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in picHrefs if hashtag in href]
        #PRINTA VALOR NO CONSOLE
        print('hashtag: ' + hashtag + ' fotos: ' + str(len(picHrefs)));

        for picHref in picHrefs:
            driver.get(picHref);
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);");
            time.sleep(5);
            #ALTERNATIVO
            # driver.find_element_by_class_name('//svg[@class="_8-yf5 "]').click();
            try:
                time.sleep(3);
                driver.find_element_by_class_name('//button[@class="wpO6b "]').click();
                time.sleep(10);
            except Exception as e:
                time.sleep(5);
                print('DEU ERRO AQUI!!! - ' + e + '.   /');
        #FECHA curtirFotos

igorBot = InstagramBot('SEU_LOGIN','SUA_SENHA');
igorBot.login();