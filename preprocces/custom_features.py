import pandas as pd 
from preprocces.helper import get_absolute_path


class Feature_find():

    def __init__(self,badwordcount=True,total_length=True ,num_words=True,num_unique_words=True,words_vs_unique=True):
        path_badwords = get_absolute_path("data_sent","bad-words.csv")
        self.badwords = pd.read_csv(path_badwords,header=None,names = ["word"])
        self.badwords = list(self.badwords.word.values)


        self.badwordcount = badwordcount
        self.total_length = total_length
        #self.capitals = capitals
        #self.caps_vs_length = caps_vs_length
        #self.num_exclamation_marks = num_exclamation_marks
        #self.num_question_marks = num_question_marks
        #self.num_punctuation = num_punctuation
        #self.num_symbols = num_symbols
        self.num_words = num_words
        self.num_unique_words = num_unique_words
        self.words_vs_unique = words_vs_unique
        

    
    def data_analysis(self,dataset,text_column):
        dataset=dataset.copy()
        if self.badwordcount:
            dataset["badwordcount"] = dataset[text_column].astype(str).apply(lambda comment: sum(comment.count(w) for w in self.badwords))
        if self.total_length:
            dataset['total_length'] = dataset[text_column].astype(str).apply(len)
        #if self.capitals:
            #dataset['capitals'] = dataset[text_column].astype(str).apply(lambda comment: sum(1 for c in comment if c.isupper()))
        #if self.caps_vs_length:  
            #dataset['caps_vs_length'] = dataset.apply(lambda row: float(row['capitals']+1)/float(row['total_length']+1),axis=1)
        #if self.num_exclamation_marks:
            #dataset['num_exclamation_marks'] = dataset[text_column].astype(str).apply(lambda comment: comment.count('!'))
        #if self.num_question_marks:
            #dataset['num_question_marks'] = dataset[text_column].astype(str).apply(lambda comment: comment.count('?'))
        #if self.num_punctuation:
            #dataset['num_punctuation'] = dataset[text_column].astype(str).apply(lambda comment: sum(comment.count(w) for w in '.,;:'))
        #if self.num_symbols:
            #dataset['num_symbols'] = dataset[text_column].astype(str).apply(lambda comment: sum(comment.count(w) for w in '*&$%'))
        if self.num_words:
            dataset['num_words'] = dataset[text_column].astype(str).apply(lambda comment: len(comment.split()))
        if self.num_unique_words:
            dataset['num_unique_words'] = dataset[text_column].astype(str).apply(lambda comment: len(set(w for w in comment.split())))
        if self.words_vs_unique:
            dataset['words_vs_unique'] = dataset['num_unique_words'] / dataset['num_words']
        return dataset