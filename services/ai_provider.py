from abc import ABC, abstractmethod


class AIProvider(ABC):

    @abstractmethod
    def generate_response(
        self,
        character,
        message: str
    ) -> str:
        pass