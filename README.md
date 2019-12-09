# 4P Corpus: opinions in Portuguese about electronic products

This repository contains a data set that was built to test methods of **contrastive opinion summarization**, which is a task that aims to compare two entities from  opinionated texts written about them. There was **manual annotation** of information about the opinions contained in each sentence, each opinion being indicated by its aspect and polarity: the **aspect** is the characteristic of the product that the opinion evaluates and the **polarity** indicates whether the opinion is positive or negative. 

The **642 sentences** of the corpus were collected from **542 opinionated** reviews published by buyers on Buscapé website and refer to **four products**: two mobile phones and two digital cameras. 

The corpus was **extended** through the creation of new arrangements that contain sentences selected with different strategies to simulate other possibilities of sets of opinionated texts. **Eight pairs of arrangements** were formed.


## Contents

The contents of this repository are organized in the following directories:

* **dataset**:  Contains different versions of the data set.
    * **skim**: A clean and extended version of the data set, in JSON format.
    * **whole**: Data set containing all information from the annotation: 
        * **sentences**: The original text is segmented in sentences. 
        * **opinion**: The text is segmented in a way that each segment contains only one opinion.
        * **json**: Contains all information from the two other directories in JSON format.

* **annotation**: Cointains tools and files used in the process of annotation.
    * **input**: Contains the annotated input set in two versions: the automatically annotated data and the manually revised data. 
    * **preview**: Contains files that help annotators revise their work.
    * **generate.py**: Script that gets the files from the `input` directory and generates files for double check (at `annotation/preview`) and writes the data set in its final format (at `dataset`). 


More information about those directories is in the readme files inside each directory.


## The dataset

For each sentence of the collected reviews, opinions were identified. Each opinion is represented by an aspect (feature being evaluated) and a polarity (which characterizes the opinion about the feature). Each sentence may contain more than one opinion. Below are the rules used for aspects and polarities identification.


### Aspects identification

Aspects are represented by an uppercase tag that names the feature being evaluated, for example, **SCREEN**. A set of aspects was defined, 16 for phones and 18 for cameras (some of which where not found in the reviews).

Special aspects were defined for exception cases. They are:
* **outscope**:  Text segments that talk not about the target product, but about some entity related to it or to the user's purchase experience, such as manufacturer, vendor, shipping company, etc. – _Arrived fast._
* **context**:  Segments that contain additional information that may add value to the review, but don't help to evaluate the product when isolated. – _It was a gift._
* **irrelevant**:  Segments that are not related to the target product and do not add value to comments about the product. – _I don't know why I'm posting this review._
* **broken**:  Segments that are missing words. – _Screen_
* **unintelligible**:  Segments that don't contain valid words. – _xvcxcvc_
* **duplicate**:  Segments that have been posted before by the same person (for example, when the reviewer repeats a sentence in the title and in the body).


### Polarities identification

Polarities are represented by symbols:
* ` +` (**positive**): something good, desirable – '_Very fast phone_'
* `.+` (**weak positive**): something conditionally good or partially good – _It's expensive, but it's worth it._
* `++` (**strong positive**): something exceptionally good – _Perfect, without any flaw_. 
* ` -` (**negative**): something bad, undesirable – _The price is too high._
* `.-` (**weak negative**): something conditionally bad or partially bad – `I believe it's not worth it for more picky users._ 
* `--` (**strong negative**): something exceptionally bad – _It was the worst phone I've ever bought._
* `.` (**moderate**): something in the middle of the scale between positive and negative – _Fair device._ 
* `*` (**relative**): subjective segment where there isn't a clear value of positive or negative – _Discreet design._
* `..` (**dual**): segment that indicates something simultaneously good and bad about the same aspect – _It accepts SD but it doesn't allow to expand the internal memory._
* `#` (**irresolute**): indicates hesitation or lack of opinion – _I'm still evaluating._
* `!` (**advice**): information that helps to better use the product – _I recommend you get a protective case._
* `&` (**experience**): narrates use experience in a way that doesn't imply an opinion – _I use it a lot to access the internet._

### Quantitative view

