import openai

def translate_japanese_to_english(text):
    # Replace 'YOUR_API_KEY' with your actual API key
    api_key = 'YOUR_API_KEY'
    
    # Set up OpenAI API credentials
    openai.api_key = api_key

    # Compose the message
    message = [
        {'role': 'system', 'content': 'You are a helpful assistant that translates Japanese to English.'},
        {'role': 'user', 'content': f'Translate "{text}" from Japanese to English.'}
    ]

    # Make the API request
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=100
    )
    
    # Process the response
    for choice in response.choices:
        if choice.role == 'assistant':
            return choice.text.strip()
    
    return None


# Example usage
japanese_word = 'こんにちは'  # Replace with your Japanese word or phrase
translation = translate_japanese_to_english(japanese_word)
print(f'Translation: {translation}')
