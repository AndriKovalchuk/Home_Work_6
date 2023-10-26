import re

CYRILLIC_SYMBOLS = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

LATIN_SYMBOLS = ('a', 'b', 'v', 'h', 'g', 'd', 'e', 'ye', 'zh', 'z', 'y', 'i', 'yi', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'yu', 'ya')

TRANSLITERATION = {}

for cyrillic, latin in zip(CYRILLIC_SYMBOLS, LATIN_SYMBOLS):

    TRANSLITERATION[ord(cyrillic)] = latin
    TRANSLITERATION[ord(cyrillic.upper())] = latin.upper()


def normalize(name: str) -> str:

    normalized_name = re.sub(r'\W', '_', name.translate(TRANSLITERATION))

    return normalized_name
