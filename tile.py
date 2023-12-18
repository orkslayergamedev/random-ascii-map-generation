ANSI_RESET = "\033[0m"
ANSI_YELLOW = "\033[33m"
ANSI_GREEN = "\033[32m"
ANSI_BLUE = "\033[34m"
ANSI_RED = "\033[31m"
ANSI_WHITE = "\033[97m"
ANSI_MAGENTA = "\033[35m"
ANSI_CYAN = "\033[36m"


"""
I simplified the logic of tile objects by deprecating the colored parameter.
The color parameter can also be used for the same purpose.


colored example: 
tile = Tile("x", ANSI_RED)

non-colored example:
tile = Tile("x")

"""


class Tile:
    def __init__(self, symbol: str, color: str | None = None):
        self.symbol = f"{color}{symbol}{ANSI_RESET}" if color else symbol


plains = Tile(".", ANSI_YELLOW)
forest = Tile("8", ANSI_GREEN)
pines = Tile("Y", ANSI_GREEN)
mountain = Tile("A", ANSI_WHITE)
water = Tile("~", ANSI_CYAN)
