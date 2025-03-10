from typing import Mapping

from colorama import Fore
from typing_extensions import Literal

SupportedColorName = Literal[
    "RED", "YELLOW", "GREEN", "CYAN", "GRAY", "MAGENTA", "RESET", "BLUE"
]


class LogColorProvider:
    def __init__(self):
        self.is_ci_mode = False

    def get_color(
        self,
        color_name: SupportedColorName,
    ) -> str:
        if self.is_ci_mode:
            return ""

        mapping: Mapping[SupportedColorName, str] = {
            "RED": Fore.RED,
            "YELLOW": Fore.YELLOW,
            "GREEN": Fore.GREEN,
            "CYAN": Fore.CYAN,
            "GRAY": Fore.LIGHTBLACK_EX,
            "MAGENTA": Fore.LIGHTMAGENTA_EX,
            "RESET": Fore.RESET,
        }

        if color_name in mapping:
            return mapping[color_name]
        return ""


log_color_provider = LogColorProvider()
