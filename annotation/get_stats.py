import json
from collections import defaultdict

DIRECTORY_REV = '../dataset/whole/json'
DIRECTORY_RAW = 'preview'

confusion_polarity = defaultdict(lambda : defaultdict(int))
confusion_aspect = defaultdict(lambda : defaultdict(int))

opinions_per_sentence = defaultdict(int)

stats_polarities = defaultdict(int)
stats_aspects = defaultdict(int)

for FILENUMBER in ['10', '11', '30', '31']:

    rev_data = json.loads(open(f'{DIRECTORY_REV}/{FILENUMBER}.json').read())
    raw_data = json.loads(open(f'{DIRECTORY_RAW}/{FILENUMBER}.json').read())

    for d in rev_data['data']:

        qnt_opinions_in_sentence = len(d['opinions'])

        opinions_per_sentence[qnt_opinions_in_sentence] += 1

        for r in raw_data['data']:

            guessed_polarity = r['polarity']
            guessed_aspect = r['aspect'].replace('Á', 'A')

            if int(r['sentence_id']) == d['id']:

                for opinion in d['opinions']:

                    revised_polarity = opinion[1]
                    revised_aspect = opinion[0].replace('Á', 'A')

                    if 'A' <= revised_aspect[0] <= 'Z':  # Lowercase aspects do not have meaningful polarity
                        stats_polarities[revised_polarity] += 1

                    stats_aspects[revised_aspect] += 1

                    if qnt_opinions_in_sentence == 1:

                        confusion_polarity[guessed_polarity][revised_polarity] += 1

                        for asp in guessed_aspect.split():
                            confusion_aspect[asp][revised_aspect] += 1


import pandas as pd

confusion_polarity_matrix = pd.DataFrame(confusion_polarity).T.fillna(0)
confusion_aspect_matrix = pd.DataFrame(confusion_aspect).T.fillna(0)
opinions_per_sentence_matrix = pd.DataFrame.from_dict(opinions_per_sentence, orient='index').fillna(0)

confusion_aspect_matrix = confusion_aspect_matrix.reindex(sorted(confusion_aspect_matrix.columns), axis=1)
confusion_polarity_matrix = confusion_polarity_matrix.reindex(sorted(confusion_polarity_matrix.columns), axis=1)
opinions_per_sentence_matrix = opinions_per_sentence_matrix.reindex(sorted(opinions_per_sentence_matrix.columns), axis=1)

confusion_aspect_matrix.to_csv('preview/statistics/aspect_confusion.csv')
confusion_polarity_matrix.to_csv('preview/statistics/polarity_confusion.csv')
opinions_per_sentence_matrix.to_csv('preview/statistics/opinions_per_sentence.csv', header=False)


print('\n\nOpinions per sentence')
for i in sorted(opinions_per_sentence.items(), key=lambda a : a[0]):
    print("  %2d :  %4d" % (i[0], i[1]))

