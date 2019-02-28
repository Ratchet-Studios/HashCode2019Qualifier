#Challenge Problem 
####- Photos
compose a slideshow from a collection of photos
photo has tags
is vertical or horizontal
each slide has either
* one horizontal photo
* two vertical photos
tags of a slide = union of all the photos it contains
photos can be used once or zero times
slideshow must have at least one slide

##Input format
Line numbers of input file:
1. N - number of photos
2. N lines after this:
   * single char, H or V (horizontal or vertical)
   * integer M, number of tags
   * M number of Strings, the tags for the photo
       * lowercase ascii, 1-10 digits

##Output format
lines:
1. S - number of slides
2. S lines after this, containing either:
* single integer of the horizontal photo, or
* two integers separated by a space - IDs of hte two vertical photos

Slides must be used once or zero times

## Scoring
Based off of the difference between the tags of sequential slides
doesn't care about the similarity between photos on the same slide, only on inter-slide differences

###Interest factor:
min of:
* number of common tags between S0 and S1
* number of tags in S0 but not S1
* number of tags in S1 but not S0 