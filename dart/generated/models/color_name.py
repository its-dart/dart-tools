from enum import Enum


class ColorName(str, Enum):
    BROWN = "Brown"
    DARK_BLUE = "Dark Blue"
    DARK_GRAY = "Dark Gray"
    DARK_GREEN = "Dark Green"
    DARK_ORANGE = "Dark Orange"
    DARK_RED = "Dark Red"
    DARK_TEAL = "Dark Teal"
    FLAT_GREEN = "Flat Green"
    GREEN = "Green"
    LIGHT_BLUE = "Light Blue"
    LIGHT_BROWN = "Light Brown"
    LIGHT_GRAY = "Light Gray"
    LIGHT_GREEN = "Light Green"
    LIGHT_ORANGE = "Light Orange"
    LIGHT_PINK = "Light Pink"
    LIGHT_PURPLE = "Light Purple"
    ORANGE = "Orange"
    PINK = "Pink"
    PURPLE = "Purple"
    RED = "Red"
    RED_ORANGE = "Red Orange"
    TAN = "Tan"
    TEAL = "Teal"
    YELLOW = "Yellow"

    def __str__(self) -> str:
        return str(self.value)
