import random

articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL")
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")

def getWords(fileName):
    with open("fileName", "r") as fileName:
        word = [word.strip() for word in fileName]
        return tuple(word)
    
def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()
    

def main():
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())
# The entry point for program execution
if __name__ == "__main__":
    main()
    articles = getWords("articles.txt")
    nouns = getWords("nouns.txt")
    verbs = getWords("verbs.txt")
    prepositions = getWords("prepositions.txt")