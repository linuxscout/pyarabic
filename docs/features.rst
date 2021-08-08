الوظائف- الدوال
^^^^^^^^^^^^^^^

أهم الوظائف
'''''''''''

+-----------------------------------+----------------------------+
| وصف الدالة                        | الدالة                     |
+===================================+============================+
| حذف الحركات كلها بما فيها الشدة   | strip\_tashkeel(text)      |
+-----------------------------------+----------------------------+
| حذف الحركات كلها ماعدا الشدة      | strip\_harakat(text)       |
+-----------------------------------+----------------------------+
| حذف الحركة الأخيرة                | strip\_lastharaka(text)    |
+-----------------------------------+----------------------------+
| حذف التطويل                       | strip\_tatweel(text)       |
+-----------------------------------+----------------------------+
| تنميط أشكال الهمزة المختلفة       | normalize\_hamza(text)     |
+-----------------------------------+----------------------------+
| تفريق كلمات النص                  | tokenize(text)             |
+-----------------------------------+----------------------------+
| تفريق جمل النص                    | sentence\_tokenize(text)   |
+-----------------------------------+----------------------------+
| تفريق النص إلى كلمات ومواضعها       | tokenize_with_location   |
+-----------------------------------+----------------------------+

-  حذف الحركات

-  حذف كل الحركات عدا الشدة

Strip Harakat from arabic word except Shadda. The striped marks are :
Example:

.. code:: python

    >>> from pyarabic.araby import strip_harakat
    >>> text = u"الْعَرَبِيّةُ"
    >>> strip_harakat(text)
    >>> العربيّة

-  حذف الحركات بما فيها الشدة

Strip vowels from a text, include Shadda.

.. code:: python

    >>> from pyarabic.araby import strip_tashkeel
    >>> text = u"الْعَرَبِيّةُ"
    >>> strip_tashkeel(text)
    العربية

-  حذف الحركة الأخيرة فقط: قد تكون هي الحركة الإعرابية، لكن ليس في كل
   الحالات، مثلا يضربه، حركة الإعراب على الباء وليس على الهاء

Strip the last Haraka from arabic word except Shadda.

.. code:: python

    >>> from pyarabic.araby import strip_lastharaka
    >>> text = u"الْعَرَبِيّةُ"
    >>> strip_lastharaka(text)
    الْعَرَبِيّة

-  حذف الزخرفات المختلفة على النص منها الحركات والحروف الصغيرة

Strip diacritics from a text, include harakats and small lettres The
striped marks are :

.. code:: python

    >>> from pyarabic.araby import strip_diacritics
    >>> text = u"الرّحمٰن"
    >>> strip_diacritics(text)
    الرحمن

-  اختزال التشكيل Reduce the Tashkeel, by deleting evident cases.

.. code:: python

    >>> from pyarabic import araby
    >>> word = u"يُتَسََلَّمْنَ"
    >>> reduced = araby.reduce_tashkeel(word)
    >>> print(reduced.encode('utf8'))
    يُتسلّمن

-  حذف التطويل أو الشدة

Strip tatweel or Shadda from a text.

.. code:: python

    >>> from pyarabic.araby import strip_tatweel, strip_shadda
    >>> text = u"العـــــربية"
    >>> strip_tatweel(text)
    العربية
    >>> text = u"الشّمسيّة"
    >>> strip_shadda(text)
     الشمسية

-  تنميط الحروف المركبة والهمزة

بعض البرامج تعطي حروف متراكبة، توحيدها يرجعها إلى حروف بسيطة

Normalize Lam Alef ligatures into two letters (LAM and ALEF) LAM\_ALEF,
LAM\_ALEF\_HAMZA\_ABOVE, LAM\_ALEF\_HAMZA\_BELOW,
LAM\_ALEF\_MADDA\_ABOVE

.. code:: python

    >>> from pyarabic.araby import normalize_ligature
    >>> text = u"لانها لالء الاسلام"
    >>> normalize_ligature(text)
    لانها لالئ الاسلام

-  توحيد الهمزة

توحيد الهمزة إلى همزة إلى السطر، مثل (الءسءلة) أو تسهيلها بتحويلها إلى
الحرف الذي تكتب عليه، مثل، الاسيلة)

Standardize the Hamzat into one form of hamza, replace Madda by hamza
and alef.

if Method is "tasheel" تسهيل, the Hamza is converted to the near
letters, for example, Hamza on Alef is converted to Alef, where Hamza on
Yeh is converted to Yeh.

.. code:: python

    >>> import pyarabic.araby as araby
    >>> text1 = u"جاء سؤال الأئمة عن الإسلام آجلا"
    >>> araby.normalize_hamza(text1)
    'جاء سءال الءءمة عن الءسلام ءءجلا'
    >>> araby.normalize_hamza(text1, method="tasheel")
    'جاء سوال الايمة عن الاسلام ا

-  فصل الحركات والحروف

يمكن استخلاص الحروف والحركات في سلسلتين متوازيتين، بحيث يقابل كل حرف
حركة محددة، إذا غابت الحركة رمزنا لها بتطويل

separate the letters from the vowels, in arabic word, if a letter hasn't
a haraka, the not definited haraka is attributed. return ( letters,
vowels)

.. code:: python

    >>> from pyarabic import araby
    >>> araby.separate(text)
    (u'\u0627\u0644\u0639\u0631\u0628\u064a\u0629', u'\u064e\u0652\u064e\u064e\u064e\u064e\u064f')
    >>> letters, marks =araby.separate(text)
    >>> print(letters.encode('utf8'))
    العربية
    >>> print(marks.encode('utf8'))
    >>> for m in marks:
    ...     print(araby.name(m))
    فتحة
    سكون
    فتحة
    فتحة
    فتحة
    فتحة
    ضمة

يمكن دمج الحركات والحروف في كلمة واحدة، شرط أن يكون طول السلسلتين
متساويا. ينوب عن غياب الحركة حرف التطويل

joint the letters with the marks the length ot letters and marks must be
equal return word

.. code:: python

    >>> from pyarabic import araby
    >>> letters = u"العربية"
    >>> marks   = u'\u064e\u0652\u064e\u064e\u064e\u064e\u064f'
    >>> word = araby.joint(letters, marks)
    >>> print(word.encode('utf8'))
    اَلْعَرَبَيَةُ

-  تهجئة الحركات و الحروف

يمكن تهجئة الحروف لاستخراج الحروف (كما تنطق) مفصولة ب"فاصلة". يمكن
استخراج اليونيكود أو النطق العربي للحرف، حسب اختيار المستخدم. يسرد النطق
العربي المستخدم في المتغير
`NAMES <https://github.com/linuxscout/pyarabic/blob/50c3a3bf0479fb2d9a8189a066044ab074a974b4/pyarabic/araby.py#L205>`__
, و يُستخرج الاسم اليونيكود باستخدام
`unicodedata <https://docs.python.org/3.8/library/unicodedata.html#unicodedata.name>`__.

.. code:: python

    >>> from pyarabic import araby

    >>> words_list = araby.spellit('لَاحظ أن المسافة تطبع كمسافة و ليس كلمة "مسافة"، كما تطبع علامات الترقيم.. كما هي!')
    >>> print(words_list)
    >>> print("-------------------------------")

    >>> words_list_unicode = araby.spellit('لَاحظ أن المسافة تطبع كمسافة و ليس كلمة "مسافة"، كما تطبع علامات الترقيم.. كما هي!', lang="unicode")
    >>> print(words_list_unicode[:154])  # printed some only. For display purposes.

    لام, فتحة, ألف, حاء, ظاء,  , همزة على الألف, نون,  , ألف, لام, ميم, سين, ألف, فاء, تاء مربوطة,  , تاء, طاء, باء, عين,  , كاف, ميم, سين, ألف, فاء, تاء مربوطة,  , واو,  , لام, ياء, سين,  , كاف, لام, ميم, تاء مربوطة,  , ", ميم, سين, ألف, فاء, تاء مربوطة, ", ،,  , كاف, ميم, ألف,  , تاء, طاء, باء, عين,  , عين, لام, ألف, ميم, ألف, تاء,  , ألف, لام, تاء, راء, قاف, ياء, ميم, ., .,  , كاف, ميم, ألف,  , هاء, ياء, !
    -------------------------------
    ARABIC LETTER LAM, ARABIC FATHA, ARABIC LETTER ALEF, ARABIC LETTER HAH, ARABIC LETTER ZAH, SPACE, ARABIC LETTER ALEF WITH HAMZA ABOVE, ARABIC LETTER NOON,

-  حساب التماثل

التماثل في الحركات بين كلمتين يون صحيحا إذا كان للكلمتين نفس الحروف،
ونفس الحركات، ولو كانت الحركات ناقصة

if the two words has the same letters and the same harakats, this
fuction return True. The two words can be full vocalized, or partial
vocalized

.. code:: python

    >>> from pyarabic import araby
    >>> word1 = u"ضَربٌ"
    >>> word2 = u"ضَرْبٌ"
    >>> araby.vocalizedlike(word1, word2)
    True

-  تماثل الوزن تتماثل كلمة مع وزن إذا كانت الحروف تتطابق مع الوزن
   والحركات مع الحركات، يمكن أن يكون التشكيل غير كامل

If the word1 is like a wazn (pattern), the letters must be equal, the
wazn has FEH, AIN, LAM letters. this are as generic letters. The two
words can be full vocalized, or partial vocalized

.. code:: python

    >>> from pyarabic import araby
    >>> word1 = u"ضارب"
    >>> wazn =  u"فَاعِل"
    >>> araby.waznlike(word1, wazn)
    True

-  تتماثل كلمتان في الشدة إذ كانت لهما نفس المكان، والحركات أيضا وقد
   يكون التشكيل غير كامل

If the two words has the same letters and the same harakats, this
fuction return True. The first word is partially vocalized, the second
is fully if the partially contians a shadda, it must be at the same
place in the fully

.. code:: python

    >>> from pyarabic import araby
    >>> word1 = u"ردّ"
    >>> word2=u"ردَّ"
    >>> araby.shaddalike(word1, word2)
    True

-  حساب التماثل في الحركات

نقيس التماثل في الحركات ، بحيث كل اختلاف ننقص 1 فنحصل على عدد سالب حسب
عدد مرات الاختلاف

if the two words has the same letters and the same harakats, this
function return True. The two words can be full vocalized, or partial
vocalized

.. code:: python

    >>> from pyarabic import araby
    >>> word1 = u"ضَربٌ"
    >>> word2 = u"ضَرْبٌ"
    >>> araby.vocalizedlike(word1, word2)
    True
    >>> word1 = u"ضَربٌ"
    >>> word2 = u"ضَرْبٍ"
    >>> araby.vocalized_similarity(word1, word2)
    -1

-  تفريق النص

يمكن استعمال الدالة tokenize لتفريق النص إلى كلمات

Tokenize text into words.

.. code:: python

    >>> from pyarabic import araby
    >>> text = u"العربية لغة جميلة."
    >>> tokens = araby.tokenize(text)
    >>> print(u"\n".join(tokens))
    ‎العربية
    ‎لغة
    ‎جميلة
    .

You can use it with conditions (restrict Arabic, keep or remove numbers,
exclude stop words ...etc).

To remove tashkeel and filter out non-Arabic words:

.. code:: python

    >>> from pyarabic.araby import tokenize, is_arabicrange, strip_tashkeel
    >>> text = u"ِاسمٌ الكلبِ في اللغةِ الإنجليزية Dog واسمُ الحمارِ Donky"
    >>> tokenize(text, conditions=is_arabicrange, morphs=strip_tashkeel)
            ['اسم', 'الكلب', 'في', 'اللغة', 'الإنجليزية', 'واسم', 'الحمار']

This structure will enable us to create functions on the fly and pass
them:

.. code:: python

    >>> from pyarabic.araby import tokenize
    >>> text = u"طلع البدر علينا من ثنيات الوداع"
    >>> tokenize(text, conditions=lambda x: x.startswith(u'ال'))
            ['البدر', 'الوداع']

-  تفريق النص إلى جمل Tokenize text into Sentences.

.. code:: python

    >>> from pyarabic import araby
    >>> text = u"العربية لغة جميلة. والبلاد بعيدة، والشوق زائد"
    >>> sentences  = araby.sentence_tokenize(text)
    >>> print(sentences)
    ['العربية لغة جميلة.', 'والبلاد بعيدة،', 'والشوق زائد']


-  تفريق النص إلى كلمات ومواضعها Tokenize text into tokens with location.

.. code:: python

    >>> from pyarabic import araby
    >>> text = "حدثنا ابن أبي عامر، قال: رايت مناما"
    >>> tokens = araby.tokenize_with_location(text)
    >>> print u"\\n".join(tokens)
     [{'token': 'حدثنا', 'start': 0,  'end': 5},
     {'token': 'ابن',   'start': 6,  'end': 9}, 
     {'token': 'أبي',   'start': 10, 'end': 13}, 
     {'token': 'عامر',  'start': 14, 'end': 18}, 
     {'token': 'قال',   'start': 20, 'end': 23}, 
     {'token': 'رايت',  'start': 25, 'end': 29},
     {'token': 'مناما','start': 30, 'end': 35}
     ]

وظائف الحروف
^^^^^^^^^^^^

دوال الحروف وهي تعيد صواب إذا انتمى الحرف إلى المجموعة المطلوبة

+-------------------------------------------------------+---------------------------+
| وصف الدالة                                            | الدالة                    |
+=======================================================+===========================+
| إذا كان الحرف المعطى سكونا يرجع صحيح                  | is\_sukun(archar)         |
+-------------------------------------------------------+---------------------------+
| إذا كان الحرف المعطى شدة يرجع صحيح                    | is\_shadda(archar)        |
+-------------------------------------------------------+---------------------------+
| إذا كان الحرف المعطى تطويلا يرجع صحيح                 | is\_tatweel(archar)       |
+-------------------------------------------------------+---------------------------+
| إذا كان الحرف المعطى تنوينا يرجع صحيح                 | is\_tanwin(archar)        |
+-------------------------------------------------------+---------------------------+
| إذا كان الحرف المعطى تشكيلا (حركة أو شدة) يرجع صحيح   | is\_tashkeel(archar)      |
+-------------------------------------------------------+---------------------------+
| إذا كان الحرف المعطى حركة يرجع صحيح                   | is\_haraka(archar)        |
+-------------------------------------------------------+---------------------------+
| إذا كان الحرف المعطى حركة قصيرة يرجع صحيح             | is\_shortharaka(archar)   |
+-------------------------------------------------------+---------------------------+
| إذا كان الحرف المعطى لام ألف يرجع صحيح                | is\_ligature(archar)      |
+-------------------------------------------------------+---------------------------+
| إذا كان الحرف المعطى همزة يرجع صحيح                   | is\_hamza(archar)         |
+-------------------------------------------------------+---------------------------+
| إذا كان الحرف المعطى ألفا يرجع صحيح                   | is\_alef(archar)          |
+-------------------------------------------------------+---------------------------+
| إذا كان الحرف المعطى يماثل الياء في رسمه يرجع صحيح    | is\_yehlike(archar)       |
+-------------------------------------------------------+---------------------------+
| إذا كان الحرف المعطى يماثل الواو في رسمه يرجع صحيح    | is\_wawlike(archar)       |
+-------------------------------------------------------+---------------------------+
| إذا كان الحرف المعطى تاء مفتوحة أو مربوطة يرجع صحيح   | is\_teh(archar)           |
+-------------------------------------------------------+---------------------------+
| إذا كان الحرف المعطى حرفا صغيرا يرجع صحيح             | is\_small(archar)         |
+-------------------------------------------------------+---------------------------+
| إذا كان الحرف المعطى حرف علة يرجع صحيح                | is\_weak(archar)          |
+-------------------------------------------------------+---------------------------+
| إذا كان الحرف المعطى حرفا قمريا يرجع صحيح             | is\_moon(archar)          |
+-------------------------------------------------------+---------------------------+
| إذا كان الحرف المعطى حرفا شمسيا يرجع صحيح             | is\_sun(archar)           |
+-------------------------------------------------------+---------------------------+

مثال
''''

