# annotation

This directory contains the framework used in the process of annotation of the corpus. It consists of two folders: 
* **input** contains the annotated input set in two versions: the automatically annotated data and the manually revised data. 
* **preview** contains files that help annotators revise their work.

The file **generate.py** is a script that gets the files from the `input` directory and generates files for `preview` and for `../dataset`. 


## Instructions

### Structure

The files edited by annotators must be in the directory `revised`. Initially, they are a copy of the automatically annotated files in `automatic`. For each text file in `revised`, there must be a file with the same name in `automatic` with the same reviews. The files in `automatic` must be kept unchanged, because they contain information that will be used to track text segmentation that may be manually made by annotators. 

 To annotate new data, place the new files in `input/automatic` following the format of the files that are already there. A tool that can help with the automatic annotation of opinions is available at www.github.com/raphsilva/naive-opinion-miner.  


### File format

Annotators should edit only the files in the `revised` directory. There is one file for each product. In those files: 
* Meta information are in lines that start with a `>` symbol followed by the meta information key, a `:` symbol and the meta information value. Annotators may change the meta information and add new keys and values if they want. For example: 
```
> My cat's name: Lalá
```
* Comments start with a `#` symbol in the beginning of the line. These lines are ignored. 
* Blank lines are ignored.
* Lines that are not one of the three types described above contain the main information of the data set, that is, the annotation. Initially, each line contains a sentence and the automatic annotation of it. 

### Opinions identification

To revise annotated sentences, annotators should change the information whenever they consider that the one automatically provided is not the more suitable for the case. Annotated sentences follow the order
```
(ID) [POLARITY][ASPECT] :: SENTENCE.
```
For example, 
```
(001.001) [+][PRODUTO] :: Bom custo/benefício.
```

#### Aspects

Any aspect tag can be used by annotators. Annotators should be provided with a list of aspect tags that they may use for the task. 

In this project, the following aspect tags (written in Portuguese) were used: 

* For entities of type **camera**: 
   * `ACESSÓRIO`: Extra items that come with the product or that can be purchased separately.
   * `ARMAZENAMENTO`: File storage system.
   * `ÁUDIO`: Audio recorded by the device.
   * `BATERIA`: Power system.
   * `DESIGN`: Features related to appearance.
   * `FOCO`: Focus control system.
   * `FOTO`: Photographs taken with the camera.
   * `FUNCIONALIDADE`: Product features and options that contribute with usability.
   * `IMAGEM`: General features of images taken by the camera, whether photos or videos: 
   * `PESO`: Equipment weight.
   * `PREÇO`: Reviews on price paid and value for money.
   * `PRODUTO`: Generic product reviews.
   * `RESISTÊNCIA`: Product's ability to withstand adverse situations and weather.
   * `TAMANHO`: Equipment size.
   * `TELA`: Screen.
   * `USABILIDADE`: Ease of use.
   * `VÍDEO`: Videos taken with the camera.
   * `ZOOM`: Zooming features.
* For entities of type **phone**:
    * `ACESSÓRIO`: Extra items that come with the product or that can be purchased separately.
    * `ARMAZENAMENTO`: File storage system.
    * `BATERIA`: Power system.
    * `CÂMERA`: Image capture.
    * `DESEMPENHO`: Processing performance.
    * `DESIGN`: Features related to appearance.
    * `OUTRO`: Specific themes not included in other categories.
    * `PESO`: Equipment weight.
    * `PREÇO`: Reviews on price paid and value for money.
    * `PRODUTO`: Generic product reviews.
    * `RESISTÊNCIA`: Product's ability to withstand adverse situations and weather.
    * `SISTEMA`: Features of the software.
    * `SOM`: Sound played by the player.
    * `TAMANHO`: Equipment size.
    * `TELA`: Part of the equipment that displays the visual interface.
    * `USABILIDADE`: Ease of use.

There is also the special aspect `outscope` that identifies opinions that are not about the entity. These opinions are usually tagged as `EMPRESA` by the automatic annotation system.

#### Polarities 

It's suggested that annotators use the following tags for polarities:
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

### Undesired excerpts

Some sentences may not be suitable for opinion identification. This may be indicated by annotators by placing a character at the beginning of the line. The character is the first letter of the following categories: 

* **context**:  Segments that contain additional information that may add value to the review, but don't help to evaluate the product when isolated. – _It was a gift._
* **irrelevant**:  Segments that are not related to the target product and do not add value to comments about the product. – _I don't know why I'm posting this review._
* **broken**:  Segments that are missing words. – _Screen_
* **unintelligible**:  Segments that don't contain valid words. – _xvcxcvc_
* **duplicate**:  Segments that have been posted before by the same person (for example, when the reviewer repeats a sentence in the title and in the body).


Aspects and polarities of undesired excerpts do not matter. They can be left with the automatic tags, but it's recommended to leave them blank for better readability.

For example:

``` 
c(199.608) [][] :: Realizei a troca do galaxy s5 para o galaxy s7.

i(218.670) [][] :: Nao comprei.

b(208.639) [][] :: Não há explicações para a fragilidade de um produto qu.

u(211.528) [][] :: Xxx xxxx xxx x xx.

(068.198) [+][PRODUTO] :: Otimo.
d(068.199) [][] :: Otimo.
```

### Segmentation

Annotators should keep only one opinion (polarity and aspect) per line. If a sentence contains opinions about more than one aspect, it should be divided while keeping its ID. For example, if the input sentence is written like 

```
[184.464]  [PRODUTO EMPRESA][+]  ::  Ótimo produto entrega rápida só fica a desejar por ele travar e ser meio lento em alguns aplicativos no mais é um ótimo aparelho.
```
annotators may rewrite it like
```
[184.464][PRODUTO][+]  ::  Ótimo produto.
[184.464][outscope][+] ::   entrega rápida.
[184.464][DESEMPENHO][-] ::  só fica a desejar por ele travar e ser meio lento em alguns aplicativos no mais é um ótimo aparelho.
```

Annotators may also join consecutive sentences when two or more sentences are very dependent of each other. To do so, they must copy all sentences to be joined in the line containing the first sentence to be joined, and then add a `J` tag in the beginning of the line of the joined sentences except the first one. For example, if the input file is like 

``` 
(209.640) [-][PRODUTO] :: Boas funções mas pouco resistente.

(209.641) [-][PRODUTO] :: O Celular é alérgico a agua, já vi celulares sem proteção resistir melhor.

(209.642) [-][PRODUTO] :: Das duas vezes que o meu entrou em contato com a agua ele foi parar na assistência, sendo que da segunda vez deu PT.
```
annotators can join the sentence 209.642 with the 209.641 by doing
```
(209.640) [-.][PRODUTO] :: Boas funções mas pouco resistente.

(209.641) [-][RESISTÊNCIA] :: O Celular é alérgico a agua, já vi celulares sem proteção resistir melhor. Das duas vezes que o meu entrou em contato com a agua ele foi parar na assistência, sendo que da segunda vez deu PT.

J(209.642) [-][PRODUTO] :: Das duas vezes que o meu entrou em contato com a agua ele foi parar na assistência, sendo que da segunda vez deu PT. 
```




### Generation of files


Run the file `generate.py` with Python 3.6. It'll generate files in `preview` to help check the annotation. If anything is wrong, go back to the manual annotation process to fix it. If everything is right, get the output files in `/dataset/whole`.

