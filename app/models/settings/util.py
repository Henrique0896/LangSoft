import collections

def get_most_used_words(text, quantity):
    skipwords = set(line.strip() for line in text)
    skipwords = skipwords.union(
        {'mr', 'mrs', 'one', 'two', 'said', 'the', 'by', 'of', 'in', 'for', 'were', 'are', 'from', 'as', 'and', 'is',
         'to', 'its', 'has', 'was', 'been', 'an', 'on', 'if', 'per', 'each', 'when'})

    wordcount = {}
    for word in text.lower().split():
        word = word.replace(".","")
        word = word.replace(",","")
        word = word.replace(":","")
        word = word.replace("\"","")
        word = word.replace("!","")
        word = word.replace("â€œ","")
        word = word.replace("â€˜","")
        word = word.replace("*","")
        if word not in skipwords:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1

    return list(collections.Counter(wordcount))[:int(quantity)]

