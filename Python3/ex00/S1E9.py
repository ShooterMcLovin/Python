from abc import ABC, abstractmethod

class Character(ABC):
    """
    Abstract class for a character. Represents a character with a first name and an alive state.
    """
    
    def __init__(self, first_name, is_alive=True):
        """
        Initializes a new character with a given first name and alive state.
        
        Parameters:
        first_name (str): The first name of the character.
        is_alive (bool, optional): The alive state of the character. Default is True.
        """
        self.first_name = first_name
        self.is_alive = is_alive
    
    def die(self):
        """
        Changes the character's alive state to False, indicating the character has died.
        """
        self.is_alive = False
    
    @abstractmethod
    def __str__(self):
        """
        Abstract method to represent the character as a string.
        Must be implemented by subclasses.
        """
        pass

class Stark(Character):
    """
    A subclass of Character, representing a member of House Stark.
    """
    
    def __init__(self, first_name, is_alive=True):
        """
        Initializes a new Stark character with a given first name and alive state.
        
        Parameters:
        first_name (str): The first name of the Stark character.
        is_alive (bool, optional): The alive state of the character. Default is True.
        """
        super().__init__(first_name, is_alive)
    
    def __str__(self):
        return f"{self.first_name} of House Stark"

