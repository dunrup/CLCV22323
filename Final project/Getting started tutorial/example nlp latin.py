decliner = CollatinusDecliner()
word_tokenizer = WordTokenizer('latin')
lemmatizer = lemmaReplacer('latin')
translator = Synonyms(dictionary='synonyms', language='latin')

sentence = "arma virumque cano troiae qui primus ab oris"
words = word_tokenizer.tokenize(sentence)

print (words)
for word in words:
    word = lemmatizer.lemmatize(word)[0]
    word = ' '.join(i for i in word if not i.isdigit())
    try:
        print(decliner.decline(word))
        synonyms = translator.lookup(word)
        print (synonyms)

    except Exception:
        pass