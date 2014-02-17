

import  pyarabic.archars as arabic
araby=arabic.arabicchars();

for c in araby.arabicrange():
    print c.encode('utf8'),'\t', araby.name(c).encode('utf8'),
    print '\t',
    if araby.isSukun(c): print "sukun",
    if araby.isHaraka(c): print "haraka",
    if araby.isShadda(c): print "shadda",
    if araby.isTatweel(c): print "tatweel",
    if araby.isTashkeel(c): print "tashkeel",
    if araby.isTanwin(c): print "tanwin",
    if araby.isShortharaka(c): print "short haraka",
    if araby.isLigature(c):print " ligature",
    if araby.isLigature(c):print 'ligature',
    if araby.isHamza(c):	print 'hamza',
    if araby.isAlef(c):	print 'alef',
    if araby.isYehlike(c):	print 'yeh',
    if araby.isWawlike(c):	print 'waw',
    if araby.isTeh(c):	print 'teh',
    if araby.isSmall(c):	print 'small',
    if araby.isWeak(c):	print 'weak',
    if araby.isMoon(c):	print 'moon',
    if araby.isSun(c):print 'sun',
    print araby.order(c),
    print;
word=u"الْعَرَيِيّةُ"
word_list=[
u"الْعَرَيِيّةُ",
u"العربية",
u"الْعَرَيِيّةُ الفصحى",
u"غير مشكول",
"Taha",
]
word1=u""
for word in word_list:
    print word.encode('utf8'),'\t',
    if araby.isVocalized(word): print ' is vocalized',
##    if araby.isArabicstring(word): print ' iisArabicstring',
##    else:print ' invalid arabicstring',
    if araby.isVocalizedtext(word): print ' is vocalized text',
    if araby.isArabicword(word): print ' is valid word',
    else: print "invalid arabic word",
    print ' strip harakat', araby.stripHarakat(word).encode('utf8'),
    print ' strip tashkeel', araby.stripTashkeel(word).encode('utf8'),
    print ' strip tatweel',araby.stripTatweel(word).encode('utf8'),
    print ' normalize ligature ', araby.normalizeLigature(word).encode('utf8'),
    if araby.vocalizedlike(word, word1): print "vocalized_like",
    print;
    word1=word;
if araby.vocalizedlike(u"العربية",u"العرَبية"): print "vocalized_like",

