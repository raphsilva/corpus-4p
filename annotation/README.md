This directory contains the framework used in the process of annotation of the corpus. It consists of three folders: 
* `input` contains the annotated input set in two versions: raw data and the data manually revised. 
* `doublecheck` contains files that help annotators revise their work.
* `formatted` contains the corpus in its final format, with the information obtained in the annotation process displayed in ways that ease both human and machine readability. 

The file `format.py` is the script that gets the files from the `input` directory and generates files for the other two directories. Run it with Python 3.6.

##Syntax

### Aspects

Aspects are represented for an uppercase tag, for example, **SCREEN**. 

Special aspects were defined for exception cases. They are:
* **outscope**:  text segments that talk not about the target product, but about some entity related to it or to the user's purchase experience, such as manufacturer, vendor, shipping company, etc. – _Arrived fast._
* **context**:  segments that contain additional information that may add value to the review, but don't help to evaluate the product when isolated. – _It was a gift._
* **irrelevant**:  segments that are not related to the target product and do not add value to comments about the product. – _I don't know why I'm posting this review._
* **duplicate**:  segments that have been posted before by the same person (for example, when the reviewer repeats a sentence in the title and in the body.
* **broken**:  segments that are missing words. – _Screen_
* **unintelligible**:  segments that don't contain valid words. – _'xvcxcvc'_


### Polarity

Polarities were represented by symbols:
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
* `!` (**advice**): information that helps to better use the product – _I recommend you get a case._
* `&` (**experience**): narrates use experience in a way that doesn't imply an opinion – _I use it a lot to access the internet_