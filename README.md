# Corpus of opinions in Portuguese about electronic products for contrastive summarization

This repository contains a corpus that was built to test methods of contrastive opinion summarization, which is a task that aims to compare two entities from  opinionated texts written about them. There was manual annotation of information about the opinions contained in each sentence, each opinion being indicated by its aspect and polarity: the aspect is the characteristic of the product that the opinion evaluates and the polarity indicates whether the opinion is positive or negative. The 642 sentences of the corpus were collected from 542 opinionated reviews published by buyers on Buscapé website and refer to four different products: two mobile phones and two digital cameras. The corpus was extended through the creation of fictitious entities that contain sentences of the selected real entities with different strategies to simulate other possibilities of sets of opinionated texts. Two pairs of real entities and six fictitious pairs were formed.


## Contents

This repository contains two directories that are different versions of the same corpus: the `dataset` directory contains a clean, extended version for general use, and the` annotation` directory contains the files and scripts used for annotation and all information extracted from the site, including information that are not necessarily useful for the task of contrastive summarization.

### Dataset 

The clean and extended version of the dataset contains 16 files in JSON format. Each file contains opinions about an entity. The entities D1a, D1b, D2a and D2b are real and the others are fictitious, formed from subsets of the sentences of real entities. The format of the files is as in the example below. The opinions found in sentences are represented by a word that identifies the aspect and a number that identifies the polarity: 100 for positive, -100 for negative, and 0 for neutral. Irrelevant opinions are not present in these sets.

```
{
    "data": [
        {
            "id": 3,
            "opinions": [
                ["PRODUTO", 100],
                ["CÂMERA", 100]
            ],
            "sentence": "Ótimo celular. Câmera excelente."
        },
        {
            "id": 18,
            "opinions": [
                ["PRODUTO", -100],
                ["DESIGN", -100],
                ["OUTRO", -100]
            ],
            "sentence": "Produto deixa a desejar, bordas metalicas riscam com facilidade, botão home então nem se fala."
        },
    ],
    "meta": {
        "Crawl date": "17/may/2018 ",
        "ID": "11",
        "Product": "Smartphone Samsung Galaxy S7 SM-G930 32GB",
        "Source": "www.buscape.com.br/smartphone-samsung-galaxy-j5-prime-sm-g570m",
        "Total of opinions": "755",
        "Total of reviews": "221",
        "Total of sentences": "641",
        "Type": "Celular"
    }
}
```


### Annotation

The annotation directory contains all data extracted from the source and the information entered by the annotators. It contains files for the four products whose comments have been collected.

In addition to the datasets, the directory contains the script that was used to transform annotated data into its final format.
