from wordfreq import zipf_frequency, tokenize
from googletrans import Translator

def process_sub(text, type, score):
    important_words = set()
    if type == '.srt':
        text = text.split('\r\n\r\n')
        for segment in text:
            segment = segment.split('\r\n')[2: ]
            for line in segment:
                line = tokenize(line, 'en')
                for word in line:
                    if score / 1.05 < zipf_frequency(word, 'en') < score:
                        important_words.add(word)
    translator = Translator()
    important_words = list(important_words)
    result = translator.translate(important_words, src='en', dest='fa')
    answer = {}
    for res in result:
        answer[res.origin] = [res.text, False]
    return answer









