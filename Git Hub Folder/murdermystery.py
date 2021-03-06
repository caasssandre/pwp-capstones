murder_note = "You may call me heartless, a killer, a monster, a murderer, but I'm still NOTHING compared to the villian that Jay was. This whole contest was a sham, an elaborate plot to shame the contestants and feed Jay's massive, massive ego. SURE you think you know him! You've seen him smiling for the cameras, laughing, joking, telling stories, waving his money around like a prop but off camera he was a sinister beast, a cruel cruel taskmaster, he treated all of us like slaves, like cattle, like animals! Do you remember Lindsay, she was the first to go, he called her such horrible things that she cried all night, keeping up all up, crying, crying, and more crying, he broke her with his words. I miss my former cast members, all of them very much. And we had to live with him, live in his home, live in his power, deal with his crazy demands. AND FOR WHAT! DID YOU KNOW THAT THE PRIZE ISN'T REAL? He never intended to marry one of us! The carrot on the stick was gone, all that was left was stick, he told us last night that we were all a terrible terrible disappointment and none of us would ever amount to anything, and that regardless of who won the contest he would never speak to any of us again! It's definitely the things like this you can feel in your gut how wrong he is! Well I showed him, he got what he deserved all right, I showed him, I showed him the person I am! I wasn't going to be pushed around any longer, and I wasn't going to let him go on pretending that he was some saint when all he was was a sick sick twisted man who deserved every bit of what he got. The fans need to know, Jay Stacksby is a vile amalgamation of all things evil and bad and the world is a better place without him."
lily_trebuchet_intro = "Hi, I'm Lily Trebuchet from East Egg, Long Island. I love cats, hiking, and curling up under a warm blanket with a book. So they gave this little questionnaire to use for our bios so lets get started. What are some of my least favorite household chores? Dishes, oh yes it's definitely the dishes, I just hate doing them, don't you? Who is your favorite actor and why? Hmm, that's a hard one, but I think recently I'll have to go with Michael B. Jordan, every bit of that man is handsome, HANDSOME! Do you remember seeing him shirtless? I can't believe what he does for the cameras! Okay okay next question, what is your perfect date? Well it starts with a nice dinner at a delicious but small restaurant, you know like one of those places where the owner is in the back and comes out to talk to you and ask you how your meal was. My favorite form of art? Another hard one, but I think I'll have to go with music, music you can feel in your whole body and it is electrifying and best of all, you can dance to it! Okay final question, let's see, What are three things you cannot live without? Well first off, my beautiful, beautiful cat Jerry, he is my heart and spirit animal. Second is pasta, definitely pasta, and the third I think is my family, I love all of them very much and they support me in everything I do. I know Jay Stacksby is a handsome man and all of us want to be the first to walk down the aisle with him, but I think he might truly be the one for me. Okay that's it for the bio, I hope you have fun watching the show!"
myrtle_beech_intro = "Salutations. My name? Myrtle. Myrtle Beech. I am a woman of simple tastes. I enjoy reading, thinking, and doing my taxes. I entered this competition because I want a serious relationship. I want a commitment. The last man I dated was too whimsical. He wanted to go on dates that had no plan. No end goal. Sometimes we would just end up wandering the streets after dinner. He called it a \"walk\". A \"walk\" with no destination. Can you imagine? I like every action I take to have a measurable effect. When I see a movie, I like to walk away with insights that I did not have before. When I take a bike ride, there better be a worthy destination at the end of the bike path. Jay seems frivolous at times. This worries me. However, it is my staunch belief that one does not make and keep money without having a modicum of discipline. As such, I am hopeful. I will now list three things I cannot live without. Water. Emery boards. Dogs. Thank you for the opportunity to introduce myself. I look forward to the competition."
gregg_t_fishy_intro = "A good day to you all, I am Gregg T Fishy, of the Fishy Enterprise fortune. I am 37 years young. An adventurous spirit and I've never lost my sense of childlike wonder. I do love to be in the backyard gardening and I have the most extraordinary time when I'm fishing. Fishing for what, you might ask? Why, fishing for compliments of course! I have a stunning pair of radiant blue eyes. They will pierce the soul of anyone who dare gaze upon my countenance. I quite enjoy going on long jaunts through garden paths and short walks through greenhouses. I hope that Jay will be as absolutely interesting as he appears on the television. I find that he has some of the most curious tastes in style and humor. When I'm out and about I quite enjoy hearing tales that instill in my heart of hearts the fascination that beguiles my every day life. Every fiber of my being scintillates and vascillates with extreme pleasure during one of these charming anecdotes and significantly pleases my beautiful personage. I cannot wait to enjoy being on A Brand New Jay. It certainly seems like a grand time to explore life and love."

