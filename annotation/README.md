This directory contains the framework used in the process of annotation of the corpus. It consists of two folders: 
* `input` contains the annotated input set in two versions: raw data and the data manually revised. 
* `doublecheck` contains files that help annotators revise their work.

The file `generate.py` is a script that gets the files from the `input` directory and generates files for the other two directories. 


## Instructions

### Manual annotation

The files edited by annotators must be in the directory `revised`. Initially, they are a copy of the automatically annotated files in `automatic`. For each text file in `revised`, there must be a file with the same name in `automatic` with the same reviews. The files in `automatic` must be kept unchanged, because they contain information that will be used to track text segmentation that may be manually made by annotators. 

In the revised directory, 

### Generation of files


Run the file `generate.py` with Python 3.6. It'll generate files in `doublecheck` to help check the annotation. If anything is wrong, go back to the manual annotation process to fix it. If everything is right, get the output files in `/dataset/whole`.

