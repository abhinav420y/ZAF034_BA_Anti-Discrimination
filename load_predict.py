import h5py
import numpy as np

# Load the trained model from the model.h5 file
with h5py.File('model.h5', 'r') as f:
    coef = f['coef'][:]
    intercept = f['intercept'][:]


# Define a function to preprocess new text data and make predictions using the trained model
def predict(text, cv, clf):
    # Preprocess the text data using the same CountVectorizer object used to train the model
    text_features = cv.transform([text]).toarray()

    # Make predictions using the trained model
    prediction = clf.predict(text_features)

    # Return the predicted label as a string
    return target_names[prediction[0]]


# Example usage
from sklearn.feature_extraction.text import CountVectorizer

# Load the CountVectorizer object used to train the model
cv = CountVectorizer()

# Fit the CountVectorizer object on the training data
cv.fit(X_train)

# Define the trained logistic regression classifier
clf = LogisticRegression(random_state=7, max_iter=1000, solver='saga', n_jobs=4, multi_class='auto')

# Set the learned coefficients and intercept values in the logistic regression classifier
clf.coef_ = coef
clf.intercept_ = intercept

# Make predictions on new text data
text1 = "This is a positive review"
text2 = "This is a negative review"
prediction1 = predict(text1, cv, clf)
prediction2 = predict(text2, cv, clf)

# Print the predictions
print(prediction1)  # should output 'positive'
print(prediction2)  # should output 'negative'