def get_average_sentence_length(text):
    new_text = text.replace("!", ".")
    final_text = new_text.replace("?", ".")
    sentences_in_text = final_text.split(".")
    combined_sentence_length = 0
    for sentence in sentences_in_text[0:(len(sentences_in_text)-1)]:
        stripped_sentence = sentence.strip()
        sentence_length = len(stripped_sentence.split(" "))
        combined_sentence_length += sentence_length
    return combined_sentence_length /(len(sentences_in_text)-1)

import string
def prepare_text(text):
    lower_case_text = text.lower()
    clean_text = ""
    for char in lower_case_text:
        if char in set(string.punctuation):
            clean_text += ""
        elif char not in set(string.punctuation):
            clean_text += char
    prepared_text = clean_text.split(" ")
    return prepared_text

def build_frequency_table(corpus):
    frequency_table = {}
    for word in corpus:
        if word not in frequency_table:
            frequency_table[word] = 1
        elif word in frequency_table:
            frequency_table[word] += 1
    return frequency_table

def ngram_creator(text_list):
    ngrammed_list = []
    for i in range(len(text_list)-1):
        ngrammed_list.append(text_list[i] + " " + text_list[i + 1])
    return ngrammed_list

class TextSample:
    def __init__(self, text, author):
        self.raw_text = text
        self.average_sentence_length = get_average_sentence_length(text)
        self.prepared_text = prepare_text(text)
        self.word_count_frequency = build_frequency_table(self.prepared_text)
        self.ngram_frequency = build_frequency_table(ngram_creator(self.prepared_text))
        self.author = author
    def __repr__(self):
        return "{author}'s text is {average_length} words long on average.".format(author = self.author, average_length = self.average_sentence_length)



murderer_sample = TextSample(murder_note, "the murderer")
lily_sample = TextSample(lily_trebuchet_intro, "Lily Trebuchet")
myrtle_sample = TextSample(myrtle_beech_intro, "Myrtle Beech")
gregg_sample = TextSample(gregg_t_fishy_intro, "Gregg T. Fishy")


def frequency_comparison(table1, table2):
    appearances = 0
    mutual_appearances = 0
    for key in table1:
        if key in table2:
            if table1[key] >= table2[key]:
                appearances += table1[key]
                mutual_appearances += table2[key]
            elif table1[key] < table2[key]:
                appearances += table2[key]
                mutual_appearances += table1[key]
        if key not in table2:
            appearances += table1[key]
    for key in table2:
        if key not in table1:
            appearances += table2[key]
    return mutual_appearances/appearances


def percent_difference(value1, value2):
    return abs(value1 - value2)/(value1 + value2)/2

def find_text_similarity(sample1, sample2):
    sentence_length_similarity = abs(1 - percent_difference(sample1.average_sentence_length, sample2.average_sentence_length))
    word_count_similarity = frequency_comparison(sample1.word_count_frequency, sample2.word_count_frequency)
    ngram_similarity = frequency_comparison(sample1.ngram_frequency, sample2.ngram_frequency)
    similarity_score = (sentence_length_similarity + word_count_similarity + ngram_similarity)/3
    return ("{contestant}'s text has a {score} out of 1 similarity score with the murderer's text".format(contestant = sample2.author, score = similarity_score))

print(find_text_similarity(murderer_sample, lily_sample))
print(find_text_similarity(murderer_sample, myrtle_sample))
print(find_text_similarity(murderer_sample, gregg_sample))
