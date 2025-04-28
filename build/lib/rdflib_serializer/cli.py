import sys
import argparse
import argcomplete
from rdflib import Graph

SUPPORTED_FORMATS = [
    "xml", "n3", "turtle", "nt", "trig", "nquads", "json-ld", "rdfa"
]

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Parse and serialize RDF data from file or stdin. Converts between formats, keeping only used prefixes."
    )
    parser.add_argument(
        "file",
        help="File path to read from, or '-' to read from stdin."
    )
    parser.add_argument(
        "-s", "--source-format",
        default="turtle",
        choices=SUPPORTED_FORMATS,
        help="Source input format (default: turtle). Choices: " + ", ".join(SUPPORTED_FORMATS)
    )
    parser.add_argument(
        "-t", "--target-format",
        default="turtle",
        choices=SUPPORTED_FORMATS,
        help="Target output format (default: turtle). Choices: " + ", ".join(SUPPORTED_FORMATS)
    )
    argcomplete.autocomplete(parser)
    args = parser.parse_args()

    g = Graph()

    if args.file == '-':
        data = sys.stdin.read()
        g.parse(data=data, format=args.source_format)
    else:
        with open(args.file, 'r', encoding='utf-8') as f:
            data = f.read()
            g.parse(data=data, format=args.source_format)

    print(g.serialize(format=args.target_format).decode('utf-8'))

if __name__ == "__main__":
    main()