from pattern import Publisher, Subscriber

publisher = Publisher()

rezende = Subscriber('Rezende')
eric = Subscriber('Eric')
raquel = Subscriber('Raquel')

publisher.register(rezende)
publisher.register(eric)
publisher.register(raquel)

publisher.dispatch("ola todo mundo")
publisher.unregister(rezende)
publisher.dispatch("ola a todos menos alguns")
publisher.unregister_all()
publisher.dispatch('ola pra ngm ne')
