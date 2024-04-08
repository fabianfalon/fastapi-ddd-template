from abc import ABC, abstractmethod


class ControllerInterfaz[T](ABC):
    """ControllerInterfaz"""

    @abstractmethod
    def execute(self, *args, **kwargs) -> T: ...
