import json
import os
import argparse


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as json_file:
        return json.load(json_file)


def pretty_print_json(data):
    print (json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help="Path to file", required=True)
    args = parser.parse_args()

    data = load_data(args.path)
    pretty_print_json(data)
