#!/usr/bin/python3
""" This fuction indent text after every . ? :"""
def text_indentation(text):
    """receives test and indent after every . ? :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lines = text.split('\n')
    result = []
    for line in lines:
        stripped_line = line.strip()
        if len(stripped_line) == 0:
            continue

        i = 0
        while i < len(stripped_line):
            if stripped_line[i] in ['.', '?', ':']:
                result.append(stripped_line[:i+1].strip())
                result.append('')
                stripped_line = stripped_line[i+1:].strip()
                i = 0
            else:
                i += 1
        result.append(stripped_line)

    print('\n'.join(result), end='')
