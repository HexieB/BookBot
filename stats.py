def word_count(text: str) -> int:
    """Counts the number of words in a given text."""
    return len(text.split())

def char_count(text):
    """Counts the number of characters in a given text."""
    lowered = str.lower(text)
    count = {}
    for character in lowered:
        if character in count:         
            count[character] += 1
        else:
            count[character] = 1
    return count

def sorted_count(text):
    """Sorts the character count dictionary by frequency."""
    count = char_count(text)
    sorted_count = sorted(count.items(), key=lambda item: item[1], reverse=True)
    return sorted_count