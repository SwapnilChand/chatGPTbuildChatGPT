import tensorflow as tf

# Load dataset
dataset = ...

# Preprocess text
dataset = dataset.map(preprocess_text)

# Tokenize text
tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(dataset)
dataset = tokenizer.texts_to_sequences(dataset)

# Pad sequences
dataset = tf.keras.preprocessing.sequence.pad_sequences(dataset, padding='post')

# Build model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=256),
    tf.keras.layers.LSTM(units=256, return_sequences=True),
    tf.keras.layers.LSTM(units=256),
    tf.keras.layers.Dense(units=len(tokenizer.word_index)+1, activation='softmax')
])
model.compile(loss='categorical_crossentropy', optimizer='adam')

# Train model
model.fit(dataset, epochs=10)
