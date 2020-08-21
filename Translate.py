import boto3

client = boto3.client('translate')

def translate_text():
    response = client.translate_text(
        Text = 'Translate this to french',
        SourceLanguageCode = 'en',
        TargetLanguageCode = 'fr'

    )
    print(response['TranslatedText'])


if __name__ == "__main__":
    translate_text()