The table below shows arrangements formed for the extended data set and the quantities of sentences, different aspects, positive opinions and negative opinions of each arrangement. Each pair is made of two arrangements of names DXa and DXb, where X is a number between 1 and 8.

```
| arr. | entity                   |  aspects | sentences | positive  | negative  |
|------|--------------------------|----------|-----------|-----------|-----------|
|  D1a | Motorola Moto G5 Plus    |       15 |       269 |       346 |       101 |
|  D1b | Galaxy S7                |       14 |       253 |       342 |        91 |
|  D2a | Canon EOS Rebel T5       |       13 |        68 |        77 |        11 |
|  D2b | Canon PowerShot SX520 HS |       15 |        52 |        68 |         8 |
|  D3a | (subset of D1a)          |       11 |       150 |       143 |        65 |
|  D3b | (subset of D1b)          |       10 |       109 |        85 |        65 |
|  D4a | (subset of D1a)          |       13 |        43 |        56 |        13 |
|  D4b | (copy of D1b)            |       14 |       253 |       342 |        91 |
|  D5a | (subset of D2a)          |       12 |        39 |        40 |        10 |
|  D5b | (subset of D2b)          |       10 |        30 |        37 |         3 |
|  D6a | (subset of D2a)          |        8 |        29 |        37 |         1 |
|  D6b | (subset of D2b)          |       11 |        22 |        31 |         5 |
|  D7a | (subset of D2a)          |        4 |        31 |        33 |         6 |
|  D7b | (subset of D2b)          |        4 |        25 |        22 |         4 |
|  D8a | (subset of D1a)          |       12 |        39 |        62 |        10 |
|  D8b | (subset of D1b)          |       12 |        32 |        36 |        15 |
```

## The project

### Authorship

This project was made by researchers of the **NILC laboratory** at the **University of São Paulo**, São Carlos: 
* **Raphael Rocha da Silva** (http://raphsilva.github.io)
* **Otávio Augusto Ferreira Sousa**
* **Thiago Alexandre Salgueiro Pardo** (http://conteudo.icmc.usp.br/pessoas/taspardo)

This work is part of the **Opinando project**: **http://sites.google.com/icmc.usp.br/opinando/**

### Publication

The creation of this dataset is described in the following paper (in Portuguese): 
* SILVA, R. R.; PARDO, T. A. S., 2019. **Corpus 4P: um córpus anotado de opiniões em português sobre produtos eletrônicos para fins de sumarização contrastiva de opinião**. In the _Proceedings of the 6a Jornada de Descrição do Português (JDP)_ . October, 15-18. Salvador/Bahia, Brazil. To appear. Preview available at http://drive.google.com/file/d/1Nqu66l-z7eQenXEsvcnAEClt1LQzioJw/view.

### Repository

The repository is publicly available at **http://github.com/raphsilva/corpus-4p** as of October, 2019. 

#### Versioning
Stable releases are listed at https://github.com/raphsilva/corpus-4p/releases.
Versions have the format X.Y.Z, where: 
* X changes when there are significant changes in the data set contents; 
* Y changes when there are small changes in the data set contents; 
* Z changes when there are changes in the documentation, changes in meta information or refactoring. 


### License

This repository is licensed under GNU GENERAL PUBLIC LICENSE  (Version 3, 29 June 2007) as of October 2019. Find the legal text in the file `LICENSE.md`.

In summary, you are free to use its contents for:
* **Commercial use**
* **Modification**
* **Distribution**
* **Patent use**
* **Private use**
 
 as long as you keep your work private or publish your work with:

* **License and copyright notice**
* **State changes**
* **Disclose source**
* **Same license**
* **Attribution**

In derivative work that uses the contents provided, we ask you to either mention the authors,  cite their publication or add a link to the public repository, whichever best fits the format of your work. 

The contents are provided **without liability or warranty**. 

The use of reviews are in accordance with Buscapé's terms of service, available at www.buscape.com.br/termos-de-uso.



### Acknowledgments

The authors are grateful to **São Paulo Research Foundation** (process 17/12236-0) and **University of São Paulo Research Office** (PRP N. 668) for the financial support.

