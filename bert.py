from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
## nltk is mainly involved with pre-processing


data = [
    {
      "id": 1,
      "title": "Implement login functionality",
      "description": "As a user, I want to be able to log in to the application so that I can access my account.",
      "acceptance_criteria": [
        "User can enter their username and password",
        "System displays an error message if the login credentials are incorrect"
      ]
    },
    {
      "id": 2,
      "title": "Allow users to search for products",
      "description": "As a user, I want to be able to search for products in the application so that I can find what I am looking for.",
      "acceptance_criteria": [
        "User can enter a keyword in the search bar",
        "System displays a list of relevant products based on the keyword",
        "User can refine their search results using filters"
      ]
    },
    {
      "id": 3,
      "title": "Add a shopping cart",
      "description": "As a user, I want to be able to add products to my shopping cart so that I can purchase multiple items at once.",
      "acceptance_criteria": [
        "User can add products to their cart from the product list or product details page",
        "System displays a notification and updates the cart icon to reflect the number of items in the cart",
        "User can view and edit the contents of their cart"
      ]
    }
]

def similar_algorithm(input):
    #Adding the input into list
    all_criteria = [input]
    
    #Adding acceptance criteria into list
    for i in data:
        all_criteria.extend(i['acceptance_criteria'])

    
    new_sen = []
    # Stripping the unnessary words
    for e in all_criteria:
        stop_words = set(stopwords.words("english"))
        words = word_tokenize(e)
        filter = []
        for w in words: # loops through sentence and adds useful words to filtered sentence
            if w not in stop_words:
                filter.append(w)
        new_sen.append(filter)

    sen = []
    # Joining the stripped lists to form sentences
    for element in new_sen:
        stripped = ' '.join(element)
        sen.append(stripped)
    print(sen)

    #Write some lines to encode (sentences 0 and 2 are both ideltical):
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    #Encoding:
    sen_embeddings = model.encode(sen)
    sen_embeddings.shape

    
    #let's calculate cosine similarity for sentence 0:
    result_cosine = cosine_similarity(
        [sen_embeddings[0]],
        sen_embeddings[1:]
    )
    
    # Formatting the percentage and getting the similarities that satisfy the threshold
    p = []
    for i in result_cosine[0]:
        n = float(i)*100
        n = round(n,2)
        if (n >= 75.00):
            p.append(n)
    return p


p = similar_algorithm("username and password")
print(p)