class Container(object):

    def __init__(self, config: dict):
        self._config = config
        self._registry = {}

    def get(self, key: str):
        if not self._registry.get(key):
            factory = self._config.get(key).get('factory')
            args = self._config.get(key).get('arguments')

            if args:
                self._registry[key] = factory.create(*args)
            else:
                self._registry[key] = factory.create()

        return self._registry.get(key)
