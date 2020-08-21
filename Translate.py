import boto3

def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)

    print(response['TranslatedText'])

kwargs={
    "Text":"Translate this code to French",
    "SourceLanguageCode":"en",
    "TargetLanguageCode":"fr"
}

if __name__ == "__main__":
    translate_text(**kwargs)
