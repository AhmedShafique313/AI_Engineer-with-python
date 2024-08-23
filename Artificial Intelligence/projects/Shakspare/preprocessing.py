from load import text, tf, file_path, np

text = open(file_path, 'rb').read().decode(encoding='utf-8').lower()
text = text[10000:70000]

characters = sorted(set(text))
char_index = dict((c, i) for i, c in enumerate(characters))
index_char = dict((i, c) for i, c in enumerate(characters))

seq_len = 50
step_size = 3

sentences = []
next_char = []

# loop
for i in range(0, len(text)-seq_len, step_size):
    sentences.append(text[i: i+seq_len])
    next_char.append(text[i+seq_len])

# numeric formating

x = np.zeros((len(sentences), seq_len,
              len(characters)), dtype=np.bool)

y = np.zeros((len(sentences), len(characters)), dtype=np.bool)
for i, satz in enumerate(sentences):
    for t, char in enumerate(satz):
        x[i, t, char_index[char]] = 1
    y[i, char_index[next_char[i]]] = 1
