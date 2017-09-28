from typing import Container, Iterable, List, Union
from . import ValidatorType

def instance_of(type: type) -> ValidatorType: ...
def provides(interface) -> ValidatorType: ...
def optional(validator: Union[ValidatorType, List[ValidatorType]]) -> ValidatorType: ...
def in_(options: Container) -> ValidatorType: ...
def and_(*validators: Iterable[ValidatorType]) -> ValidatorType: ...
