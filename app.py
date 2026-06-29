import pickle

# Load trained model
model = pickle.load(open("models/sentiment_model.pkl", "rb"))

# Load TF-IDF vectorizer
tfidf = pickle.load(open("models/tfidf_vectorizer.pkl", "rb"))

print("=" * 50)
print("      IMDB Movie Review Sentiment Analysis")
print("=" * 50)

while True:

    review = input("\nEnter a movie review: ")

    review_vector = tfidf.transform([review])

    prediction = model.predict(review_vector)

    if prediction[0] == 1:
        print("\nPrediction: Positive 😊")

    else:
        print("\nPrediction: Negative 😞")

    choice = input("\nDo you want to test another review? (y/n): ").lower()

    if choice != 'y':
        print("\nThank you for using the Sentiment Analysis App!")
        break