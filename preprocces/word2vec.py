import gensim
from gensim.models import Word2Vec, KeyedVectors
from preprocces.helper import get_absolute_path
import numpy as np



class w2v():
    def __init__(self):
        w2v_turkish_path = get_absolute_path("data_sent","turkish_model.bin")
        self.w2v_turkish = KeyedVectors.load_word2vec_format(w2v_turkish_path,limit=10000,binary=True)

    def embedding_feats(self,list_of_lists, DIMENSION):
        zeros_vector = np.zeros(DIMENSION)
        feats = []
        
        for tokens in list_of_lists:
            feat_for_this = np.zeros(DIMENSION)
            
            for token in tokens:
                if token in self.w2v_turkish:
                    feat_for_this += self.w2v_turkish[token]
                    
            feats.append(feat_for_this)
             
           
        return feats
