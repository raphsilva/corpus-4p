import json
from pprint import pprint
from collections import defaultdict

DIRECTORY_REV = '../dataset/whole/json'
DIRECTORY_RAW = 'preview'

confusion_polarity = defaultdict(lambda : defaultdict(int))
confusion_aspect = defaultdict(lambda : defaultdict(int))

opinion_amount_stats = defaultdict(int)

stats_polarities = defaultdict(int)
stats_aspects = defaultdict(int)

count_sentences = defaultdict(int)
count_reviews = defaultdict(int)

count_words = 0

for FILENUMBER in ['10', '11', '30', '31']:

    distinct_sentences = set()
    distinct_reviews = set()

    rev_data = json.loads(open(f'{DIRECTORY_REV}/{FILENUMBER}.json').read())
    raw_data = json.loads(open(f'{DIRECTORY_RAW}/{FILENUMBER}.json').read())

    for r in raw_data['data']:
        distinct_sentences.add(r['sentence_id'])
        distinct_reviews.add(r['review_id'])
        count_words += len(r['sentence'].split())

    count_sentences[FILENUMBER] = len(distinct_sentences)
    count_reviews[FILENUMBER] = len(distinct_reviews)

    for d in rev_data['data']:

        amount_opinions = len(d['opinions'])

        opinion_amount_stats[amount_opinions] += 1

        for r in raw_data['data']:

            ori_pol = r['polarity']
            ori_asp = r['aspect']

            if int(r['sentence_id']) == d['id']:

                for opinion in d['opinions']:

                    rev_pol = opinion[1]
                    rev_asp = opinion[0].replace('Á', 'A')

                    if 'scope' in rev_asp and amount_opinions > 1:
                        print(FILENUMBER, d['id'])
                        print(d['opinions'])
                        print()

                    if 'A' <= rev_asp[0] <= 'Z':
                        stats_polarities[rev_pol] += 1
                    stats_aspects[rev_asp] += 1

                    if amount_opinions == 1:

                        confusion_polarity[ori_pol][rev_pol] += 1

                        for asp in ori_asp.split():
                            confusion_aspect[asp][rev_asp] += 1


    # pprint(raw_data)
# exit()

pprint(confusion_polarity)

pprint(confusion_aspect)

pprint(opinion_amount_stats)

import pandas as pd

confusion_polarity_matrix = pd.DataFrame(confusion_polarity).T.fillna(0)
print(confusion_polarity_matrix)

confusion_aspect_matrix = pd.DataFrame(confusion_aspect).T.fillna(0)
confusion_aspect_matrix = confusion_aspect_matrix.reindex(sorted(confusion_aspect_matrix.columns), axis=1)
# confusion_aspect_matrix = confusion_aspect_matrix.sort_index(by=0, ascending=[True])
print(confusion_aspect_matrix)


confusion_aspect_matrix.to_csv('confusion_aspect_matrix.csv')

pprint(stats_aspects)
pprint(stats_polarities)

pprint(count_sentences)
pprint(count_reviews)
pprint(count_words)