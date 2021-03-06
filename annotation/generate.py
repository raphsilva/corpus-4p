import datetime
import io
import json
import os

date = datetime.datetime.now()

SENTENCE_BEGIN_INDICATOR = '::'  # Symbol used to indicate beginning of sentence in the dataset.

# Input directories
DIR_ANNOTATED_MANUAL = 'input/revised'
DIR_ANNOTATED_AUTO = 'input/automatic'

# Output directories
DIR_FORMATTED_SPLIT = '../dataset/whole/opinions'  # Folder where formatted files will be saved to.
DIR_FORMATTED_NOSPLIT = '../dataset/whole/sentences'  # Folder where formatted files will be saved to.
DIR_OUTPUT_JSON = '../dataset/whole/json'  # Folder where formatted files will be saved to.
DIR_PREVIEW = 'preview'  # Folder that will contain files to help review the annotation.

# Create directories 
output_directories = [DIR_FORMATTED_SPLIT, DIR_FORMATTED_NOSPLIT, DIR_OUTPUT_JSON, DIR_PREVIEW]
for i in output_directories:
    if not os.path.exists(i):
        os.makedirs(i)


# Read file (revised or automatically annotated)
def getInfo(filename):
    # Get product ID from filename 
    product_id = filename.split('/')[-1].split('.')[0]

    # /r/ will contain the information returned.
    r = {}
    r['data'] = []  # Will save the main info
    r['meta'] = []  # Will save metadata 

    entry_id = 0  # Will keep track of the position of each entry in the file

    data = io.open(filename, 'r', encoding="utf-8").read()  # Read file

    for line in data.splitlines():

        # Skip blank lines
        if len(line) == 0:
            continue

        # Line containing metadata
        if line[0] == '>':
            r['meta'].append(line)
            continue

        # Skip line containing comment
        if line[0] == '#':
            continue

        # Unexpected line (not a comment, not metadata, not data)
        if '[' not in line:
            print("Weird line. Please check:")
            print(line, end="\n")
            continue

        flag = line[0:line.find('(')].replace(' ', '')  # Gets flags (such as 'd' for "duplicated", 'x' for "garbage")

        line = line[line.find('('):]  # Removes flags from line (were already saved)

        sentence = line.split('::')[-1]  # Get sentence from the entry
        info = line.split('::')[0]  # Get info (polarity, aspect, etc) from the sentence
        info = info.replace('[', '').replace('(',
                                             '')  # Remove characters that won't be used (they are there for human readability)
        line_id = info.split(')')[0]

        n = {}  # Will save information about this entry
        n['product_id'] = product_id
        n['review_id'] = line_id.split('.')[0]
        n['sentence_id'] = line_id.split('.')[1]
        n['polarity'] = info.split(' ')[1].split(']')[0]
        n['aspect'] = cleanExtraSpaces(info.split(']')[1])
        n['sentence'] = cleanExtraSpaces(sentence)
        n['entry_id'] = entry_id
        n['flags'] = flag

        entry_id += 1

        r['data'].append(n)

    return r


def opinionToStringPlain(opinion):
    s = ''
    s += opinion['flags']
    for a in range(3 - len(opinion['flags'])):
        s += ' '
    s += '[' + str(opinion['review_id']) + '.'
    s += str(opinion['sentence_id']) + ']'
    s += '%22s' % ('[' + opinion['aspect'] + '][' + opinion['polarity'] + ']')
    s += '    '
    s += str(opinion['sentence'])
    return s


# Removes any spaces in the beginning or end of a string; transforms double spaces into single spaces.
def cleanExtraSpaces(text):
    r = text
    while len(r) > 0 and r[0] == ' ':
        r = r[1:]
    while len(r) > 0 and r[-1] == ' ':
        r = r[:-1]
    return r.replace('  ', ' ')


def formatSentence(sentence):
    r = sentence
    while sentence[0] == ' ' and len(sentence) > 0:
        sentence = sentence[1:]
    r = sentence[0].upper() + sentence[1:]
    if sentence[-1].isalpha() or sentence[-1].isdigit():
        r += '.'
    return cleanExtraSpaces(r)


