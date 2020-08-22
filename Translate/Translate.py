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
        if input_validation(item):
            translate_text(**item)
        else:
            raise SystemError
def input_validation(item):
    languages = ["af","sq","am","ar","az","bn","bs","bg","zh","zh-TW","hr","cs","da","fa-AF",
                "nl","en","et","fi","fr","fr-CA","ka","de","el","ha","he","hi","hu","id","it",
                "ja","ko","lv","ms","no","fa","ps","pl","pt","ro","ru","sr","sk","sl","so","es",
                "sw","sv","tl","ta","th","tr","uk","ur","vi"]
    json_input = item
    SourceLanguageCode = json_input['SourceLanguageCode']
    TargetLanguageCode = json_input['TargetLanguageCode']

    if SourceLanguageCode == TargetLanguageCode:
        print("The SourceLanguageCode is the same as the TargetLanguageCode - nothing to do")
        return False
    elif SourceLanguageCode not in languages and TargetLanguageCode not in languages:
        print(f"Neither the SourceLanguageCode ({SourceLanguageCode}) and TargetLanguageCode ({TargetLanguageCode}) are valid - stopping")
        return False
    elif SourceLanguageCode not in languages:
        print(f"The SourceLanguageCode ({SourceLanguageCode}) is not valid - stopping")
        return False
    elif TargetLanguageCode not in languages:
        print(f"The TargetLanguageCode ({TargetLanguageCode}) is not valid - stopping")
        return False
    elif SourceLanguageCode in languages and TargetLanguageCode in languages:
        return True
    else:
        print("There is an issue")
        return False

if __name__ == '__main__':
    translate_loop()

