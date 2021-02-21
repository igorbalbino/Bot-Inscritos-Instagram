'''
Titulo: Criar BOT Inscritos Instagram
Autor: Igor do Espírito Santo
Linguagem: Python
'''

#IMPORTA DEPENDENCIAS NECESSARIAS
from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver import FirefoxOptions
import os;
import time;
import random;
import PySimpleGUI as sg;

def delay():
    time.sleep(random.randint(2, 15))

#CRIA CLASSE QUE CONTEM A LOGICA DO SISTEMA.
class InstagramBot:
    #CRIA FUNCAO CONSTRUTOR
    def __init__(self, username, password, hashtag):
        #DECLARA DADOS NECESSARIOS EM VARIAVEIS
        self.username = username;
        self.password = password;
        self.hashtag = hashtag;

        #REFERENCIA O EDGE COMO NAVEGADOR E EXECUTA O DRIVER NELE
        #COM O EDGE ESTÁ DANDO PROBLEMA. POR ISSO USEI O FIREFOX
        #COM O FIREFOX ESTÁ DANDO PROBLEMA. POR ISSO USEI O CHROME
        #self.driver = webdriver.Edge(executable_path=r'geckodriver\geckodriver.exe');
        #self.driver = webdriver.Firefox(executable_path=r'geckodriver\geckodriver.exe');
        self.driver = webdriver.Chrome(executable_path=r'geckodriver\chromedriver.exe');
    #FECHA __init__

    #CRIA METODO login
    def login(self):
        #PASSA A REFERENCIA DO EDGE COM SELENIUM
        driver = self.driver;
        #COMANDO QUE ABRE O SITE (PRECISA DO LINK)
        driver.get('https://www.instagram.com/');
        delay();

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
        delay();
        self.curtirFotos();
        #FECHA login

    #CRIA FUNCAO curtirFotos
    def curtirFotos(self):
        driver = self.driver;
        #CONCATENA VARIAVEIS E TEXTO
        driver.get('https://www.instagram.com/explore/tags/' + self.hashtag + '/');
        delay();

        #COMANDO PARA DESCER A PAGINA
        for i in range(1, random.randint(5, 28)):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);");
            delay();

        #COMANDO PARA PEGAR ALGO PELA TAG_NAME
        hrefs = driver.execute_script('var as = document.getElementsByTagName("a");'
                                      'var arr = Array.prototype.slice.call(as);'
                                      'console.log(arr);'
                                      'return arr;');

        #EXTRAI APENAS A URL QUE QUEREMOS PARA CURTIR A FOTO
        picHrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in picHrefs if self.hashtag in href]

        for picHref in picHrefs:
            driver.get(picHref);
            delay();
            try:
                driver.find_element_by_xpath('//div/section/span/button[@class="wpO6b "]').click();
                delay();
            except Exception as e:
                delay();
                print(f'DEU ERRO AQUI!!! -> {e}.   /');
            #FECHA try/except
        #FECHA for
    #FECHA curtirFotos

####################################################################

class TelaPython:
    #CRIA FUNCAO CONSTRUTOR
    def __init__(self):
        #LAYOUT
        layout = [
            #CRIA ELEMENTO NA TELA COM UM INPUT PARA RECEBER DADOS
            [sg.Text(f'Olá! Seja bem vindo ao InstaBot.{os.linesep}'
                     f'Como funciona?{os.linesep}'
                     f'Digite o nome de usuário e senha nos respectivos campos.{os.linesep}'
                     f'O campo de hashtag, refere-se à hashtag que o robô irá pesquisar.'
                     f'Após essa pesquisa, o robô irá curtir um número aleatório de postagens relacionadas a essa hashtag.'
                     f'{os.linesep}Assim, algumas páginas responsáveis por postar o que foi curtido, começarão a te seguir.'
                     f'{os.linesep}Clique em "Enviar Dados" e aguarde. O robô irá iniciar.', size=(60, 15))],
            [sg.Text('Usuário', size=(10, 0)), sg.Input(size=(30, 0), key='username')],
            [sg.Text('Senha', size=(10, 0)), sg.Input(size=(30, 0), key='password')],
            [sg.Text('Hashtag (sem o #, apenas letras)', size=(25, 0)), sg.Input(size=(30, 0), key='hashtag')],
            [sg.Button('Enviar Dados',size=(30, 0))]
            #CRIA TELA DE OUTPUT PARA MOSTRAR OS DADOS NO LAYOUT
            #[sg.Output(size=(50, 10))]
        ];
        #JANELA
        #CRIA A TELA E COLOCA OS ELEMENTOS DE LAYOUT NELA
        self.janela = sg.Window('Dados do Usuário').layout(layout);
        #EXTRAIR DADOS DA TELA
        #PEGA OS DADOS DOS INPUTS E USA O METODO READ() NA JANELA PARA GRAVAR OS DADOS
        #self.button, self.values = self.janela.Read();
        #^ ISSO FOI PASSADO PARA DENTRO DE UM "while" NA FUNCAO "Iniciar"

    #FECHA __init__

    def Iniciar(self):
        while True:
            # EXTRAIR DADOS DA TELA
            self.button, self.values = self.janela.Read();
            username = self.values['username'];
            password = self.values['password'];
            hashtag = self.values['hashtag'];

            logBot = InstagramBot(username, password, hashtag);
            logBot.login();
        #FECHA while
    # FECHA Iniciar

#INSTANCIA CLASSE TelaPython EM tela
tela = TelaPython();
tela.Iniciar();