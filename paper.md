---
title:
    PyArabic: A Python package for Arabic text
tags:
    Python
    Arabic Language
    Natural Language Processing
    Text Preprocessing
authors:
  - name: Taha Zerrouki
    email: t.zerrouki@univ-bouira.dz
    affiliation: [1]
    orcid: 0000-0001-9960-5533
    corresponding: true
affiliations:
    index: 1
    name: Bouira University , Algeria
date: 12 September 2022
bibliography: paper.bib
---
# Summary

Because text is the most common type of information representation, text processing and manipulation require recurring routines and functions.
Every day, massive amounts of text are processed.
Indeed, with the advent of artificial intelligence and new machine learning and deep learning enhancements, natural language processing has become a critical domain.

PyArabic is a collection of modules that provide basic functionality for manipulating Arabic texts, phrases, words, numbers, and letters.
It primarily provides preprocessing tools such as normalization, tokenization, diacritics removal, number conversion, transliteration, and so on.


For years, researchers and developers have used the library to process and preprocess texts in their projects.
Before using machine learning algorithms, the library becomes even more important for text processing. 


# Statement of need

PyArabic is a Natural Language Processing Python package for Arabic text.
It is a simple library with basic functions for manipulating Arabic letters and text, such as detecting Arabic letters, Arabic letter groups and characteristics, removing diacritics, and so on.
It contains the most basic and useful routines used by developers and researchers working with Arabic texts. Some key features are as follows:

-   Text tokenization into tokens.
-   Remove diacriticts (Harakat) from words (all, except Shadda, Tatweel, last haraka).
-   Separate a word into letters and diacritics.
-   Reduce diactritics of words.
-   Measure tashkeel similarity (Harakats, fully or partially vocalized   similarity with a template).
-  Letter normalization (ligatures and Hamza).
-   Numbers to words.
-   Extract numerical phrases and prevocalize it.
-   Unshaping texts to handle letter glyphs.
-   Convert encoding and transliteration.


The library can be found at [PyPi.org index](https://pypi.org/project/PyArabic/) \footnote{\url{https://pypi.org/project/PyArabic/}}.

The PyArabic package includes five major submodules:

- Araby: Basic tools and routines for manipulating Arabic text and letters, such as tokenization and diacritics removal, are provided.
- Number: contains routines for dealing with numbers and numeric words; allows conversion of numbers to words and words to numbers; detects numeric phrases, and more.
- Named provides simple tools for extracting named entities from text.
- Trans: provides functions for converting between Arabic transliterations such as SAMPA, TIM Bukwalter, and Unicode.
- Normalize: Utility functions that are used to prepare an arabic text for searching and indexing.

More advanced projects use PyArabic, such as:

- Adawat is an open framework for processing Arabic language that the author developed as part of his PhD research. In this work, we release a set of tools, the most important of which are:

- Mishkal, for restoring Arabic text diacritics [@mishkal].
- Qalsadi is an Arabic morphology analyzer [@qalsadi].
- Tashaphyne, Arabic light stemming [@tashaphyne].
- Qutrub is an Arabic verb conjugator [@qutrub].

- The Classical Language Toolkit (CLTK)\footnote{\url{http://cltk.org}} [@johnson2014:2014] provides natural language processing support for Ancient, Classical, and Medieval Eurasia languages. CLTK integrates PyArabic functionalities for corpus importer, tokenization, text converting, and transliteration for classical Arabic [@johnson2014:2014], which is the form of the Arabic language used in texts from the 7th century AD to the 9th century AD (like the orthography of the Quran).



PyArabic was created to aid researchers and developers in natural language processing tasks, particularly text preprocessing. It has already appeared in several scientific publications. It is mentioned in:

- Text alignment [@mikhael2014greek:2014].
- Text Classification [@abufayad2018semantic:2018; @abozinadah2016improved:2016; @ajlouni2021experience:2021; @habash2021team:2021; @mgheed2021scalable:2021;@AlBatayha:2021].
- Sentiment Analysis [@al2016sentiment:2016;  @alotaibi2019sentiment:2019;@laachfoubi2019comparative:2019; @kaibi2019comparative:2019; @kaibi2020sentiment:2020; @alharbi2020asad:2020; @al2020exploration:2020; @oussous2020asa:2020; @mihi2020mstd:2020; @almutairi2021cyberbullying:2021; @mihi2022dialectal:2022; @khabour2022new:2022].
- Language model [@hamed2017building:2017; @alzu2021detecting:2021].
- Text Preprocessing (remove diacritics,  tokenization, etc.): [@tarmom2019non:2019; @yusuf2019arabic:2019; @Nguyen:2019; @AlSarem:2020;@elouali2020hate:2020@zhang2021rise:2021;@duwairi2021deep:2021; @jimin:2021;@Moaz:2022;@alrumayyan2022neural:2022; @al2022flusa:2022; @solyman2022automatic:2022; @marie2022samee:2022; @alasmari2022hybrid:2022]
- Lexical resources [@choe2019word2word:2019]
- Text Similarity [@mouty2019effect:2019]

# Acknowledgements

We gratefully acknowledge the contributions of Assem Chelli, Khaled Alshamaa, Lakhdar Benzahia, Mouhamad AboShokor, David Lowe, Ahmed Alq, and Arabeyes.org during the project's inception.



# References

