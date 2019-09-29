# Corpus of opinions in Portuguese about electronic products for contrastive summarization

This repository contains a corpus that was built to test methods of contrastive opinion summarization, which is a task that aims to compare two entities from  opinionated texts written about them. There was manual annotation of information about the opinions contained in each sentence, each opinion being indicated by its aspect and polarity: the aspect is the characteristic of the product that the opinion evaluates and the polarity indicates whether the opinion is positive or negative. The 642 sentences of the corpus were collected from 542 opinionated reviews published by buyers on Buscapé website and refer to four different products: two mobile phones and two digital cameras. The corpus was extended through the creation of fictitious entities that contain sentences of the selected real entities with different strategies to simulate other possibilities of sets of opinionated texts. Two pairs of real entities and six fictitious pairs were formed.


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
