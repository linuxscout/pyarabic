---
title: >-
    PyArabic: A Python package for Arabic text
tags:
    Python
    Arabic Language
    Natural Language Processing
    Text Preprocessing
authors:
  - name: Taha Zerrouki
    email: t.zerrouki@univ-bouira.dz
    affiliation: "1"
    orcid: 0000-0001-9960-5533
    corresponding: true
affiliations:
  - name: Bouira University, Bouira, Algeria
    index: 1
date: 12 September 2022
bibliography: paper.bib
---
# Summary

Because text is the most common type of information representation, text processing and manipulation require recurring routines and functions.
Every day, massive amounts of text are processed.
Indeed, with the advent of artificial intelligence and new machine learning and deep learning enhancements, natural language processing has become a critical domain.

PyArabic is a collection of modules that provide basic functionality for manipulating Arabic texts, phrases, words, numbers, and letters.
It primarily provides preprocessing tools such as normalization, tokenization, diacritics removal, number conversion, transliteration, and so on.


For years, researchers and developers who worked on machine learning algorithms for natural language processing have used the library for Arabic text preprocessing and cleaning. The library becomes more important for machine learning.


# Statement of need

PyArabic is a Natural Language Processing Python package for Arabic text\footnote{The library can be found at [PyPi.org index](https://pypi.org/project/PyArabic/)}.
It is a simple library with basic functions for manipulating Arabic letters and text, such as detecting Arabic letters, Arabic letter groups and characteristics, removing diacritics, and so on.
It contains the most basic and useful routines used by developers and researchers working with Arabic texts. Some key features are as follows:

-   Text tokenization.
-   Remove diacriticts (Harakat) from words (all, except Shadda, Tatweel, last haraka).
-   Separate a word into letters and diacritics.
-   Reduce diactritics of words.
-   Measure tashkeel similarity (Harakats, fully or partially vocalized   similarity with a template).
-  Letter normalization (ligatures and Hamza).
-   Numbers to words.
-   Extract numerical phrases and prevocalize it.
-   Unshaping texts to handle letter glyphs.
-   Convert encoding and transliteration.




The PyArabic package includes five major submodules:

- Araby: Basic tools and routines for manipulating Arabic text and letters, such as tokenization and diacritics removal, are provided.
- Number: Contains routines for dealing with numbers and numeric words; allows conversion of numbers to words and words to numbers; detects numeric phrases, and more.
- Named: Provides simple tools for extracting named entities from text.
- Trans: Provides functions for converting between Arabic transliterations such as SAMPA, TIM Bukwalter, and Unicode.
- Normalize: Utility functions that are used to prepare an Arabic text for searching and indexing.



- More advanced projects use PyArabic, such as Adawat, which is an open framework for processing Arabic that the author developed as part of his PhD research. In our PhD work, we release a set of tools, the most important of which are:

  - Tashaphyne, Arabic Light Stemming Library [@tashaphyne]. We primarily use tokenization, diacritics removal, and letter constants from PyArabic in this basic library.
  - Qalsadi is an Arabic morphology analyzer [@qalsadi], which is based on Tashaphyne Stemmer, It uses Pyarabic, especially for tokenization and letters and diacritics handling, which includes removing tashkeel, handling Shadda, removing the last diacritic for inflection cases, and comparing two words with full or partial diacritization.
  - Qutrub [@qutrub] is an Arabic verb conjugator, and this conjugation library requires basic features such as the separation of diacritics from letters and rejoining them to form words during conjugation. normalizing letters and words to prepare them for conjugation.
  - Mishkal, is a system for Arabic text diacritization [@mishkal]. It is built on cited libraries like the Qalsadi morphology analyzer, the Tashaphyne stemmer, the Qutrub conjugator, and others. For basic routines, it uses PyArabic for letter constant names, diacritics management, word normalization, tokenization, and numeric phrase detection.

  

  The Classical Language Toolkit (CLTK)\footnote{\url{http://cltk.org}} [@johnson2014:2014] provides natural language processing support for Ancient, Classical, and Medieval Eurasia languages. CLTK integrates PyArabic functionalities for corpus importer, tokenization, text converting, and transliteration for classical Arabic [@johnson2014:2014], which is the form of the Arabic language used in texts from the 7th century AD to the 9th century AD (like the orthography of the Quran).



PyArabic was created to aid researchers and developers in natural language processing tasks, particularly text preprocessing (tokenization, cleaning, normalization, strip diacritics). It has already appeared in several scientific publications. It is mentioned in:

- Text alignment [@mikhael2014greek:2014].
- Text classification [@abufayad2018semantic:2018; @abozinadah2016improved:2016; @ajlouni2021experience:2021; @habash2021team:2021; @mgheed2021scalable:2021;@AlBatayha:2021].
- Sentiment analysis [@al2016sentiment:2016;  @alotaibi2019sentiment:2019;@laachfoubi2019comparative:2019; @kaibi2019comparative:2019; @kaibi2020sentiment:2020; @alharbi2020asad:2020; @al2020exploration:2020; @oussous2020asa:2020; @mihi2020mstd:2020; @almutairi2021cyberbullying:2021; @mihi2022dialectal:2022; @khabour2022new:2022].
- Language model [@hamed2017building:2017; @alzu2021detecting:2021].
- Text preprocessing (remove diacritics,  tokenization, etc.): [@tarmom2019non:2019; @yusuf2019arabic:2019; @Nguyen:2019; @AlSarem:2020;@elouali2020hate:2020@zhang2021rise:2021;@duwairi2021deep:2021; @jimin:2021;@Moaz:2022;@alrumayyan2022neural:2022; @al2022flusa:2022; @solyman2022automatic:2022; @marie2022samee:2022; @alasmari2022hybrid:2022]
- Lexical resources [@choe2019word2word:2019]
- Text similarity [@mouty2019effect:2019]


PyArabic was inspired by Ar-PHP[@ar-php], an Arabic library for the PHP programming language that provides basic routines for web developers. Then the two libraries grow together through collaborations, and they are inspired mutually by each other. Ar-PHP provides basic routines for PHP and MySQL databases and attempts to solve web development issues such as arabic glyph rendering; however, the Ar-PHP library also includes advanced modules such as sentiment analysis, muslim prayer times, and auto-summarize [@ar-php].

There are many dedicated frameworks for Arabic natural language processing, like MADAMIRA(Java) [@pasha2014madamira], FARASA(Java)[@abdelali2016farasa], CAMeL(Python) [@obeid-etal-2020-camel]. Many multilingual frameworks, however, such as NLTK (Python) [@loper2002nltk], Spacy (Python) [@vasiliev2020natural], and CLTK (Python) [@johnson2014:2014], only partially support Arabic.

In PyArabic, we focused on basic routines and build our library to be native and independent enough to be embedded in complex projects. This library was used in many projects and adopted by frameworks like CLTK[@johnson2014:2014], and has been inspired to build more specific libraries like TaKseem (a tokenization library for Arabic) [@tkseem2020] and Tankeeh (Arabic cleaning, normalization, and segmentation library) [@tnkeeh2020].

# Acknowledgements

We gratefully acknowledge the contributions of Assem Chelli, Khaled Alshamaa, Lakhdar Benzahia, Mouhamad AboShokor, David Lowe, Ahmed Alq, and Arabeyes.org during the project's inception.



# References

