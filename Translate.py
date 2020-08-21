import boto3

def translate_text(**kwargs):
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)

    print(response['TranslatedText'])


if __name__ == "__main__":
    translate_text(Text='Translate this to french', SourceLanguageCode='en', TargetLanguageCode='fr')
