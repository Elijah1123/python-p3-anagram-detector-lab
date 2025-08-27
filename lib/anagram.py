class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Normalize for case-insensitive comparison
        self.sorted_word = sorted(self.word)

    def match(self, possible_anagrams):
        matches = []
        for candidate in possible_anagrams:
            if candidate.lower() != self.word and sorted(candidate.lower()) == self.sorted_word:
                matches.append(candidate)
        return matches


if __name__ == "__main__":
    detector = Anagram("listen")
    words = ["enlists", "google", "inlets", "banana", "Silent"]

    print("Anagrams found:", detector.match(words))