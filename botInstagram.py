'''
Titulo: Criar BOT Inscritos Instagram
Autor: Igor do Espírito Santo
Linguagem: Python
'''

#IMPORTA DEPENDENCIAS NECESSARIAS
from selenium import webdriver;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver import FirefoxOptions
import time;
import PySimpleGUI as sg;

#CRIA CLASSE QUE CONTEM A LOGICA DO SISTEMA.
class InstagramBot:
    #CRIA FUNCAO CONSTRUTOR
    def __init__(self, username, password, hashtag):
        #DECLARA DADOS NECESSARIOS EM VARIAVEIS
        self.username = username;
        self.password = password;
        self.hashtag = hashtag;

        opts = FirefoxOptions()
        opts.add_argument("--headless")

        #REFERENCIA O EDGE COMO NAVEGADOR E EXECUTA O DRIVER NELE
        #COM O EDGE ESTÁ DANDO PROBLEMA. POR ISSO USEI O FIREFOX
        #DEPENDENCIA DO EDGE FOI BAIXADA DO SITE https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
        #self.driver = webdriver.Edge(executable_path=r'geckodriver\geckodriver.exe');
        self.driver = webdriver.Firefox(executable_path=r'geckodriver\geckodriver.exe');
        #self.driver = webdriver.Chrome(executable_path=r'geckodriver\geckodriver.exe');
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
        self.curtirFotos();
        #FECHA login

    #CRIA FUNCAO curtirFotos
    def curtirFotos(self):
        driver = self.driver;
        #CONCATENA VARIAVEIS E TEXTO
        driver.get('https://www.instagram.com/explore/tags/' + self.hashtag + '/');
        time.sleep(5);

        #COMANDO PARA DESCER A PAGINA
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);");
            time.sleep(5);
        #COMANDO PARA PEGAR ALGO PELA TAG_NAME
        hrefsList = [];
        hrefs = driver.find_element_by_tag_name('a');
        print(type(hrefs))
        #EXTRAI APENAS A URL QUE QUEREMOS PARA CURTIR A FOTO
        picHrefs = [elem.get_attribute('outerHTML') for elem in hrefs]
        [href for href in picHrefs if self.hashtag in href]
        print('PicHrefs: -> '+picHrefs);
        hrefsList.append(picHrefs.text);
        print('hrefsList: -> '+hrefsList)

        for picHref in hrefsList:
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

#logBot = InstagramBot('SEU_LOGIN','SUA_SENHA');
#logBot.login();

####################################################################
####################################################################
####################################################################

class TelaPython:
    #CRIA FUNCAO CONSTRUTOR
    def __init__(self):
        #LAYOUT
        layout = [
            #CRIA ELEMENTO NA TELA COM UM INPUT PARA RECEBER DADOS
            [sg.Text('Usuário', size=(10, 0)), sg.Input(size=(30, 0), key='username')],
            [sg.Text('Senha', size=(10, 0)), sg.Input(size=(30, 0), key='password')],
            [sg.Text('Hashtag', size=(10, 0)), sg.Input(size=(40, 0), key='hashtag')],
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
            #IMPRIMI INFORMAÇÕES EXTRAIDAS DA TELA
            #print(self.values);
            #username = self.values['username'];
            #password = self.values['password'];
            #hashtag = self.values['hashtag'];
            username = 'igor927482';
            password = '12131212aA@';
            hashtag = 'memes';

            print(f'Usuário: {username}');
            print(f'Senha: {password}');
            print(f'Hashtag: {hashtag}');

            logBot = InstagramBot(username, password, hashtag);
            logBot.login();
        #FECHA while
    # FECHA Iniciar



#INSTANCIA CLASSE TelaPython EM tela
tela = TelaPython();
tela.Iniciar();