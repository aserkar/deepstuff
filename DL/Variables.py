def main():
    dictionary = {"learning": "awesome", "coding": "fun", "learn": "boring"}
    remove_keys_containing_string(dictionary, "learn")
    print(dictionary)


"""
This Python function takes in a dict and a string and removes all keys containing that string from the dict
"""


def remove_keys_containing_string(dictionary, remove):
    toRemove = []
    for key in dictionary:
        for i in range(len(key)):
            if key[i:i + len(remove)] == remove:
                toRemove.append(key)

    if toRemove:
        for key in toRemove:
            del dictionary[key]


if __name__ == "__main__": main()
