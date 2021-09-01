COLOURS = {
    'Red': '\u001b[31m',
    'Blue': '\u001b[34m',
    'reset': '\u001b[0m'
}
BACKGROUND_COLOURS = {
    'Background Red': '\u001b[41m',
    'Background Blue': '\u001b[44m'
}


def text_color(text):
    for color in COLOURS:
        text = text.replace("[[" + color + "]]", COLOURS[color])
    return text

