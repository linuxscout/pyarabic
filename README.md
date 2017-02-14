#pyarabic
A specific *Arabic language* library for **Python**, provides basic functions to manipulate Arabic letters and text, like detecting Arabic letters, Arabic letters groups and characteristics, remove diacritics etc.

# pyarabic
=======
pyarabic: A specific *Arabic language* library for **Python**  مكتبة برمجية للغة العربية بلغة بيثون


  Developpers:  Taha Zerrouki: http://tahadz.com
    taha dot zerrouki at gmail dot com

Features |   value
---------|---------------------------------------------------------------------------------
Authors  | [Authors.md](https://github.com/linuxscout/pyarabic/master/AUTHORS.md)
Release  | 0.6
License  |[GPL](https://github.com/linuxscout/pyarabic/master/LICENSE)
Tracker  |[linuxscout/pyarabic/Issues](https://github.com/linuxscout/pyarabic/issues)
Website  |[https://pypi.python.org/pypi/pyarabic](https://pypi.python.org/pypi/pyarabic)
Doc  |[package Documentaion](http://pythonhosted.org/pyarabic/)
Source  |[Github](http://github.com/linuxscout/pyarabic)
Download  |[pypi.python.org](https://pypi.python.org/pypi/pyarabic)
Feedbacks  |[Comments](http://tahadz.com/pyarabic/contact)
Accounts  |[@Twitter](https://twitter.com/linuxscout)  [@Sourceforge](http://sourceforge.net/projects/pyarabic/)



## Citation
If you would cite it in academic work, can you use this citation
```
T. Zerrouki‏, Pyarabic, An Arabic language library for Python,  https://pypi.python.org/pypi/pyarabic/, 2010
```
or in bibtex format

```bibtex
@misc{zerrouki2012pyarabic,
  title={pyarabic, An Arabic language library for Python},
  author={Zerrouki, Taha},
  url={https://pypi.python.org/pypi/pyarabic,
  year={2010}
}
```


##مزايا


##Features



Applications
====


Installation
=====
```
pip install pyarabic
```    
    
Usage
=====




### Example 


Package Documentation
=====
[https://pythonhosted.org/PyArabic/](https://pythonhosted.org/PyArabic/)

Files
=====
* file/directory    category    description 

* [docs]
    docs/   docs    documentation

* [support]
    - pyarabic  : basic arabic library

* [test]
    - output/   test    test output
    - samples/  test    sample files
    - tools/    test    script to use pyarabic

# وصف
مكتبة بيثون للعربيةPyArabic  مكتبة برمجية تجمع في طياتها خصائص ووظائف يحتاجها المبرمج للتعامل مع النصوص العربية، وهي مستوحاة من مكتبة بي أتش بي العربية لصديقنا خالد الشمعة، التي تستهدف توفير مصدر مفتوح لكثير من وظائف النصوص العربية لاستعمالها في مجال النشر في الإنترنت.

#تعريف نص عربي
أفضل طريقة للتعامل مع النصوص العربية بلغة بيثون هو استخدام الترميز يونيكود، التي يدعمها بيثون دعما أصليا، لا حاجة فيه إلى مكتبات خارجية أو دوال خاصة، وقد يكون هذا أهمّ ما دفعني لاختيار لغة بيثون، إذ يكفي أن تسبق النص بحرف يو u  لتدع بيثون يريحك من عناء التفكير وبرمجة النصوص، ويعامل معها بشفافية عالية.

تعريف نص عربي بترميز يونيكود

```python
text = u'الإسلام ديننا'
```

اختيار ترميز ملف المتن.
```
﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
```

عرض النص العربي في المخرج
```
print text.encode('utf8')
```

اسم المكتبة pyarabic
فيها العديد من الوظائف المجمعة في وحدات:

فيها العديد من الوظائف المجمعة في وحدات:
* وحدة : araby.py  وفيها الثوابت كالحروف وأسمائها ومجموعاتها والوظائف العامة كحذف الحركات وحذف التطويل ومقارنة التشكيل بين الكلمات، وضبط  علامات الترقيم.
* وحدة الأعداد number.py : وفيها وظائف تحويل الأعداد إلى كلمات والكلمات إلى أعداد، كشف ألفاظ الأعداد في النص، وتشكيلها.
* وحدة المسميات : named.py وفيها وظائف لكشف الأسماء والمسميات في النص.


###وحدة الوظائف العامة araby
يمكن استدعاؤها بالأمر 
```python
Import pyarabic.araby as araby
```

وسنستعمل الاختصار araby  فيما بعد
الثوابت العامة في مكتبة عربي:
تضم الحروف العربية  ومجموعاتها المختلفة وبعض الأنماط المستخدمة لاحقا في وظائف مختلفة
1- الحروف العربية الأساسية مع تسميات لاتينية لاستعمالها في البرمجة

The arabic chars contains all arabic letters, a sub class of unicode,

```python
COMMA            = u'\u060C'
SEMICOLON        = u'\u061B'
QUESTION         = u'\u061F'
HAMZA            = u'\u0621'
ALEF_MADDA       = u'\u0622'
ALEF_HAMZA_ABOVE = u'\u0623'
```
المزيد في ملف araby.py

تضم مجموعة الحروف العربية الحروف الأساسية، والحركات والأرقام، وعلامات الترقيم، وبعض الحروف الخاصة كالألف الخنجرية والياء الصغيرة، و لامات الألف بأشكالها.
####مجموعات الأحرف: 
ويمكن تقسيم الحروف في مجموعات وتصنيفات نستعملها فيما بعد في الوظائف المختلفة

الاسم العربي | وصف المجموعة | عناصرها
--------|--------------|------------
الحروف | مجموعة الحروف العربية دون حركات | LETTERS = u'ابتةثجحخدذرزسشصضطظعغفقكلمنهويءآأؤإئ' 
التشكيل  | مجموعة الحركات مع الشدة مدرجة  | TASHKEEL =(FATHATAN, DAMMATAN, KASRATAN, FATHA,DAMMA,KASRA, SUKUN,   SHADDA)
الحركات | مجموعة الحركات دون الشدة مدرجة | HARAKAT =(  FATHATAN,   DAMMATAN,   KASRATAN,  FATHA,  DAMMA,  KASRA, SUKUN);
الحركات القصيرة | الحركات القصيرة دون تنوين | SHORTHARAKAT =( FATHA,  DAMMA,  KASRA, SUKUN);
التنوين | حركات التنوين | TANWIN =(FATHATAN,  DAMMATAN,   KASRATAN);
المركبات | لامات الألف في أشكالها المختلفة | LIGUATURES = (u'ﻻ', u'ﻷ', u'ﻹ', u'ﻵ') 
الهمزات | الهمزة في أشكالها المختلفة | HAMZAT = (u'ء', u'ؤ', u'ئ', u'ٔ', u'ٕ', u'إ', u'أ') 
الألفات | الألف في أشكالها المختلفة | ALEFAT = (u'ا', u'آ', u'أ', u'إ', u'ٱ', u'ى', u'ٰ') 
حروف العلة | الياء والواو والألف | WEAK = (u'ا', u'و', u'ي', u'ى') 
الياءات | ما يرسم مثل الياء، الصغيرة منها، والألف المقصورة والهمزة على النبرة | YEHLIKE = (u'ي', u'ئ', u'ى', u'ۦ') 
الواوات | ما يرسم مثل الواو | WAWLIKE = (u'و', u'ؤ', u'ۥ') 
التاءات | التاء المربوطة والمفتوحة | TEHLIKE = (u'ت', u'ة') 
الحروف الصغيرة | الألف والياء والواو الصغار | SMALL = (u'ٰ', u'ۥ', u'ۦ') 
الحروف القمرية | الحروف القمرية | MOON = (u'ء', u'آ', u'أ', u'إ', u'ا', u'ب', u'ج', u'ح', u'خ', ... 
الحروف الشمسية | الحروف القمرية | SUN = (u'ت', u'ث', u'د', u'ذ', u'ر', u'ز', u'س', u'ش', u'ص', u... 
ترتيب الحروف العربية | يعطي لكل حرف عربي رقما ترتيبيا فالألف واحد والباء اثنان والهمزة 29. | AlphabeticOrder = {u'ء': 29, u'آ': 29, u'أ': 29, u'ؤ': 29, u'إ... 
أسماء الحروف | يعطي كل حرف اسمه العربي | NAMES = {u'ء': u'همزة', u'آ': u'ألف ممدودة', u'أ': u'همزة على ... 


####الوظائف- الدوال
الوظائف (الدوال)
دوال الحروف وهي تعيد صواب إذا انتمى الحرف إلى المجموعة المطلوبة

وصف الدالة  |الدالة
------|------------
حذف الحركات كلها بما فيها الشدة|strip_tashkeel(text)
حذف الحركات كلها ماعدا الشدة|strip_harakat(text)
حذف الحركة الأخيرة|strip_lastharaka(text)
حذف التطويل| strip_tatweel(text)
تنميط أشكال الهمزة المختلفة | normalize_hamza(text)
تفريق كلمات النص |tokenize(text)إذا كان الحرف المعطى سكونا يرجع صحيح | is_sukun(archar)
إذا كان الحرف المعطى شدة يرجع صحيح | is_shadda(archar)
إذا كان الحرف المعطى تطويلا يرجع صحيح | is_tatweel(archar)
إذا كان الحرف المعطى تنوينا يرجع صحيح | is_tanwin(archar)
إذا كان الحرف المعطى تشكيلا (حركة أو شدة) يرجع صحيح | is_tashkeel(archar)
إذا كان الحرف المعطى حركة يرجع صحيح | is_haraka(archar)
إذا كان الحرف المعطى حركة قصيرة يرجع صحيح | is_shortharaka(archar)
إذا كان الحرف المعطى لام ألف يرجع صحيح | is_ligature(archar)
إذا كان الحرف المعطى همزة يرجع صحيح | is_hamza(archar)
إذا كان الحرف المعطى ألفا يرجع صحيح | is_alef(archar)
إذا كان الحرف المعطى يماثل الياء في رسمه يرجع صحيح | is_yehlike(archar)
إذا كان الحرف المعطى يماثل الواو في رسمه يرجع صحيح | is_wawlike(archar)
إذا كان الحرف المعطى تاء مفتوحة أو مربوطة يرجع صحيح | is_teh(archar)
إذا كان الحرف المعطى حرفا صغيرا يرجع صحيح | is_small(archar)
إذا كان الحرف المعطى حرف علة يرجع صحيح | is_weak(archar)
إذا كان الحرف المعطى حرفا قمريا يرجع صحيح | is_moon(archar)
إذا كان الحرف المعطى حرفا شمسيا يرجع صحيح | is_sun(archar)

###مثال

في نطق الأسماء يتحوّل الحرف الشمسي بعد ال التعريف إلى حرف مشدد أي أنّ "الشمس" تنطق "أششمس"، 
```python
#!/usr/bin/python
# -*- coding=utf-8 -*-
import pyarabic.araby as araby
words=[u'الشمس', u'القمر', u'الرجل', u'بصل', u'البصل']
for word in words:
    if word.startswith(araby.ALEF+araby.LAM) and araby.isSun(word[2]):
        word=u''.join([araby.ALEF+word[2],word[2:]]);
    print word.encode('utf8');
```
في المثال، نعطي عددا من الكلمات لكتابة نطقها، بتحويل الحرف الشمسي بعد ال التعريف إلى حرف مكرر والنتيجة تكون 
```
اششمس
القمر
اررجل
بصل
البصل
```

