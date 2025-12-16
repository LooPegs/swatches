import json
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('jswatch')
    parser.add_argument('-o', '--order', choices=['asc', 'desc'], default='asc', help='Sort order: asc (ascending) or desc (descending)')

    args = parser.parse_args()

    reverse = args.order == 'desc'

    with open(args.jswatch, "r") as fs:
        data: list[dict] = json.load(fs)
        sorted_data = sorted(data, key=lambda item: item['id'], reverse=reverse)

    with open(args.jswatch, "w") as fs:
        json.dump(sorted_data, fs, indent=4)