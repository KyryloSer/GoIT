from abc import ABC, abstractmethod


class SerializationInterface(ABC):
    @abstractmethod
    def serialization_data(self, data):
        pass


class SerializationJson(SerializationInterface):
    def serialization_data(self, data):
        pass


class SerializationBin(SerializationInterface):
    def serialization_data(self, data):
        pass
