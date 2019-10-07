import random
# Arquivo python para demonstração rápida de como o pattern é aplicado

#Classe Subscriber, que conterá apenas um nome para identificar e um método update, dizendo que recebeu a mensagem
class Subscriber:
    def __init__(self, name):
        self.name = name
  
    def update(self, message):
        print(f'{self.name} got message {message}')

#Classe Publisher, que conterá uma referência a todos os subscribers (self.subscribers) e alguns métodos para adicionar, remover, remover todos etc
#principal método dessa classe é o "dispatch", que vai percorrer o set de subscribers e enviar a mensagem a todos que estão inscritos.
class Publisher:
    def __init__(self):
        self.subscribers = set()

    def register(self, subscriber):
        self.subscribers.add(subscriber)

    def unregister(self, subscriber):
        self.subscribers.discard(subscriber)
        
    def unregister_all(self):
        self.subscribers.clear()

    def dispatch(self, message):
        if not self.subscribers:
            return
        for subscriber in self.subscribers:
            subscriber.update(message)


publisher = Publisher()

rezende = Subscriber('Rezende')
eric = Subscriber('Eric')
raquel = Subscriber('Raquel')

#registrando os subscribers ao publisher
publisher.register(rezende)
publisher.register(eric)
publisher.register(raquel)

#publisher envia mensagen, todos recebem
publisher.dispatch("Olá a todos!")

#escolha aleatória de alguém a ser descartado
choice = random.choice(list(publisher.subscribers))

#remove a pessoa aleatória
publisher.unregister(choice)

#manda novamente uma mensagem, que somente duas pessoas vão receber
publisher.dispatch(f"Olá a todos, menos para {choice.name}.")

#remove todos
publisher.unregister_all()

#envia mensagem que nunca será mostrada pois não há ninguém para ouvi-la
publisher.dispatch('Esta mensagem nunca será entregue.')

#para rodar o arquivo basta ter o python 3 instalado e rodar pelo cmd com o comando "python pattern.py"