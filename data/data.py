from dataclasses import dataclass


@dataclass
class Person:
    # Test Text Box
    full_name: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None

    # Test Web Tables
    firstname: str = None
    lastname: str = None
    age: int = None
    salary: int = None
    department: str = None
