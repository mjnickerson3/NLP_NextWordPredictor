"""
Trigram Next-Word Predictor - Starter Template

Name: Mandi Schmuhl
Date: 10/11/2026

Instructions:
- Complete each function where indicated with TODO comments.
- Do NOT delete function definitions.
- You may add helper functions if needed.
"""

import string
from collections import defaultdict, Counter


def preprocess_text(text):
    """
    Convert text to lowercase, remove punctuation, and split into tokens.
    """
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(
        str.maketrans('', '', string.punctuation)
    )

    # Split into tokens
    tokens = text.split()

    return tokens


def build_trigram_counts(tokens):
    """
    Build trigram counts in the form:
    (word1, word2) -> Counter({next_word: count})
    """
    trigram_counts = defaultdict(Counter)

    #Loop through tokens and count trigrams
    for i in range(len(tokens) - 2):
        word1 = tokens[i]
        word2 = tokens[i + 1]
        word3 = tokens[i + 2]

        trigram_counts[(word1, word2)][word3] += 1

    return trigram_counts


def build_trigram_probabilities(trigram_counts):
    """
    Convert trigram counts into probabilities.
    Returns:
    (word1, word2) -> {next_word: probability}
    """

    trigram_probs = {}

    # Loop through each context in trigram_counts
    for context, counter in trigram_counts.items():

        # Find total count for that context
        total = sum(counter.values())

        trigram_probs[context] = {}

        # Compute probabilities for each next word
        for next_word, count in counter.items():
            trigram_probs[context][next_word] = count / total

    return trigram_probs


def predict_next_words(word1, word2, trigram_probs, top_n=3):
    """
    Return the top N most likely next words for the given two-word context.

    Example return value:
    [("natural", 0.5), ("machine", 0.25), ("learning", 0.25)]
    """
    context = (word1.lower(), word2.lower())

    # Return empty list if context is not found
    if context not in trigram_probs:
        return []

    # Convert predictions to a list of tuples
    predictions = list(trigram_probs[context].items())

    # Sort by probability, highest first
    predictions.sort(
        key=lambda x: x[1],
        reverse=True
    )
    # Return top_n items
    return predictions[:top_n]


def generate_text(start_words, trigram_probs, max_length=10):
    """
    Generate text by repeatedly choosing the highest-probability next word.

    start_words should contain exactly two words.
    """
    words = start_words.lower().split()

    #Check that exactly two start words were given
    if len(words) != 2:
        return "Error: Please provide exactly two starting words."

    generated = words[:]

    # Repeatedly predict and append the next word
    # Stop if the context is not found
    while len(generated) < max_length:

        context = (generated[-2], generated[-1])

        if context not in trigram_probs:
            break

        next_word = max(
            trigram_probs[context],
            key=trigram_probs[context].get
        )

        generated.append(next_word)

    return " ".join(generated)


def print_trigram_counts(trigram_counts):
    """
    Print trigram counts in a readable way.
    """
    print("\nTrigram Counts:")
    for context, counter in trigram_counts.items():
        print(f"{context} -> {dict(counter)}")


def print_trigram_probabilities(trigram_probs):
    """
    Print trigram probabilities in a readable way.
    """
    print("\nTrigram Probabilities:")
    for context, prob_dict in trigram_probs.items():
        print(f"{context} -> {prob_dict}")


def main():
    text = """
    I love natural language processing.
    I love machine learning.
    Natural language processing is fun.
    Machine learning is powerful.
    I love learning new things.
    I love natural language models.
    Natural language models are useful.
    """

    # Step 1: Preprocess text
    tokens = preprocess_text(text)

    print("Tokens:")
    print(tokens)

    # Step 2: Build trigram counts
    trigram_counts = build_trigram_counts(tokens)
    print_trigram_counts(trigram_counts)

    # Step 3: Build trigram probabilities
    trigram_probs = build_trigram_probabilities(trigram_counts)
    print_trigram_probabilities(trigram_probs)

    # Step 4: Test next-word prediction
    print("\nTop 3 Next-Word Predictions:")

    test_contexts = [
        ("i", "love"),
        ("natural", "language"),
        ("machine", "learning"),
    ]

    for word1, word2 in test_contexts:
        predictions = predict_next_words(word1, word2, trigram_probs, top_n=3)
        print(f"\nContext: '{word1} {word2}'")

        if not predictions:
            print("No predictions found.")
        else:
            for i, (word, prob) in enumerate(predictions, start=1):
                print(f"{i}. {word} ({prob:.3f})")

    # Step 5: Generate text
    print("\nGenerated Text:")
    prompts = [
        "i love",
        "natural language",
        "machine learning"
    ]

    for prompt in prompts:
        generated = generate_text(prompt, trigram_probs, max_length=8)
        print(f"Prompt: '{prompt}'")
        print(f"Generated: {generated}")
        print("-" * 50)


if __name__ == "__main__":
    main()