This directory contains the framework used in the process of annotation of the corpus. It consists of three folders: 
* `input` contains the annotated input set in two versions: raw data and the data manually revised. 
* `doublecheck` contains files that help annotators revise their work.
* `formatted` contains the corpus in its final format, with the information obtained in the annotation process displayed in ways that ease both human and machine readability. 

The file `format.py` is the script that gets the files from the `input` directory and generates files for the other two directories. Run it with Python 3.6.