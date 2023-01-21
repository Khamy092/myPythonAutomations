import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
from keras.layers import Flatten

# Define the sentences to learn
sentences = [
    "I love to eat pizza",
    "I don't love to eat sushi",
    "I love to play soccer",
    "I love to play basketball"
]

# Create a tokenizer
tokenizer = Tokenizer()

# Fit the tokenizer on the sentences
tokenizer.fit_on_texts(sentences)

# Encode the sentences
encoded_sentences = tokenizer.texts_to_sequences(sentences)

# Pad the encoded sentences
padded_sentences = pad_sequences(encoded_sentences, padding='post', value=0)

# Define the model
vocab_size = len(tokenizer.word_index) + 1
max_length = max([len(s.split()) for s in sentences])
model = Sequential()
model.add(Embedding(vocab_size, 8, input_shape=(max_length,)))
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Define x_train and y_train 
x_train = padded_sentences
y_train = np.array([1, 0, 1, 1])
y_train = to_categorical(y_train)

# Train the model
model.fit(x_train, y_train, epochs=10, batch_size=32)

# Define a new sentence
new_sentence = "I love to play tennis"

# Preprocess the new sentence
encoded_sentence = tokenizer.texts_to_sequences([new_sentence])
padded_sentence = pad_sequences(encoded_sentence, maxlen=max_length, padding='post', value=0)

# Make a prediction
prediction = model.predict(padded_sentence)

# Print the prediction
print(prediction)

# Get the class label
predicted_class = np.round(prediction)
print(predicted_class)