def opinionToString(opinion):
    s = ''
    s += opinion['review_id'] + '.' + opinion['sentence_id'] + '.' + str(opinion['id_f']) + ')  '
    for a in range(2 - len(opinion['polarity'])):
        s += ' '
    s += '[' + opinion['polarity'] + ']'
    s += '[' + opinion['aspect'] + ']'
    for a in range(16 - len(opinion['aspect'])):
        s += ' '
    s += '  ::  '
    s += str(formatSentence(opinion['sentence']))  # Sentence separator can't be used in the middle of a sentence

    return s


def originString(opinion):
    s = ''
    s += str(opinion['product_id']) + '.' + str(opinion['id_f'])
    s += '  >  '
    s += str(opinion['product_id']) + '.'
    s += str(opinion['review_id']) + '.'
    s += str(opinion['sentence_id'])
    if opinion['id_complement'].replace(' ', '') != '':
        s += '-' + str(opinion['id_complement'])
    return s


ids_correspondency = {}


def register_id(opinion):
    global ids_correspondency
    new_id = str(opinion['product_id']) + '.' + str(opinion['id_f'])
    old_id = str(opinion['product_id']) + '.' + str(opinion['review_id']) + '.' + str(opinion['sentence_id'])
    ids_correspondency[new_id] = old_id


def getPolarity(s):
    if '+' in s:
        return '+'
    elif '-' in s:
        return '-'
    elif 'x' in s or 'X' in s:
        return 'x'
    else:
        return '.'


def isExceptionAspect(aspectname):
    if 'a' <= aspectname[0] <= 'z':
        return True
    return False


def countAspects(info):
    count_aspects = {}
    count_aspects['_TOTAL_'] = {'+': 0, '-': 0, '.': 0, 'x': 0, 'total': 0}

    for i in info:

        for d in range(len(i['aspect'])):
            aspect = i['aspect'][d]
            polarity = i['polarity'][d]

            if aspect not in count_aspects:
                count_aspects[aspect] = {'+': 0, '-': 0, '.': 0, 'x': 0, 'total': 0}
            count_aspects[aspect][getPolarity(polarity)] += 1

            if not isExceptionAspect(aspect):
                count_aspects['_TOTAL_'][getPolarity(polarity)] += 1

    return count_aspects


def countAspects_segments(info):
    count_aspects = {}
    count_aspects['_TOTAL_'] = {'+': 0, '-': 0, '.': 0, 'x': 0, 'total': 0}
    for i in info:
        if i['aspect'] not in count_aspects:
            count_aspects[i['aspect']] = {'+': 0, '-': 0, '.': 0, 'x': 0, 'total': 0}
        count_aspects[i['aspect']][getPolarity(i['polarity'])] += 1
        count_aspects['_TOTAL_'][getPolarity(i['polarity'])] += 1
    return count_aspects


def lineAspectsCounts(list_of_aspects, aspect):
    s = ''
    s += "%-21s" % (aspect)
    s += "%6d" % list_of_aspects[aspect]['+']
    s += "%10d" % list_of_aspects[aspect]['-']
    s += "%10d" % list_of_aspects[aspect]['.']
    s += "%10d" % list_of_aspects[aspect]['x']
    s += "%10d" % (list_of_aspects[aspect]['+'] + list_of_aspects[aspect]['-'] + list_of_aspects[aspect]['.'] +
                   list_of_aspects[aspect]['x'])
    return s.replace(' 0 ', '   ')


# Kludge to be able to sort Portuguese words alphabetically. 
s = 'aáÁàÀAâÂbBcCçÇdDeêÊéEfFgGğĞhHiİîÎíīıIÍjJkKlLmMnNóoOÓöÖôpPqQrRsSşŞtTuUÚûúÛüÜvVwWxXyYzZ_'
s2 = 'aaAaAAaAbBcCcCdDeeEeEfFgGgGhHiIiIiiıIIjJkKlLmMnNooOOoOopPqQrRsSsStTuUUuuUuUvVwWxXyYzZ_'
trans = str.maketrans(s, s2)


