class Subscriber:
    def __init__(self, name):
        self.name = name
    
    def update(self, message):
        print(f'{self.name} got message {message}')


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
        print(f'dispatching message...')
        if not self.subscribers:
            print('nao há ninguem para ouvir a mensagem')
            return
        for subscriber in self.subscribers:
            subscriber.update(message)