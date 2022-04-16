from textblob import TextBlob, Word
import nltk
from nltk.corpus import gutenberg
from typing import List


stop_words = "he she I we they our a about after all also always am an and any are at be been being but by came can cant come could did didn't do does doesn't doing don't else for from get give goes going had happen has have having how i if ill i'm in into is isn't it its i've just keep let like made make many may me mean more most much no not now of only or our really say see some something take tell than that the their them then they thing this to try up us use used uses very want was way we what when where which who why will with without wont you your youre"
unwanted_tags = "CC CD DT EX MD PRP PRP$ TO WDT WP WP$ NNP POS"

#text = TextBlob("Once upon a time there was an old mother pig who had three little pigs and not enough food to feed them. So when they were old enough, she sent them out into the world to seek their fortunes. The first little pig was very lazy. He didn't want to work at all and he built his house out of straw. The second little pig worked a little bit harder but he was somewhat lazy too and he built his house out of sticks. Then, they sang and danced and played together the rest of the day.")
with open("sample.txt") as file:
	text = TextBlob(file.read())


word_list = text.words #list of str
all_sentences = text.sentences #list of named tuples
pos_tags = text.tags #list of tuples



def clean_text(text: str) -> List[tuple]:
	clean_tags = [w for w in text.tags if w[1] not in unwanted_tags] #filter out tags
	clean = [w for w in clean_tags if w[0] not in stop_words] #filter out stop words
	
	return clean

def get_all_definitions(word: str) -> List[str]:
	definitions = Word(word).define()

	return definitions

def get_definition(word: str) -> str:
	definition = Word(word).define()
	if definition:
		return definition[0]
	return definition #returns empty list

def simple_pos(text: List[tuple]) -> List[tuple]:
	for word in text:
		linguistic_tag = word[1]
		if linguistic_tag in 'VB VBD VBG VBN VBP VBZ':
			word[1] = 'verb'
		if linguistic_tag in 'RB RBR RBS':
			word[1] = 'adverb'
		if linguistic_tag in 'NNPS NNP NNS NN':
			word[1] = 'noun'
		if linguistic_tag in 'JJS JJR JJ':
			word[1] = 'adjective'
	return text


def count_sylls(word: str) -> int:
    count = 0
    vowels = 'aeiouy'
    word = word.lower()

    if word[0] in vowels:
        count +=1
    for index in range(1,len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            count +=1
    if word.endswith('e'):
        count -= 1
    if word.endswith('le'):
        count += 1
    if count == 0:
        count += 1

    return count


#def score_words(text: List[str]) -> List[dict]:
# 	cleaned_text = clean_text(text) 

# 	scored_words = []
# 	for word in set(cleaned_text): #set takes out duplicates
# 		word_len = len(word)
# 		num_sylls = count_sylls(word)
# 		frequency = cleaned_text.count(word) 
# 		definition_len = len([w for w in get_definition(word) if w not in stop_words]) 
		
# 		complexity_score = (definition_len) + (2*num_sylls) + (1.75*frequency) + (1.25*word_len) #no idea what I'm doing
		
# 		scored_words.append({
# 			'word': word, 
# 			'score': complexity_score,
# 			'def_len': definition_len 
# 			})
	
# 	sorted_words = sorted(scored_words, key = lambda k: k['score'], reverse = True) #sorts words from high score to low

# 	return sorted_words

def score_words(text: str) -> List[dict]:
	cleaned_text = clean_text(text) #list of tuples [(word, tag)]
	word_list = [w[0] for w in cleaned_text]

	scored_words = []
	for word in cleaned_text:
		word_len = len(word[0])
		num_sylls = count_sylls(word[0])
		frequency = word_list.count(word[0]) 
		definition_len = len([w for w in get_definition(word[0]) if w not in stop_words]) 
		
		complexity_score = (definition_len) + (2*num_sylls) + (1.75*frequency) + (1.25*word_len) #no idea what I'm doing
		
		scored_words.append({
			'word': word[0],
			'tag': word[1],
			'def_len': definition_len,
			'frequency': frequency,  
			'score': complexity_score,
			})
	
	sorted_words = sorted(scored_words, key = lambda k: k['score'], reverse = True) #sorts words from high score to low

	return sorted_words

def vocab_list(text: List[str], num_words: int) -> list:
	sorted_words = score_words(text)

	vocab = [i['word'] for i in sorted_words][:num_words]
	
	return vocab

print(score_words(text))


# def get_examples(word: str) -> List[str]:
# 	while len(examples) < 5:
# 	examples = []
# 	for fileid in gutenberg.fileids():
# 		sentences = gutenberg.sents(fileid)
# 		for sentence in sentences:
# 			if word in sentence:
# 				examples.append(sentence)


# 	return examples



# def write_to_excel():
# 	return

# def write_to_db():
# 	word
# 	definition
# 	pos
# 	examples
# 	score
# 	return


