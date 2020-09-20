from unittest.mock import patch
from src.application import menu


def test_menu():

    with patch("builtins.input", return_value="1"):
        with patch("src.functions.getHistoricalQuotes") as mock:
            selection = menu()
            mock.assert_called()
