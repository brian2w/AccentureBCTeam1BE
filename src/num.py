import numpy as np

# List to store similarity scores
similarity_scores = []

# Loop over the sentences in the JSON array (acceptance-criteria)
for sentence in json_array:
    # Calculate similarity score between the user input and current sentence
    score = calculate_similarity(user_input, sentence["acceptance-criteria"]) # we need to define calculate similarity ourselves
    similarity_scores.append(score)

# Find the index of the maximum similarity score
max_index = np.argmax(similarity_scores)

# Get the corresponding ID of the sentence with the maximum similarity score
max_id = json_array[max_index]["id"]

print(max_id)
