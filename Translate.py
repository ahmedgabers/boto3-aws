import argparse
import json
import boto3

parser = argparse.ArgumentParser(description="Provides translation  between one source language and another of the same set of languages.")

parser.add_argument(
    '--file',
    dest='filename',
    help='The path to the input file. The file should be valid json',
    required=True
)

args = parser.parse_args()

def open_input():
    with open(args.filename) as file_object:
        contents = json.load(file_object)
    return contents['Input']

def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response['TranslatedText'])

def translate_loop():
    input_text = open_input()
    for item in input_text:
        translate_text(**item)

if __name__ == '__main__':
    translate_loop()

