from container import Container

def test_container():

    class ServiceFactory:

        def create(self):
            return 'I\'m a service!'

    config = {
        'service': {
            'factory': ServiceFactory(),
        },
    }

    container = Container(config)

    assert container.get('service') == 'I\'m a service!'

def test_get_service_with_args():

    class ServiceWithArgsFactory:

        def create(self, text: str, number: int):
            return [text, number]

    config = {
        'service_with_args': {
            'factory': ServiceWithArgsFactory(),
            'arguments': ('A nice little string', 5),
        },
    }

    container = Container(config)

    assert container.get('service_with_args') == ['A nice little string', 5]
