from abc import ABC, abstractmethod

# this is abstract class


class Stream(ABC):
    def open(self):
        pass

    def close(self):
        pass

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def redd(self):
        pass


class MemoryStream(Stream):
    def read(self):
        pass


stream = MemoryStream()
