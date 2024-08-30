from models import text, char_index, index_char, seq_len, sample, sentences, model, characters
import random
import numpy as np

def generate_text(length, temperature):
    start_index = random.randint(0, len(text) - seq_len - 1)
    generated = ''
    sentence = text[start_index: start_index + seq_len]
    generated += sentence
    for i in range(length):
        x_predictions = np.zeros((1, seq_len, len(characters)))
        for t, char in enumerate(sentence):
            x_predictions[0, t, char_index[char]] = 1

        predictions = model.predict(x_predictions, verbose=0)[0]
        next_index = sample(predictions,
                                 temperature)
        next_character = index_char[next_index]

        generated += next_character
        sentence = sentence[1:] + next_character
    return generated

# print(generate_text(300, 0.2))
# print(generate_text(300, 0.4))
# print(generate_text(300, 0.5))
# print(generate_text(300, 0.6))
print(generate_text(300, 0.7))
# print(generate_text(300, 0.8))