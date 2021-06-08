from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from tqdm.notebook import tqdm
import nltk
import string

def preprocess_corpus(texts):
    
    mystopwords = set(stopwords.words("english"))
    def remove_stops_digits(tokens):
        
        return [token.lower() for token in tokens if token not in mystopwords and not token.isdigit()
                and token not in punctuation]
    
    return [remove_stops_digits(word_tokenize(text)) for text in tqdm(texts)]




def stopwords_punc(text):
        WPT = nltk.WordPunctTokenizer()
        stop_word_list = nltk.corpus.stopwords.words('turkish')
        gereksiz_kelimeler = ["falan",
                      "filan",
                     "açıkçası",
                     "ancak",
                     "ben",
                     "bence",
                     "bir",
                     "bile",
                     "bunu",
                     "bu yüzden",
                     "dahi",
                     "demek ki",
                     "fakat",
                     "gerçekten",
                     "gene",
                     "gerek",
                     "gerekse",
                     "hâlbuki",
                     "halbuki",
                     "hatta",
                     "hele",
                     "kadar",
                     "kere",
                     "keza",
                     "kısacası",
                     "lakin",
                     "lâkin",
                     "madem",
                     "mi",
                     "nitekim",
                     "ilk",
                     "olan",
                     "olarak",
                     "oysa",
                     "oysaki",
                     "öyleyse",
                     "üstelik",
                     "sonra",
                     "var",
                     "veyahut",
                     "yahut",
                     "yine",
                     "yoksa",
                     "zira"]
        for i in gereksiz_kelimeler:
            stop_word_list.append(i)

        text = text.translate(str.maketrans('', '', string.punctuation))
        text = [word.lower() for word in text.split() if word not in stop_word_list]
        return " ".join(text)