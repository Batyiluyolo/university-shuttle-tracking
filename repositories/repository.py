
# repositories/repository.py

from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List

T = TypeVar('T')   # Entity type (e.g., Trip, User)
ID = TypeVar('ID') # Identifier type (e.g., str, int)

class Repository(ABC, Generic[T, ID]):
    @abstractmethod
    def save(self, entity: T) -> None:
        pass

    @abstractmethod
    def find_by_id(self, entity_id: ID) -> T:
        pass

    @abstractmethod
    def find_all(self) -> List[T]:
        pass

    @abstractmethod
    def delete(self, entity: T) -> None:
        pass
