from rest_framework.decorators import api_view
from rest_framework.response import Response
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# initialize the lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

@api_view(['POST'])
def chatbot(request):
    # get the user's message from the POST request
    message = request.data['message']

    # tokenize the user's message
    words = nltk.word_tokenize(message.lower())

    # remove stop words from the user's message
    words = [word for word in words if word not in stop_words]

    # lemmatize the remaining words in the user's message
    words = [lemmatizer.lemmatize(word) for word in words]

    # determine the chatbot's response based on the user's message
    response = 'Hello, how can I help you?'
    if 'help' in words:
        response = 'Sure, what do you need help with?'
    elif 'problem' in words:
        response = 'What seems to be the problem?'
    elif 'thanks' in words or 'thank you' in words:
        response = 'You\'re welcome!'

    # return the chatbot's response in a JSON format
    return Response({'message': response})
