This repository contains two directories that are different versions of the same corpus: the `skim` directory contains a clean, extended version for general use, and the` whole` directory contains the files and scripts used for annotation and all information extracted from the site displayed in ways that ease both human and machine readability, including information that are not necessarily useful for the task of contrastive summarization. Meta information is kept in all files.


## Skim dataset

The clean and extended version of the dataset contains 16 files in JSON format and is in the `skim` directory. Each file contains opinions about an entity. The entities D1a, D1b, D2a and D2b are real and the others are fictitious, formed from subsets of the sentences of real entities. The format of the files is as in the example below. The opinions found in sentences are represented by a word that identifies the aspect and a number that identifies the polarity: 100 for positive, -100 for negative, and 0 for neutral. Irrelevant opinions are not present in these sets.

```json
{
    "id": 328,
    "sentence": "Gostei do produto, apenas a bateria a bateria podia ser melhor.",
    "opinions": [
        ["PRODUTO",100],
        ["BATERIA",-100]
    ]
}
```


## Whole

The directory `whole` contains all data extracted from the source after it has been annotated and formatted. It contains files for the four products whose comments have been collected. The dataset comes in three flavors, two intended for human readability and one that joins all information thought for machine input:

**sentences**: Text is segmented by sentences. All opinions of each sentence are identified:
```
(133.328)
Gostei do produto, apenas a bateria a bateria podia ser melhor.

PRODUTO + 
BATERIA - 
```
**opinions**: Text is segmented by excerpts where each excerpt contain only one opinion:
```
133.328.0459)   [+][PRODUTO]           ::  Gostei do produto.
133.328.0044)   [-][BATERIA]           ::  Apenas a bateria a bateria podia ser melhor.
```
**json**: Information of segmentation is kept for both sentences and opinions:
```json
{
        "id": 328,    
        "sentence": "Gostei do produto, apenas a bateria a bateria podia ser melhor.",    
        "opinions": [
            ["PRODUTO","+"],
            ["BATERIA","-"]
        ],
        "excerpts": [
            "Gostei do produto.",
            "apenas a bateria a bateria podia ser melhor."
        ]          
    }
}
``` 

## Metadata

Metadata are kept in all files. They show information about the entity, the reviews extracted and the annotation process. Example of metadata is:
```buildoutcfg
ID: 10
Type: Celular
Product: Smartphone Motorola Moto G 5 Plus XT1683
Average rating: 9/10 
Total of reviews: 229
Crawl date: 17/may/2018 
Source: www.buscape.com.br/smartphone-motorola-moto-g-5-plus-xt1683
Human annotators: Otávio (May 2018), Raphael (July 2018, September 2019)
File generation date: 2019-09-29
Total of opinions: 799
Total of sentences: 592
```

Files intended for human readability contain a table that summarizes quantitatively the aspects and polarities found for the entity: 
```buildoutcfg
#_aspect_____________positive__negative___neutral____non-op_____total
# ACESSÓRIO                 6         5                            11
# ÁUDIO _  _  _  _  _  _  _  _  _  _  1 _  _  _  _  _  _  _  _  _   1
# BATERIA                             1                             1
# DESIGN _  _  _  _  _  _   2 _  _  _  _  _  _  _  _  _  _  _  _  _ 2
# FOCO                      3         1                             4
# FOTO _  _  _  _  _  _  _  8 _  _  _  _  _  _  _  _  _  _  _  _  _ 8
# IMAGEM                    2                                       2
# PESO _  _  _  _  _  _  _  _  _  _   1 _  _  _  _  _  _  _  _  _   1
# PREÇO                    11                                      11
# PRODUTO _  _  _  _  _  _ 90 _  _  _  _  _  _  1 _  _  _  _  _  _ 91
# RESISTÊNCIA               1                                       1
# TAMANHO _  _  _  _  _  _  1 _  _  _ 1 _  _  _  _  _  _  _  _  _   2
# TELA                      2                                       2
# USABILIDADE _  _  _  _  _ 9 _  _  _ 1 _  _  _ 1 _  _  _  _  _  _ 11
# _TOTAL__________________135________11_________2_________________148
# broken _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _   3 _  _  _ 3
# context                                                 2         2
# duplicate _  _  _  _  _  _  _  _  _  _  _  _  _  _  _   5 _  _  _ 5
# outscope                  2         1                             3
```