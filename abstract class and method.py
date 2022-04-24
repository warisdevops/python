#abstract class
from abc import ABC, abstractmethod

class computer(ABC):
    @abstractmethod
    def process(self):
        pass

class laptop(computer):
    def process(self):
        print('its running')


#a=computer()
b=laptop()
b.process()
