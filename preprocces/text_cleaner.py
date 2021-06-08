
import pandas as pd
import re
import string
import nltk
from nltk.corpus import stopwords


class cleaner():
    def __init__(self, numbers=True, usernames=True, endline_chars=True, urls=True, hashtags=True, emojis=True,
                 character_entity_references=False, dates=True, times=True, words_with_digits=True, clean_special_chars=False,
                 repeated_letters=True, words_with_repeated_letters=True, one_letter_words=True, two_letter_words=True,
                 digits=True, multiple_spaces=True,enc_decode=True):
        
        self.numbers = numbers
        self.usernames = usernames
        self.endline_chars = endline_chars
        self.urls = urls
        self.hashtags = hashtags
        self.emojis = emojis
        self.character_entity_references = character_entity_references
        self.dates = dates
        self.times = times
        self.words_with_digits = words_with_digits
        self.clean_special_chars = clean_special_chars
        self.repeated_letters = repeated_letters
        self.words_with_repeated_letters = words_with_repeated_letters
        self.one_letter_words = one_letter_words
        self.two_letter_words = two_letter_words
        self.digits = digits
        self.multiple_spaces = multiple_spaces
        self.enc_decode = enc_decode

    def clean_numbers (self,text):
        
        number = re.compile(r" \d+")
        text = number.sub(" ", str(text))
        return text
        
    def clean_usernames(self,text):
        """
        Replace the usernames of the form '@username' with a space character in the given string. The preceding
        '@' signs are also removed.

        :param text: Input string to be cleaned
        :return: Cleaned version of the input
        """
        username = re.compile(r"@\S+")
        text = username.sub(" ", text)
        return text

    def clean_urls(self,text):
        """
        Replace the urls with a space character in the given string. The urls can be of the form 'https://.....'
        or 'http://.....'"

        :param text: Input string to be cleaned
        :return: Cleaned version of the input
        """
        url = re.compile(r"https?://\S+")
        text = url.sub(" ", text)
        return text
    
    def clean_endline_chars(self,text):
        """
        Replace the endline characters of the form '\n' with a space character in the given string.

        :param text: Input string to be cleaned
        :return: Cleaned version of the input
        """
        endline_char = re.compile(r"\\n")
        text = endline_char.sub(" ", text)
        return text
    
    def clean_hashtags(self,text):
        """
        Replace the hashtags of the form '#hashtag' with a space character in the given string. The preceding '#' signs
        are also removed.

        :param text: Input string to be cleaned
        :return: Cleaned version of the input
        """
        hashtag = re.compile(r"#\S+")
        text = hashtag.sub(" ", text)
        return text
    
    def clean_emojis(self,text):
        """
        Replace unicode emoji characters with a space character in the given string.

        :param text: Input string to be cleaned
        :return: Cleaned version of the input
        """
        emoji = re.compile(
            r"(["
            "\U0001F1E0-\U0001F1FF"  # flags (iOS)
            "\U0001F300-\U0001F5FF"  # symbols & pictographs
            "\U0001F600-\U0001F64F"  # emoticons
            "\U0001F680-\U0001F6FF"  # transport & map symbols
            "\U0001F700-\U0001F77F"  # alchemical symbols
            "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
            "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
            "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
            "\U0001FA00-\U0001FA6F"  # Chess Symbols
            "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
            "\U00002702-\U000027B0"  # Dingbats
            "])")
        text = emoji.sub(" ", text)
        return text
    def clean_character_entity_references(self,text):
        """
        Do the following conversions in a given string:
            '&amp;' --> '&',   '&lt;' --> '<',   '&gt;' --> '>'

        :param text: Input string to be cleaned
        :return: Cleaned version of the input
        """
        ampersand_cer = re.compile(r"&amp;")
        text = ampersand_cer.sub("&", text)
        less_than_cer = re.compile(r"&lt;")
        text = less_than_cer.sub("<", text)
        greater_then_cer = re.compile(r"&gt;")
        text = greater_then_cer.sub(">", text)
        return text

    def clean_dates(self,text):
        """
        Replace dates with a space character in the given string. The dates can be of the following forms:
        'D-M-YYYY', 'DD-MM-YYYY', 'DD-MM-YY', 'M-D-YYYY', 'MM-DD-YYYY', 'MM-DD-YY'
        'YYYY-M-D', 'YYYY-MM-DD', 'YY-MM-DD', 'YYYY-D-M', 'YYYY-DD-MM', 'YY-DD-MM'

        The splitting character '-' can be replaced by '.' or '/'.

        :param text: Input string to be cleaned
        :return: Cleaned version of the input
        """
        date = re.compile(r"(\d\d?[-./]\d\d?[-./]\d\d(\d\d)?)|(\d\d(\d\d)?[-./]\d\d?[-./]\d\d?)")
        text = date.sub(" ", text)
        return text


    def clean_times(self,text):
        """
        Replace times with a space character in the given string. The times can be of the following forms:
        'HH:MM', 'HH:MM:SS', 'HH:MM:SS:S', 'HH:MM:SS:SS', 'HH:MM:SS:SSS'...

        The splitting character ':' can be replaced by '.'.

        :param text: Input string to be cleaned
        :return: Cleaned version of the input
        """
        time = re.compile(r"\d\d[:.]\d\d([:.]\d\d([:.]\d+)?)?")
        text = time.sub(" ", text)
        return text

    def clean_words_with_digits(self,text):
        """
        Replace all chunks of characters that include digits with a space character in the given string. Special
        characters at the boundaries are not removed.
        This method removes all the dates and times as well.
        Examples: 'as asd12. as' --> 'as  . as', 'class 43c accepted' --> 'class   accepted'

        :param text: Input string to be cleaned
        :return: Cleaned version of the input
        """
        word_with_digit = re.compile(r"\b\S*\d+\S*\b")
        text = word_with_digit.sub(" ", text)
        return text


    def clean_special_chars(self,text):
        """
        Replace all special characters, that is, characters that are not a letter, digit or a namespace character, with
        a space character in the given string.

        :param text: Input string to be cleaned
        :return: Cleaned version of the input
        """
        # not a letter nor a digit
        special_char = re.compile(r"[^a-zA-Z0-9\s]")
        text = special_char.sub(" ", text)
        return text

    def clean_repeated_letters(self,text):
        """
        If a letter is repeated three or more times consecutively in a given string, remove some of those letters
        so that only one remains.
        Examples: 'hahahahaaaahaa' --> 'hahahahaha', 'this is sooo goooood' --> 'this is so god'

        :param text: Input string to be cleaned
        :return: Cleaned version of the input
        """
        # leave only one if the letter is repeated more than 2 times
        repeated_letter = re.compile(r"([a-zA-Z])\1{2,}")
        text = repeated_letter.sub(r"\1", text)
        return text

    def clean_words_with_repeated_letters(self,text):
        """
        If the given string contains words that have a certain letter repeating three or more times consecutively,
        replace those words with a space character in the given string.

        :param text: Input string to be cleaned
        :return: Cleaned version of the input
        """
        word_with_repeated_letter = re.compile(r"\b\S*([a-zA-Z])\1{2,}\S*\b")
        text = word_with_repeated_letter.sub(" ", text)
        return text

    def clean_one_letter_words(self,text):
        """
        Remove words that consist of only one letter from a given string.

        :param text: Input string to be cleaned
        :return: Cleaned version of the input
        """
        one_letter_word = re.compile(r"\b[a-zA-Z]\b")
        text = one_letter_word.sub("", text)
        return text

    def clean_two_letter_words(self,text):
        """
        Remove words that consist of only two letters from a given string

        :param text: Input string to be cleaned
        :return: Cleaned version of the input
        """
        two_letter_word = re.compile(r"\b[a-zA-Z][a-zA-Z]\b")
        text = two_letter_word.sub("", text)
        return text


    def clean_digits(self,text):
        """
        Replace all digits with a space character in the given string.

        :param text: Input string to be cleaned
        :return: Cleaned version of the input
        """
        digit = re.compile(r"\d")
        text = digit.sub(" ", text)
        return text

    def clean_multiple_spaces(self,text):
        """
        If the given string contains multiple space characters consecutively, replace those multiple space characters
        with only one space character.

        :param text: Input string to be cleaned
        :return: Cleaned version of the input
        """
        multiple_space = re.compile(r"\s{2,}")
        text = multiple_space.sub(" ", text)
        return text
    
    def enc_decode(self,text):
        text = text.encode('ascii','ignore') 
        text = text.decode(encoding='UTF-8') 
        return text
    
    """
    def slang(self,text):
        if any(item in text.split() for item in slang_words["acronym"].tolist()):
            a = text.split()
            for i,row in slang_words.iterrows():
                if row["acronym"] in a:
                    a = [row["real"] if x==row["acronym"] else x for x in a]
                    x = ' '.join(a)
            return x
        else:
            return text
     """
    
    
    def clean(self, text):
        """
        Applies all of the cleaning methods specified by the initial parameters in order to a given string.

        :param text: Input string to be cleaned
        :return: Cleaned version of the input
        """
    

        clean_methods = [self.clean_numbers, self.clean_usernames, self.clean_urls, self.clean_endline_chars,                      
                         self.clean_hashtags,self.clean_emojis, 
                         self.clean_character_entity_references,
                         self.clean_dates, self.clean_times, self.clean_words_with_digits, self.clean_special_chars,
                         self.clean_repeated_letters, self.clean_words_with_repeated_letters,
                         self.clean_one_letter_words, self.clean_two_letter_words, self.clean_digits,
                         self.clean_multiple_spaces,self.enc_decode]

        for ind, attr in enumerate(list(self.__dict__.keys())[:-1]):
            if self.__dict__[attr]:
                text = clean_methods[ind](text)

        return text
