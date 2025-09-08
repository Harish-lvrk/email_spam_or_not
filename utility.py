
import pickle

cv = pickle.load(open("models/cv.pkl", "rb"))
clf = pickle.load(open("models/clf.pkl", "rb"))

def model_predict(email):
    if email == "":
        return ""
    tokenized_email = cv.transform([email])
    prediction = clf.predict(tokenized_email)
    #if the email is spam prediction is should be 1
    prediction = 1 if prediction == 1 else -1
    return prediction