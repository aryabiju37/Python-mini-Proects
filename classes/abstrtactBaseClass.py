from abc import ABC, abstractmethod

class InvalidOperationException(Exception):
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationException("Stream is already opened")
        self.opened = True
    
    def close(self):
        if self.opened:
            raise InvalidOperationException("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")
     
class MemoryStream(Stream):
    def read(self):
        print("Reading from MemoryStream")
