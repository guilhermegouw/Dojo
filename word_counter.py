def word_count(text):
    return len(text.split("."))


if __name__ == "__main__":
    text = "Hello.world!"
    print(text.split("."))
    print("@".join(text.split(".")))
    print(text.replace(".", " "))
