import keyword
def convert_source_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    tokens = []
    current_word = []
    for char in content:
        if char.isalnum() or char == '_':
            current_word.append(char)
        else:
            if current_word:
                tokens.append(''.join(current_word))
                current_word = []
            tokens.append(char)
    if current_word:
        tokens.append(''.join(current_word))
    processed_tokens = []
    for token in tokens:
        if token in keyword.kwlist:
            processed_tokens.append(token)
        else:
            processed_tokens.append(token.upper())
    processed_content = ''.join(processed_tokens)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(processed_content)
convert_source_file('random_int.py', 'converted_random_int.py')
