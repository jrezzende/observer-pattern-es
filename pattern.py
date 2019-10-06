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
        if not self.subscribers:
            return

        for subscriber in self.subscribers:
            subscriber.update(message)


# from pattern import Publisher, Subscriber

# publisher = Publisher()

# rezende = Subscriber('Rezende')
# eric = Subscriber('Eric')
# raquel = Subscriber('Raquel')

# publisher.register(rezende)
# publisher.register(eric)
# publisher.register(raquel)

# publisher.dispatch("ola todo mundo")
# publisher.unregister(rezende)
# publisher.dispatch("ola a todos menos alguns")
# publisher.unregister_all()
# publisher.dispatch('ola pra ngm ne')