def respond_to_input(input_text):
    input_text = preprocess_text(input_text)
    if 'hello' in input_text:
        return 'Hello, my dear student! How may I assist you today?'
    elif 'learn' in input_text and 'magic' in input_text:
        return 'Ah, magic! A fascinating subject indeed. Let us begin with the basics. Have you learned about wand movements yet?'
    elif 'wand movements' in input_text:
        return 'Excellent! Wand movements are the foundation of
