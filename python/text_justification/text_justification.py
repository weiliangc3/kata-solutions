def justify_text(input, expected_width):
    words = input.split()
    justified_text = ""
    line_char_count = 0
    word_stack = []

    for i, word in enumerate(words):
        word_length = len(word)
        if (line_char_count + word_length > expected_width):
            justified_text = resolve_stack(word_stack, justified_text, expected_width)
            justified_text += "\n"
            line_char_count = 0
            word_stack.clear()
        word_stack.append(word)
        line_char_count += (word_length + 1)
        if (i == len(words) - 1):
            justified_text = resolve_stack(word_stack, justified_text, expected_width)

    return justified_text

def resolve_stack(word_stack, justified_text, expected_width):
    current_index = 0
    while get_line_length_from_array(word_stack) < expected_width:
        if len(word_stack) == 1:
            break
        word_stack[current_index] += " "
        current_index += 1
        if current_index == len(word_stack)-1:
            current_index = 0

    for word in word_stack:
        justified_text += word
    
    return justified_text

def get_line_length_from_array(line):
    line_length = 0
    for word in line:
        line_length += len(word)
    return line_length