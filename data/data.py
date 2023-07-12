from dataclasses import dataclass


@dataclass
class Person:
    full_name: str
    email: str
    current_address: str
    permanent_address: str

    def __eq__(self, other):
        return (
            self.full_name == other.full_name
            and self.email == other.email
            and self.current_address == other.current_address
            and self.permanent_address == other.permanent_address
        )

    def __str__(self):
        return f"full_name={self.full_name}, email={self.email}, current_address={self.current_address}, permanent_address={self.permanent_address}"
