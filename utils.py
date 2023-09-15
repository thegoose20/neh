#####################################################
# Functions for 'exploratory-analysis.ipynb' Notebook
#####################################################


# Import relevant programming libraries
import xml.etree.ElementTree as ET

# INPUT: the XML data tree's root and the name of an XML tag in the tree
# OUTPUT: list of strings of text contained within the input XML tag
def getTextBeneathTag(root, tagName):
    text_list = []
    for child in root.iter():
        tag = child.tag
        if tagName in tag:
            text_elem = ""
            for subchild_text in child.itertext():
                text_elem = text_elem + subchild_text
            text_list.append(text_elem)
    return text_list

# INPUT: NLTK frequency distribution
# OUTPUT: List of dictionaries with keys "word" and "count" recording a text string and its frequency
def makeFreqDistList(fdist):
    words = list(fdist.keys())
    values = list(fdist.values())
    i, maxI, frequencies = 0, len(words), []
    while i < maxI:
        d = dict()
        d["word"] = words[i]
        d["count"] = values[i]
        frequencies += [d]
        i += 1
    return frequencies