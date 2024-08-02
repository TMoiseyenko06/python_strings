#Task 1: Keyoword Highlighter

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
neutral_words = ['average']
all_words = positive_words + negative_words + neutral_words

def bold_words(reviews,words):
    for review in reviews:
        for word in words:
            if review.find(word) >= 0:
                print(review.replace(word,word.upper()))

def tally_words(reviews,positive,negative):
    for review in reviews:
        review_low = review.lower()
        positive_tally = 0
        negative_tally = 0
        for word in positive:
            if word in review_low:
                positive_tally += 1
        for word in negative:
            if word in review_low:
                negative_tally += 1
        print(f'This review has {positive_tally} positive words and {negative_tally} words : {review}')

def summary(reviews):
    for review in reviews:
        review_temp = review.split()
        review_final = []
        counter = 0
        for word in review_temp:
                if counter <= 30:
                    counter += len(word)
                    review_final.append(word)
        print(' '.join(review_final) + '...')

            
    




print('Task 1: vvvvvvvvvvvvvvvvvvvvvvv')
bold_words(reviews,all_words)
print('Task 2: vvvvvvvvvvvvvvvvvvvvvvv')
tally_words(reviews,positive_words,negative_words)
print('Task 3: vvvvvvvvvvvvvvvvvvvvvvv')
summary(reviews)

