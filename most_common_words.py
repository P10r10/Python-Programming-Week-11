from pathlib import Path


def most_common_words(filename: str, lower_limit: int) -> dict:
    s = Path(filename).read_text().replace(".", " ").replace(",", "")
    return {word: s.split().count(word)
            for word in s.split() if s.split().count(word) >= lower_limit}


if __name__ == "__main__":
    print(most_common_words("comprehensions.txt", 3))
