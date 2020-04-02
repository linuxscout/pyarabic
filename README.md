# PyArabic
A specific *Arabic language* library for **Python**, provides basic functions to manipulate Arabic letters and text, like detecting Arabic letters, Arabic letters groups and characteristics, remove diacritics etc.

مكتبة برمجية للغة العربية بلغة بيثون، توفر دوالا للتحكم في الحروف والنصوص، مثلا تحديد نوع الحرف، حذف الحركات، مقارنة التشكيل.


  Developpers:  Taha Zerrouki: http://tahadz.com
    taha dot zerrouki at gmail dot com

Features |   value
---------|---------------------------------------------------------------------------------
Authors  | Taha Zerrouki: http://tahadz.com,  taha dot zerrouki at gmail dot com
Release  | 0.6.7
License  |[GPL](https://github.com/linuxscout/pyarabic/master/LICENSE)
Tracker  |[linuxscout/pyarabic/Issues](https://github.com/linuxscout/pyarabic/issues)
Website  |[https://pypi.python.org/pypi/pyarabic](https://pypi.python.org/pypi/pyarabic)
Doc  |[package Documentaion](https://pyarabic.readthedocs.io/)
Source  |[Github](http://github.com/linuxscout/pyarabic)
Download  |[pypi.python.org](https://pypi.python.org/pypi/pyarabic)
Feedbacks  |[Comments](https://github.com/linuxscout/pyarabic/issues)
Accounts  |[@Twitter](https://twitter.com/linuxscout)  [@Sourceforge](http://sourceforge.net/projects/pyarabic/)



## Citation
If you would cite it in academic work, can you use this citation
```
T. Zerrouki‏, Pyarabic, An Arabic language library for Python,
  https://pypi.python.org/pypi/pyarabic/, 2010
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


## مزايا
* تصنيف الحروف
* تفريق النص إلى وحدات
* حذف الحركات:( كل الحركات، الحركات عدا الشدة، حذف الشدة، حذف التطويل، حذف الحركة الأخيرة)
* فصل الحركات عن النصوص وإدماجها
* اختزال التشكيل
* قياس التماثل بين كلمتين ( في الحركات جزئيا وكليا، التماثل مع وزن)
* تنميط الحروف ( توحيد التراكيب مثل لام الألف، والهمزات)
* تحويل الأعداد إلى كلمات
* استخلاص العبارات العددية من النص
* تشكيل أولي للعبارات العددية
* قلب النصوص العربية للأنظمة التي لا تدعم تشبيك الحروف

## Features
* Arabic letters classification
* Text tokenization
* Strip Harakat ( all, except Shadda, tatweel, last_haraka)
* Sperate and  join Letters and Harakat
* Reduce tashkeel
* Mesure tashkeel similarity ( Harakats, fully or partially vocalized, similarity with a template)
* Letters normalization ( Ligatures and Hamza)
* Numbers to words
* Extract numerical phrases
* Pre-vocalization of numerical phrases
* Unshiping texts


Applications
====
* Arabic text processing

Installation
=====
```
pip install pyarabic
```    
    
Usage
=====
```python
import pyarabic.araby as araby
import pyarabic.number as number
```




Package Documentation
=====
[https://pythonhosted.org/PyArabic/](https://pythonhosted.org/PyArabic/)

Files
=====
* file/directory    category    description 
 * araby.py: arabic routins.
 * named.py: handle named enteties recognation.
 * unshape.py: unshaping arabic text

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


### وحدة الوظائف العامة araby
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
الحروف الشمسية | الحروف الشمسية | SUN = (u'ت', u'ث', u'د', u'ذ', u'ر', u'ز', u'س', u'ش', u'ص', u... 
ترتيب الحروف العربية | يعطي لكل حرف عربي رقما ترتيبيا فالألف واحد والباء اثنان والهمزة 29. | AlphabeticOrder = {u'ء': 29, u'آ': 29, u'أ': 29, u'ؤ': 29, u'إ... 
أسماء الحروف | يعطي كل حرف اسمه العربي | NAMES = {u'ء': u'همزة', u'آ': u'ألف ممدودة', u'أ': u'همزة على ... 


#### الوظائف- الدوال

##### أهم الوظائف

وصف الدالة  |الدالة
------|------------
حذف الحركات كلها بما فيها الشدة|strip_tashkeel(text)
حذف الحركات كلها ماعدا الشدة|strip_harakat(text)
حذف الحركة الأخيرة|strip_lastharaka(text)
حذف التطويل| strip_tatweel(text)
تنميط أشكال الهمزة المختلفة | normalize_hamza(text)
تفريق كلمات النص |tokenize(text)

طالع الوظائف والأمثلة في ]ملف المزايا[
[features.md](doc/features.md)
