# Python Dependency Injection Container

A lightweight, experimental Dependency Injection Container for python.

# Usage

```python

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

```
