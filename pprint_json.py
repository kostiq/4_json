import json
import os
import pprint


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as json_file:
        return json.load(json_file)


def pretty_print_json(data):
    pprint.PrettyPrinter().pprint(data)


if __name__ == '__main__':
    bars = load_data('bars.json')
    pretty_print_json(bars)
