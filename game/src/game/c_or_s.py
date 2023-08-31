from gensim.models import KeyedVectors

class COrS:
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)
        return cls._instances[cls]

    def __init__(self, valid_words, min_similarity=.4, model_path="c_or_s_game/game/resources/skip_s100.txt"):
        self.model = KeyedVectors.load_word2vec_format(model_path)
        self.valid_words = valid_words
        self.min_similarity = min_similarity
        self.history = list()

    def add(self, type, word):
        self.history.append((type, word))

    def _get_similarity(self, word_a, word_b):
        return self.model.similarity(word_a, word_b)

    def get_latest_word_by_type(self, desired_type):
        return next((word for type, word in reversed(self.history) if type == desired_type), None)

    def is_valid(self, user_word):
        latest_system_word = self.get_latest_word_by_type("system")
        similarity_score = self._get_similarity(user_word, latest_system_word)

        return (user_word in self.valid_words) and (similarity_score >= self.min_similarity) and (latest_system_word != user_word)

    def get_similar_word(self, word):
        most_similar_word, most_similar_score = self.model.most_similar(word, topn=1)[0]
        if most_similar_score >= self.min_similarity:
            return most_similar_word
        else:
            return None