def unikey(seq):
    if seq == '_TOTAL_':
        return 'ZZ'
    return seq.translate(trans)


def tabularAspectsCount(list_of_aspects):
    s = '# '
    s += "%-17s" % 'aspect'
    s += "%10s" % 'positive'
    s += "%10s" % 'negative'
    s += "%10s" % 'neutral'
    s += "%10s" % 'non-op'
    s += "%10s" % 'total'
    s = s.replace(' ', '_')
    s += '\n'
    for a in sorted(list_of_aspects, key=unikey):
        s += '# '
        l = lineAspectsCounts(list_of_aspects, a)
        if len(s.splitlines()) % 2 == 1:
            l = l.replace('   ', ' _ ')
        if a == '_TOTAL_':
            l = l.replace(' ', '_')
        s += l
        s += '\n'
    return s


files_to_read = []
list_of_files = [f for f in os.listdir(DIR_ANNOTATED_MANUAL) if
                 os.path.isfile(os.path.join(DIR_ANNOTATED_MANUAL, f))]  # List of data files already saved in the disk
for i in list_of_files:
    i_filename = i.split('.')[0]  # Get filename without extension, which is that product's ID
    files_to_read.append(i)

iteration = 0

for filename in files_to_read:

    iteration += 1

    print(">> PROCESSING FILE %s (%d/%d)" % (filename, iteration, len(files_to_read)))

    i_filename = filename.split('.')[0]

    info_revised = getInfo(DIR_ANNOTATED_MANUAL + '/' + filename)
    info_raw = getInfo(DIR_ANNOTATED_AUTO + '/' + filename)

    data_revised = info_revised['data']

    data_merged = []

    count_stats = {}

    c_sentences_included = 0

    for r in info_raw['data']:

        n = {}
        n['aspect'] = []
        n['polarity'] = []
        n['excerpts'] = []
        n['review_id'] = r['review_id']
        n['product_id'] = r['product_id']
        n['sentence_id'] = r['sentence_id']
        n['sentence'] = formatSentence(r['sentence'])

        for p in data_revised:
            if p['sentence_id'] == r['sentence_id']:
                n['excerpts'].append(p['sentence'])
                if p['flags'] != '':
                    if p['flags'] == 'J':
                        n = None
                        break
                    if p['flags'] == 'd':
                        n['aspect'] = ['duplicate']
                        p['aspect'] = 'duplicate'
                    elif p['flags'] == 'u':
                        n['aspect'] = ['unintelligible']
                        p['aspect'] = 'unintelligible'
                    elif p['flags'] == 'b':
                        n['aspect'] = ['broken']
                        p['aspect'] = 'broken'
                    elif p['flags'] == 'i':
                        n['aspect'] = ['irrelevant']
                        p['aspect'] = 'irrelevant'
                    elif p['flags'] == 'c':
                        n['aspect'] = ['context']
                        p['aspect'] = 'context'
                    else:
                        n['aspect'] = ['outscope']
                        p['aspect'] = 'outscope'
                    n['polarity'] = ['x']
                    p['polarity'] = 'x'
                    # continue
                else:
                    n['aspect'].append(p['aspect'])
                    n['polarity'].append(p['polarity'])

        if n == None:
            continue

        if len(n['aspect']) == 0:
            n['aspect'] = ['none']
            n['polarity'] = ['x']

        aspects = n['aspect']
        polarities = n['polarity']

        for i in range(len(aspects)):

            if aspects[i] not in count_stats:
                count_stats[aspects[i]] = {}
            if polarities[i][0] not in count_stats[aspects[i]]:
                count_stats[aspects[i]][polarities[i][0]] = 0
            count_stats[aspects[i]][polarities[i][0]] += 1

        data_merged.append(n)

        c_sentences_included += 1

    # Count reviews
    rrr = []
    for i in data_merged:
        if i['review_id'] not in rrr:
            rrr.append(i['review_id'])

    print(filename)
    print(len(rrr))

    filename_save = i_filename

    info_revised['meta'].append("> File generation date: " + str(date.strftime("%Y-%m-%d")))

    f = open(DIR_PREVIEW + '/' + filename_save + '.txt', 'w')
    for i in info_revised['meta']:
        f.write(i + '\n\n')
    f.write('\n')
    for i in data_revised:
        f.write(opinionToStringPlain(i))
        f.write('\n\n')
    f.close()

    f = open(DIR_PREVIEW + '/' + filename_save + '.diff', 'w')
    for i in info_revised['meta']:
        f.write(i.replace('>', ' ') + '\n\n')
    f.write('\n')
    for i in info_raw['data']:
        if i['sentence'] not in [y['sentence'] for y in info_revised['data']]:
            f.write('<' + opinionToStringPlain(i))
            f.write('\n')
            for j in info_revised['data']:
                if j['sentence_id'] == i['sentence_id']:
                    f.write('>' + opinionToStringPlain(j))
                    f.write('\n')
            f.write('\n')
    f.close()

    count_aspects = countAspects(data_merged)

    f = open(DIR_FORMATTED_SPLIT + '/' + filename_save + '.txt', 'w')

    for i in info_revised['meta']:
        f.write(i + '\n\n')
    f.write(tabularAspectsCount(count_aspects))
    f.write('\n\n\n\n')

    data_parsed_by_aspects = sorted(data_revised, key=lambda k: (
    unikey(k['aspect']), k['polarity'], len(k['sentence']), unikey(formatSentence(k['sentence']))))
    id_f = 1
    for i in data_parsed_by_aspects:
        i['id_f'] = ("%04d" % (id_f))
        register_id(i)
        id_f += 1
        f.write(opinionToString(i))
        f.write('\n\n')
    f.close()

    f = open(DIR_FORMATTED_NOSPLIT + '/' + filename_save + '.txt', 'w')

    info_revised['meta'].append('> Total of opinions: %d' % (len(data_revised)))
    info_revised['meta'].append('> Total of sentences: %d' % (len(data_merged)))

    for i in info_revised['meta']:
        f.write(i + '\n\n')
    f.write(tabularAspectsCount(count_aspects))
    f.write('\n\n\n\n')
    data_parsed_by_aspects = sorted(data_merged, key=lambda k: (
    len(k['aspect']) == 0, len(k['aspect']), unikey(str(sorted(k['aspect']))), str(k['polarity']), len(k['sentence']),
    unikey(formatSentence(k['sentence']))))

    for i in data_parsed_by_aspects:

        f.write('(%03d.%03d)\n%s\n\n' % (int(i['review_id']), int(i['sentence_id']), i['sentence']))
        for s in range(len(i['aspect'])):
            f.write('%s %-2s\n' % (i['aspect'][s], i['polarity'][s]))

        f.write('\n')
        f.write('\n\n')
    f.close()

    meta_info = {}
    for i in info_revised['meta']:
        a = i.split(':')[0].replace('> ', '')
        b = i.split(':')[1][1:]
        meta_info[a] = b

    s = {}
    s['meta'] = meta_info
    s['data'] = data_merged

    for i in s['data']:
        i['opinions'] = []
        for j in range(len(i['aspect'])):
            i['opinions'].append((i['aspect'][j], i['polarity'][j]))
        del i['aspect']
        del i['polarity']
        del i['product_id']
        # del i['sentence_id']
        del i['review_id']
        i['id'] = int(i['sentence_id'])
        del i['sentence_id']
        if len(i['excerpts']) <= 1:
            del i['excerpts']

    s['meta']['Human editor'] = None
    del s['meta']['Human editor']

    for i in s['data']:
        i['sentence'] = i['sentence'].replace('\"', '&dquote&')
        i['sentence'] = i['sentence'].replace('\'', '&squote&')

    f = open(DIR_OUTPUT_JSON + '/' + filename_save + '.json', 'w')
    f.write(json.dumps(s, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False))
    f.close()
