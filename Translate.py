import boto3

client = boto3.client('translate')

def translate_text(text, source_language_code, target_language_code):
    response = client.translate_text(
        Text = text,
        SourceLanguageCode = source_language_code,
        TargetLanguageCode = target_language_code

    )
    print(response['TranslatedText'])


if __name__ == "__main__":
    translate_text('Translate this to french', 'en', 'fr')
