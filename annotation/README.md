# annotation

This directory contains the framework used in the process of annotation of the corpus. It consists of two folders: 
* **input** contains the annotated input set in two versions: the automatically annotated data and the manually revised data. 
* **preview** contains files that help annotators revise their work.

The file **generate.py** is a script that gets the files from the `input` directory and generates files for `preview` and the data set in `../dataset`. 


## Instructions

### Structure

The files edited by annotators must be in the directory `revised`. Initially, they are a copy of the automatically annotated files in `automatic`. For each text file in `revised`, there must be a file with the same name in `automatic` with the same reviews. The files in `automatic` must be kept unchanged, because they contain information that will be used to track text segmentation that may be manually made by annotators. 


### Annotation

Annotators should edit only the files in the `revised` directory. There is one file for each product. In those files: 
* Meta information are in lines that start with a `>` symbol followed by the meta information key, a `:` symbol and the meta information value. Annotators may change the meta information and add new keys and values if they want. For example: 
```
> My cat's name: Lalá
```
* Comments start with a `#` symbol in the beginning of the line. These lines are ignored. 
* Blank lines are ignored.
* Lines that are not one of the three types described above contain the main information of the data set, that is, the annotation. Initially, each line contains a sentence and the automatic annotation of it. 

To revise annotated sentences, annotators should change the information whenever they consider that the one automatically provided is not the more suitable for the case. Annotated sentences follow the order
```
(ID) [POLARITY][ASPECT] :: SENTENCE.
```
For example, 
```
(001.001) [+][PRODUTO] :: Bom custo/benefício.
```




### Generation of files


Run the file `generate.py` with Python 3.6. It'll generate files in `preview` to help check the annotation. If anything is wrong, go back to the manual annotation process to fix it. If everything is right, get the output files in `/dataset/whole`.