في نطق الأسماء يتحوّل الحرف الشمسي بعد ال التعريف إلى حرف مشدد أي أنّ
"الشمس" تنطق "أششمس"،

.. code:: python

    #!/usr/bin/python
    # -*- coding=utf-8 -*-
    import pyarabic.araby as araby
    words=[u'الشمس', u'القمر', u'الرجل', u'بصل', u'البصل']
    for word in words:
        if word.startswith(araby.ALEF+araby.LAM) and araby.isSun(word[2]):
            word=u''.join([araby.ALEF+word[2],word[2:]]);
        print(word.encode('utf8');)

في المثال، نعطي عددا من الكلمات لكتابة نطقها، بتحويل الحرف الشمسي بعد ال
التعريف إلى حرف مكرر والنتيجة تكون

::

    اششمس
    القمر
    اررجل
    بصل
    البصل

وظائف الأعداد والأرقام
======================

number.py
---------

توفر هذه المكتبة وظائف مثل :

-  تحويل عدد إلى كلمات
-  البحث عن مواضع العبارات العددية
-  تحويل الكلمات إلى أعداد،
-  استخلاص العبارات العددية
-  تشكيلها
-  تنميط الأرقام بتنويعاتها المختلفة

-  تحويل عدد إلى كلمات Convert number to words

