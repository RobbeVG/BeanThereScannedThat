from typing import Any 

class CoffeeData():
    variables: dict[str, Any] = {}

    def __init__(self, variables: dict[str, Any]):
        self.variables = variables

    def __str__(self) -> str:
        if self.variables == {}:
            return "Coffee Data has no variables"
        result = "Coffee Data Variables:\n"
        for key, value in self.variables.items():
            max_key_length = max(len(key) for key in self.variables.keys())
            result += f"{key.ljust(max_key_length)}: {str(value)}\n"
        return result
