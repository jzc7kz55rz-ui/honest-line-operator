import os

ENTRY = "Your prompt said 'quick fix,' then pasted 400 lines and a screenshot of a different error. I love you, but I billed this one to therapy."

MAX_CHARS = 200


def entry_text():
    text = ENTRY.strip()
    assert 1 <= len(text) <= MAX_CHARS
    return text


def main():
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(entry_text())
    except OSError:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(entry_text())
    print(entry_text())


if __name__ == "__main__":
    main()