.. code:: python

    >>> import pyarabic.number
    >>> an = pyarabic.number.ArNumbers()
    >>> an.int2str('125')
    مئة و خمسة وعشرون

-  تحويل عدد إلى كلمات ترتيبية Convert number to ordinal words

.. code:: python

    >>> import pyarabic.number
    >>> pyarabic.number.number2ordinal(125)
    المئة والخامس والعشرون

-  تحويل الكلمات إلى أعداد Convert arabic text into number, for example
   convert تسعة وعشرون = >29.

.. code:: python

    >>> from pyarabic.number import text2number
    >>> text2number(u"خمسمئة وثلاث وعشرون")
    523

-  تشكيل جملة كلمات عددية Vocalize a number words clause

.. code:: python

    >>> from pyarabic import araby
    >>> from pyarabic.number import vocalize_number
    >>> txt = u"خمسمئة وثلاثة وعشرين"
    >>> wordlist = araby.tokenize(txt)
    >>> vocalized =  vocalize_number(wordlist)
    >>> print(u" ".join(vocalized))
    خَمْسمِئَة وَثَلاثَة وَعِشْرِينَ
    >>>

-  استخلاص العبارات العددية من جملة

Extract number words in a text.

.. code:: python

    >>> from pyarabic.number import extract_number_phrases
    >>> extract_number_phrases(u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا")
    خمسمئة وثلاثة وعشرين
    ثلاثة عشر

-  استخلاص العبارات العددية مع سياقها

Extract number words in a text with context.

.. code:: python

    >>> from pyarabic.number import extract_number_context
    >>> extract_number_context(u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا")
    ‎وجدت، خمسمئة وثلاثة وعشرين، دينارا
    ‎فاشتريت، ثلاثة عشر ، دفتر

-  استخلاص مواضع العبارات العددية

Detect number words in a text and return positions of each phrase.

.. code:: python

    >>> from pyarabic import araby
    >>> from pyarabic.number import detect_number_phrases_position
    >>> txt = u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا"
    >>> wordlist = araby.tokenize(txt)
    >>> positions_phrases =  detect_number_phrases_position(wordlist)
    >>> print(positions_phrases)
    [(1, 3), (6, 7)]

-  استخلاص مواضع العبارات العددية باستعمال الوسوم

-  DO: لاشيء
-  DB: بداية العبارة العددية
-  DI: داخل العبارة العددية

Detect number words in a text and return a taglist as BIO.

.. code:: python

    >>> from pyarabic import araby
    >>> from pyarabic.number import detect_numbers
    >>> wordlist = araby.tokenize(u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا")
    >>> detect_numbers(wordlist)
    ['DO', 'DB', 'DI', 'DI', 'DO', 'DO', 'DB', 'DI', 'DO']

-  استخلاص العبارات العددية وإرجاع الجمل

Detect number words in a text, return strings.

.. code:: python

    >>> from pyarabic.number import detect_number_words
    >>> detect_number_words(u"وجدت خمسمئة وثلاثة وعشرين دينارا")
    خمسمئة وثلاثة وعشرين

-  تشكيل أولي للعبارات العددية

Vocalized a number clauses in a text.

.. code:: python

    >>> from pyarabic import araby
    >>> from pyarabic.number import pre_tashkeel_number
    >>> txt = u"وجدت خمسمئة وثلاثة وعشرين دينارا فاشتريت ثلاثة عشر دفترا"
    >>> wordlist = araby.tokenize(txt)
    >>> vocalized =  pre_tashkeel_number(wordlist)
    >>> print(u" ".join(vocalized))
    وجدت خَمْسمِئَة وَثَلاثَة وَعِشْرِينَ دينارا فاشتريت ثَلاثَةَ عَشَرَ دفترا

وظائف تنميط الأرقام
^^^^^^^^^^^^^^^^^^^

تستعمل في العربية تنويعتين مشرقية ومغربية، وتنويعات أخرى مثل الفارسية
والهندية

Normalize digits to and from the following writing systems: west:
Western Arabic numerals (0123456789) east: Eastern Arabic (Hindu-Arabic)
numerals (٠١٢٣٤٥٦٧٨٩) persian: Persian/Urdu numerals (۰۱۲۳۴۵۶۷۸۹)

if ``source = all``, then all digits contained in the text will be
normalized into ``out`` writing system. Otherwise digits written in
``source`` will be normalized without affecting the rest of the digits.

Uniformize Arabic digits normalize\_digits(nd\_text, source='all',
out='east')

.. code:: python

    >>> import pyarabic.trans
    >>> text = u'۰۱۲۳۴۵۶۷۸۹ ٠١٢٣٤٥٦٧٨٩ 123456789'
    >>> pyarabic.trans.normalize_digits(text, source='all', out='west')
    '0123456789 0123456789 123456789'
    >>> pyarabic.trans.normalize_digits(text, source='persian', out='west')
    '0123456789 ٠١٢٣٤٥٦٧٨٩ 123456789'

وظائف قلب النصوص
^^^^^^^^^^^^^^^^

تستعمل لقلب الحروف، بسبب عدم دعم بعض البرامج للغة العربية، مما يدعونا
إلى قلب الحروف.

-  قلب النص

Unshape a text

.. code:: python

    >>> from pyarabic.unshape import unshaping_text
    >>> TEXTS = u'لو والحيـاة مريرة   وليتك ترضى والانـــام غضاب '
    >>> print(unshaping_text(TEXTS).encode('utf8'))
    باضغ ماـــنالاو ىضرت كتيلو   ةريرم ةاـيحلاو ولحت كتيلف

-  قلب سطر

Unshape a line

.. code:: python

    >>> from pyarabic.unshape import unshaping_line
    >>> line = u'فليتك تحلو والحيـاة مريرة   وليتك ترضى والانـــام غضاب '
    >>> print(unshaping_line(line).encode('utf8'))
    باضغ ماـــنالاو ىضرت كتيلو   ةريرم ةاـيحلاو ولحت كتيلف

-  قلب كلمة

Unshape a word

.. code:: python

    >>> from pyarabic.unshape import unshaping_word
    >>> word = u'العربية'
    >>> print(unshaping_word(word).encode('utf8'))
    ةيبرعلا

وظائف نقل حرفي
^^^^^^^^^^^^^^

تستعمل في تحويل ترميز النص من العربية يونيكود إلى ترميز Tim buckwalter
أو sampa

Transliterate

Unshape a text

.. code:: python

    >>> import pyarabic.trans
    >>> worda = u"العربية"
    >>> wordb=u"Al'rabiya"
    >>> pyarabic.trans.convert(worda,'arabic','tim')
    u'AlErbyp'
    >>> pyarabic.trans.convert(wordb,'tim','arabic')
    الءرَبِيَ

وظائف كشف اللغة
^^^^^^^^^^^^^^^

كشف اللغة العربية بواسطة segment\_language وضع علامات على لغة معينة
delimite\_language

.. code:: python

    >>> import pyarabic.trans
    >>> text =u"""السلام عليكم how are you, لم اسمع أخبارك منذ مدة, where are you going"""
    >>> pyarabic.trans.segment_language(text)
    [(u'arabic', u'السلام عليكم'), (u'latin', u' how are you, '), (u'arabic', u'لم اسمع أخبارك منذ مدة'), (u'latin', u', where are you going')]
    >>> pyarabic.trans.delimite_language(text, start='\RL{', end="}")
    \RL{السلام عليكم}  how are you,  \RL{لم اسمع أخبارك منذ مدة} , where are you going
    >>> pyarabic.trans.delimite_language(text, start="<arabic>", end="</arabic>")
    <arabic>السلام عليكم</arabic>  how are you,  <arabic>لم اسمع أخبارك منذ مدة</arabic> , where are you going

    >>> pyarabic.trans.delimite_language(text, language="latin")
    السلام عليكم < how are you, > لم اسمع أخبارك منذ مدة <, where are you going>

ترميز التشكيل رقميا
^^^^^^^^^^^^^^^^^^^

تفيد هذه الوظيفة في ترميز الحركات من الكلمة بطريقة قابلة للقراءة، في شكل
عدد أو سلسلة حروف لاتينية، ويهدف إلى تسهيل حفظها على حدى أو إرسالها.

Encode word marks into decimal or Ascii string to be saved or
transmitted.

.. code:: python

    >>> import pyarabic.trans
    >>> word1 = u"هَارِبًا"
    >>> pyarabic.trans.encode_tashkeel(word1)
    ('هاربا', 'a0iA0')
    >>> pyarabic.trans.encode_tashkeel(word1, "decimal")
    ('هاربا', 40610)
    >>> letters = u"هاربا" 
    >>> encoded_marks = u"a0iA0"
    >>> pyarabic.trans.decode_tashkeel(letters, encoded_marks)
    'هَارِبًا'
    >>> letters = u"هاربا" 
    >>> encoded_marks = 40610
    >>> pyarabic.trans.decode_tashkeel(letters, encoded_marks, "decimal")
    'هَارِبًا'

