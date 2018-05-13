import os
import re
import pickle


class SpamClassifier:
    """
    This class contains pre-trained classification model.
    To be used with string type input.
    Should be stored in the same directory as folder 'pkl_objects' !!!
    """
    def __init__(self):
        self.dir = os.path.dirname(__file__)
        self.clf = pickle.load(open(os.path.join(self.dir, 'pkl_objects', 'classifier.pkl'), 'rb'))
        self.vectorizer = pickle.load(open(os.path.join(self.dir, 'pkl_objects', 'vectorizer.pkl'), 'rb'))

    @staticmethod
    def _preprocessor(text):
        """
        Private method for SpamClassifier class.
        Deletes HTML tags and encodes emoticons in plaintext
        :param text: String type input
        :return: Iterable object for vectorizer
        """
        text = re.sub('<[^>]*>', '', text)
        emoticons = re.findall('(?:[:;=])(?:-)?(?:[)(DP])', text)
        text = re.sub('[\W]+', ' ', text.lower()) + ' '.join(emoticons).replace('-', '')

        return [text]

    def classify(self, text):
        """
        Does binary comment classification
        Model has been build with scikit RandomForestClassifier
        :param text: String type
        :return: label: String type
                 probs: Double type
        """
        label = {0: 'Prawidłowy komentarz', 1: 'SPAM'}
        prep = self._preprocessor(str(text))
        vectorized = self.vectorizer.transform(prep)
        predicted = self.clf.predict(vectorized)[0]
        probs = self.clf.predict_proba(vectorized).max()

        return label[predicted], probs
