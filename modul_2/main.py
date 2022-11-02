from abc import ABC, abstractmethod


class WebUserInterface(ABC):

    @abstractmethod
    def show_contacts(self):
        pass

    @abstractmethod
    def show_notes(self):
        pass

    @abstractmethod
    def show_commands(self):
        pass

    @abstractmethod
    def connect_db(self):
        pass
