class Container(object):
    """Dependency Injection Container.

    Manages the instantiation of services by factories specified in the configuration.

    Example:
        from di-container.container import Container

        config = {
            'service_one': {
                'factory': ServiceOneFactory(),
            },
            'service_two': {
                'factory': ServiceTwoFactory(),
                'arguments': (argument1, argument2),
            }
        }

        container = Container(config)

        service_one = container.get('service_one')
        service_two = container.get('service_two')

    """

    def __init__(self, config: dict):
        """Creates the Container

        Args:
            config: A dictionary of dictionaries that maps service keys to the factories that create them. Example:

                {
                    'service': {
                        'factory': ServiceFactory(),
                        'arguments': (argument1, argument2),
                    }
                }
        """
        self._config = config
        self._registry = {}

    def get(self, key: str):
        """Returns the specified service, or creates one if it doesn't exist

        Checks the internal registry to see if the service already exists. If
        it does not, it will call the create() method on the factory specified
        in the config, passing any optional arguments that are specified in the
        config.

        Args:
            key: The name of the service.

        """

        if not self._registry.get(key):
            factory = self._config.get(key).get('factory')
            args = self._config.get(key).get('arguments')

            if args:
                self._registry[key] = factory.create(*args)
            else:
                self._registry[key] = factory.create()

        return self._registry.get(key)
