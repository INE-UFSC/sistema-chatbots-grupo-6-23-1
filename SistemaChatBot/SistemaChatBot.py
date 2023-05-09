from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa: str,lista_bots: list):
        self.__empresa=nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        self.__valido = True
        for i in lista_bots:
            if not isinstance(i, Bot):
                self.__valido = False
        if self.__valido:
            self.__lista_bots=lista_bots
        self.__bot = None
    
    def boas_vindas(self):
        ##mostra mensagem de boas vindas do sistema
        print(f'Olá, esse é o sistema de chatbots da empresa {self.__empresa}')
        print('\nOs Chat bots disponíveis no momento são:')

    def mostra_menu(self):
        ##mostra o menu de escolha de bots
        contador_bots = 0
        for i in self.__lista_bots:
            print(f'{contador_bots} - Bot: {i.nome} - Mensagem de apresentação: {i.apresentacao()}')
            contador_bots+=1
    
    def escolhe_bot(self):
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 
        while True:
            try:
                seletor = int(input('Digite o número do chat bot desejado: '))
            
            except: #Se houver algum erro de entrada
                print("> Digite um numero valido")
                continue
            else:
                if seletor>=0 and seletor<=len(self.__lista_bots)-1:
                    break
                else:
                    print('Seleção fora do range dos bots')

        self.__bot = seletor
        self.__lista_bots[seletor].apresentacao()

    def mostra_comandos_bot(self):
        ##mostra os comandos disponíveis no bot escolhido
        self.__lista_bots[self.__bot].mostra_comandos()

    def le_envia_comando(self):
        ##faz a entrada de dados do usuário e executa o comando no bot ativo
        while True:
            try:
                comando = int(input('Digite o comando desejado (-1 para sair do programa) :'))
            
            except:
                print("> Digite um valor valido")
                continue
            else:
                if comando == -1:
                    return False
                if comando>=0 and comando<=len(self.__lista_bots[self.__bot].comandos):
                    self.__lista_bots[self.__bot].executa_comando(comando)
                else:
                    break
        print(self.__lista_bots[self.__bot].despedida())

    def inicio(self):
        ##mostra mensagem de boas-vindas do sistema
        ##mostra o menu ao usuário
        ##escolha do bot      
        ##mostra mensagens de boas-vindas do bot escolhido
        ##entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ##ao sair mostrar a mensagem de despedida do bot
        if self.__valido:
            self.boas_vindas()
            self.mostra_menu()
            self.escolhe_bot()
            self.mostra_comandos_bot()
            self.le_envia_comando()