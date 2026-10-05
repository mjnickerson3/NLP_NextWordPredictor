Project Overview

This project uses a trigram language model to predict the next word based on the two words that come before it. The model is trained using a small text corpus and learns patterns by counting how often words appear together.

The project demonstrates how basic language models use context and probability to make next-word predictions and generate text one word at a time.

Screenshot: Trigram Counts

<img width="554" height="523" alt="image" src="https://github.com/user-attachments/assets/46e5a884-c4e1-45ec-89d7-86d83e57cf78" />


Screenshot: Trigram Probabilities

<img width="635" height="520" alt="image" src="https://github.com/user-attachments/assets/6541baf9-054d-4f63-923a-4bcae15b8087" />


Screenshot: Next-Word Predictions

<img width="360" height="342" alt="image" src="https://github.com/user-attachments/assets/d3b7fcce-2c6e-4411-b4b1-a628d058d6fd" />


Screenshot: Generated Text

<img width="645" height="239" alt="image" src="https://github.com/user-attachments/assets/1630a926-414e-4e4a-8897-774b5013bd3a" />


How My Model Works

This project uses a trigram language model to predict the next word based on the two words that come before it. First, the training text is converted to lowercase, punctuation is removed, and the text is split into individual words. The model then looks at groups of three words and keeps track of how often certain words follow a specific two-word combination.

Once those counts are collected, the model converts them into probabilities. When I enter two words, the model looks for that word pair in the training data and predicts the most likely next word based on what it learned. It can also generate text by repeatedly predicting the next word until it reaches the desired length.

Reflection Question 1

My trigram model predicts the next word by looking at the previous two words and checking the patterns it learned from the training text. It counts how many times a particular word follows a specific two-word combination and uses those counts to calculate probabilities. The words with the highest probabilities are returned as the most likely predictions.

Reflection Question 2

One limitation is that the model only looks at the previous two words and doesn't understand the bigger meaning of a sentence or paragraph. Because of that, the generated text can sometimes sound repetitive or not flow naturally. Modern language models can use a much larger amount of context, which helps them understand relationships between ideas and generate more accurate responses. Trigram models also have trouble predicting word combinations that weren't included in the training data.
