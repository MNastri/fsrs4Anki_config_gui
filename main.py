import toml

KEYS_OF_DECKPARAMS = (
    "deckName",
    "w",
    "requestRetention",
    "maximumInterval",
    "easyBonus",
    "hardInterval",
)
my_config_file = "config.toml"


def generate_deck_params_code_from(file) -> str:
    """
    Creates the deckParams part of the FSRS4Anki custom scheduler code from
    the given toml file.
    :param file: The toml file
    :return: the string to be pasted inside the custom scheduler
    """
    deck_data = toml.load(file)
    decks_parameters = ["const deckParams = [\n", "];\n"]
    for deck_name, deck_params in deck_data.items():
        deck = [
            "  {\n",
            f'    "{KEYS_OF_DECKPARAMS[0]}": "{deck_name}",\n',
            "  },\n",
        ]
        for key_of_deck_params, deck_parameter in zip(
            KEYS_OF_DECKPARAMS[1:], deck_params.values()
        ):
            # insert before the last item in list
            deck.insert(-1, f'    "{key_of_deck_params}": "{deck_parameter}",\n')
        deck = "".join(deck)
        # insert before the last item in list
        decks_parameters.insert(-1, deck)
    decks_parameters = "".join(decks_parameters)
    return decks_parameters


if __name__ == "__main__":
    config_str = generate_deck_params_code_from(my_config_file)
    print(config_str)
