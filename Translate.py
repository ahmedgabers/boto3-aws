import argparse
import boto3

parser = argparse.ArgumentParser(description="Provides translation between one source language and another of the same set of languages.")

parser.add_argument(
    '--text',
    dest="Text",
    type=str,
    help="The text to translate. The text string can be a maximum of 5,000 bytes long.",
    required=True
)

parser.add_argument(
    '--source-language-code',
    dest="SourceLanguageCode",
    type=str,
    help="The code for the language of the source text",
    required=True
)

parser.add_argument(
    '--target-language-code',
    dest="TargetLanguageCode",
    type=str,
    help="The code for the language of the target text",
    required=True
)

args = parser.parse_args()

def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)

    print(f"Translation: {response['TranslatedText']}")

if __name__ == "__main__":
    translate_text(**vars(args))
