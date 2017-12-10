# -*- coding=utf-8 -*-
#Lexeme Label
"""
Proper Nouns Constants, actually whole list
"""
TEXT = u"""
السيسي nasab
محمد    nom
أبا زبر konia
أبا زبيد    konia
أبا زحارة   konia
أبا زرارة   konia
أبا زرعة    konia
أبا زفر konia
أبا زكريا   konia
أبا زميل    konia
أبا زهرة    konia
أبا زهير    konia
أبا زياد    konia
أبا زيادة   konia
أبا زيد konia
أبا زينب    konia
أبا زينب الحجازى    konia
أبا زينب الحجازي    konia
أبا ساج konia
أبا ساسان   konia
أبا سالم    konia
أبا سبأ konia
أبا سبرة    konia
أبا سحيم    konia
أبا سخيلة   konia
أبا سروعة   konia
أبا سريحة   konia
أبا سريرة   konia
أبا سعاد    konia
أبا سعد konia
أبا سعدة    konia
أبا سعيد    konia
أبا سعيد الخير  konia
أبا سعيد المؤدب konia
أبا سفيان   konia
أبا سكينة   konia
أبا سلام    konia
أبا سلامة   konia
أبا سلمان   konia
أبا سلمان المؤذن    konia
أبا سلمة    konia
أبا سلمى    konia
أبا سلمي    konia
أبا سليم    konia
أبا سليمان  konia
أبا سماك    konia
أبا سمية    konia
أبا سنان    konia
أبا سهل konia
أبا سهلة    konia
أبا سهيل    konia
أبا سورة    konia
أبا سوية    konia
أبا سويد    konia
أبا سويرة   konia
أبا سيارة   konia
أبا سيدان   konia
أبا سيف konia
أبا شاكر    konia
أبا شبرمة   konia
أبا شبل konia
أبا شجاع    konia
أبا شجرة    konia
أبا شرحبيل  konia
أبا شريح    konia
أبا شريك    konia
أبا شعبة    konia
أبا شعيب    konia
أبا شمر konia
أبا شهاب    konia
أبا شهر konia
أبا شهم konia
أبا شهيد    konia
أبا شيبان   konia
أبا شيبة    konia
أبا شيخ konia
أبا صادق    konia
أبا صالح    konia
أبا صخر konia
أبا صخرة    konia
أبا صدقة    konia
أبا صرمة    konia
أبا صعير    konia
أبا صفوان   konia
أبا صيفى    konia
أبا صيفي    konia
أبا ضمرة    konia
أبا طارق    konia
أبا طالب    konia
أبا طالوت   konia
أبا طاهر    konia
أبا طريف    konia
أبا طعمة    konia
أبا طلحة    konia
أبا طوالة   konia
أبا طيبة    konia
أبا ظبيان   konia
أبا ظبية    konia
أبا ظفر konia
أبا ظلال    konia
أبا عائذ    konia
أبا عائذ الله   konia
أبا عائشة   konia
أبا عاتكة   konia
أبا عازب    konia
أبا عاصم    konia
أبا عامر    konia
أبا عباد    konia
أبا عبادة   konia
أبا عبد الجبار  konia
أبا عبد الحمن   konia
أبا عبد الحميد  konia
أبا عبد الدائم  konia
أبا عبد الرحمن  konia
أبا عبد الرحمن ‎    konia
أبا عبد الرحيم  konia
أبا عبد السلام  konia
أبا عبد الصمد   konia
أبا عبد العزيز  konia
أبا عبد القدوس  konia
أبا عبد الكريم  konia
أبا عبد الله    konia
أبا عبد الله الجهنى konia
أبا عبد الله الجهني konia
أبا عبد الله الخياط konia
أبا عبد الله الضرير konia
أبا عبد الله المؤدب المكتب  konia
أبا عبد الله المؤذن konia
أبا عبد الملك   konia
أبا عبد رب  konia
أبا عبد رب العزة    konia
أبا عبد ربه konia
أبا عبدالرحمن   konia
أبا عبدة    konia
أبا عبس konia
أبا عبيد    konia
أبا عبيد الله   konia
أبا عبيدة   konia
أبا عتاب    konia
أبا عتبة    konia
أبا عتيق    konia
أبا عتيك    konia
أبا عثمان   konia
أبا عثيم    konia
أبا عدى konia
أبا عدي konia
أبا عذرة    konia
أبا عرفة    konia
أبا عروبة   konia
أبا عروة    konia
أبا عزة konia
أبا عشانة   konia
أبا عصام    konia
أبا عصمة    konia
أبا عصيدة   konia
أبا عطاء    konia
أبا عطية    konia
أبا عفان    konia
أبا عقال    konia
أبا عقبة    konia
أبا عقرب    konia
أبا عقيل    konia
أبا عكاشة   konia
أبا عكرمة   konia
أبا علقمة   konia
أبا علوان   konia
أبا علويه   konia
أبا علي konia
أبا عمار    konia
أبا عمارة   konia
أبا عمر konia
‏أبا عمران  konia
أبا عمرة    konia
أبا عمرو    konia
أبا عمير    konia
أبا عميرة   konia
أبا عنبة    konia
أبا عنبسة   konia
‏أبا عوانة  konia
أبا عوف konia
أبا عون konia
أبا عياش    konia
أبا عياض    konia
أبا عيسى    konia
أبا عيسي    konia
أبا غالب    konia
أبا غانم    konia
أبا غرارة   konia
أبا غزوان   konia
أبا غسان    konia
أبا غطفان   konia
أبا غطيف    konia
أبا غفار    konia
أبا غلاب    konia
أبا غلباء   konia
أبا غياث    konia
أبا فاختة   konia
أبا فاطمة   konia
أبا فراس    konia
أبا فروة    konia
أبا فروة الأصغر konia
أبا فزارة   konia
أبا فضالة   konia
أبا قابوس   konia
أبا قبيصة   konia
أبا قبيل    konia
أبا قتادة   konia
أبا قتيبة   konia
أبا قتيلة   konia
أبا قدامة   konia
أبا قديد    konia
أبا قرة konia
أبا قرصافة  konia
أبا قريش    konia
أبا قزعة    konia
أبا قضاعة   konia
أبا قطن konia
أبا قلابة   konia
أبا قنان    konia
أبا قيس konia
أبا كامل    konia
أبا كاهل    konia
أبا كباش    konia
أبا كبشة    konia
أبا كبشة البراء konia
أبا كثير    konia
أبا كدينة   konia
أبا كرب konia
أبا كردوس   konia
أبا كرز konia
أبا كريب    konia
أبا كريمة   konia
أبا كعب konia
أبا كلثم    konia
أبا كليب    konia
أبا كنانة   konia
أبا لاس konia
أبا لبابة   konia
أبا لبيد    konia
أبا لقمان   konia
أبا لوط konia
أبا ليث konia
أبا ليلى    konia
أبا ليلي    konia
أبا ماجد    konia
أبا ماجدة   konia
أبا مالك    konia
أبا مجاهد   konia
أبا مجلز    konia
أبا محذورة  konia
أبا محرر    konia
أبا محرز    konia
أبا محصن    konia
أبا محلم    konia
أبا محمد    konia
أبا محمود   konia
أبا محيريز  konia
أبا مخارق   konia
أبا مخاشن   konia
أبا مخلد    konia
أبا مدرك    konia
أبا مدلة    konia
أبا مرازم   konia
أبا مراوح   konia
أبا مرة konia
أبا مرثد    konia
أبا مرحب    konia
أبا مرحوم   konia
أبا مرزوق   konia
أبا مروان   konia
أبا مريم    konia
أبا مزاحم   konia
أبا مزرد    konia
أبا مساحق   konia
أبا مسافر   konia
أبا مسعود   konia
أبا مسقبة   konia
أبا مسكين   konia
أبا مسلم    konia
أبا مسلمة   konia
أبا مسهر    konia
أبا مشجعة   konia
أبا مصبح    konia
أبا مصعب    konia
أبا مصلح    konia
أبا مضر konia
آل أبى بردة kabila
آل أبي بردة kabila
آل أبى بكر  kabila
آل أبي بكر  kabila
آل أبى سفيان    kabila
آل أبي سفيان    kabila
آل الحارث   kabila
آل الحكم    kabila
آل الزبير   kabila
آل العباس   kabila
آل بنى أسد  kabila
آل جرير kabila
آل جعدة kabila
آل حجير kabila
آل حنين kabila
آل رياح kabila
آل زيد  kabila
آل سعيد kabila
آل طلحة kabila
آل عباس kabila
آل عثمان    kabila
آل عقبة kabila
آل عمر  kabila
آل عمرو kabila
آل قارظ kabila
آل قيس  kabila
آل كثير kabila
آل مروان    kabila
آل معاوية   kabila
أهل البصرة  kabila
الأنصار kabila
النضير  kabila
بنو عمرو بن عوف kabila
بني أبي معيط    kabila
بنى أسد kabila
بنى أمية    kabila
بنى الحارث  kabila
بنى الحريش  kabila
بنى الديل   kabila
بنى الصيداء من بنى أسد  kabila
بني النجار  kabila
بنى بكر kabila
بنى تميم    kabila
بنى تيم kabila
بنى تيم الله    kabila
بنى ثعلبة   kabila
بني حارثة   kabila
بنى حمان    kabila
بني حنيفة   kabila
بنى رياح    kabila
بنى زهرة    kabila
بني سالم    kabila
بنى سامة    kabila
بنى سعد kabila
بنى سليم    kabila
الرسول  rasoul
بنى شيبان   kabila
بنى عامر    kabila
بنى عبد الدار   kabila
بنى عبيد الله   kabila
بنى عجل kabila
بنى عدى kabila
بنى عدي kabila
بني عمرو بن عوف kabila
بنى عوذ kabila
بنى غفار    kabila
بنى غنى kabila
بنى غني kabila
بني فراس    kabila
بنى فزارة   kabila
بني فزارة   kabila
بنى قيس kabila
بنى كعب kabila
بنى كعب من خزاعة    kabila
بنى كليب    kabila
بنى كنانة   kabila
بنى ليث kabila
بنى مخزوم   kabila
بنى نوفل    kabila
بنى هاشم    kabila
بنى هلال    kabila
بهراء   kabila
تميم    kabila
ثقيف    kabila
خزاعة   kabila
قريش    kabila
قريظة   kabila
أبا أبا konia
أبا إبراهيم konia
أبا أحمد    konia
أبا إدام    konia
أبا إدريس   konia
أبا أرطاة   konia
أبا أسامة   konia
أبا إسحاق   konia
أبا أسد konia
أبا إسرائيل konia
أبا أسماء   konia
أبا إسماعيل konia
أبا أسيد    konia
أبا أفلح    konia
أبا إلياس   konia
أبا أمامة   konia
أبا أمية    konia
أبا أمية المكى  konia
أبا أمية المكي  konia
أبا أميمة   konia
أبا أمين    konia
أبا أنس konia
أبا أنيس    konia
أبا أنيسة   konia
أبا أويس    konia
أبا إياس    konia
أبا أيمن    konia
أبا أيوب    konia
أبا الأباض  konia
أبا الأبرد  konia
أبا الأحوص  konia
أبا الأخيل  konia
أبا الأزهر  konia
أبا الأسباط konia
أبا الأسد   konia
أبا الأسقع  konia
أبا الأسود  konia
أبا الأشرس  konia
أبا الأشعث  konia
أبا الأشهب  konia
أبا الأصبغ  konia
أبا الأعور  konia
أبا الأعيس  konia
أبا الأغر   konia
أبا البخترى konia
أبا البختري konia
أبا البداح  konia
أبا البزرى  konia
أبا البزري  konia
أبا التجيب  konia
أبا التياح  konia
أبا الثورين konia
أبا الجارود konia
أبا الجارية konia
أبا الجحاف  konia
أبا الجراح  konia
أبا الجزل   konia
أبا الجعد   konia
أبا الجلاس  konia
أبا الجماهر konia
أبا الجنوب  konia
أبا الجنيد  konia
أبا الجهم   konia
أبا الجواب  konia
أبا الجودى  konia
أبا الجودي  konia
أبا الجوزاء konia
أبا الجويرية    konia
أبا الجويرية الصغير konia
أبا الجيش   konia
أبا الحارث  konia
أبا الحباب  konia
أبا الحجاج  konia
أبا الحجر   konia
أبا الحسام  konia
أبا الحسن   konia
أبا الحسناء konia
أبا الحسين  konia
أبا الحصن   konia
أبا الحصين  konia
أبا الحكم   konia
أبا الحمراء konia
أبا الحوارى konia
أبا الحواري konia
أبا الحوراء konia
أبا الحويرث konia
أبا الخصيب  konia
أبا الخطاب  konia
أبا الخليل  konia
أبا الخيار  konia
أبا الخير   konia
أبا الدرداء konia
أبا الدهماء konia
أبا الذيال  konia
أبا الربيع  konia
أبا الرحال  konia
أبا الرشيد  konia
أبا الرقاد  konia
أبا الرواع  konia
أبا الريان  konia
أبا الزاهرية    konia
أبا الزبير  konia
أبا الزرقاء konia
أبا الزعراء konia
أبا الزناد  konia
أبا الزنباع konia
أبا السائب  konia
أبا السباق  konia
أبا السرى   konia
أبا السري   konia
أبا السفاح  konia
أبا السفر   konia
أبا السقر   konia
أبا السكن   konia
أبا السكين  konia
أبا السلم   konia
أبا السليل  konia
أبا السمح   konia
أبا السمط   konia
أبا السنابل konia
أبا السوار  konia
أبا السوداء konia
أبا الشعثاء konia
أبا الشمال  konia
أبا الشموس  konia
أبا الصامت  konia
أبا الصباح  konia
أبا الصديق  konia
أبا الصعبة  konia
أبا الصفير  konia
أبا الصقر   konia
أبا الصلت   konia
أبا الصهباء konia
أبا الصواب  konia
أبا الضحاك  konia
أبا الضحى   konia
أبا الضحي   konia
أبا الطاهر  konia
أبا الطفيل  konia
أبا الطيب   konia
أبا العالية konia
أبا العباس  konia
أبا العبيد ين   konia
أبا العبيدين    konia
أبا العجفاء konia
أبا العجلان konia
أبا العجماء konia
أبا العدبس  konia
أبا العدبس الأصغر   konia
أبا العدبس الأكبر   konia
أبا العريان konia
أبا العشراء konia
أبا العلاء  konia
أبا العلانية    konia
أبا العلباء konia
أبا العميس  konia
أبا العنبر  konia
أبا العنبس  konia
أبا العوام  konia
أبا الغادية konia
أبا الغاز   konia
أبا الغريف  konia
أبا الغصن   konia
أبا الغوث   konia
أبا الغيث   konia
أبا الفتح   konia
أبا الفرات  konia
أبا الفرات البصرى   konia
أبا الفرات البصري   konia
أبا الفرج   konia
أبا الفرجل  konia
أبا الفضل   konia
‏أبا الفضيل konia
أبا الفيض   konia
أبا القاسم  konia
أبا القلوص  konia
أبا القموص  konia
أبا الكنود  konia
أبا الليث   konia
أبا المؤمر  konia
أبا المؤمن  konia
أبا المبارك konia
أبا المتوكل konia
أبا المثنى  konia
أبا المثني  konia
أبا المحياة konia
أبا المخارق konia
أبا المختار konia
أبا المساور konia
أبا المسور  konia
أبا المسيب  konia
أبا المصفى  konia
أبا المصفي  konia
أبا المضاء  konia
أبا المطرف  konia
أبا المطوس  konia
أبا المطوس هو يزيد  konia
أبا المعافى konia
أبا المعافي konia
أبا المعتمر konia
أبا المعلى  konia
أبا المعلي  konia
أبا المغراء konia
أبا المغلس  konia
أبا المغيرة konia
أبا المفضل  konia
أبا المقدام konia
أبا الملك   konia
أبا المليح  konia
أبا المنازل konia
أبا المنذر  konia
أبا المنقع  konia
أبا المنهال konia
أبا المنيب  konia
أبا المنير  konia
أبا المهاجر konia
أبا المهزم  konia
أبا المهلب  konia
أبا المهنا  konia
أبا المورع  konia
أبا النجاشى konia
أبا النجاشي konia
أبا النجم   konia
أبا النجيب  konia
أبا النضر   konia
أبا النعمان konia
أبا الهذيل  konia
أبا الهياج  konia
أبا الهيثم  konia
أبا الوازع  konia
أبا الوداك  konia
أبا الورد   konia
أبا الورقاء konia
أبا الوزير  konia
أبا الوسيم  konia
أبا الوضىء  konia
أبا الوليد  konia
أبا اليسر   konia
أبا اليسع   konia
أبا اليسير  konia
أبا اليقظان konia
أبا اليمان  konia
أبا اليمن   konia
أبا بجير    konia
أبا بحر konia
أبا بحرية   konia
أبا بدر konia
أبا بدل konia
أبا بردة    konia
أبا برزة    konia
أبا بريد    konia
أبا بسر konia
أبا بسرة    konia
أبا بسطام   konia
أبا بشر konia
أبا بشر ‎   konia
أبا بشير    konia
أبا بصرة    konia
أبا بصير    konia
أبا بكار    konia
أبا بكر konia
أبا بكرة    konia
أبا بكير    konia
أبا بلال    konia
أبا بلج konia
أبا بلج الصغير  konia
أبا بهيسة   konia
أبا تحيى    konia
أبا تحيي    konia
أبا تقى konia
أبا تقي konia
أبا تمام    konia
أبا تميلة   konia
أبا تميم    konia
أبا تميمة   konia
أبا توبة    konia
أبا ثابت    konia
أبا ثابت المدنى konia
أبا ثابت المدني konia
أبا ثرية    konia
أبا ثعلبة   konia
أبا ثفال    konia
أبا ثلجة    konia
أبا ثمامة   konia
أبا ثوبان   konia
أبا ثور konia
أبا جابر    konia
أبا جبر konia
أبا جبير    konia
أبا جبيرة   konia
أبا جحيفة   konia
أبا جرو konia
أبا جرى konia
أبا جري konia
أبا جزء konia
أبا جعفر    konia
أبا جعفر المؤذن konia
أبا جمرة    konia
أبا جمعة    konia
أبا جميع    konia
أبا جميلة   konia
أبا جناب    konia
أبا جنادة   konia
أبا جهضم    konia
أبا جهمة    konia
أبا جهيم    konia
أبا جوين    konia
أبا حاتم    konia
أبا حاجب    konia
أبا حاجر    konia
أبا حارثة   konia
أبا حازم    konia
أبا حاضر    konia
أبا حبة konia
أبا حبيب    konia
أبا حبيبة   konia
أبا حجر konia
أبا حجية    konia
أبا حجير    konia
أبا حدرد    konia
أبا حدير    konia
أبا حذافة   konia
أبا حذيفة   konia
أبا حرب konia
أبا حرة konia
أبا حرمل    konia
أبا حرملة   konia
أبا حريز    konia
أبا حزرة    konia
أبا حسان    konia
أبا حصين    konia
أبا حضير    konia
أبا حفص konia
أبا حفصة    konia
أبا حكيم    konia
أبا حلبس    konia
أبا حليمة   konia
أبا حماد    konia
أبا حمان    konia
أبا حمة konia
أبا حمدان   konia
أبا حمران   konia
أبا حمزة    konia
أبا حميد    konia
أبا حمير    konia
أبا حنظلة   konia
أبا حنيفة   konia
أبا حوالة   konia
أبا حومل    konia
أبا حى  konia
أبا حي  konia
أبا حيان    konia
أبا حية konia
أبا حيوة    konia
أبا حيويل   konia
أبا حيى konia
أبا حيي konia
أبا حيية    konia
أبا خارجة   konia
أبا خازم    konia
أبا خالد    konia
أبا خبيب    konia
أبا خثيمة   konia
أبا خداش    konia
أبا خديج    konia
أبا خراش    konia
أبا خربق    konia
أبا خريم    konia
أبا خزامة   konia
أبا خزيمة   konia
أبا خشينة   konia
أبا خفاف    konia
أبا خلاد    konia
أبا خلدة    konia
أبا خلف konia
أبا خلف الأعمى  konia
أبا خلف الأعمي  konia
أبا خليد    konia
أبا خليفة   konia
أبا خنيس    konia
أبا خيثمة   konia
أبا داود    konia
أبا دثار    konia
أبا دحية    konia
أبا دسمة    konia
أبا دغفل    konia
أبا دلان    konia
أبا دلف konia
أبا دوس konia
أبا ذبيان   konia
أبا ذر  konia
أبا ذراع    konia
أبا ذرامة   konia
أبا رئاب    konia
أبا راشد    konia
أبا رافع    konia
أبا ربعى    konia
أبا ربعي    konia
أبا ربيعة   konia
أبا رجاء    konia
أبا رزيق    konia
أبا رزين    konia
أبا رشدين   konia
أبا رفاعة   konia
أبا رفيع    konia
أبا رقية    konia
أبا رمثة    konia
أبا رملة    konia
أبا رهم konia
أبا رواحة   konia
أبا روح konia
أبا روق konia
أبا رويحة   konia
أبا رويق    konia
أبا رويم    konia
أبا رياح    konia
أبا ريحانة  konia
أبا زائد    konia
أبا زائدة   konia
أبا زايد    konia
أبا مطر konia
أبا مطرف    konia
أبا مطيع    konia
أبا معاذ    konia
أبا معان    konia
أبا معانق   konia
أبا معاوية  konia
أبا معبد    konia
أبا معدان   konia
أبا معشر    konia
‏أبا معفس   konia
أبا معقل    konia
أبا معمر    konia
أبا معن konia
أبا معن محمد    konia
أبا معيد    konia
أبا معيوف   konia
أبا مقاتل   konia
أبا مكرم    konia
أبا مكين    konia
أبا مليكة   konia
أبا منصور   konia
أبا منظور   konia
أبا منين    konia
أبا مهدى    konia
أبا مهدي    konia
أبا مهل konia
أبا مودود   konia
أبا مودود هو بحر    konia
أبا موسى    konia
أبا موسي    konia
أبا موسى هو علي konia
أبا مية konia
أبا ميسرة   konia
أبا ميمون   konia
أبا ميمونة  konia
أبا نافع    konia
أبا نباتة   konia
أبا نجيح    konia
أبا نجيد    konia
‏أبا نحيلة  konia
أبا نخيلة   konia
أبا نذير    konia
أبا نشيط    konia
أبا نصر konia
‏أبا نصير   konia
أبا نصيرة   konia
أبا نضرة    konia
أبا نضلة    konia
أبا نعامة   konia
أبا نعيم    konia
أبا نملة    konia
أبا نهار    konia
أبا نهيك    konia
أبا نوح konia
أبا نوفل    konia
أبا ه   konia
أبا هارون   konia
أبا هاشم    konia
أبا هانىء   konia
أبا هبيرة   konia
أبا هريرة   konia
أبا هشام    konia
أبا هلال    konia
أبا همام    konia
أبا هند konia
أبا هنيد    konia
أبا هنيدة   konia
أبا هود konia
أبا وائل    konia
أبا واثلة   konia
أبا واقد    konia
أبا وجزة    konia
أبا وحشية   konia
أبا وقاص    konia
أبا وكيع    konia
أبا وهب konia
أبا ياسر    konia
أبا يحمد    konia
أبا يحيى    konia
أبا يحيي    konia
أبا يربوع   konia
أبا يزيد    konia
أبا يسار    konia
أبا يعفور   konia
أبا يعقوب   konia
أبا يعلى    konia
أبا يعلي    konia
أبا يعيش    konia
أبا يوسف    konia
أبا يونس    konia
أبو إبراهيم konia
أبو أبى konia
أبو أبي konia
أبو أحمد    konia
أبو إدام    konia
أبو إدريس   konia
أبو أرطاة   konia
أبو أسامة   konia
أبو إسحاق   konia
أبو أسد konia
أبو إسرائيل konia
أبو أسماء   konia
أبو إسماعيل konia
أبو أسيد    konia
أبو أفلح    konia
أبو إلياس   konia
أبو أمامة   konia
أبو أمية    konia
أبو أمية المكى  konia
أبو أمية المكي  konia
أبو أميمة   konia
أبو أمين    konia
أبو أنس konia
أبو أنيس    konia
أبو أنيسة   konia
أبو أويس    konia
أبو إياس    konia
أبو أيمن    konia
أبو أيوب    konia
أبو اسامة   konia
أبو الأبرد  konia
أبو الأبيض  konia
أبو الأحوص  konia
أبو الأخيل  konia
أبو الأزهر  konia
أبو الأسباط konia
أبو الأسد   konia
أبو الأسقع  konia
أبو الأسود  konia
أبو الأشرس  konia
أبو الأشعث  konia
أبو الأشهب  konia
أبو الأصبغ  konia
أبو الأعور  konia
أبو الأعيس  konia
أبو الأغر   konia
أبو البخترى konia
أبو البختري konia
أبو البداح  konia
أبو البزرى  konia
أبو البزري  konia
أبو التجيب  konia
أبو التياح  konia
أبو الثورين konia
أبو الجارود konia
أبو الجارية konia
أبو الجحاف  konia
أبو الجراح  konia
أبو الجزل   konia
أبو الجعد   konia
أبو الجلاس  konia
أبو الجماهر konia
أبو الجنوب  konia
أبو الجنيد  konia
أبو الجهم   konia
أبو الجواب  konia
أبو الجودى  konia
أبو الجودي  konia
أبو الجوزاء konia
أبو الجويرية    konia
أبو الجويرية الصغير konia
أبو الجيش   konia
أبو الحارث  konia
أبو الحباب  konia
أبو الحجاج  konia
أبو الحجر   konia
أبو الحسام  konia
أبو الحسن   konia
أبو الحسناء konia
أبو الحسين  konia
أبو الحصن   konia
أبو الحصين  konia
أبو الحكم   konia
أبو الحمراء konia
أبو الحوارى konia
أبو الحواري konia
أبو الحوراء konia
أبو الحويرث konia
أبو الخصيب  konia
أبو الخطاب  konia
أبو الخليل  konia
أبو الخيار  konia
أبو الخير   konia
أبو الدرداء konia
أبو الدهماء konia
أبو الذيال  konia
أبو الربيع  konia
أبو الرحال  konia
أبو الرشيد  konia
أبو الرقاد  konia
أبو الرواع  konia
أبو الريان  konia
أبو الزاهرية    konia
أبو الزبير  konia
أبو الزرقاء konia
أبو الزعراء konia
أبو الزناد  konia
أبو الزنباع konia
أبو السائب  konia
أبو السباق  konia
أبو السرى   konia
أبو السري   konia
أبو السفاح  konia
أبو السفر   konia
أبو السقر   konia
أبو السكن   konia
أبو السكين  konia
أبو السلم   konia
أبو السليل  konia
أبو السمح   konia
أبو السمط   konia
أبو السنابل konia
أبو السوار  konia
أبو السوداء konia
أبو الشعثاء konia
أبو الشمال  konia
أبو الشموس  konia
أبو الصامت  konia
أبو الصباح  konia
أبو الصديق  konia
أبو الصعبة  konia
أبو الصفير  konia
أبو الصقر   konia
أبو الصلت   konia
أبو الصهباء konia
أبو الصواب  konia
أبو الضحاك  konia
أبو الضحى   konia
أبو الضحي   konia
أبو الطاهر  konia
أبو الطفيل  konia
أبو الطيب   konia
أبو العالية konia
أبو العباس  konia
أبو العبيد ين   konia
أبو العبيدين    konia
أبو العجفاء konia
أبو العجلان konia
أبو العجماء konia
أبو العدبس  konia
أبو العدبس الأصغر   konia
أبو العدبس الأكبر   konia
أبو العريان konia
أبو العشراء konia
أبو العلاء  konia
أبو العلانية    konia
أبو العلباء konia
أبو العميس  konia
أبو العنبر  konia
أبو العنبس  konia
أبو العوام  konia
أبو الغادية konia
أبو الغاز   konia
أبو الغريف  konia
أبو الغصن   konia
أبو الغوث   konia
أبو الغيث   konia
أبو الفتح   konia
أبو الفرات  konia
أبو الفرات البصرى   konia
أبو الفرات البصري   konia
أبو الفرج   konia
أبو الفرجل  konia
أبو الفضل   konia
‏أبو الفضيل konia
أبو الفيض   konia
أبو القاسم  konia
أبو القلوص  konia
أبو القموص  konia
أبو الكنود  konia
أبو الليث   konia
أبو المؤمر  konia
أبو المؤمن  konia
أبو المبارك konia
أبو المتوكل konia
أبو المثنى  konia
أبو المثني  konia
أبو المحياة konia
أبو المخارق konia
أبو المختار konia
أبو المساور konia
أبو المسور  konia
أبو المسيب  konia
أبو المصفى  konia
أبو المصفي  konia
أبو المضاء  konia
أبو المطرف  konia
أبو المطوس  konia
أبو المطوس هو يزيد  konia
أبو المعافى konia
أبو المعافي konia
أبو المعتمر konia
أبو المعلى  konia
أبو المعلي  konia
أبو المغراء konia
أبو المغلس  konia
أبو المغيرة konia
أبو المفضل  konia
أبو المقدام konia
أبو الملك   konia
أبو المليح  konia
أبو المنازل konia
أبو المنذر  konia
أبو المنقع  konia
أبو المنهال konia
أبو المنيب  konia
أبو المنير  konia
أبو المهاجر konia
أبو المهزم  konia
أبو المهلب  konia
أبو المهنا  konia
أبو المورع  konia
أبو النجاشى konia
أبو النجاشي konia
أبو النجم   konia
أبو النجيب  konia
أبو النضر   konia
أبو النعمان konia
أبو الهذيل  konia
أبو الهياج  konia
أبو الهيثم  konia
أبو الوازع  konia
أبو الوداك  konia
أبو الورد   konia
أبو الورقاء konia
أبو الوزير  konia
أبو الوسيم  konia
أبو الوضىء  konia
أبو الوليد  konia
أبو اليسر   konia
أبو اليسع   konia
أبو اليسير  konia
أبو اليقظان konia
أبو اليمان  konia
أبو اليمن   konia
أبو بجير    konia
أبو بحر konia
أبو بحرية   konia
أبو بدر konia
أبو بدل konia
أبو بردة    konia
أبو برزة    konia
أبو بريد    konia
أبو بسر konia
أبو بسرة    konia
أبو بسطام   konia
أبو بشر konia
أبو بشر ‎   konia
أبو بشير    konia
أبو بصرة    konia
أبو بصير    konia
أبو بكار    konia
أبو بكر konia
أبو بكرة    konia
أبو بكير    konia
أبو بلال    konia
أبو بلج konia
أبو بلج الصغير  konia
أبو بهيسة   konia
أبو تحيى    konia
أبو تحيي    konia
أبو تقى konia
أبو تقي konia
أبو تمام    konia
أبو تميلة   konia
أبو تميم    konia
أبو تميمة   konia
أبو توبة    konia
أبو ثابت    konia
أبو ثابت المدنى konia
أبو ثابت المدني konia
أبو ثرية    konia
أبو ثعلبة   konia
أبو ثفال    konia
أبو ثلجة    konia
أبو ثمامة   konia
أبو ثوبان   konia
أبو ثور konia
أبو جابر    konia
أبو جبر konia
أبو جبير    konia
أبو جبيرة   konia
أبو جحيفة   konia
أبو جرو konia
أبو جرى konia
أبو جري konia
أبو جزء konia
أبو جعفر    konia
أبو جعفر المؤذن konia
أبو جمرة    konia
أبو جمعة    konia
أبو جميع    konia
أبو جميلة   konia
أبو جناب    konia
أبو جنادة   konia
أبو جهضم    konia
أبو جهمة    konia
أبو جهيم    konia
أبو جوين    konia
أبو حاتم    konia
أبو حاجب    konia
أبو حاجر    konia
أبو حارثة   konia
أبو حازم    konia
أبو حاضر    konia
أبو حبة konia
أبو حبيب    konia
أبو حبيبة   konia
أبو حجر konia
أبو حجية    konia
أبو حجير    konia
أبو حدرد    konia
أبو حدير    konia
أبو حذافة   konia
أبو حذيفة   konia
أبو حرب konia
أبو حرة konia
أبو حرمل    konia
أبو حرملة   konia
أبو حريز    konia
أبو حزرة    konia
أبو حسان    konia
أبو حصين    konia
أبو حضير    konia
أبو حفص konia
أبو حفصة    konia
أبو حكيم    konia
أبو حلبس    konia
أبو حليمة   konia
أبو حماد    konia
أبو حمان    konia
أبو حمة konia
أبو حمدان   konia
أبو حمران   konia
أبو حمزة    konia
أبو حميد    konia
أبو حمير    konia
أبو حنظلة   konia
أبو حنيفة   konia
أبو حوالة   konia
أبو حومل    konia
أبو حى  konia
أبو حي  konia
أبو حيان    konia
أبو حية konia
أبو حيوة    konia
أبو حيويل   konia
أبو حيى konia
أبو حيي konia
أبو حيية    konia
أبو خارجة   konia
أبو خازم    konia
أبو خالد    konia
أبو خبيب    konia
أبو خثيمة   konia
أبو خداش    konia
أبو خديج    konia
أبو خراش    konia
أبو خربق    konia
أبو خريم    konia
أبو خزامة   konia
أبو خزيمة   konia
أبو خشينة   konia
أبو خفاف    konia
أبو خلاد    konia
أبو خلدة    konia
أبو خلف konia
أبو خلف الأعمى  konia
أبو خلف الأعمي  konia
أبو خليد    konia
أبو خليفة   konia
أبو خنيس    konia
أبو خيثمة   konia
أبو داود    konia
أبو دثار    konia
أبو دحية    konia
أبو دسمة    konia
أبو دغفل    konia
أبو دلان    konia
أبو دلف konia
أبو دوس konia
أبو ذبيان   konia
أبو ذر  konia
أبو ذراع    konia
أبو ذرامة   konia
أبو رئاب    konia
أبو راشد    konia
أبو رافع    konia
أبو ربعى    konia
أبو ربعي    konia
أبو ربيعة   konia
أبو رجاء    konia
أبو رزيق    konia
أبو رزين    konia
أبو رشدين   konia
أبو رفاعة   konia
أبو رفيع    konia
أبو رقية    konia
أبو رمثة    konia
أبو رملة    konia
أبو رهم konia
أبو رواحة   konia
أبو روح konia
أبو روق konia
أبو رويحة   konia
أبو رويق    konia
أبو رويم    konia
أبو رياح    konia
أبو ريحانة  konia
أبو زائد    konia
أبو زائدة   konia
أبو زايد    konia
أبو زبر konia
أبو زبيد    konia
أبو زحارة   konia
أبو زرارة   konia
أبو زرعة    konia
أبو زفر konia
أبو زكريا   konia
أبو زميل    konia
أبو زهرة    konia
أبو زهير    konia
أبو زياد    konia
أبو زيادة   konia
أبو زيد konia
أبو زينب    konia
أبو زينب الحجازى    konia
أبو زينب الحجازي    konia
أبو ساج konia
أبو ساسان   konia
أبو سالم    konia
أبو سبأ konia
أبو سبرة    konia
أبو سحيم    konia
أبو سخيلة   konia
أبو سروعة   konia
أبو سريحة   konia
أبو سريرة   konia
أبو سعاد    konia
أبو سعد konia
أبو سعدة    konia
أبو سعيد    konia
أبو سعيد الخير  konia
أبو سعيد المؤدب konia
أبو سفيان   konia
أبو سكينة   konia
أبو سلام    konia
أبو سلامة   konia
أبو سلمان   konia
أبو سلمان المؤذن    konia
أبو سلمة    konia
أبو سلمى    konia
أبو سلمي    konia
أبو سليم    konia
أبو سليمان  konia
أبو سماك    konia
أبو سمية    konia
أبو سنان    konia
أبو سهل konia
أبو سهلة    konia
أبو سهيل    konia
أبو سورة    konia
أبو سوية    konia
أبو سويد    konia
أبو سويرة   konia
أبو سيارة   konia
أبو سيدان   konia
أبو سيف konia
أبو شاكر    konia
أبو شبرمة   konia
أبو شبل konia
أبو شجاع    konia
أبو شجرة    konia
أبو شرحبيل  konia
أبو شريح    konia
أبو شريك    konia
أبو شعبة    konia
أبو شعيب    konia
أبو شمر konia
أبو شهاب    konia
أبو شهر konia
أبو شهم konia
أبو شهيد    konia
أبو شيبان   konia
أبو شيبة    konia
أبو شيخ konia
أبو صادق    konia
أبو صالح    konia
أبو صخر konia
أبو صخرة    konia
أبو صدقة    konia
أبو صرمة    konia
أبو صعير    konia
أبو صفوان   konia
أبو صيفى    konia
أبو صيفي    konia
أبو ضمرة    konia
أبو طارق    konia
أبو طالب    konia
أبو طالوت   konia
أبو طاهر    konia
أبو طريف    konia
أبو طعمة    konia
أبو طلحة    konia
أبو طوالة   konia
أبو طيبة    konia
أبو ظبيان   konia
أبو ظبية    konia
أبو ظفر konia
أبو ظلال    konia
أبو عائذ    konia
أبو عائذ الله   konia
أبو عائشة   konia
أبو عاتكة   konia
أبو عازب    konia
أبو عاصم    konia
أبو عامر    konia
أبو عباد    konia
أبو عبادة   konia
أبو عبد الجبار  konia
أبو عبد الحمن   konia
أبو عبد الحميد  konia
أبو عبد الدائم  konia
أبو عبد الرحمن  konia
أبو عبد الرحمن ‎    konia
أبو عبد الرحيم  konia
أبو عبد السلام  konia
أبو عبد الصمد   konia
أبو عبد العزيز  konia
أبو عبد القدوس  konia
أبو عبد الكريم  konia
أبو عبد الله    konia
أبو عبد الله الجهنى konia
أبو عبد الله الجهني konia
أبو عبد الله الخياط konia
أبو عبد الله الضرير konia
أبو عبد الله المؤدب المكتب  konia
أبو عبد الله المؤذن konia
أبو عبد الملك   konia
أبو عبد رب  konia
أبو عبد رب العزة    konia
أبو عبد ربه konia
أبو عبدالرحمن   konia
أبو عبدة    konia
أبو عبس konia
أبو عبيد    konia
أبو عبيد الله   konia
أبو عبيدة   konia
أبو عتاب    konia
أبو عتبة    konia
أبو عتيق    konia
أبو عتيك    konia
أبو عثمان   konia
أبو عثيم    konia
أبو عدى konia
أبو عدي konia
أبو عذرة    konia
أبو عرفة    konia
أبو عروبة   konia
أبو عروة    konia
أبو عزة konia
أبو عشانة   konia
أبو عصام    konia
أبو عصمة    konia
أبو عصيدة   konia
أبو عطاء    konia
أبو عطية    konia
أبو عفان    konia
أبو عقال    konia
أبو عقبة    konia
أبو عقرب    konia
أبو عقيل    konia
أبو عكاشة   konia
أبو عكرمة   konia
أبو علقمة   konia
أبو علوان   konia
أبو علويه   konia
أبو علي konia
أبو عمار    konia
أبو عمارة   konia
أبو عمر konia
‏أبو عمران  konia
أبو عمرة    konia
أبو عمرو    konia
أبو عمير    konia
أبو عميرة   konia
أبو عميس    konia
أبو عنبة    konia
أبو عنبسة   konia
أبو عوانة   konia
أبو عوف konia
أبو عون konia
أبو عياش    konia
أبو عياض    konia
أبو عيسى    konia
أبو عيسي    konia
أبو غالب    konia
أبو غانم    konia
أبو غرارة   konia
أبو غزوان   konia
أبو غسان    konia
أبو غطفان   konia
أبو غطيف    konia
أبو غفار    konia
أبو غلاب    konia
أبو غلباء   konia
أبو غياث    konia
أبو فاختة   konia
أبو فاطمة   konia
أبو فراس    konia
أبو فروة    konia
أبو فروة الأصغر konia
أبو فزارة   konia
أبو فضالة   konia
أبو قابوس   konia
أبو قبيصة   konia
أبو قبيل    konia
أبو قتادة   konia
أبو قتيبة   konia
أبو قتيلة   konia
أبو قدامة   konia
أبو قديد    konia
أبو قرة konia
أبو قرصافة  konia
أبو قريش    konia
أبو قزعة    konia
أبو قضاعة   konia
أبو قطن konia
أبو قلابة   konia
أبو قنان    konia
أبو قيس konia
أبو كامل    konia
أبو كاهل    konia
أبو كباش    konia
أبو كبشة    konia
أبو كبشة البراء konia
أبو كثير    konia
أبو كدينة   konia
أبو كرب konia
أبو كردوس   konia
أبو كرز konia
أبو كريب    konia
أبو كريمة   konia
أبو كعب konia
أبو كلثم    konia
أبو كليب    konia
أبو كنانة   konia
أبو لاس konia
أبو لبابة   konia
أبو لبيد    konia
أبو لقمان   konia
أبو لوط konia
أبو ليث konia
أبو ليلى    konia
أبو ليلي    konia
أبو ماجد    konia
أبو ماجدة   konia
أبو مالك    konia
أبو مجاهد   konia
أبو مجلز    konia
أبو محذورة  konia
أبو محرر    konia
أبو محرز    konia
أبو محصن    konia
أبو محلم    konia
أبو محمد    konia
أبو محمود   konia
أبو محيريز  konia
أبو مخارق   konia
أبو مخاشن   konia
أبو مخلد    konia
أبو مدرك    konia
أبو مدلة    konia
أبو مرازم   konia
أبو مراوح   konia
أبو مرة konia
أبو مرثد    konia
أبو مرحب    konia
أبو مرحوم   konia
أبو مرزوق   konia
أبو مروان   konia
أبو مريم    konia
أبو مزاحم   konia
أبو مزرد    konia
أبو مساحق   konia
أبو مسافر   konia
أبو مسعود   konia
أبو مسقبة   konia
أبو مسكين   konia
أبو مسلم    konia
أبو مسلمة   konia
أبو مسهر    konia
أبو مشجعة   konia
أبو مصبح    konia
أبو مصعب    konia
أبو مصلح    konia
أبو مضر konia
أبو مطر konia
أبو مطرف    konia
أبو مطيع    konia
أبو معاذ    konia
أبو معان    konia
أبو معانق   konia
أبو معاوية  konia
أبو معبد    konia
أبو معدان   konia
أبو معشر    konia
أبو معفس    konia
أبو معقل    konia
أبو معمر    konia
أبو معن konia
أبو معن محمد    konia
أبو معيد    konia
أبو معيوف   konia
أبو مقاتل   konia
أبو مكرم    konia
أبو مكين    konia
أبو مليكة   konia
أبو منصور   konia
أبو منظور   konia
أبو منين    konia
أبو مهدى    konia
أبو مهدي    konia
أبو مهر konia
أبو مهل konia
أبو مودود   konia
أبو مودود هو بحر    konia
أبو موسى    konia
أبو موسي    konia
أبو موسى هو علي konia
أبو مية konia
أبو ميسرة   konia
أبو ميمون   konia
أبو ميمونة  konia
أبو نافع    konia
أبو نباتة   konia
أبو نجيح    konia
أبو نجيد    konia
‏أبو نحيلة  konia
أبو نخيلة   konia
أبو نذير    konia
أبو نشيط    konia
أبو نصر konia
‏أبو نصير   konia
أبو نصيرة   konia
أبو نضرة    konia
أبو نضلة    konia
أبو نعامة   konia
أبو نعيم    konia
أبو نملة    konia
أبو نهار    konia
أبو نهيك    konia
أبو نوح konia
أبو نوفل    konia
أبو ه   konia
أبو هارون   konia
أبو هاشم    konia
أبو هانىء   konia
أبو هبيرة   konia
أبو هريرة   konia
أبو هشام    konia
أبو هلال    konia
أبو همام    konia
أبو هند konia
أبو هنيد    konia
أبو هنيدة   konia
أبو هود konia
أبو وائل    konia
أبو واثلة   konia
أبو واقد    konia
أبو وجزة    konia
أبو وحشية   konia
أبو وقاص    konia
أبو وكيع    konia
أبو وهب konia
أبو ياسر    konia
أبو يحمد    konia
أبو يحيى    konia
أبو يحيي    konia
أبو يربوع   konia
أبو يزيد    konia
أبو يسار    konia
أبو يعفور   konia
أبو يعقوب   konia
أبو يعلى    konia
أبو يعلي    konia
أبو يعيش    konia
أبو يوسف    konia
أبو يونس    konia
أبوعبد ربه  konia
أبى إبراهيم konia
أبي إبراهيم konia
أبى أبى konia
أبى أبي konia
أبي أبى konia
أبي أبي konia
أبى أحمد    konia
أبي أحمد    konia
أبى إدام    konia
أبي إدام    konia
أبى إدريس   konia
أبي إدريس   konia
أبى أرطاة   konia
أبي أرطاة   konia
أبى أسامة   konia
أبي أسامة   konia
أبى إسحاق   konia
أبي إسحاق   konia
أبى أسد konia
أبي أسد konia
أبى إسرائيل konia
أبي إسرائيل konia
أبى أسماء   konia
أبي أسماء   konia
أبى إسماعيل konia
أبي إسماعيل konia
أبى أسيد    konia
أبي أسيد    konia
أبى أفلح    konia
أبي أفلح    konia
أبى إلياس   konia
أبي إلياس   konia
أبى أمامة   konia
أبي أمامة   konia
أبى أمية    konia
أبي أمية    konia
أبى أمية المكى  konia
أبى أمية المكي  konia
أبي أمية المكى  konia
أبي أمية المكي  konia
أبى أميمة   konia
أبي أميمة   konia
أبى أمين    konia
أبي أمين    konia
أبى أنس konia
أبي أنس konia
أبى أنيس    konia
أبي أنيس    konia
أبى أنيسة   konia
أبي أنيسة   konia
أبى أويس    konia
أبي أويس    konia
أبى إياس    konia
أبي إياس    konia
أبى أيمن    konia
أبي أيمن    konia
أبى أيوب    konia
أبي أيوب    konia
أبى الأبرد  konia
أبي الأبرد  konia
أبى الأبيض  konia
أبي الأبيض  konia
أبى الأحوص  konia
أبي الأحوص  konia
أبى الأخيل  konia
أبي الأخيل  konia
أبى الأزهر  konia
أبي الأزهر  konia
أبى الأسباط konia
أبي الأسباط konia
أبى الأسد   konia
أبي الأسد   konia
أبى الأسقع  konia
أبي الأسقع  konia
أبى الأسود  konia
أبي الأسود  konia
أبى الأشرس  konia
أبي الأشرس  konia
أبى الأشعث  konia
أبي الأشعث  konia
أبى الأشهب  konia
أبي الأشهب  konia
أبى الأصبغ  konia
أبي الأصبغ  konia
أبى الأعور  konia
أبي الأعور  konia
أبى الأعيس  konia
أبي الأعيس  konia
أبى الأغر   konia
أبي الأغر   konia
أبى البخترى konia
أبى البختري konia
أبي البخترى konia
أبي البختري konia
أبى البداح  konia
أبي البداح  konia
أبى البزرى  konia
أبى البزري  konia
أبي البزرى  konia
أبي البزري  konia
أبى التجيب  konia
أبي التجيب  konia
أبى التياح  konia
أبي التياح  konia
أبى الثورين konia
أبي الثورين konia
أبى الجارود konia
أبي الجارود konia
أبى الجارية konia
أبي الجارية konia
أبى الجحاف  konia
أبي الجحاف  konia
أبى الجراح  konia
أبي الجراح  konia
أبى الجزل   konia
أبي الجزل   konia
أبى الجعد   konia
أبي الجعد   konia
أبى الجلاس  konia
أبي الجلاس  konia
أبى الجماهر konia
أبي الجماهر konia
أبى الجنوب  konia
أبي الجنوب  konia
أبى الجنيد  konia
أبي الجنيد  konia
أبى الجهم   konia
أبي الجهم   konia
أبى الجواب  konia
أبي الجواب  konia
أبى الجودى  konia
أبى الجودي  konia
أبي الجودى  konia
أبي الجودي  konia
أبى الجوزاء konia
أبي الجوزاء konia
أبي الجون   konia
أبى الجويرية    konia
أبي الجويرية    konia
أبى الجويرية الصغير konia
أبي الجويرية الصغير konia
أبى الجيش   konia
أبي الجيش   konia
أبى الحارث  konia
أبي الحارث  konia
أبى الحباب  konia
أبي الحباب  konia
أبى الحجاج  konia
أبي الحجاج  konia
أبى الحجر   konia
أبي الحجر   konia
أبى الحسام  konia
أبي الحسام  konia
أبى الحسن   konia
أبي الحسن   konia
أبى الحسناء konia
أبي الحسناء konia
أبى الحسين  konia
أبي الحسين  konia
أبى الحصن   konia
أبي الحصن   konia
أبى الحصين  konia
أبي الحصين  konia
أبى الحكم   konia
أبي الحكم   konia
أبى الحمراء konia
أبي الحمراء konia
أبى الحوارى konia
أبى الحواري konia
أبي الحوارى konia
أبي الحواري konia
أبى الحوراء konia
أبي الحوراء konia
أبي الحوص   konia
أبى الحويرث konia
أبي الحويرث konia
أبى الخصيب  konia
أبي الخصيب  konia
أبى الخطاب  konia
أبي الخطاب  konia
أبى الخليل  konia
أبي الخليل  konia
أبى الخيار  konia
أبي الخيار  konia
أبى الخير   konia
أبي الخير   konia
أبى الدرداء konia
أبي الدرداء konia
أبى الدهماء konia
أبي الدهماء konia
أبى الذيال  konia
أبي الذيال  konia
أبى الربيع  konia
أبي الربيع  konia
أبي الرجال  konia
أبى الرحال  konia
أبي الرحال  konia
أبى الرشيد  konia
أبي الرشيد  konia
أبى الرقاد  konia
أبي الرقاد  konia
أبى الرواع  konia
أبي الرواع  konia
أبى الريان  konia
أبي الريان  konia
أبى الزاهرية    konia
أبي الزاهرية    konia
أبى الزبير  konia
أبي الزبير  konia
أبى الزرقاء konia
أبي الزرقاء konia
أبى الزعراء konia
أبي الزعراء konia
أبى الزناد  konia
أبي الزناد  konia
أبى الزنباع konia
أبي الزنباع konia
أبى السائب  konia
أبي السائب  konia
أبى السباق  konia
أبي السباق  konia
أبى السرى   konia
أبى السري   konia
أبي السرى   konia
أبي السري   konia
أبى السفاح  konia
أبي السفاح  konia
أبى السفر   konia
أبي السفر   konia
أبى السقر   konia
أبي السقر   konia
أبى السكن   konia
أبي السكن   konia
أبى السكين  konia
أبي السكين  konia
أبى السلم   konia
أبي السلم   konia
أبى السليل  konia
أبي السليل  konia
أبى السمح   konia
أبي السمح   konia
أبى السمط   konia
أبي السمط   konia
أبى السنابل konia
أبي السنابل konia
أبى السوار  konia
أبي السوار  konia
أبى السوداء konia
أبي السوداء konia
أبى الشعثاء konia
أبي الشعثاء konia
أبى الشمال  konia
أبي الشمال  konia
أبى الشموس  konia
أبي الشموس  konia
أبى الصامت  konia
أبي الصامت  konia
أبى الصباح  konia
أبي الصباح  konia
أبى الصديق  konia
أبي الصديق  konia
أبى الصعبة  konia
أبي الصعبة  konia
أبى الصفير  konia
أبي الصفير  konia
أبى الصقر   konia
أبي الصقر   konia
أبى الصلت   konia
أبي الصلت   konia
أبى الصهباء konia
أبي الصهباء konia
أبى الصواب  konia
أبي الصواب  konia
أبى الضحاك  konia
أبي الضحاك  konia
أبى الضحى   konia
أبى الضحي   konia
أبي الضحى   konia
أبي الضحي   konia
أبى الطاهر  konia
أبي الطاهر  konia
أبى الطفيل  konia
أبي الطفيل  konia
أبى الطيب   konia
أبي الطيب   konia
أبي العاتكة konia
أبي العاص   konia
أبى العالية konia
أبي العالية konia
أبى العباس  konia
أبي العباس  konia
أبى العبيد ين   konia
أبي العبيد ين   konia
أبى العبيدين    konia
أبي العبيدين    konia
أبى العجفاء konia
أبي العجفاء konia
أبى العجلان konia
أبي العجلان konia
أبى العجماء konia
أبي العجماء konia
أبى العدبس  konia
أبي العدبس  konia
أبى العدبس الأصغر   konia
أبي العدبس الأصغر   konia
أبى العدبس الأكبر   konia
أبي العدبس الأكبر   konia
أبى العريان konia
أبي العريان konia
أبى العشراء konia
أبي العشراء konia
أبى العلاء  konia
أبي العلاء  konia
أبى العلانية    konia
أبي العلانية    konia
أبى العلباء konia
أبي العلباء konia
أبى العميس  konia
أبي العميس  konia
أبى العنبر  konia
أبي العنبر  konia
أبى العنبس  konia
أبي العنبس  konia
أبى العوام  konia
أبي العوام  konia
أبى الغادية konia
أبي الغادية konia
أبى الغاز   konia
أبي الغاز   konia
أبى الغريف  konia
أبي الغريف  konia
أبى الغصن   konia
أبي الغصن   konia
أبى الغوث   konia
أبي الغوث   konia
أبى الغيث   konia
أبي الغيث   konia
أبى الفتح   konia
أبي الفتح   konia
أبى الفرات  konia
أبي الفرات  konia
أبى الفرات البصرى   konia
أبى الفرات البصري   konia
أبي الفرات البصرى   konia
أبي الفرات البصري   konia
أبى الفرج   konia
أبي الفرج   konia
أبى الفرجل  konia
أبي الفرجل  konia
أبى الفضل   konia
أبي الفضل   konia
أبى الفضيل  konia
أبي الفضيل  konia
أبى الفيض   konia
أبي الفيض   konia
أبى القاسم  konia
أبي القاسم  konia
أبى القلوص  konia
أبي القلوص  konia
أبى القموص  konia
أبي القموص  konia
أبى الكنود  konia
أبي الكنود  konia
أبى الليث   konia
أبي الليث   konia
أبى المؤمر  konia
أبي المؤمر  konia
أبى المؤمن  konia
أبي المؤمن  konia
أبى المبارك konia
أبي المبارك konia
أبى المتوكل konia
أبي المتوكل konia
أبى المثنى  konia
أبى المثني  konia
أبي المثنى  konia
أبي المثني  konia
أبى المحياة konia
أبي المحياة konia
أبى المخارق konia
أبي المخارق konia
أبى المختار konia
أبي المختار konia
أبى المساور konia
أبي المساور konia
أبى المسور  konia
أبي المسور  konia
أبى المسيب  konia
أبي المسيب  konia
أبى المصفى  konia
أبى المصفي  konia
أبي المصفى  konia
أبي المصفي  konia
أبى المضاء  konia
أبي المضاء  konia
أبى المطرف  konia
أبي المطرف  konia
أبى المطوس  konia
أبي المطوس  konia
أبى المطوس هو يزيد  konia
أبي المطوس هو يزيد  konia
أبى المعافى konia
أبى المعافي konia
أبي المعافى konia
أبي المعافي konia
أبى المعتمر konia
أبي المعتمر konia
أبى المعلى  konia
أبى المعلي  konia
أبي المعلى  konia
أبي المعلي  konia
أبى المغراء konia
أبي المغراء konia
أبى المغلس  konia
أبي المغلس  konia
أبى المغيرة konia
أبي المغيرة konia
أبى المفضل  konia
أبي المفضل  konia
أبى المقدام konia
أبي المقدام konia
أبى الملك   konia
أبي الملك   konia
أبى المليح  konia
أبي المليح  konia
أبى المنازل konia
أبي المنازل konia
أبى المنذر  konia
أبي المنذر  konia
أبى المنقع  konia
أبي المنقع  konia
أبى المنهال konia
أبي المنهال konia
أبى المنيب  konia
أبي المنيب  konia
أبى المنير  konia
أبي المنير  konia
أبى المهاجر konia
أبي المهاجر konia
أبى المهزم  konia
أبي المهزم  konia
أبى المهلب  konia
أبي المهلب  konia
أبى المهنا  konia
أبي المهنا  konia
أبى المورع  konia
أبي المورع  konia
أبى النجاشى konia
أبى النجاشي konia
أبي النجاشى konia
أبي النجاشي konia
أبى النجم   konia
أبي النجم   konia
أبى النجيب  konia
أبي النجيب  konia
أبى النضر   konia
أبي النضر   konia
أبى النعمان konia
أبي النعمان konia
أبى الهذيل  konia
أبي الهذيل  konia
أبى الهياج  konia
أبي الهياج  konia
أبى الهيثم  konia
أبي الهيثم  konia
أبى الوازع  konia
أبي الوازع  konia
أبى الوداك  konia
أبي الوداك  konia
أبى الورد   konia
أبي الورد   konia
أبى الورقاء konia
أبي الورقاء konia
أبى الوزير  konia
أبي الوزير  konia
أبى الوسيم  konia
أبي الوسيم  konia
أبى الوضىء  konia
أبي الوضىء  konia
أبى الوليد  konia
أبي الوليد  konia
أبى اليسر   konia
أبي اليسر   konia
أبى اليسع   konia
أبي اليسع   konia
أبى اليسير  konia
أبي اليسير  konia
أبى اليقظان konia
أبي اليقظان konia
أبى اليمان  konia
أبي اليمان  konia
أبى اليمن   konia
أبي اليمن   konia
أبى بجير    konia
أبي بجير    konia
أبى بحر konia
أبي بحر konia
أبى بحرية   konia
أبي بحرية   konia
أبى بدر konia
أبي بدر konia
أبى بدل konia
أبي بدل konia
أبى بردة    konia
أبي بردة    konia
أبى برزة    konia
أبي برزة    konia
أبى بريد    konia
أبي بريد    konia
أبى بسر konia
أبي بسر konia
أبى بسرة    konia
أبي بسرة    konia
أبى بسطام   konia
أبي بسطام   konia
أبى بشر konia
أبي بشر konia
أبى بشر ‎   konia
أبي بشر ‎   konia
أبى بشير    konia
أبي بشير    konia
أبى بصرة    konia
أبي بصرة    konia
أبى بصير    konia
أبي بصير    konia
أبى بكار    konia
أبي بكار    konia
أبى بكر konia
أبي بكر konia
أبى بكرة    konia
أبي بكرة    konia
أبى بكير    konia
أبي بكير    konia
أبى بلال    konia
أبي بلال    konia
أبى بلج konia
أبي بلج konia
أبى بلج الصغير  konia
أبي بلج الصغير  konia
أبى بهيسة   konia
أبي بهيسة   konia
أبى تحيى    konia
أبى تحيي    konia
أبي تحيى    konia
أبي تحيي    konia
أبى تقى konia
أبى تقي konia
أبي تقى konia
أبي تقي konia
أبى تمام    konia
أبي تمام    konia
أبى تميلة   konia
أبي تميلة   konia
أبى تميم    konia
أبي تميم    konia
أبى تميمة   konia
أبي تميمة   konia
أبى توبة    konia
أبي توبة    konia
أبى ثابت    konia
أبي ثابت    konia
أبى ثابت المدنى konia
أبى ثابت المدني konia
أبي ثابت المدنى konia
أبي ثابت المدني konia
أبى ثرية    konia
أبي ثرية    konia
أبى ثعلبة   konia
أبي ثعلبة   konia
أبى ثفال    konia
أبي ثفال    konia
أبى ثلجة    konia
أبي ثلجة    konia
أبى ثمامة   konia
أبي ثمامة   konia
أبى ثوبان   konia
أبي ثوبان   konia
أبى ثور konia
أبي ثور konia
أبى جابر    konia
أبي جابر    konia
أبى جبر konia
أبي جبر konia
أبى جبير    konia
أبي جبير    konia
أبى جبيرة   konia
أبي جبيرة   konia
أبى جحيفة   konia
أبي جحيفة   konia
أبى جرو konia
أبي جرو konia
أبى جرى konia
أبى جري konia
أبي جرى konia
أبي جري konia
أبى جزء konia
أبي جزء konia
أبى جعفر    konia
أبي جعفر    konia
أبى جعفر المؤذن konia
أبي جعفر المؤذن konia
أبى جمرة    konia
أبي جمرة    konia
أبى جمعة    konia
أبي جمعة    konia
أبى جميع    konia
أبي جميع    konia
أبى جميلة   konia
أبي جميلة   konia
أبى جناب    konia
أبي جناب    konia
أبى جنادة   konia
أبي جنادة   konia
أبى جهضم    konia
أبي جهضم    konia
أبى جهمة    konia
أبي جهمة    konia
أبى جهيم    konia
أبي جهيم    konia
أبى جوين    konia
أبي جوين    konia
أبى حاتم    konia
أبي حاتم    konia
أبى حاجب    konia
أبي حاجب    konia
أبى حاجر    konia
أبي حاجر    konia
أبى حارثة   konia
أبي حارثة   konia
أبى حازم    konia
أبي حازم    konia
أبى حاضر    konia
أبي حاضر    konia
أبى حبة konia
أبي حبة konia
أبى حبيب    konia
أبي حبيب    konia
أبى حبيبة   konia
أبي حبيبة   konia
أبى حثمة    konia
أبي حثمة    konia
أبى حجر konia
أبي حجر konia
أبى حجية    konia
أبي حجية    konia
أبى حجير    konia
أبي حجير    konia
أبى حدرد    konia
أبي حدرد    konia
أبى حدير    konia
أبي حدير    konia
أبى حذافة   konia
أبي حذافة   konia
أبى حذيفة   konia
أبي حذيفة   konia
أبى حرب konia
أبي حرب konia
أبى حرة konia
أبي حرة konia
أبى حرمل    konia
أبي حرمل    konia
أبى حرملة   konia
أبي حرملة   konia
أبى حريز    konia
أبي حريز    konia
أبى حزرة    konia
أبي حزرة    konia
أبى حسان    konia
أبي حسان    konia
أبي حسين    konia
أبى حصين    konia
أبي حصين    konia
أبى حضير    konia
أبي حضير    konia
أبى حفص konia
أبي حفص konia
أبى حفصة    konia
أبي حفصة    konia
أبى حكيم    konia
أبي حكيم    konia
أبى حلبس    konia
أبي حلبس    konia
أبى حليمة   konia
أبي حليمة   konia
أبى حماد    konia
أبي حماد    konia
أبى حمان    konia
أبي حمان    konia
أبى حمة konia
أبي حمة konia
أبى حمدان   konia
أبي حمدان   konia
أبى حمران   konia
أبي حمران   konia
أبى حمزة    konia
أبي حمزة    konia
أبى حميد    konia
أبي حميد    konia
أبى حمير    konia
أبي حمير    konia
أبى حنظلة   konia
أبي حنظلة   konia
أبى حنيفة   konia
أبي حنيفة   konia
أبى حوالة   konia
أبي حوالة   konia
أبى حومل    konia
أبي حومل    konia
أبى حى  konia
أبى حي  konia
أبي حى  konia
أبي حي  konia
أبى حيان    konia
أبي حيان    konia
أبى حية konia
أبي حية konia
أبى حيوة    konia
أبي حيوة    konia
أبى حيويل   konia
أبي حيويل   konia
أبى حيى konia
أبى حيي konia
أبي حيى konia
أبي حيي konia
أبى حيية    konia
أبي حيية    konia
أبى خارجة   konia
أبي خارجة   konia
أبى خازم    konia
أبي خازم    konia
أبى خالد    konia
أبي خالد    konia
أبى خبيب    konia
أبي خبيب    konia
أبى خثيمة   konia
أبي خثيمة   konia
أبى خداش    konia
أبي خداش    konia
أبى خديج    konia
أبي خديج    konia
أبى خراش    konia
أبي خراش    konia
أبى خربق    konia
أبي خربق    konia
أبى خريم    konia
أبي خريم    konia
أبى خزامة   konia
أبي خزامة   konia
أبى خزيمة   konia
أبي خزيمة   konia
أبى خشينة   konia
أبي خشينة   konia
أبى خفاف    konia
أبي خفاف    konia
أبى خلاد    konia
أبي خلاد    konia
أبى خلدة    konia
أبي خلدة    konia
أبى خلف konia
أبي خلف konia
أبى خلف الأعمى  konia
أبى خلف الأعمي  konia
أبي خلف الأعمى  konia
أبي خلف الأعمي  konia
أبى خليد    konia
أبي خليد    konia
أبى خليفة   konia
أبي خليفة   konia
أبى خنيس    konia
أبي خنيس    konia
أبى خيثمة   konia
أبي خيثمة   konia
أبى داود    konia
أبي داود    konia
أبى دثار    konia
أبي دثار    konia
أبى دحية    konia
أبي دحية    konia
أبى دسمة    konia
أبي دسمة    konia
أبى دغفل    konia
أبي دغفل    konia
أبى دلان    konia
أبي دلان    konia
أبى دلف konia
أبي دلف konia
أبى دوس konia
أبي دوس konia
أبى ذبيان   konia
أبي ذبيان   konia
أبى ذر  konia
أبي ذر  konia
أبى ذراع    konia
أبي ذراع    konia
أبى ذرامة   konia
أبي ذرامة   konia
أبى رئاب    konia
أبي رئاب    konia
أبى راشد    konia
أبي راشد    konia
أبى رافع    konia
أبي رافع    konia
أبي رباح    konia
أبى ربعى    konia
أبى ربعي    konia
أبي ربعى    konia
أبي ربعي    konia
أبى ربيعة   konia
أبي ربيعة   konia
أبى رجاء    konia
أبي رجاء    konia
أبى رزيق    konia
أبي رزيق    konia
أبى رزين    konia
أبي رزين    konia
أبى رشدين   konia
أبي رشدين   konia
أبى رفاعة   konia
أبي رفاعة   konia
أبى رفيع    konia
أبي رفيع    konia
أبى رقية    konia
أبي رقية    konia
أبى رمثة    konia
أبي رمثة    konia
أبى رملة    konia
أبي رملة    konia
أبى رهم konia
أبي رهم konia
أبى رواحة   konia
أبي رواحة   konia
أبي رواد    konia
أبى روح konia
أبي روح konia
أبى روق konia
أبي روق konia
أبى رويحة   konia
أبي رويحة   konia
أبى رويق    konia
أبي رويق    konia
أبى رويم    konia
أبي رويم    konia
أبى رياح    konia
أبي رياح    konia
أبى ريحانة  konia
أبي ريحانة  konia
أبى زائد    konia
أبي زائد    konia
أبى زائدة   konia
أبي زائدة   konia
أبى زايد    konia
أبي زايد    konia
أبى زبر konia
أبي زبر konia
أبى زبيد    konia
أبي زبيد    konia
أبى زحارة   konia
أبي زحارة   konia
أبى زرارة   konia
أبي زرارة   konia
أبى زرعة    konia
أبي زرعة    konia
أبى زفر konia
أبي زفر konia
أبى زكريا   konia
أبي زكريا   konia
أبى زميل    konia
أبي زميل    konia
أبى زهرة    konia
أبي زهرة    konia
أبى زهير    konia
أبي زهير    konia
أبى زياد    konia
أبي زياد    konia
أبى زيادة   konia
أبي زيادة   konia
أبى زيد konia
أبي زيد konia
أبى زينب    konia
أبي زينب    konia
أبى زينب الحجازى    konia
أبى زينب الحجازي    konia
أبي زينب الحجازى    konia
أبي زينب الحجازي    konia
أبى ساج konia
أبي ساج konia
أبى ساسان   konia
أبي ساسان   konia
أبى سالم    konia
أبي سالم    konia
أبى سبأ konia
أبي سبأ konia
أبى سبرة    konia
أبي سبرة    konia
أبى سحيم    konia
أبي سحيم    konia
أبى سخيلة   konia
أبي سخيلة   konia
أبى سروعة   konia
أبي سروعة   konia
أبى سريحة   konia
أبي سريحة   konia
أبى سريرة   konia
أبي سريرة   konia
أبى سعاد    konia
أبي سعاد    konia
أبى سعد konia
أبي سعد konia
أبى سعدة    konia
أبي سعدة    konia
أبى سعيد    konia
أبي سعيد    konia
أبى سعيد الخير  konia
أبي سعيد الخير  konia
أبى سعيد المؤدب konia
أبي سعيد المؤدب konia
أبى سفيان   konia
أبي سفيان   konia
أبى سكينة   konia
أبي سكينة   konia
أبى سلام    konia
أبي سلام    konia
أبى سلامة   konia
أبي سلامة   konia
أبى سلمان   konia
أبي سلمان   konia
أبى سلمان المؤذن    konia
أبي سلمان المؤذن    konia
أبى سلمة    konia
أبي سلمة    konia
أبى سلمى    konia
أبى سلمي    konia
أبي سلمى    konia
أبي سلمي    konia
أبي سليك    konia
أبى سليم    konia
أبي سليم    konia
أبى سليمان  konia
أبي سليمان  konia
أبى سماك    konia
أبي سماك    konia
أبى سمية    konia
أبي سمية    konia
أبى سنان    konia
أبي سنان    konia
أبى سهل konia
أبي سهل konia
أبى سهلة    konia
أبي سهلة    konia
أبى سهيل    konia
أبي سهيل    konia
أبى سورة    konia
أبي سورة    konia
أبى سوية    konia
أبي سوية    konia
أبى سويد    konia
أبي سويد    konia
أبى سويرة   konia
أبي سويرة   konia
أبى سيارة   konia
أبي سيارة   konia
أبى سيدان   konia
أبي سيدان   konia
أبى سيف konia
أبي سيف konia
أبى شاكر    konia
أبي شاكر    konia
أبى شبرمة   konia
أبي شبرمة   konia
أبى شبل konia
أبي شبل konia
أبى شجاع    konia
أبي شجاع    konia
أبى شجرة    konia
أبي شجرة    konia
أبى شرحبيل  konia
أبي شرحبيل  konia
أبى شريح    konia
أبي شريح    konia
أبى شريك    konia
أبي شريك    konia
أبى شعبة    konia
أبي شعبة    konia
أبى شعيب    konia
أبي شعيب    konia
أبى شمر konia
أبي شمر konia
أبى شهاب    konia
أبي شهاب    konia
أبى شهر konia
أبي شهر konia
أبى شهم konia
أبي شهم konia
أبى شهيد    konia
أبي شهيد    konia
أبى شيبان   konia
أبي شيبان   konia
أبى شيبة    konia
أبي شيبة    konia
أبى شيخ konia
أبي شيخ konia
أبى صادق    konia
أبي صادق    konia
أبى صالح    konia
أبي صالح    konia
أبى صخر konia
أبي صخر konia
أبى صخرة    konia
أبي صخرة    konia
أبى صدقة    konia
أبي صدقة    konia
أبى صرمة    konia
أبي صرمة    konia
أبي صعصعة   konia
أبى صعير    konia
أبي صعير    konia
أبى صفوان   konia
أبي صفوان   konia
أبى صيفى    konia
أبى صيفي    konia
أبي صيفى    konia
أبي صيفي    konia
أبى ضمرة    konia
أبي ضمرة    konia
أبى طارق    konia
أبي طارق    konia
أبى طالب    konia
أبي طالب    konia
أبى طالوت   konia
أبي طالوت   konia
أبى طاهر    konia
أبي طاهر    konia
أبى طريف    konia
أبي طريف    konia
أبى طعمة    konia
أبي طعمة    konia
أبى طلحة    konia
أبي طلحة    konia
أبى طوالة   konia
أبي طوالة   konia
أبى طيبة    konia
أبي طيبة    konia
أبى ظبيان   konia
أبي ظبيان   konia
أبى ظبية    konia
أبي ظبية    konia
أبى ظفر konia
أبي ظفر konia
أبى ظلال    konia
أبي ظلال    konia
أبى عائذ    konia
أبي عائذ    konia
أبى عائذ الله   konia
أبي عائذ الله   konia
أبى عائشة   konia
أبي عائشة   konia
أبى عاتكة   konia
أبي عاتكة   konia
أبى عازب    konia
أبي عازب    konia
أبى عاصم    konia
أبي عاصم    konia
أبى عامر    konia
أبي عامر    konia
أبى عباد    konia
أبي عباد    konia
أبى عبادة   konia
أبي عبادة   konia
أبى عبد الجبار  konia
أبي عبد الجبار  konia
أبى عبد الحمن   konia
أبي عبد الحمن   konia
أبى عبد الحميد  konia
أبي عبد الحميد  konia
أبى عبد الدائم  konia
أبي عبد الدائم  konia
أبى عبد الرحمن  konia
أبي عبد الرحمن  konia
أبى عبد الرحمن ‎    konia
أبي عبد الرحمن ‎    konia
أبى عبد الرحيم  konia
أبي عبد الرحيم  konia
أبى عبد السلام  konia
أبي عبد السلام  konia
أبى عبد الصمد   konia
أبي عبد الصمد   konia
أبى عبد العزيز  konia
أبي عبد العزيز  konia
أبى عبد القدوس  konia
أبي عبد القدوس  konia
أبى عبد الكريم  konia
أبي عبد الكريم  konia
أبى عبد الله    konia
أبي عبد الله    konia
أبى عبد الله الجهنى konia
أبى عبد الله الجهني konia
أبي عبد الله الجهنى konia
أبي عبد الله الجهني konia
أبى عبد الله الخياط konia
أبي عبد الله الخياط konia
أبى عبد الله الضرير konia
أبي عبد الله الضرير konia
أبى عبد الله المؤدب المكتب  konia
أبي عبد الله المؤدب المكتب  konia
أبى عبد الله المؤذن konia
أبي عبد الله المؤذن konia
أبى عبد الملك   konia
أبي عبد الملك   konia
أبى عبد رب  konia
أبي عبد رب  konia
أبى عبد رب العزة    konia
أبي عبد رب العزة    konia
أبى عبد ربه konia
أبي عبد ربه konia
أبى عبدالرحمن   konia
أبي عبدالرحمن   konia
أبى عبدة    konia
أبي عبدة    konia
أبى عبس konia
أبي عبس konia
أبى عبيد    konia
أبي عبيد    konia
أبى عبيد الله   konia
أبي عبيد الله   konia
أبى عبيدة   konia
أبي عبيدة   konia
أبى عتاب    konia
أبي عتاب    konia
أبى عتبة    konia
أبي عتبة    konia
أبى عتيق    konia
أبي عتيق    konia
أبى عتيك    konia
أبي عتيك    konia
أبى عثمان   konia
أبي عثمان   konia
أبى عثيم    konia
أبي عثيم    konia
أبى عدى konia
أبى عدي konia
أبي عدى konia
أبي عدي konia
أبى عذرة    konia
أبي عذرة    konia
أبى عرفة    konia
أبي عرفة    konia
أبي عروبة   konia
أبى عروة    konia
أبي عروة    konia
أبى عزة konia
أبي عزة konia
أبى عشانة   konia
أبي عشانة   konia
أبى عصام    konia
أبي عصام    konia
أبى عصمة    konia
أبي عصمة    konia
أبى عصيدة   konia
أبي عصيدة   konia
أبى عطاء    konia
أبي عطاء    konia
أبى عطية    konia
أبي عطية    konia
أبى عفان    konia
أبي عفان    konia
أبى عقال    konia
أبي عقال    konia
أبى عقبة    konia
أبي عقبة    konia
أبى عقرب    konia
أبي عقرب    konia
أبى عقيل    konia
أبي عقيل    konia
أبى عكاشة   konia
أبي عكاشة   konia
أبى عكرمة   konia
أبي عكرمة   konia
أبى علقمة   konia
أبي علقمة   konia
أبى علوان   konia
أبي علوان   konia
أبى علويه   konia
أبي علويه   konia
أبى علي konia
أبي علي konia
أبى عمار    konia
أبي عمار    konia
أبى عمارة   konia
أبي عمارة   konia
أبى عمر konia
أبي عمر konia
أبى عمران   konia
‏أبي عمران  konia
أبى عمرة    konia
أبي عمرة    konia
أبى عمرو    konia
أبي عمرو    konia
أبى عمير    konia
أبي عمير    konia
أبى عميرة   konia
أبي عميرة   konia
أبى عنبة    konia
أبي عنبة    konia
أبى عنبسة   konia
أبي عنبسة   konia
أبي عوان    konia
أبى عوانة   konia
أبي عوانة   konia
أبى عوف konia
أبي عوف konia
أبى عون konia
أبي عون konia
أبى عياش    konia
أبي عياش    konia
أبى عياض    konia
أبي عياض    konia
أبى عيسى    konia
أبى عيسي    konia
أبي عيسى    konia
أبي عيسي    konia
أبى غالب    konia
أبي غالب    konia
أبى غانم    konia
أبي غانم    konia
أبى غرارة   konia
أبي غرارة   konia
أبى غزوان   konia
أبي غزوان   konia
أبى غسان    konia
أبي غسان    konia
أبى غطفان   konia
أبي غطفان   konia
أبى غطيف    konia
أبي غطيف    konia
أبى غفار    konia
أبي غفار    konia
أبى غلاب    konia
أبي غلاب    konia
أبى غلباء   konia
أبي غلباء   konia
أبى غياث    konia
أبي غياث    konia
أبى فاختة   konia
أبي فاختة   konia
أبى فاطمة   konia
أبي فاطمة   konia
أبى فراس    konia
أبي فراس    konia
أبى فروة    konia
أبي فروة    konia
أبى فروة الأصغر konia
أبي فروة الأصغر konia
أبى فزارة   konia
أبي فزارة   konia
أبى فضالة   konia
أبي فضالة   konia
أبى قابوس   konia
أبي قابوس   konia
أبى قبيصة   konia
أبي قبيصة   konia
أبى قبيل    konia
أبي قبيل    konia
أبى قتادة   konia
أبي قتادة   konia
أبى قتيبة   konia
أبي قتيبة   konia
أبى قتيلة   konia
أبي قتيلة   konia
أبي قحافة   konia
أبى قدامة   konia
أبي قدامة   konia
أبى قديد    konia
أبي قديد    konia
أبى قرة konia
أبي قرة konia
أبى قرصافة  konia
أبي قرصافة  konia
أبى قريش    konia
أبي قريش    konia
أبى قزعة    konia
أبي قزعة    konia
أبى قضاعة   konia
أبي قضاعة   konia
أبى قطن konia
أبي قطن konia
أبى قلابة   konia
أبي قلابة   konia
أبى قنان    konia
أبي قنان    konia
أبى قيس konia
أبي قيس konia
أبى كامل    konia
أبي كامل    konia
أبى كاهل    konia
أبي كاهل    konia
أبى كباش    konia
أبي كباش    konia
أبى كبشة    konia
أبي كبشة    konia
أبى كبشة البراء konia
أبي كبشة البراء konia
أبى كثير    konia
أبي كثير    konia
أبى كدينة   konia
أبي كدينة   konia
أبى كرب konia
أبي كرب konia
أبى كردوس   konia
أبي كردوس   konia
أبى كرز konia
أبي كرز konia
أبى كريب    konia
أبي كريب    konia
أبى كريمة   konia
أبي كريمة   konia
أبى كعب konia
أبي كعب konia
أبى كلثم    konia
أبي كلثم    konia
أبى كليب    konia
أبي كليب    konia
أبى كنانة   konia
أبي كنانة   konia
أبى لاس konia
أبي لاس konia
أبى لبابة   konia
أبي لبابة   konia
أبى لبيد    konia
أبي لبيد    konia
أبى لقمان   konia
أبي لقمان   konia
أبى لوط konia
أبي لوط konia
أبى ليث konia
أبي ليث konia
أبى ليلى    konia
أبى ليلي    konia
أبي ليلى    konia
أبي ليلي    konia
أبى ماجد    konia
أبي ماجد    konia
أبى ماجدة   konia
أبي ماجدة   konia
أبى مالك    konia
أبي مالك    konia
أبى مجاهد   konia
أبي مجاهد   konia
أبى مجلز    konia
أبي مجلز    konia
أبى محذورة  konia
أبي محذورة  konia
أبى محرر    konia
أبي محرر    konia
أبى محرز    konia
أبي محرز    konia
أبى محصن    konia
أبي محصن    konia
أبى محلم    konia
أبي محلم    konia
أبى محمد    konia
أبي محمد    konia
أبى محمود   konia
أبي محمود   konia
أبى محيريز  konia
أبي محيريز  konia
أبى مخارق   konia
أبي مخارق   konia
أبى مخاشن   konia
أبي مخاشن   konia
أبى مخلد    konia
أبي مخلد    konia
أبى مدرك    konia
أبي مدرك    konia
أبى مدلة    konia
أبي مدلة    konia
أبى مرازم   konia
أبي مرازم   konia
أبى مراوح   konia
أبي مراوح   konia
أبى مرة konia
أبي مرة konia
أبى مرثد    konia
أبي مرثد    konia
أبى مرحب    konia
أبي مرحب    konia
أبى مرحوم   konia
أبي مرحوم   konia
أبى مرزوق   konia
أبي مرزوق   konia
أبى مروان   konia
أبي مروان   konia
أبى مريم    konia
أبي مريم    konia
أبى مزاحم   konia
أبي مزاحم   konia
أبى مزرد    konia
أبي مزرد    konia
أبى مساحق   konia
أبي مساحق   konia
أبى مسافر   konia
أبي مسافر   konia
أبى مسعود   konia
أبي مسعود   konia
أبى مسقبة   konia
أبي مسقبة   konia
أبى مسكين   konia
أبي مسكين   konia
أبى مسلم    konia
أبي مسلم    konia
أبى مسلمة   konia
أبي مسلمة   konia
أبى مسهر    konia
أبي مسهر    konia
أبى مشجعة   konia
أبي مشجعة   konia
أبى مصبح    konia
أبي مصبح    konia
أبى مصعب    konia
أبي مصعب    konia
أبى مصلح    konia
أبي مصلح    konia
أبى مضر konia
أبي مضر konia
أبى مطر konia
أبي مطر konia
أبى مطرف    konia
أبي مطرف    konia
أبى مطيع    konia
أبي مطيع    konia
أبى معاذ    konia
أبي معاذ    konia
أبى معان    konia
أبي معان    konia
أبى معانق   konia
أبي معانق   konia
أبى معاوية  konia
أبي معاوية  konia
أبى معبد    konia
أبي معبد    konia
أبى معدان   konia
أبي معدان   konia
أبى معشر    konia
أبي معشر    konia
‏أبى معفس   konia
‏أبي معفس   konia
أبى معقل    konia
أبي معقل    konia
أبى معمر    konia
أبي معمر    konia
أبى معن konia
أبي معن konia
أبى معن محمد    konia
أبي معن محمد    konia
أبى معيد    konia
أبي معيد    konia
أبي معيط    konia
أبى معيوف   konia
أبي معيوف   konia
أبى مقاتل   konia
أبي مقاتل   konia
أبى مكرم    konia
أبي مكرم    konia
أبى مكين    konia
أبي مكين    konia
أبى مليكة   konia
أبي مليكة   konia
أبى منصور   konia
أبي منصور   konia
أبى منظور   konia
أبي منظور   konia
أبى منين    konia
أبي منين    konia
أبى مهدى    konia
أبى مهدي    konia
أبي مهدى    konia
أبي مهدي    konia
أبى مهل konia
أبي مهل konia
أبى مودود   konia
أبي مودود   konia
أبى مودود هو بحر    konia
أبي مودود هو بحر    konia
أبى موسى    konia
أبى موسي    konia
أبي موسى    konia
أبي موسي    konia
أبى موسى هو علي konia
أبي موسى هو علي konia
أبى مية konia
أبي مية konia
أبى ميسرة   konia
أبي ميسرة   konia
أبى ميمون   konia
أبي ميمون   konia
أبى ميمونة  konia
أبي ميمونة  konia
أبى نافع    konia
أبي نافع    konia
أبى نباتة   konia
أبي نباتة   konia
أبى نجيح    konia
أبي نجيح    konia
أبى نجيد    konia
أبي نجيد    konia
‏أبى نحيلة  konia
‏أبي نحيلة  konia
أبى نخيلة   konia
أبي نخيلة   konia
أبى نذير    konia
أبي نذير    konia
أبى نشيط    konia
أبي نشيط    konia
أبى نصر konia
أبي نصر konia
‏أبى نصير   konia
‏أبي نصير   konia
أبى نصيرة   konia
أبي نصيرة   konia
أبي نضربة   konia
أبى نضرة    konia
أبي نضرة    konia
أبى نضلة    konia
أبي نضلة    konia
أبى نعامة   konia
أبي نعامة   konia
أبى نعيم    konia
أبي نعيم    konia
أبى نملة    konia
أبي نملة    konia
أبى نهار    konia
أبي نهار    konia
أبى نهيك    konia
أبي نهيك    konia
أبى نوح konia
أبي نوح konia
أبى نوفل    konia
أبي نوفل    konia
أبى ه   konia
أبي ه   konia
أبى هارون   konia
أبي هارون   konia
أبى هاشم    konia
أبي هاشم    konia
أبى هانىء   konia
أبي هانىء   konia
أبى هبيرة   konia
أبي هبيرة   konia
أبى هريرة   konia
أبي هريرة   konia
أبى هشام    konia
أبي هشام    konia
أبى هلال    konia
أبي هلال    konia
أبى همام    konia
أبي همام    konia
أبى هند konia
أبي هند konia
أبى هنيد    konia
أبي هنيد    konia
أبى هنيدة   konia
أبي هنيدة   konia
أبى هود konia
أبي هود konia
أبى وائل    konia
أبي وائل    konia
أبى واثلة   konia
أبي واثلة   konia
أبى واقد    konia
أبي واقد    konia
أبى وجزة    konia
أبي وجزة    konia
أبى وحشية   konia
أبي وحشية   konia
أبى وقاص    konia
أبي وقاص    konia
أبى وكيع    konia
أبي وكيع    konia
أبى وهب konia
أبي وهب konia
أبى ياسر    konia
أبي ياسر    konia
أبى يحمد    konia
أبي يحمد    konia
أبى يحيى    konia
أبى يحيي    konia
أبي يحيى    konia
أبي يحيي    konia
أبى يربوع   konia
أبي يربوع   konia
أبى يزيد    konia
أبي يزيد    konia
أبى يسار    konia
أبي يسار    konia
أبى يعفور   konia
أبي يعفور   konia
أبى يعقوب   konia
أبي يعقوب   konia
أبى يعلى    konia
أبى يعلي    konia
أبي يعلى    konia
أبي يعلي    konia
أبى يعيش    konia
أبي يعيش    konia
أبى يوسف    konia
أبي يوسف    konia
أبى يونس    konia
أبي يونس    konia
أم الدرداء  konia
أم حبيبة    konia
أم سلمة konia
أم سليم konia
أم عبد الملك    konia
أم عطية konia
أم غراب konia
أم فروة konia
أم مكتوم    konia
أم هانئ konia
ابو محمد    konia
الضرير أبو جعفر konia
الضرير أبو محمد konia
الفضيل  konia
عبد الرازق  konia
أبو الأحوص  laqab
أبو الآذان  laqab
أبو البداح  laqab
أبو التياح  laqab
أبو الجماهر laqab
أبو الجوزاء laqab
أبو الرجال  laqab
أبو الزناد  laqab
أبو الشعثاء laqab
أبو المساكين    laqab
أبو المليح  laqab
أبو المنين  laqab
أبو بطن laqab
أبو تراب    laqab
أبو ثور laqab
أبو حرزة    laqab
أبو حزرة    laqab
أبو خديج    laqab
أبو زكار    laqab
أبو زكير    laqab
أبو ساسان   laqab
أبو عصيدة   laqab
أبو عوف laqab
أبو قلابة   laqab
أبو كباش    laqab
أبو كشوثاء  laqab
أبو نشيط    laqab
أبو هريرة   laqab
أبو همام    laqab
آبى اللحم   laqab
أذينة   laqab
أسد السنة   laqab
أشج عبد القيس   laqab
إشكاب   laqab
أشهب    laqab
أشياخ كوثا  laqab
أمين هذه الأمة  laqab
أيسر    laqab
ابن أخى الإمام  laqab
‏ابن خت laqab
ابن راهويه  laqab
ابن سنوطا   laqab
ابن صفيراء  laqab
ابن علية    laqab
الأبح   laqab
الأبرش  laqab
الأثبج  laqab
الأثرم  laqab
الأجلح  laqab
الأحدب  laqab
الأحمر  laqab
الأحنف  laqab
الأحول  laqab
الأزرق  laqab
الأسود  laqab
الأشتر  laqab
الأشج   laqab
الأشدق  laqab
الأشقر  laqab
الأشل   laqab
الأشيب  laqab
الأصفر  laqab
الأصم   laqab
الأعجم  laqab
الأعرج  laqab
الأعرج الأحرد   laqab
الأعسم  laqab
الأعشى  laqab
الأعشي  laqab
الأعلم  laqab
الأعمش  laqab
الأعنق  laqab
الأعور  laqab
الأعين  laqab
الأغر   laqab
الأغطش  laqab
الأفرق  laqab
الأفطس  laqab
الأفوه  laqab
الأقرع  laqab
الأقمر  laqab
الأكبر  laqab
الأكوع  laqab
الأمير  laqab
الاسلمى laqab
الاسلمي laqab
الاعرج  laqab
الاعين  laqab
الاكوع  laqab
الاوزاعى    laqab
الاوزاعي    laqab
الباقر  laqab
البحر   laqab
البراد  laqab
البردى  laqab
البردي  laqab
البرصاء laqab
البطين  laqab
البكاء  laqab
البناي  laqab
البهى   laqab
البهي   laqab
الترك   laqab
التل    laqab
التميمي laqab
التوأم  laqab
الجرادة الصفراء laqab
الجمل   laqab
الجهدمة laqab
الجوبارى    laqab
الجوباري    laqab
الحافظ  laqab
الحافى  laqab
الحافي  laqab
الحذاء  laqab
الحسام  laqab
الحكيم  laqab
الحمال  laqab
الحناط  laqab
الحوت   laqab
الخباط  laqab
الخطاب  laqab
الخياط  laqab
الداناج laqab
الداني  laqab
الدرامي laqab
الدندانى    laqab
الدنداني    laqab
الديباج laqab
الرأى   laqab
الرأي   laqab
الرزقي  laqab
الرشك   laqab
الرضى   laqab
الرضي   laqab
الرقاشي laqab
الرميصاء    laqab
الزاهد  laqab
الزمن   laqab
الزهراء laqab
الساعدي laqab
السراج  laqab
السمين  laqab
الشاعر  laqab
الشاه   laqab
الشهيد  laqab
الصادق  laqab
الصاغاني    laqab
الصدوق  laqab
الصديق  laqab
الصغير  laqab
الصفى   laqab
الصفي   laqab
الصواف  laqab
الصيد   laqab
الصيقل  laqab
الضال   laqab
الضبى   laqab
الضبي   laqab
الضخم   laqab
الضرير  laqab
الطفيل  laqab
الطويل  laqab
الطيب   laqab
العابد  laqab
العجلى  laqab
العجلي  laqab
العرشى  laqab
الغميصاء    laqab
الغميصاء أو الرميصاء    laqab
الغول   laqab
الفأفأ  laqab
الفأفاء laqab
الفاروق laqab
الفرخ   laqab
الفقير  laqab
الفقيه  laqab
القارىء laqab
القاضى  laqab
القاضي  laqab
القباع  laqab
القراد  laqab
القرظ   laqab
القرظ المؤذن    laqab
القرظي  laqab
القس    laqab
القسملى laqab
القسملي laqab
القصير  laqab
القلب   laqab
القوى   laqab
القوي   laqab
الكاظم  laqab
الكوسج  laqab
الماجشون    laqab
المجدر  laqab
المحاربي    laqab
المحرق  laqab
المرمي  laqab
المزلق  laqab
المزي   Laqab
المسبح  laqab
المسندى laqab
المسندي laqab
‏المصبح laqab
المصفي  laqab
المصلوب laqab
المضروب laqab
المطرف  laqab
المعرقب laqab
المفلوج laqab
المقري  laqab
المقعد  laqab
المقفع  laqab
المقوم  laqab
المقومى laqab
المقومي laqab
المهاجر laqab
الناقد  laqab
النبيل  laqab
النفس الزكية    laqab
بانى كعبة الرحمن    laqab
ببة laqab
بحر الجود   laqab
بحشل    laqab
بدعة    laqab
برق laqab
بريه    laqab
بشمين   laqab
بكير    laqab
بن أذينة    laqab
بن زبان laqab
بن غراب laqab
بن مطرف laqab
بنان    laqab
بندار   laqab
بومة    laqab
بياع الأكسية    laqab
تيار الفرات laqab
جبير    laqab
جردقة   laqab
جمعة    laqab
جويبر   laqab
حبويه   laqab
حبى laqab
حبي laqab
حرمى    laqab
حرمي    laqab
حسنويه  laqab
حفيص    laqab
حلق laqab
حلقوم   laqab
حماد    laqab
حمدان   laqab
حمدون   laqab
حمدويه  laqab
حمك laqab
حميد    laqab
حنش laqab
حية الوادى  laqab
حية الوادي  laqab
حيدرة   laqab
حيكان   laqab
حيويه   laqab
خاقان   laqab
خت  laqab
ختن المقرىء laqab
خياط السنة  laqab
دار أم سلمة laqab
دافن    laqab
دجين    laqab
دحروجة الجعل    laqab
دحيم    laqab
دراج    laqab
درة العراق  laqab
دلويه   laqab
ذات النطاقين    laqab
ذو الأذنين  laqab
ذو الجناحين laqab
ذو الجوشن   laqab
ذو الزوائد  laqab
ذو الشهادتين    laqab
ذو العينين  laqab
ذو النورين  laqab
ذو مر   laqab
ذو مصر  laqab
ذى الرمحين  laqab
ذي مخبر laqab
راهب قريش   laqab
رباح    laqab
ربع الإسلام laqab
ربيح    laqab
رخ  laqab
رزق الله    laqab
رزيق    laqab
رسته    laqab
ريحانة البصرة   laqab
ريحانة النبى صلى الله عليه وسلم laqab
ريحانة نيسابور  laqab
زاج laqab
زبان    laqab
زبريق   laqab
زحابا   laqab
زرغنده  laqab
زغبة    laqab
زكار    laqab
زنبقة   laqab
زنبور   laqab
زنيج    laqab
زوج جبرة    laqab
زين العابدين    laqab
سؤر الأسد   laqab
سابق الحبشة laqab
سابق الروم  laqab
سابق العرب  laqab
سابق الفرس  laqab
سبلان   laqab
سجادة   laqab
سحبل    laqab
سرق laqab
سعدان   laqab
سعدويه  laqab
سفينة   laqab
سكرة    laqab
سلام    laqab
سلمويه  laqab
سندل    laqab
سندول   laqab
سندولا  laqab
سندولة  laqab
سنوطا   laqab
سنيد    laqab
سيف الله    laqab
سيمين كوش   laqab
شاباص   laqab
شاذ laqab
شاذان   laqab
شارب الذهب  laqab
شباب    laqab
شداد    laqab
شعبة الصغير laqab
شقران   laqab
شقوصا   laqab
صاحب الأغمية    laqab
صاحب الحرير laqab
صاحب الحلى  laqab
صاحب الحلي  laqab
صاحب الحناء laqab
صاحب الدستوائى  laqab
صاحب الدستوائي  laqab
صاحب الزيادى    laqab
صاحب الزيادي    laqab
صاحب السقاية    laqab
صاحب السلعة laqab
صاحب الطعام laqab
صاحب الطيالسة   laqab
صاحب العباء laqab
صاحب القصب  laqab
صاحب القناديل   laqab
صاحب القوهى laqab
صاحب القوهي laqab
صاحب الكرابيس   laqab
صاحب اللؤلؤ laqab
صاحب المصاحف    laqab
صاحب المصلى laqab
صاحب المصلي laqab
صاحب المقصورة   laqab
صاعقة   laqab
صدرة    laqab
صفيرا   laqab
صميد    laqab
صندل    laqab
صهيب الرومى laqab
صهيب الرومي laqab
طاووس   laqab
طلحة الجود  laqab
طلحة الخير  laqab
طلحة الفياض laqab
طلحة الندى  laqab
طلحة الندي  laqab
ظئر العناق  laqab
ظل الشيطان  laqab
عارم    laqab
عباد رقبة   laqab
عبادل   laqab
عباسويه laqab
عبثر    laqab
عبدان   laqab
عبدة    laqab
عبدوس   laqab
عبدويه  laqab
عبويه   laqab
عبيد    laqab
عتريس   laqab
عتيق    laqab
عصا ابن إدريس   laqab
عصفور الجنة laqab
عصيدة   laqab
عكة العسل   laqab
علان    laqab
علي laqab
عليلة   laqab
عنبر    laqab
عويمر   laqab
غراب    laqab
غريق الجحفة laqab
غنجار   laqab
غندر    laqab
فريخ    laqab
فليت    laqab
فليح    laqab
فهير    laqab
قاضى الجن   laqab
قاضى المصرين    laqab
قراد    laqab
قرة laqab
قريب    laqab
قصى laqab
قصي laqab
قيصر    laqab
كاتب العمرى laqab
كاتب العمري laqab
كاتب المغيرة    laqab
كاتب الواقدى    laqab
كاتب الواقدي    laqab
كاو laqab
كراع    laqab
كردوس   laqab
كزمان   laqab
كشاكش   laqab
كعبان   laqab
كميل    laqab
كيلجة   laqab
لؤلؤ    laqab
لزم laqab
لزيم    laqab
لوين    laqab
مؤذن رسول الله صلى الله عليه وسلم   laqab
محبوب   laqab
مردويه  laqab
مستقيم  laqab
مسدد    laqab
مشفر    laqab
مشكدانة laqab
مطرف    laqab
مغيرة الرأى laqab
مغيرة الرأي laqab
منبوذ   laqab
مندل    laqab
ميمون   laqab
نسيج وحده   laqab
هداب    laqab
هقل laqab
هلب laqab
وحشى    laqab
وحشي    laqab
وقدان   laqab
ولاد    laqab
وهب laqab
وهب الخير   laqab
وهبان   laqab
وهيب    laqab
يؤيؤ    laqab
ياقوتة العلماء  laqab
يتيم زيد    laqab
يتيم عروة   laqab
يزيد الخير  laqab
يوسف هذه الأمة  laqab
أصله كوفي   laqab2
الأحمر  laqab2
الأكبر  laqab2
الإمام  laqab2
الثقيفة laqab2
الجمل   laqab2
الخير   laqab2
السرح   laqab2
السفر   laqab2
الضعيف  laqab2
الطباع  laqab2
العبد   laqab2
الفرج   laqab2
القارئ  laqab2
القداح  laqab2
الكبرى  laqab2
الكبير  laqab2
المؤذن  laqab2
المبارك laqab2
اليمنى  laqab2
بدل laqab2
تمام    laqab2
ثابت    laqab2
جميع    laqab2
حميد    laqab2
خلف laqab2
خير laqab2
زيادة   laqab2
سلم laqab2
صالح    laqab2
صبح laqab2
صلح laqab2
عباد    laqab2
عبد laqab2
فارس    laqab2
فلان    laqab2
قريب    laqab2
كبير    laqab2
كثير    laqab2
لمقرئ   laqab2
مؤذن ل  laqab2
مؤذن مسجد الأكبر    laqab2
مؤذن مسجد العريان   laqab2
محبب    laqab2
محفوظ   laqab2
مرة laqab2
نسى laqab2
نسي laqab2
هدية    laqab2
مولاة   Mawla
مولاة لهم   Mawla
مولاهم  Mawla
مولى    Mawla
مولي    Mawla
مولى لهم    Mawla
أهل الشام   nasab
أهل المدينة من الأنصار  nasab
االضبى  nasab
االضبي  nasab
ابن الأصبهانى   nasab
ابن الأصبهاني   nasab
ابن البرقى  nasab
ابن البرقي  nasab
ابن البيلمانى   nasab
ابن البيلماني   nasab
ابن الثلجى  nasab
ابن الثلجي  nasab
ابن الديلمى nasab
ابن الديلمي nasab
ابن الرومى  nasab
ابن الرومي  nasab
ابن السندى  nasab
ابن السندي  nasab
ابن العجمى  nasab
ابن العجمي  nasab
ابن الواسطى nasab
ابن الواسطي nasab
الأبار  nasab
الأبلى  nasab
الأبلي  nasab
الأبناوى    nasab
الأبناوي    nasab
الأبيوردى   nasab
الأبيوردي   nasab
الأثرم  nasab
الأجروى nasab
الأجروي nasab
الأحدب  nasab
الأحدبى nasab
الأحدبي nasab
الأحرد  nasab
الأحروجى    nasab
الأحروجي    nasab
الأحلافى    nasab
الأحلافي    nasab
الأحمرى nasab
الأحمري nasab
الأحمسى nasab
الأحمسي nasab
الأحمسية    nasab
الأحنفى nasab
الأحنفي nasab
الأحول  nasab
الأخبارى    nasab
الأخباري    nasab
الأخنسى nasab
الأخنسي nasab
الآدم   nasab
الأدمى  nasab
الأدمي  nasab
الأديب  nasab
الأذرمى nasab
الأذرمي nasab
الأذنى  nasab
الأذني  nasab
الأرحبى nasab
الأرحبي nasab
الأردنى nasab
الأردني nasab
الأرزى  nasab
الأرزي  nasab
الأرسوفى    nasab
الأرسوفي    nasab
الأرطبانى   nasab
الأرطباني   nasab
الأزدى  nasab
الأزدي  nasab
الأزدية nasab
الأزرق  nasab
الأزرقى nasab
الأزرقي nasab
الأسباطى    nasab
الأسباطي    nasab
الإستراباذى nasab
الإستراباذي nasab
الأستوائى   nasab
الأستوائي   nasab
الأسدى  nasab
الأسدي  nasab
الأسدى‏العجلى   nasab
الأسدى‏العجلي   nasab
الأسدية nasab
الإسرائيلى  nasab
الإسرائيلي  nasab
الإسرائيلية nasab
الأسفاطى    nasab
الأسفاطي    nasab
الأسفذنى    nasab
الأسفذني    nasab
الإسفرايينى nasab
الإسفراييني nasab
الإسكاف nasab
الإسكافى    nasab
الإسكافي    nasab
الإسكندرانى nasab
الإسكندراني nasab
الأسلمى nasab
الأسلمي nasab
الأسلمية    nasab
الأسلى  nasab
الأسلي  nasab
الأسوارى    nasab
الأسواري    nasab
الأسيدى nasab
الأسيدي nasab
الأشجعى nasab
الأشجعي nasab
الأشجعية    nasab
الأشعثى nasab
الأشعثي nasab
الأشعرى nasab
الأشعري nasab
الأشعرية    nasab
الأشقرى nasab
الأشقري nasab
الأشنانى    nasab
الأشناني    nasab
الأشهلى nasab
الأشهلي nasab
الأشهلية    nasab
الأصبحى nasab
الأصبحي nasab
الأصبهانى   nasab
الأصبهاني   nasab
الأصغر  nasab
الأصل   nasab
الأصم   nasab
الأصمعى nasab
الأصمعي nasab
الأطرابلسى  nasab
الأطرابلسي  nasab
الأعدولى    nasab
الأعدولي    nasab
الأعرابى    nasab
الأعرابي    nasab
الأعرج  nasab
الأعرجى nasab
الأعرجي nasab
الأعشى  nasab
الأعشي  nasab
الأعمى  nasab
الأعمي  nasab
الأعور  nasab
الأفريقى    nasab
الأفريقي    nasab
الإفريقى    nasab
الإفريقي    nasab
الأفزر  nasab
الأفطس  nasab
الأكافى nasab
الأكافي nasab
الأكفانى    nasab
الأكفاني    nasab
الألهانى    nasab
الألهاني    nasab
الأمامى nasab
الأمامي nasab
الأملوكى    nasab
الأملوكي    nasab
الآملى  nasab
الآملي  nasab
الأموى  nasab
الأموي  nasab
الأموية nasab
الأنبارى    nasab
الأنباري    nasab
الأندلسى    nasab
الأندلسي    nasab
الأنصارى    nasab
الأنصاري    nasab
الأنصارية   nasab
الأنطاكى    nasab
الأنطاكي    nasab
الأنعمى nasab
الأنعمي nasab
الأنمارى    nasab
الأنماري    nasab
الأنمارية   nasab
الأنماطى    nasab
الأنماطي    nasab
الأنيسى nasab
الأنيسي nasab
الأهتمى nasab
الأهتمي nasab
الأهوازى    nasab
الأهوازي    nasab
الأوابى nasab
الأوابي nasab
الأودى  nasab
الأودي  nasab
الأوزاعى    nasab
الأوزاعي    nasab
الأوسى  nasab
الأوسي  nasab
الأوسية nasab
الأوصابى    nasab
الأوصابي    nasab
الأوصابية   nasab
الأويسى nasab
الأويسي nasab
الإيادى nasab
الإيادي nasab
الأيامى nasab
الأيامي nasab
الإيامى nasab
الإيامي nasab
الأيلى  nasab
الأيلي  nasab
الانصارى    nasab
البابلتى    nasab
البابلتي    nasab
البابوسى    nasab
البابوسي    nasab
البابونى    nasab
البابوني    nasab
البابى  nasab
البابي  nasab
الباجدائى   nasab
الباجدائي   nasab
البارقى nasab
البارقي nasab
البارودى    nasab
البارودي    nasab
الباكسائى   nasab
الباكسائي   nasab
الباكندى    nasab
الباكندي    nasab
البالسى nasab
البالسي nasab
الباهلى nasab
الباهلي nasab
الباوردى    nasab
الباوردي    nasab
البتلهى nasab
البتلهي nasab
البتى   nasab
البتي   nasab
البجلى  nasab
البجلي  nasab
البحترى nasab
البحتري nasab
البحرانى    nasab
البحراني    nasab
البخارى nasab
البخاري nasab
البخترى nasab
البختري nasab
البدرى  nasab
البدري  nasab
البدوى  nasab
البدوي  nasab
البذشى  nasab
البذشي  nasab
البراء  nasab
البراد  nasab
البربرى nasab
البربري nasab
البرجلانى   nasab
البرجلاني   nasab
البرجمى nasab
البرجمي nasab
البردى  nasab
البردي  nasab
البرزى  nasab
البرزي  nasab
البرسانى    nasab
البرساني    nasab
البرسمى nasab
البرسمي nasab
البرقى  nasab
البرقي  nasab
البركى  nasab
البركي  nasab
البرلسى nasab
البرلسي nasab
البرمكى nasab
البرمكي nasab
البريدى nasab
البريدي nasab
البزار  nasab
البزاز  nasab
البزورى nasab
البزوري nasab
البزيعى nasab
البزيعي nasab
البسرى  nasab
البسري  nasab
البسطامى    nasab
البسطامي    nasab
البصرى  nasab
البصري  nasab
البصرية nasab
البعلبكى    nasab
البعلبكي    nasab
البغدادى    nasab
البغدادي    nasab
البغلانى    nasab
البغلاني    nasab
البغوى  nasab
البغوي  nasab
البقال  nasab
البكاء  nasab
البكائى nasab
البكائي nasab
البكالى nasab
البكالي nasab
البكراوى    nasab
البكراوي    nasab
البكرى  nasab
البكري  nasab
البكرية nasab
البكيلى nasab
البكيلي nasab
البلاطى nasab
البلاطي nasab
البلخى  nasab
البلخي  nasab
البلدى  nasab
البلدي  nasab
البلقاوى    nasab
البلقاوي    nasab
البلوى  nasab
البلوي  nasab
البناء  nasab
البنانى nasab
البناني nasab
البهدلى nasab
البهدلي nasab
البهرانى    nasab
البهراني    nasab
البهزى  nasab
البهزي  nasab
البهزية nasab
البورانى    nasab
البوراني    nasab
البوشنجى    nasab
البوشنجي    nasab
البويطى nasab
البويطي nasab
البياضى nasab
البياضي nasab
البيروتى    nasab
البيروتي    nasab
البيكندى    nasab
البيكندي    nasab
البيلمانى   nasab
البيلماني   nasab
البيوردى    nasab
البيوردي    nasab
التابوتى    nasab
التابوتي    nasab
# التاجر    nasab
التبان  nasab
التبوذكى    nasab
التبوذكي    nasab
التجيبى nasab
التجيبي nasab
التجيى  nasab
التجيي  nasab
التراغمى    nasab
التراغمي    nasab
الترجمانى   nasab
الترجماني   nasab
الترقفى nasab
الترقفي nasab
التركى  nasab
التركي  nasab
الترمذى nasab
الترمذي nasab
التسترى nasab
التستري nasab
التسنيمى    nasab
التسنيمي    nasab
التغلبى nasab
التغلبي nasab
التمار  nasab
التميمى nasab
التميمي nasab
التميمية    nasab
التنعى  nasab
التنعي  nasab
التنوخى nasab
التنوخي nasab
التنورى nasab
التنوري nasab
التنيسى nasab
التنيسي nasab
التوزى  nasab
التوزي  nasab
التونسى nasab
التونسي nasab
التياس  nasab
التيمى  nasab
التيمي  nasab
التيمية nasab
الثعلبى nasab
الثعلبي nasab
الثعلى  nasab
الثعلي  nasab
الثغرى  nasab
الثغري  nasab
الثقفى  nasab
الثقفي  nasab
الثقفية nasab
الثلجى  nasab
الثلجي  nasab
الثمالى nasab
الثمالي nasab
الثوبانى    nasab
الثوباني    nasab
الثورى  nasab
الثوري  nasab
الجارودى    nasab
الجارودي    nasab
الجارى  nasab
الجاري  nasab
الجبلانى    nasab
الجبلاني    nasab
الجبلى  nasab
الجبلي  nasab
الجبيرى nasab
الجبيري nasab
الجحدرى nasab
الجحدري nasab
الجحشى  nasab
الجحشي  nasab
الجدعانى    nasab
الجدعاني    nasab
الجدلى  nasab
الجدلي  nasab
الجدى   nasab
الجدي   nasab
الجذامى nasab
الجذامي nasab
الجذمى  nasab
الجذمي  nasab
الجرار  nasab
الجرجانى    nasab
الجرجاني    nasab
الجرجرائى   nasab
الجرجرائي   nasab
الجرجسى nasab
الجرجسي nasab
الجرشى  nasab
الجرشي  nasab
الجرموزى    nasab
الجرموزي    nasab
الجرمى  nasab
الجرمي  nasab
الجروى  nasab
الجروي  nasab
الجريرى nasab
الجريري nasab
الجزار  nasab
الجزرى  nasab
الجزري  nasab
الجسرى  nasab
الجسري  nasab
الجشمى  nasab
الجشمي  nasab
الجصاص  nasab
الجعفرى nasab
الجعفري nasab
الجعفرية    nasab
الجعفى  nasab
الجعفي  nasab
الجفرى  nasab
الجفري  nasab
الجلاب  nasab
الجمال  nasab
الجمحى  nasab
الجمحي  nasab
الجملى  nasab
الجملي  nasab
الجنبى  nasab
الجنبي  nasab
الجندعى nasab
الجندعي nasab
الجندى  nasab
الجندي  nasab
الجنديسابورى    nasab
الجنديسابوري    nasab
الجهبذ  nasab
الجهضمى nasab
الجهضمي nasab
الجهنى  nasab
الجهني  nasab
الجهنية nasab
الجواز  nasab
الجوبارى    nasab
الجوباري    nasab
الجوبرى nasab
الجوبري nasab
الجوزجانى   nasab
الجوزجاني   nasab
الجوشنى nasab
الجوشني nasab
الجوفى  nasab
الجوفي  nasab
الجونى  nasab
الجوني  nasab
الجوهرى nasab
الجوهري nasab
الجوينى nasab
الجويني nasab
الجيزى  nasab
الجيزي  nasab
الجيشانى    nasab
الجيشاني    nasab
الحادى  nasab
الحادي  nasab
الحارثى nasab
الحارثي nasab
الحاطبى nasab
الحاطبي nasab
الحافظ  nasab
الحبحابى    nasab
الحبحابي    nasab
الحبرانى    nasab
الحبراني    nasab
الحبشة  nasab
الحبشى  nasab
الحبشي  nasab
الحبطى  nasab
الحبطي  nasab
الحبلى  nasab
الحبلي  nasab
الحجازى nasab
الحجازي nasab
الحجازية    nasab
الحجام  nasab
الحجبى  nasab
الحجبي  nasab
الحجرى  nasab
الحجري  nasab
الحجورى nasab
الحجوري nasab
الحداد  nasab
الحدادى nasab
الحدادي nasab
الحدانى nasab
الحداني nasab
الحدثانى    nasab
الحدثاني    nasab
الحدثى  nasab
الحدثي  nasab
الحذاء  nasab
الحرازى nasab
الحرازي nasab
الحرامى nasab
الحرامي nasab
الحرانى nasab
الحراني nasab
الحربى  nasab
الحربي  nasab
الحرسى  nasab
الحرسي  nasab
الحرشى  nasab
الحرشي  nasab
الحرقى  nasab
الحرقي  nasab
الحريرى nasab
الحريري nasab
الحزامى nasab
الحزامي nasab
الحزمى  nasab
الحزمي  nasab
الحسانى nasab
الحساني nasab
الحصار  nasab
الحصرى  nasab
الحصري  nasab
الحضرمى nasab
الحضرمي nasab
الحفرى  nasab
الحفري  nasab
الحكمى  nasab
الحكمي  nasab
الحلبى  nasab
الحلبي  nasab
الحلوانى    nasab
الحلواني    nasab
الحمال  nasab
الحمانى nasab
الحماني nasab
الحمرانى    nasab
الحمراني    nasab
الحمراوى    nasab
الحمراوي    nasab
الحمصى  nasab
الحمصي  nasab
الحميدى nasab
الحميدي nasab
الحميرى nasab
الحميري nasab
الحميرية    nasab
الحميسى nasab
الحميسي nasab
الحناط  nasab
الحنظلى nasab
الحنظلي nasab
الحنفى  nasab
الحنفي  nasab
‏الحنفىالإيادى  nasab
‏الحنفىالإيادي  nasab
الحنينى nasab
الحنيني nasab
الحوارى nasab
الحواري nasab
الحوتى  nasab
الحوتي  nasab
الحوشبى nasab
الحوشبي nasab
الحوضى  nasab
الحوضي  nasab
الحوطى  nasab
الحوطي  nasab
الحويطبى    nasab
الحويطبي    nasab
الخارجى nasab
الخارجي nasab
الخارفى nasab
الخارفي nasab
الخاركى nasab
الخاركي nasab
الخازن  nasab
الخاشتى nasab
الخاشتي nasab
الخاقانى    nasab
الخاقاني    nasab
الخبائرى    nasab
الخبائري    nasab
الخباز  nasab
الخبذعى nasab
الخبذعي nasab
الختلى  nasab
الختلي  nasab
الخثعمى nasab
الخثعمي nasab
الخثعمية    nasab
الخدرى  nasab
الخدري  nasab
الخدرية nasab
الخراز  nasab
الخراسانى   nasab
الخراساني   nasab
الخراط  nasab
الخرططى nasab
الخرططي nasab
الخرقى  nasab
الخرقي  nasab
الخريبى nasab
الخريبي nasab
الخريمى nasab
الخريمي nasab
الخزاز  nasab
الخزاعى nasab
الخزاعي nasab
الخزاعية    nasab
الخزاف  nasab
الخزرجى nasab
الخزرجي nasab
الخزرجية    nasab
الخشاب  nasab
الخشرمى nasab
الخشرمي nasab
الخشنى  nasab
الخشني  nasab
الخصى   nasab
الخصي   nasab
الخصيفى nasab
الخصيفي nasab
الخضرمى nasab
الخضرمي nasab
الخضرى  nasab
الخضري  nasab
الخطاب  nasab
الخطابى nasab
الخطابي nasab
الخطمى  nasab
الخطمي  nasab
الخفاف  nasab
الخلاطى nasab
الخلاطي nasab
الخلال  nasab
الخلقانى    nasab
الخلقاني    nasab
الخلنجى nasab
الخلنجي nasab
الخندفى nasab
الخندفي nasab
الخوارزمى   nasab
الخوارزمي   nasab
الخوارى nasab
الخواري nasab
الخواشتى    nasab
الخواشتي    nasab
الخواص  nasab
الخوزى  nasab
الخوزي  nasab
الخولانى    nasab
الخولاني    nasab
الخياط  nasab
الخيبرى nasab
الخيبري nasab
الخيوانى    nasab
الخيواني    nasab
الدؤلى  nasab
الدؤلي  nasab
الداراكانى  nasab
الداراكاني  nasab
الدارانى    nasab
الداراني    nasab
الداركانى   nasab
الداركاني   nasab
الدارمى nasab
الدارمي nasab
الدارى  nasab
الداري  nasab
الدارية nasab
الدالانى    nasab
الدالاني    nasab
الدامغانى   nasab
الدامغاني   nasab
الدباغ  nasab
الدرابجردى  nasab
الدرابجردي  nasab
الدراوردى   nasab
الدراوردي   nasab
الدرهمى nasab
الدرهمي nasab
الدستوائى   nasab
الدستوائي   nasab
الدشتكى nasab
الدشتكي nasab
الدقاق  nasab
الدقيقى nasab
الدقيقي nasab
الدلال  nasab
الدمشقى nasab
الدمشقي nasab
الدمشقيان   nasab
الدمشقية    nasab
الدندانى    nasab
الدنداني    nasab
الدهان  nasab
الدهقان nasab
الدهكى  nasab
الدهكي  nasab
الدهنى  nasab
الدهني  nasab
الدورقى nasab
الدورقي nasab
الدورى  nasab
الدوري  nasab
الدوسى  nasab
الدوسي  nasab
الدوسية nasab
الدولابى    nasab
الدولابي    nasab
الديرعاقولى nasab
الديرعاقولي nasab
الديلمى nasab
الديلمي nasab
الديلى  nasab
الديلي  nasab
الدينورى    nasab
الدينوري    nasab
الذارع  nasab
الذبحانى    nasab
الذبحاني    nasab
الذبيانى    nasab
الذبياني    nasab
الذراع  nasab
الذكوانى    nasab
الذكواني    nasab
الذمارى nasab
الذماري nasab
الذهبى  nasab
الذهبي  nasab
الذهلى  nasab
الذهلي  nasab
الذهلية nasab
الرؤاسى nasab
الرؤاسي nasab
الراذانى    nasab
الراذاني    nasab
الراذكانى   nasab
الراذكاني   nasab
الرازى  nasab
الرازي  nasab
الراسبى nasab
الراسبي nasab
الراسبية    nasab
الراسى  nasab
الراسي  nasab
الراعى  nasab
الراعي  nasab
الرافعى nasab
الرافعي nasab
الرافقى nasab
الرافقي nasab
الرام   nasab
الرامى  nasab
الرامي  nasab
الراهبى nasab
الراهبي nasab
الرباطى nasab
الرباطي nasab
الربالى nasab
الربالي nasab
الربذى  nasab
الربذي  nasab
الربضى  nasab
الربضي  nasab
الربعى  nasab
الربعي  nasab
الربيعى nasab
الربيعي nasab
الرحال  nasab
الرحبى  nasab
الرحبي  nasab
الرخامى nasab
الرخامي nasab
الردمانى    nasab
الردماني    nasab
الرزى   nasab
الرزي   nasab
الرستنى nasab
الرستني nasab
الرسعنى nasab
الرسعني nasab
الرصافى nasab
الرصافي nasab
الرعينى nasab
الرعيني nasab
الرفاعى nasab
الرفاعي nasab
الرقاشى nasab
الرقاشي nasab
الرقام  nasab
الرقى   nasab
الرقي   nasab
الرماح  nasab
الرمادى nasab
الرمادي nasab
الرمانى nasab
الرماني nasab
الرملى  nasab
الرملي  nasab
الرهاوى nasab
الرهاوي nasab
الرواجنى    nasab
الرواجني    nasab
الرواس  nasab
الرومى  nasab
الرومي  nasab
الرومية nasab
الرياحى nasab
الرياحي nasab
الرياشى nasab
الرياشي nasab
الريحانى    nasab
الريحاني    nasab
الزاهد  nasab
الزبيدى nasab
الزبيدي nasab
الزبيرى nasab
الزبيري nasab
الزجاج  nasab
الزراد  nasab
الزرقى  nasab
الزرقي  nasab
الزرقية nasab
الزعافرى    nasab
الزعافري    nasab
الزعفرانى   nasab
الزعفراني   nasab
الزمانى nasab
الزماني nasab
الزمعى  nasab
الزمعي  nasab
الزمى   nasab
الزمي   nasab
الزنبرى nasab
الزنبري nasab
الزنجارى    nasab
الزنجاري    nasab
الزهرانى    nasab
الزهراني    nasab
الزهرى  nasab
الزهري  nasab
الزهرية nasab
الزهريون    nasab
الزوفى  nasab
الزوفي  nasab
الزيات  nasab
الزيادى nasab
الزيادي nasab
الزيدية nasab
الساجى  nasab
الساجي  nasab
الساحلى nasab
الساحلي nasab
الساعدى nasab
الساعدي nasab
الساعدية    nasab
السالحينى   nasab
السالحيني   nasab
السالمى nasab
السالمي nasab
السامرى nasab
السامري nasab
السامى  nasab
السامي  nasab
الساوى  nasab
الساوي  nasab
السبأى  nasab
السبأي  nasab
السبئى  nasab
السبئي  nasab
السبائى nasab
السبائي nasab
السبخى  nasab
السبخي  nasab
السبرى  nasab
السبري  nasab
السبيعى nasab
السبيعي nasab
السجزى  nasab
السجزي  nasab
السجستانى   nasab
السجستاني   nasab
السحتنى nasab
السحتني nasab
السحولى nasab
السحولي nasab
السحيمى nasab
السحيمي nasab
السختيانى   nasab
السختياني   nasab
السدوسى nasab
السدوسي nasab
السدوسية    nasab
السدى   nasab
السدي   nasab
السراج  nasab
السراقى nasab
السراقي nasab
السرحى  nasab
السرحي  nasab
السرخسى nasab
السرخسي nasab
السرمارى    nasab
السرماري    nasab
السروجى nasab
السروجي nasab
السرى   nasab
السري   nasab
السعدى  nasab
السعدي  nasab
السعدية nasab
السعيدى nasab
السعيدي nasab
السغدى  nasab
السغدي  nasab
السقطى  nasab
السقطي  nasab
السكرى  nasab
السكري  nasab
السكسكى nasab
السكسكي nasab
السكونى nasab
السكوني nasab
السلامانى   nasab
السلاماني   nasab
السلامى nasab
السلامي nasab
السلعى  nasab
السلعي  nasab
السلفى  nasab
السلفي  nasab
السلمانى    nasab
السلماني    nasab
السلمسينى   nasab
السلمسيني   nasab
السلمى  nasab
السلمي  nasab
السلمية nasab
السلهمى nasab
السلهمي nasab
السلولى nasab
السلولي nasab
السلى   nasab
السلي   nasab
السليحى nasab
السليحي nasab
السليطى nasab
السليطي nasab
السليمى nasab
السليمي nasab
السماعى nasab
السماعي nasab
السماك  nasab
السمان  nasab
السمتى  nasab
السمتي  nasab
السمرقندى   nasab
السمرقندي   nasab
السمرى  nasab
السمري  nasab
السمسار nasab
السمعى  nasab
السمعي  nasab
السمنانى    nasab
السمناني    nasab
السنبسى nasab
السنبسي nasab
السنجارى    nasab
السنجاري    nasab
السنجى  nasab
السنجي  nasab
السندى  nasab
السندي  nasab
السهمى  nasab
السهمي  nasab
السهمية nasab
السوائى nasab
السوائي nasab
السوارقى    nasab
السوارقي    nasab
السواق  nasab
السوسى  nasab
السوسي  nasab
السويقى nasab
السويقي nasab
السيارى nasab
السياري nasab
السيبانى    nasab
السيباني    nasab
السيلحونى   nasab
السيلحوني   nasab
السيلحى nasab
السيلحي nasab
السيلحينى   nasab
السيلحيني   nasab
السينانى    nasab
السيناني    nasab
الشاعر  nasab
الشافعى nasab
الشافعي nasab
الشامى  nasab
الشامي  nasab
الشبامى nasab
الشبامي nasab
الشجرى  nasab
الشجري  nasab
الشحام  nasab
الشرعبى nasab
الشرعبي nasab
الشروى  nasab
الشروي  nasab
الشطوى  nasab
الشطوي  nasab
الشطى   nasab
الشطي   nasab
الشعبانى    nasab
الشعباني    nasab
الشعبى  nasab
الشعبي  nasab
الشعرانى    nasab
الشعراني    nasab
الشعيثى nasab
الشعيثي nasab
الشعيرى nasab
الشعيري nasab
الشقرى  nasab
الشقري  nasab
الشقيقى nasab
الشقيقي nasab
الشلاثائى   nasab
الشلاثائي   nasab
الشنائى nasab
الشنائي nasab
الشنى   nasab
الشني   nasab
الشهيدى nasab
الشهيدي nasab
الشيبانى    nasab
الشيباني    nasab
الشيرازى    nasab
الشيرازي    nasab
الشيعى  nasab
الشيعي  nasab
الشيلمانى   nasab
الشيلماني   nasab
الصائدى nasab
الصائدي nasab
الصائغ  nasab
الصاغانى    nasab
الصاغاني    nasab
الصالحى nasab
الصالحي nasab
الصباغ  nasab
الصبيحى nasab
الصبيحي nasab
الصدائى nasab
الصدائي nasab
الصدفى  nasab
الصدفي  nasab
الصراف  nasab
الصريفينى   nasab
الصريفيني   nasab
الصريمية    nasab
الصغانى nasab
الصغاني nasab
الصغير  nasab
الصفار  nasab
الصنابحى    nasab
الصنابحي    nasab
الصنعانى    nasab
الصنعاني    nasab
الصنمى  nasab
الصنمي  nasab
الصهبانى    nasab
الصهباني    nasab
الصواف  nasab
الصورى  nasab
الصوري  nasab
الصوفى  nasab
الصوفي  nasab
الصومعى nasab
الصومعي nasab
الصياد  nasab
الصيداوى    nasab
الصيداوي    nasab
الصيدلانى   nasab
الصيدلاني   nasab
الصيرفى nasab
الصيرفي nasab
الصيقل  nasab
الصينى  nasab
الصيني  nasab
الضبابى nasab
الضبابي nasab
الضبعى  nasab
الضبعي  nasab
الضبى   nasab
الضبي   nasab
الضبية  nasab
الضجيعى nasab
الضجيعي nasab
الضرارى nasab
الضراري nasab
الضرير  nasab
الضمرى  nasab
الضمري  nasab
الضنى   nasab
الضني   nasab
الطائفى nasab
الطائفي nasab
الطائى  nasab
الطائي  nasab
الطائى‏السليحى  nasab
الطائى‏السليحي  nasab
الطابخى nasab
الطابخي nasab
الطاحى  nasab
الطاحي  nasab
الطاطرى nasab
الطاطري nasab
الطالقانى   nasab
الطالقاني   nasab
الطانجى nasab
الطانجي nasab
الطبرانى    nasab
الطبراني    nasab
الطبرى  nasab
الطبري  nasab
الطبيب  nasab
‏الطحان nasab
الطرائفى    nasab
الطرائفي    nasab
الطرابلسى   nasab
الطرابلسي   nasab
الطرسوسى    nasab
الطرسوسي    nasab
الطريثيثى   nasab
الطريثيثي   nasab
الطريقى nasab
الطريقي nasab
الطفاوى nasab
الطفاوي nasab
الطلاس  nasab
الطلحى  nasab
الطلحي  nasab
الطنافسى    nasab
الطنافسي    nasab
الطنبذى nasab
الطنبذي nasab
الطهرانى    nasab
الطهراني    nasab
الطهوى  nasab
الطهوي  nasab
الطوسانى    nasab
الطوساني    nasab
الطوسى  nasab
الطوسي  nasab
الطويل  nasab
الطيالسى    nasab
الطيالسي    nasab
الظفرى  nasab
الظفري  nasab
الظهرى  nasab
الظهري  nasab
العائذى nasab
العائذي nasab
العائشى nasab
العائشي nasab
العابد  nasab
العابدى nasab
العابدي nasab
العامرى nasab
العامري nasab
العامرية    nasab
العاملى nasab
العاملي nasab
العبادانى   nasab
العباداني   nasab
العبادى nasab
العبادي nasab
العباسى nasab
العباسي nasab
العبدرى nasab
العبدري nasab
العبدرية    nasab
العبدى  nasab
العبدي  nasab
العبسى  nasab
العبسي  nasab
العبسية nasab
العبشمى nasab
العبشمي nasab
العبشمية    nasab
العتابى nasab
العتابي nasab
العتقى  nasab
العتقي  nasab
العتكى  nasab
العتكي  nasab
العتكية nasab
العتوارى    nasab
العتواري    nasab
العثمانى    nasab
العثماني    nasab
العجلانى    nasab
العجلاني    nasab
العجلى  nasab
العجلي  nasab
العجلىالتميمى   nasab
العجلىالتميمي   nasab
العجمى  nasab
العجمي  nasab
العجيفى nasab
العجيفي nasab
العدنى  nasab
العدني  nasab
العدوانى    nasab
العدواني    nasab
العدوى  nasab
العدوي  nasab
العدوية nasab
العذرى  nasab
العذري  nasab
العراقى nasab
العراقي nasab
العرجى  nasab
العرجي  nasab
العرزمى nasab
العرزمي nasab
العرضى  nasab
العرضي  nasab
العرعرى nasab
العرعري nasab
العرفى  nasab
العرفي  nasab
العرنى  nasab
العرني  nasab
العروقى nasab
العروقي nasab
العريانى    nasab
العرياني    nasab
العريجى nasab
العريجي nasab
العزربى nasab
العزربي nasab
العسال  nasab
العسقلانى   nasab
العسقلاني   nasab
العسكرى nasab
العسكري nasab
العصاب  nasab
العصار  nasab
العصرى  nasab
العصري  nasab
العصفرى nasab
العصفري nasab
العطار  nasab
العطاردى    nasab
العطاردي    nasab
العفانى nasab
العفاني nasab
العفيفى nasab
العفيفي nasab
العقدى  nasab
العقدي  nasab
العقيلى nasab
العقيلي nasab
العقيلى‏العبدى  nasab
العقيلى‏العبدي  nasab
العكاشى nasab
العكاشي nasab
العكبرى nasab
العكبري nasab
العكلى  nasab
العكلي  nasab
العكى   nasab
العكي   nasab
العلاف  nasab
العلقى  nasab
العلقي  nasab
العلوى  nasab
العلوي  nasab
العمانى nasab
العماني nasab
العمرى  nasab
العمري  nasab
العمى   nasab
العمي   nasab
العميرى nasab
العميري nasab
العنبرى nasab
العنبري nasab
العنبرية    nasab
العنزى  nasab
العنزي  nasab
العنسى  nasab
العنسي  nasab
العنقزى nasab
العنقزي nasab
‏العنى  nasab
‏العني  nasab
العوذى  nasab
العوذي  nasab
العوصى  nasab
العوصي  nasab
العوفى  nasab
العوفي  nasab
العوقى  nasab
العوقي  nasab
العوهى  nasab
العوهي  nasab
العيذى  nasab
العيذي  nasab
العيشى  nasab
العيشي  nasab
الغازى  nasab
الغازي  nasab
الغاضرى nasab
الغاضري nasab
الغاضرية    nasab
الغافقى nasab
الغافقي nasab
الغامدى nasab
الغامدي nasab
الغبرى  nasab
الغبري  nasab
الغبيرى nasab
الغبيري nasab
الغدانى nasab
الغداني nasab
الغريرى nasab
الغريري nasab
الغزال  nasab
الغزى   nasab
الغزي   nasab
الغسانى nasab
الغساني nasab
الغطفان nasab
الغطفانى    nasab
الغطفاني    nasab
الغطيفى nasab
الغطيفي nasab
الغفارى nasab
الغفاري nasab
الغفارية    nasab
الغنوى  nasab
الغنوي  nasab
الغنوية nasab
الغوثى  nasab
الغوثي  nasab
الغيلانى    nasab
الغيلاني    nasab
الفاخورى    nasab
الفاخوري    nasab
الفارسى nasab
الفارسي nasab
‏الفاكندى   nasab
‏الفاكندي   nasab
الفتيانى    nasab
الفتياني    nasab
الفحام  nasab
الفدكى  nasab
الفدكي  nasab
الفراء  nasab
الفرائضى    nasab
الفرائضي    nasab
الفراديسى   nasab
الفراديسي   nasab
الفراسى nasab
الفراسي nasab
الفراسية    nasab
الفراهيدى   nasab
الفراهيدي   nasab
الفرسى  nasab
الفرسي  nasab
الفروى  nasab
الفروي  nasab
الفريابى    nasab
الفريابي    nasab
الفزارى nasab
الفزاري nasab
الفزارية    nasab
الفساطيطى   nasab
الفساطيطي   nasab
الفسوى  nasab
الفسوي  nasab
الفطرى  nasab
الفطري  nasab
الفقعسى nasab
الفقعسي nasab
الفقير  nasab
الفقيمى nasab
الفقيمي nasab
الفقيه  nasab
الفلاس  nasab
الفلسطينى   nasab
الفلسطيني   nasab
الفهرى  nasab
الفهري  nasab
الفهرية nasab
الفهمى  nasab
الفهمي  nasab
الفوزى  nasab
الفوزي  nasab
الفيدى  nasab
الفيدي  nasab
القارظى nasab
القارظي nasab
القارى  nasab
القاري  nasab
القارىء nasab
القاص   nasab
القاضى  nasab
القاضي  nasab
القافلائى   nasab
القافلائي   nasab
القبائى nasab
القبائي nasab
القبانى nasab
القباني nasab
القبضى  nasab
القبضي  nasab
القبطى  nasab
القبطي  nasab
القبطية nasab
القبى   nasab
القبي   nasab
القتاب  nasab
القتات  nasab
القتبانى    nasab
القتباني    nasab
القتيرى nasab
القتيري nasab
القحطانى    nasab
القحطاني    nasab
القدرى  nasab
القدري  nasab
القدسى  nasab
القدسي  nasab
القرادى nasab
القرادي nasab
القرارى nasab
القراري nasab
القراطيسى   nasab
القراطيسي   nasab
القراظ  nasab
القربى  nasab
القربي  nasab
القردوانى   nasab
القردواني   nasab
القردوسى    nasab
القردوسي    nasab
القرش   nasab
القرشى  nasab
القرشي  nasab
القرشية nasab
القرطبى nasab
القرطبي nasab
القرظى  nasab
القرظي  nasab
القرقسانى   nasab
القرقساني   nasab
القرنى  nasab
القرني  nasab
القرى   nasab
القري   nasab
القزاز  nasab
القزوينى    nasab
القزويني    nasab
القسام  nasab
القسرى  nasab
القسري  nasab
القسملى nasab
القسملي nasab
القشيرى nasab
القشيري nasab
القصاب  nasab
‏القصار nasab
القصرى  nasab
القصري  nasab
القصير  nasab
القضاعى nasab
القضاعي nasab
القطان  nasab
القطربلى    nasab
القطربلي    nasab
القطعى  nasab
القطعي  nasab
القطوانى    nasab
القطواني    nasab
القطيعى nasab
القطيعي nasab
القعنبى nasab
القعنبي nasab
القلاء  nasab
القلانسى    nasab
القلانسي    nasab
القلورى nasab
القلوري nasab
القماح  nasab
القمى   nasab
القمي   nasab
القناد  nasab
القنبارى    nasab
القنباري    nasab
القنسرينى   nasab
القنسريني   nasab
القنطرى nasab
القنطري nasab
القنوى  nasab
القنوي  nasab
القهستانى   nasab
القهستاني   nasab
القهندزى    nasab
القهندزي    nasab
القواريرى   nasab
القواريري   nasab
القواس  nasab
القومسى nasab
القومسي nasab
القيسرانى   nasab
القيسراني   nasab
القيسى  nasab
القيسي  nasab
القيسية nasab
القينى  nasab
القيني  nasab
الكابلى nasab
الكابلي nasab
الكاتب  nasab
الكاهلى nasab
الكاهلي nasab
الكحال  nasab
الكديمى nasab
الكديمي nasab
الكرابيسى   nasab
الكرابيسي   nasab
الكراجكى    nasab
الكراجكي    nasab
الكراشكى    nasab
الكراشكي    nasab
الكردى  nasab
الكردي  nasab
الكرمانى    nasab
الكرماني    nasab
الكريزى nasab
الكريزي nasab
الكسائى nasab
الكسائي nasab
الكسى   nasab
الكسي   nasab
الكشميهنى   nasab
الكشميهني   nasab
الكعبى  nasab
الكعبي  nasab
الكعبية nasab
الكفرسوسى   nasab
الكفرسوسي   nasab
الكلابى nasab
الكلابي nasab
الكلاعى nasab
الكلاعي nasab
الكلبى  nasab
الكلبي  nasab
الكلفى  nasab
الكلفي  nasab
الكلوذانى   nasab
الكلوذاني   nasab
الكلينى nasab
الكليني nasab
الكناسى nasab
الكناسي nasab
الكنانى nasab
الكناني nasab
الكندى  nasab
الكندي  nasab
الكندية nasab
الكهيلى nasab
الكهيلي nasab
الكوخارانى  nasab
الكوخاراني  nasab
الكوسج  nasab
الكوفى  nasab
الكوفي  nasab
الكوفية nasab
الكيخارانى  nasab
الكيخاراني  nasab
اللآل   nasab
اللؤلؤى nasab
اللؤلؤي nasab
اللاحونى    nasab
اللاحوني    nasab
اللاذقى nasab
اللاذقي nasab
اللانى  nasab
اللاني  nasab
اللبقى  nasab
اللبقي  nasab
اللحام  nasab
اللخمى  nasab
اللخمي  nasab
اللخمية nasab
اللغوى  nasab
اللغوي  nasab
اللقيطى nasab
اللقيطي nasab
اللهبى  nasab
اللهبي  nasab
الليثى  nasab
الليثي  nasab
الليثية nasab
المؤدب  nasab
المأربى nasab
المأربي nasab
الماجشون    nasab
الماخونى    nasab
الماخوني    nasab
المازنى nasab
المازني nasab
المازنية    nasab
الماسرجسى   nasab
الماسرجسي   nasab
الماصر  nasab
الماكيانى   nasab
الماكياني   nasab
المالكى nasab
المالكي nasab
المباركى    nasab
المباركي    nasab
المتعى  nasab
المتعي  nasab
المثرودى    nasab
المثرودي    nasab
المجاشعى    nasab
المجاشعي    nasab
المجاشعية   nasab
المجالدى    nasab
المجالدي    nasab
المجمر  nasab
المحاربى    nasab
‎المحاربي   nasab
المحاسبى    nasab
المحاسبي    nasab
المحاملى    nasab
المحاملي    nasab
المحتسب nasab
المحرى  nasab
المحري  nasab
المحلمى nasab
المحلمي nasab
المخدجى nasab
المخدجي nasab
المخرمى nasab
المخرمي nasab
المخزومى    nasab
المخزومي    nasab
المخزومية   nasab
المدائنى    nasab
المدائني    nasab
المدرى  nasab
المدري  nasab
المدعى  nasab
المدعي  nasab
المدلجى nasab
المدلجي nasab
المدنى  nasab
المدني  nasab
‏المدنى‏المصرى  nasab
‏المدنى‏المصري  nasab
المدنية nasab
المديبرى    nasab
المديبري    nasab
المدينى nasab
المديني nasab
المذحجى nasab
المذحجي nasab
المرئى  nasab
المرئي  nasab
المرادى nasab
المرادي nasab
المراغى nasab
المراغي nasab
المربدى nasab
المربدي nasab
المرهبى nasab
المرهبي nasab
المروذى nasab
المروذي nasab
المروزى nasab
المروزي nasab
المرى   nasab
المري   nasab
المرية  nasab
المزرفى nasab
المزرفي nasab
المزنى  nasab
المزني  nasab
المزنية nasab
المستملى    nasab
المستملي    nasab
المسروقى    nasab
المسروقي    nasab
المسعودى    nasab
المسعودي    nasab
المسلى  nasab
المسلي  nasab
المسمعى nasab
المسمعي nasab
المسندى nasab
المسندي nasab
المسورى nasab
المسوري nasab
المسيبى nasab
المسيبي nasab
المشرقى nasab
المشرقي nasab
المشقى  nasab
المشقي  nasab
المصاحفى    nasab
المصاحفي    nasab
المصرى  nasab
المصري  nasab
المصريان    nasab
المصطلقى    nasab
المصطلقي    nasab
المصطلقية   nasab
المصيصى nasab
المصيصي nasab
المطرز  nasab
المطرفى nasab
المطرفي nasab
المطرقى nasab
المطرقي nasab
المطرى  nasab
المطري  nasab
المطلبى nasab
المطلبي nasab
المطوعى nasab
المطوعي nasab
المعافرى    nasab
المعافري    nasab
المعافرية   nasab
المعاوى nasab
المعاوي nasab
المعبر  nasab
المعدل  nasab
المعشارى    nasab
المعشاري    nasab
المعقرى nasab
المعقري nasab
المعقلى nasab
المعقلي nasab
المعلم  nasab
المعمرى nasab
المعمري nasab
المعنى  nasab
المعني  nasab
المعولى nasab
المعولي nasab
المعيطى nasab
المعيطي nasab
المغربى nasab
المغربي nasab
المفلوج nasab
المقابرى    nasab
المقابري    nasab
المقبرى nasab
المقبري nasab
المقدسى nasab
المقدسي nasab
المقدمى nasab
المقدمي nasab
المقرائى    nasab
المقرائي    nasab
المقرىء nasab
المقسمى nasab
المقسمي nasab
المقوم  nasab
المقومى nasab
المقومي nasab
المكتب  nasab
المكحولى    nasab
المكحولي    nasab
المكفوف nasab
المكى   nasab
المكي   nasab
المكية  nasab
الملائى nasab
الملائي nasab
الملجكانى   nasab
الملجكاني   nasab
الملطى  nasab
الملطي  nasab
المليكى nasab
المليكي nasab
المنارى nasab
المناري nasab
المنبجى nasab
المنبجي nasab
المنبهى nasab
المنبهي nasab
المنجنيقى   nasab
المنجنيقي   nasab
المنجوفى    nasab
المنجوفي    nasab
المنقرى nasab
المنقري nasab
المنكدرى    nasab
المنكدري    nasab
المهرقانى   nasab
المهرقاني   nasab
المهرى  nasab
المهري  nasab
المهلبى nasab
المهلبي nasab
الموصلى nasab
الموصلي nasab
الموقرى nasab
الموقري nasab
الميتمى nasab
الميتمي nasab
الميسرى nasab
الميسري nasab
الميمونى    nasab
الميموني    nasab
الناجى  nasab
الناجي  nasab
الناشرى nasab
الناشري nasab
الناعطى nasab
الناعطي nasab
الناقد  nasab
الناقط  nasab
النبال  nasab
النبطى  nasab
النبطي  nasab
النبهانى    nasab
النبهاني    nasab
النجار  nasab
النجارى nasab
النجاري nasab
النجارية    nasab
النجرانى    nasab
النجراني    nasab
النحاس  nasab
النحوى  nasab
النحوي  nasab
النخاس  nasab
النخعى  nasab
النخعي  nasab
الندبى  nasab
الندبي  nasab
النرسى  nasab
النرسي  nasab
النرمقى nasab
النرمقي nasab
النسائى nasab
النسائي nasab
النسابة nasab
النسوى  nasab
النسوي  nasab
النشائى nasab
النشائي nasab
النشاستجى   nasab
النشاستجي   nasab
النشيطى nasab
النشيطي nasab
النصرى  nasab
النصري  nasab
النصيبى nasab
النصيبي nasab
النضرويى    nasab
النضرويي    nasab
النضرى  nasab
النضري  nasab
النضيرية    nasab
النفيلى nasab
النفيلي nasab
النقاش  nasab
النكرى  nasab
النكري  nasab
النمرى  nasab
النمري  nasab
النميرى nasab
النميري nasab
النهاوندى   nasab
النهاوندي   nasab
النهدى  nasab
النهدي  nasab
النهروانى   nasab
النهرواني   nasab
النهشلى nasab
النهشلي nasab
النهمى  nasab
النهمي  nasab
النواء  nasab
النوبى  nasab
النوبي  nasab
النوفلى nasab
النوفلي nasab
النوفلية    nasab
النيزكى nasab
النيزكي nasab
النيسابورى  nasab
النيسابوري  nasab
النيلى  nasab
النيلي  nasab
الهاشمى nasab
الهاشمي nasab
الهاشمية    nasab
الهبارى nasab
الهباري nasab
الهجرى  nasab
الهجري  nasab
الهجيمى nasab
الهجيمي nasab
الهدادى nasab
الهدادي nasab
الهديرى nasab
الهديري nasab
الهذلى  nasab
الهذلي  nasab
الهذلية nasab
الهرثمى nasab
الهرثمي nasab
الهروى  nasab
الهروي  nasab
الهسنجانى   nasab
الهسنجاني   nasab
الهفانى nasab
الهفاني nasab
الهلالى nasab
الهلالي nasab
الهلالية    nasab
الهمدانى    nasab
الهمداني    nasab
الهمذانى    nasab
الهمذاني    nasab
الهنائى nasab
الهنائي nasab
الهوزنى nasab
الهوزني nasab
الهياجى nasab
الهياجي nasab
الوائلى nasab
الوائلي nasab
الوابصى nasab
الوابصي nasab
الواثلى nasab
الواثلي nasab
الوادعى nasab
الوادعي nasab
الوادى  nasab
الوادي  nasab
الواسطى nasab
الواسطي nasab
الواشحى nasab
الواشحي nasab
الواقدى nasab
الواقدي nasab
الواقفى nasab
الواقفي nasab
الوالبى nasab
الوالبي nasab
الوحاظى nasab
الوحاظي nasab
الوحيدى nasab
الوحيدي nasab
الوراق  nasab
الورتنيسى   nasab
الورتنيسي   nasab
الوردانى    nasab
الورداني    nasab
الوركانى    nasab
الوركاني    nasab
الوزان  nasab
الوشاء  nasab
الوشقية nasab
الوصابى nasab
الوصابي nasab
الوصابية    nasab
الوصافى nasab
الوصافي nasab
الوضاحى nasab
الوضاحي nasab
الوعلانى    nasab
الوعلاني    nasab
الوقاصى nasab
الوقاصي nasab
الوكيعى nasab
الوكيعي nasab
الوهبى  nasab
الوهبي  nasab
الوهبيلى    nasab
الوهبيلي    nasab
اليافعى nasab
اليافعي nasab
اليامى  nasab
اليامي  nasab
اليحصبى nasab
اليحصبي nasab
اليحمدى nasab
اليحمدي nasab
اليربوعى    nasab
اليربوعي    nasab
اليزنى  nasab
اليزني  nasab
اليسارى nasab
اليساري nasab
اليسارية    nasab
اليشكرى nasab
اليشكري nasab
اليعمرى nasab
اليعمري nasab
اليمامى nasab
اليمامي nasab
اليمانى nasab
اليماني nasab
اليمني  nasab
بن البخترى  nasab
بن البختري  nasab
بن الجارودى nasab
بن الجارودي nasab
بن الحضرمى  nasab
بن الحضرمي  nasab
بن الحوارى  nasab
بن الحواري  nasab
بن السرى    nasab
بن السري    nasab
بني أسد بن خزيمة    nasab
بني النجار  nasab
بني زريق    nasab
حليف الأنصار    nasab
حليف بنى    nasab
حليف بني    nasab
قاضيها  nasab
مزينة   nasab
أبان    nom
إبراهيم nom
أبرة    nom
أبي الزناد  nom
أبي بكر nom
أبي ذئب nom
أبي نمر nom
أبيض    nom
آثال    nom
أثال    nom
أجلح    nom
أحزاب   nom
أحمد    nom
أحمر    nom
أخضر    nom
أدرع    nom
إدريس   nom
آدم nom
أربد    nom
أربدة   nom
أرطاة   nom
أرقم    nom
أزداد   nom
أزهر    nom
إساف    nom
أسامة   nom
أسباط   nom
إسحاق   nom
أسد nom
إسرائيل nom
أسعد    nom
أسلم    nom
أسماء   nom
إسماعيل nom
أسمر    nom
أسيد    nom
أسير    nom
أسيرة   nom
أشجع    nom
أشعث    nom
أشكاب   nom
إشكاب   nom
أشهل    nom
أصبغ    nom
أصله من دمشق    nom
أصيهب   nom
أعرابى  nom
أعرابي  nom
أعين    nom
أفلت    nom
أفلح    nom
أقرع    nom
أقرم    nom
أكيمة   nom
أمامة   nom
أمة nom
أمة الله    nom
أمة الواحد  nom
أمية    nom
أميمة   nom
أمينة   nom
أنس nom
أنسا    nom
أنيس    nom
أنيسة   nom
إهاب    nom
أهبان   nom
أوس nom
أوسط    nom
أوفى    nom
أوفي    nom
أويس    nom
إياد    nom
إياس    nom
أيفع    nom
أيمن    nom
أيوب    nom
ا الفارعة   nom
ا لنضر  nom
احمد    nom
ازداذبنداذ  nom
اسلم    nom
اسماعيل nom
ال دخشن nom
الأحوص  nom
الأحول  nom
الأخضر  nom
الأخنس  nom
الأدرع  nom
الأردنى nom
الأردني nom
الأزدى  nom
الأزدي  nom
الأزرق  nom
الأزهر  nom
الأسدى  nom
الأسدي  nom
الأسقع  nom
الأسلمى nom
الأسلمي nom
الأسود  nom
الأشج   nom
الأشعث  nom
الأصغر  nom
الأعرج  nom
الأعرج أبو زكريا    nom
الأعمش  nom
الأعمى  nom
الأعمي  nom
الأعمى أبو عبد الرحمن   nom
الأعور  nom
الأغر   nom
الأفطس  nom
الأكبر  nom
الألهانى أبو سلام   nom
الأمير  nom
الأمير أبو سعيد nom
الأنبارى    nom
الأنباري    nom
الأنصارى    nom
الأنصاري    nom
الأودى  nom
الأودي  nom
الأوزاعي    nom
الأوسط  nom
الإيادى nom
الإيادي nom
الاحنف  nom
البجلى  nom
البجلي  nom
البحترى nom
البحتري nom
البخترى nom
البختري nom
البدى أبو أسيد  nom
البراء  nom
البراز  nom
البريد  Nom
البصرى  nom
البصري  nom
البهبذان    nom
البهرانى    nom
البهراني    nom
البية   nom
البير   nom
# التاجر    nom
التجيبى nom
التجيبي nom
التلب   nom
التميمى nom
التميمي nom
التيمى  nom
التيمي  nom
الثعلبى nom
الثعلبي nom
الجارود nom
الجراح  nom
الجعد   nom
الجعفى  nom
الجعفي  nom
الجلاح  nom
الجلاس  nom
الجهدمة nom
الحارث  nom
الحارثى nom
الحارثي nom
الحاسب  nom
الحباب  nom
الحجاج  nom
الحجازى nom
الحجازي nom
الحداد  nom
الحر    nom
الحرث   nom
الحسن   nom
الحسين  nom
الحصين  nom
الحكم   nom
الحكيم  nom
الحميد  nom
الحنفى  nom
الحنفي  nom
الحويرث nom
الخزاعى nom
الخزاعي nom
الخزرج  nom
الخشخاش nom
الخصيب  nom
الخضر   nom
الخليل  nom
الدارقطني   nom
الدخيشن nom
الدخيل  nom
الدمشقى nom
الدمشقي nom
الدوسى  nom
الدوسي  nom
الذارع  nom
الذهلى  nom
الذهلي  nom
الرباب  nom
الربيع  nom
الرحبى  nom
الرحبي  nom
الرقى   nom
الرقي   nom
الرماح  nom
الرميصاء خالة أنس   nom
الزبرقان    nom
الزبير  nom
الزنجى  nom
الزنجي  nom
الزهري  nom
السائب  nom
السائح  nom
السحماء سهيل    nom
السرى   nom
السري   nom
السعدى  nom
السعدي  nom
السفاح  nom
السكن   nom
السكين  Nom
السليحى الحمصى  nom
السليحى الحمصي  nom
السمط   nom
السميدع nom
الشامى  nom
الشامي  nom
الشريد  nom
الشفاء  nom
الصائغ  nom
الصامت  nom
الصباح  nom
الصباغ  nom
الصديق  nom
الصعب   nom
الصعق   nom
الصغرى  nom
الصغري  nom
الصغير  nom
الصغير يزيد nom
الصقعب  nom
الصلت   nom
الصماء  nom
الصنابح nom
الصواب أبو اليسر    nom
الصيدنانى   nom
الصيدناني   nom
الضحاك  nom
الضرير  nom
الضريس  nom
الطحان  nom
الطفيل  nom
العائشى nom
العائشي nom
العاص   nom
العالية nom
العامرى nom
العامري nom
العباس  nom
العجلى  nom
العجلي  nom
العداء  nom
العرس   nom
العريان nom
العطار  nom
العكلى أبو إسحاق التمار nom
العلاء  nom
العلاف  nom
العمرى  nom
العمري  nom
العنزى  nom
العنزي  nom
العنى   nom
العني   nom
العوام  nom
العيزار nom
العيشى  nom
العيشي  nom
الغريف  nom
الغميصاء    nom
الفأفاء nom
الفاكه  nom
الفريعة nom
الفضل   nom
القارىء nom
القاسم  nom
القاص   nom
القرد   nom
القرشى  nom
القرشي  nom
القرظ   nom
القصاب  nom
القعقاع nom
الكاتب  nom
الكاهن  nom
الكشى   nom
الكشي   nom
الكنانى nom
الكناني nom
اللآل   nom
اللحام  nom
الليث   nom
الماضى  nom
الماضي  nom
المتصر  nom
المثنى  nom
المثني  nom
المجاشعى    nom
المجاشعي    nom
المجبر  nom
المختار nom
المدنى  nom
المدني  nom
المرجى  nom
المرزبان    nom
المروزى nom
المروزي nom
المزي   nom
المستمر nom
المستنير    nom
المستورد    nom
المسور  nom
المسيب  nom
المشمعل nom
المصرى  nom
المصري  nom
المطلب  nom
المطوس  nom
المعافى nom
المعافي nom
المعتمر nom
المعرور nom
المعلم  nom
المعنى  nom
المعني  nom
المغلس  nom
المغيرة nom
المفتى  nom
المفتي  nom
المفضل  nom
المقداد nom
المقدام nom
المقرىء nom
المنذر  nom
المنذر أبو يحيى nom
المنذر أبو يحيي nom
المنكدر nom
المنهال nom
المنيب  nom
المهاجر nom
المهلب  nom
الموفق  nom
النباش  nom
النجاشي nom
النزال  nom
النسوى  nom
النسوي  nom
النضر   nom
النعمان nom
النمر   nom
النميرى nom
النميري nom
النهاس  nom
النواس  nom
الهاد   nom
الهذلى  nom
الهذلي  nom
الهرماس nom
الهرمزان    nom
الهيثم  nom
الوراق  nom
الوصابى nom
الوصابي nom
الوضاح  nom
الوضين  nom
الوليد  nom
اليحمدى أبو غسان    nom
اليسع   nom
اليشكرى nom
اليشكري nom
اليمانى nom
اليماني nom
امرأة من بنى غفار   nom
انس nom
باذام   nom
باذان   nom
بجير    nom
بجينة   nom
بحر nom
بحير    nom
بدر nom
بدرة    nom
بدية    nom
بديل    nom
برد nom
بردان   nom
برقان   nom
بركان   nom
بركة    nom
برمة    nom
بريد    nom
بريدة   nom
بريرة   nom
بزيع    nom
بسام    nom
بسر nom
بسرة    nom
بسطام   nom
بشار    nom
بشر nom
بشير    nom
بصرة    nom
بعجة    nom
بقية    nom
بكار    nom
بكر nom
بكرة    nom
بكير    nom
بلاد    nom
بلال    nom
بلالا   nom
بلج nom
بليل    nom
بنانة   nom
بنانة مولاة عبد الرحمن  nom
بنة nom
بهدلة   nom
بهز nom
بهلول   nom
بهية    nom
بهية مولاة عائشة    nom
بهيسة   nom
بهيمة   nom
بور nom
بياع الأقتاب    nom
بيان    nom
بيهس    nom
تبيع    nom
تليد    nom
تميم    nom
توبة    nom
تيم الرباب  nom
ثابت    nom
ثابتا   nom
ثبات    nom
ثعلبة   nom
ثمامة   nom
ثواب    nom
ثوبان   nom
ثور nom
ثوير    nom
جابان   nom
جابر    nom
جابرا   nom
جارية   nom
جالة    nom
جامع    nom
جبارة   nom
جبر nom
جبريل   nom
جبلة    nom
جبير    nom
جبيرة   nom
جحادة   nom
جحش nom
جدامة   nom
جدته    nom
جدتها   nom
جده nom
جرهد    nom
جرول    nom
جرى nom
جري nom
جريج    nom
جريح    nom
جرير    nom
جريرا   nom
جسر nom
جسرة    nom
جشم nom
جعثل    nom
جعدة    nom
جعفر    nom
جعيل    nom
جمهان   nom
جميع    nom
جميل    nom
جميلة   nom
جنادة   nom
جنبذ    nom
جندب    nom
جندب الخير  nom
جندرة   nom
جندل    nom
جنيد    nom
جهضم    nom
جهم nom
جهيمة   nom
جواب    nom
جودان   nom
جون nom
جويرية  nom
حابس    nom
حاتم    nom
حاجب    nom
حارثة   nom
حازم    nom
حاضر    nom
حاطب    nom
حامد    nom
حبابة   nom
حبان    nom
حبة nom
حبشى    nom
حبشي    nom
حبيب    nom
حبيبة   nom
حبيش    nom
حجاج    nom
حجر nom
حجز nom
حجية    nom
حجير    nom
حجين    nom
حدرد    nom
حديج    nom
حدير    nom
حذافة   nom
حذلم    nom
حذيفة   nom
حذيم    nom
حرام    nom
حرب nom
حرة nom
حرملة   nom
حرمى    nom
حرمي    nom
حريث    nom
حريز    nom
حريش    nom
حريف    nom
حزام    nom
حزم nom
حزن nom
حزور    nom
حسام    nom
حسان    nom
حسل nom
حسن nom
حسناء   nom
حسيل    nom
حسين    nom
حشرج    nom
حصن nom
حصين    nom
حضرمى   nom
حضرمي   nom
حضين    nom
حطان    nom
حفص nom
حفصة    nom
حكام    nom
حكيم    nom
حكيمة   nom
حماد    nom
حمادا   nom
حمان    nom
حمران   nom
حمزة    nom
حمل nom
حمنة    nom
حميدا   nom
حميدة   nom
حمير    nom
حميرى   nom
حميري   nom
حميضة   nom
حميل    nom
حميمة   nom
حنان    nom
حنبل    nom
حنش nom
حنطب    nom
حنظلة   nom
حنيف    nom
حنيفة   nom
حنين    nom
حواء    nom
حوثرة   nom
حوشب    nom
حوى nom
حوي nom
حويطب   nom
حى  nom
حياش    nom
حيان    nom
حية nom
حيوان   nom
حيوة    nom
حيى nom
حيي nom
خارجة   nom
خازم    nom
خالد    nom
خالدة   nom
خباب    nom
خبيب    nom
خثيم    nom
خداش    nom
خدرة    nom
خديج    nom
خرشة    nom
خريم    nom
خزيمة   nom
خشرم    nom
خشف nom
خشيش    nom
خصيف    nom
خصيفة   nom
خطاب    nom
خفاف    nom
خلاد    nom
خلاس    nom
خليد    nom
خليفة   nom
خميل    nom
خنساء   nom
خوات    nom
خولة    nom
خويلة   nom
خويلد   nom
خيار    nom
خيثمة   nom
خيرة    nom
خيرة مولاة  nom
خيوان   nom
دارج    nom
دارم    nom
داود    nom
دثار    nom
دحيبة   nom
دحية    nom
دخين    nom
درست    nom
درع nom
دغفل    nom
دفاع    nom
دقرة    nom
دكين    nom
دلهم    nom
دهثم    nom
دويد    nom
ديسم    nom
ديلم    nom
دينار   nom
ذؤيب    nom
ذر  nom
ذرع nom
ذريح    nom
ذكوان   nom
ذهيل    nom
ذو الغرة    nom
ذو اللحية   nom
ذو مخبر nom
ذو مخمر nom
ذواد    nom
ذى الرمحين  nom
ذيال    nom
ذيخ nom
رؤبة    nom
رؤيبة   nom
رائطة   nom
راشد    nom
رافع    nom
رباح    nom
ربعى    nom
ربعي    nom
ربيع    nom
ربيعة   nom
رجاء    nom
رحيل    nom
رداد    nom
رديح    nom
رزام    nom
رزيق    nom
رزين    nom
رشدين   nom
رشيد    nom
رفاعة   nom
رفدة    nom
رفيدة   nom
رفيع    nom
رقبة    nom
رقية    nom
ركانة   nom
ركين    nom
رمح nom
رملة    nom
رميثة   nom
رميح    nom
رميلة   nom
رهم nom
رواد    nom
روح nom
رويفع   nom
رى  nom
ري  nom
رياح    nom
ريحان   nom
ريطة    nom
زائدة   nom
زاذان   nom
زارع    nom
زافر    nom
زاهر    nom
زبان    nom
زبيب    nom
زبيد    nom
زر  nom
زرارة   nom
زربى    nom
زربي    nom
زرعة    nom
زريع    nom
زريق    nom
زفر nom
زكريا   nom
زكرياء  nom
زمعة    nom
زميل    nom
زنباع   nom
زنفل    nom
زهدم    nom
زهرة    nom
زهره    nom
زهير    nom
زوجته   nom
زياد    nom
زيادة   nom
زيد nom
زيد مناة    nom
زينب    nom
سائبة   nom
سابط    nom
سابق    nom
سابور   nom
سارة    nom
سالم    nom
سالما   nom
سباع    nom
سبرة    nom
سبيع    nom
سبيعة   nom
سحامة   nom
سحيم    nom
سخبرة   nom
سراء    nom
سراج    nom
سرار    nom
سراقة   nom
سريج    nom
سريع    nom
سس  nom
سعاد    nom
سعد nom
سعدان   nom
سعدى    nom
سعدي    nom
سعر nom
سعوة    nom
سعيد    nom
سعيد سعيد   nom
سعيدا   nom
سعير    nom
سفيان   nom
سكين    nom
سلام    nom
سلامة   nom
سلمان   nom
سلمة    nom
سلمى    nom
سلمي    nom
سليط    nom
سليم    nom
سليمان  nom
سليمان الأسود   nom
سماك    nom
سمرة    nom
سمعان   nom
سملى    nom
سمى nom
سمي nom
سمية    nom
سمير    nom
سميط    nom
سميع    nom
سنان    nom
سنبر    nom
سنين    nom
سهاب    nom
سهل nom
سهلة    nom
سهم nom
سهيل    nom
سواء    nom
سواد    nom
سوادة   nom
سوار    nom
سودة    nom
سويد    nom
سويدة   nom
سيار    nom
سياه    nom
سيدان   nom
سيرين   nom
سيف nom
شاذ nom
شبابة   nom
شباك    nom
شبة nom
شبث nom
شبل nom
شبيب    nom
شبيل    nom
شتير    nom
شجاع    nom
شداد    nom
شراحيل  nom
شرحبيل  nom
شرقى    nom
شرقي    nom
شريح    nom
شريق    nom
شريك    nom
شعبة    nom
شعثاء   nom
شعيب    nom
شعيث    nom
شفعة    nom
شفى nom
شفي nom
شقيق    nom
شكل nom
شمر nom
شمعون   nom
شمغون   nom
شمير    nom
شميسة   nom
شميط    nom
شميل    nom
شنتم    nom
شهاب    nom
شهر nom
شونير   nom
شويس    nom
شيبان   nom
شيبة    nom
شيرزاد  nom
شييم    nom
صاعد    nom
صالح    nom
صبيح    nom
صخر nom
صدقة    nom
صدى nom
صدي nom
صرد nom
صعصعة   nom
صفوان   nom
صفية    nom
صلة nom
صليح    nom
صميتة   nom
صهبان   nom
صهبة    nom
صهيب    nom
صهيبة   nom
صيفى    nom
صيفي    nom
ضبارة   nom
ضباعة   nom
ضبة nom
ضبيعة   nom
ضرار    nom
ضريب    nom
ضمام    nom
ضمرة    nom
ضمضم    nom
ضمعج    nom
ضميرة   nom
طارق    nom
طالب    nom
طاوس    nom
طحلاء   nom
طخفة    nom
طرفة    nom
طريف    nom
طعمة    nom
طلحة    nom
طلحة الطلحات    nom
طلق nom
طليق    nom
طهمان   nom
طود nom
طيسلة   nom
ظالم    nom
ظليم    nom
ظهير    nom
عائذ    nom
عائذ الله   nom
عائش    nom
عائشة   nom
عابس    nom
عاتكة   nom
عازب    nom
عاصم    nom
عافية   nom
عامر    nom
عباءة   nom
عبادة   nom
عباس    nom
عباية   nom
عبثر    nom
عبد الأسد   nom
عبد الأعلى  nom
عبد الأعلي  nom
عبد الأكبر  nom
عبد الأكرم  nom
عبد البر    nom
عبد الجبار  nom
عبد الجليل  nom
عبد الحكم   nom
عبد الحكيم  nom
عبد الحميد  nom
عبد الحى    nom
عبد الحي    nom
عبد الخالق  nom
عبد الخبير  nom
عبد الرحمن  nom
عبد الرحيم  nom
عبد الرزاق  nom
عبد السلام  nom
عبد الصمد   nom
عبد العزيز  nom
عبد العظيم  nom
عبد الغفار  nom
عبد الغنى   nom
عبد الغني   nom
عبد القاهر  nom
عبد القدوس  nom
عبد الكبير  nom
عبد الكريم  nom
عبد الله    nom
عبد المؤمن  nom
عبد المتعال nom
عبد المجيد  nom
عبد المطلب  nom
عبد الملك   nom
عبد المنعم  nom
عبد المهيمن nom
عبد النور   nom
عبد الواحد  nom
عبد الوارث  nom
عبد الوهاب  nom
عبد خير nom
عبد ربه nom
عبد شمس nom
عبد مناف    nom
عبد ويه nom
عبدة    nom
عبده    nom
عبيد    nom
عبيد الله   nom
عبيدة   nom
عتاب    nom
عتبان   nom
عتبة    nom
عتى nom
عتي nom
عتيبة الضرير    nom
عتيك    nom
عثام    nom
عثمان   nom
عثيم    nom
عجرة    nom
عجلان   nom
عجير    nom
عدى nom
عدي nom
عديسة   nom
عذافر   nom
عراك    nom
عرباض   nom
عربى    nom
عربي    nom
عرزم    nom
عرعرة   nom
عرفجة   nom
عروة    nom
عريب    nom
عزرة    nom
عسل nom
عصام    nom
عصمة    nom
عطاء    nom
عطارد   nom
عطاف    nom
عطية    nom
عفان    nom
عفير    nom
عفيف    nom
عقار    nom
عقبة    nom
عقيل    nom
عقيلة   nom
عكراش   nom
عكرمة   nom
علاج    nom
علاق    nom
علاقة   nom
علباء   nom
علقمة   nom
علقمى   nom
علي nom
عليا    nom
علية    nom
عمار    nom
عمارة   nom
عمة له  nom
عمر nom
عمران   nom
عمرة    nom
عمرو    nom
عمش nom
عمير    nom
عميرة   nom
عنبر    nom
عنبسة   nom
عنترة   nom
عوان    nom
عوسجة   nom
عوف nom
عون nom
عويج    nom
عويم    nom
عويمر   nom
عياش    nom
عياض    nom
عيذ الله    nom
عيسى    nom
عيسي    nom
عيينة   nom
غالب    nom
غانم    nom
غبطة    nom
غرفة    nom
غرية    nom
غزوان   nom
غزية    nom
غزيلة   nom
غسان    nom
غضيف    nom
غطيف    nom
غلاق    nom
غنام    nom
غنيم    nom
غياث    nom
غيلان   nom
فائد    nom
فاتك    nom
فاختة   nom
فاطمة   nom
فجيع    nom
فديك    nom
فرات    nom
فراس    nom
فرج nom
فرقد    nom
فروة    nom
فروخ    nom
فسيلة   nom
فضاء    nom
فضالة   nom
فضة nom
فضيل    nom
فطر nom
فلفل    nom
فلفلة   nom
فليت    nom
فيروز   nom
قابوس   nom
قارظ    nom
قباث    nom
قبيصة   nom
قتاد ة  nom
قتادة   nom
قتيبة   nom
قتيلة   nom
قثم nom
قحافة   nom
قدامة   nom
قران    nom
قرة nom
قرثع    nom
قرصافة  nom
قرظة    nom
قرفة    nom
قريبة   nom
قزعة    nom
قزمان   nom
قسامة   nom
قسيم    nom
قشير    nom
قضاعة   nom
قطبة    nom
قطن nom
قعنب    nom
قليب    nom
قمير    nom
قنان    nom
قهزاذ   nom
قهيد    nom
قيس nom
قيلة    nom
كاسب    nom
كامل    nom
كبشة    nom
كبير    nom
كبيشة   nom
كدام    nom
كرب nom
كردوس   nom
كرز nom
كريب    nom
كريم    nom
كريمة   nom
كعب nom
كلاب    nom
كلثم    nom
كلثوم   nom
كلدة    nom
كليب    nom
كميل    nom
كناز    nom
كنانة   nom
كهمس    nom
كهيل    nom
كيسان   nom
كيسة    nom
لؤلؤة   nom
لاحق    nom
لبابة   nom
لبيد    nom
لتميم   nom
لجلاج   nom
لقمان   nom
لقيط    nom
لمازة   nom
لهيعة   nom
ليث nom
ليلى    nom
ليلي    nom
ليلى مولاة  nom
مؤثر    nom
مؤمل    nom
مأمون   nom
مابنة   nom
ماجة    nom
ماعز    nom
مافنة   nom
مالك    nom
مالك الدار  nom
ماهان   nom
مبارك   nom
مبشر    nom
مجاشع   nom
مجاعة   nom
مجالد   nom
مجاهد   nom
مجزأة   nom
مجمع    nom
مجيبة   nom
محارب   nom
محاضر   nom
محبوب   nom
محجن    nom
محدوج   nom
محرر    nom
محرز    nom
محرش    nom
محرم    nom
محصن    nom
محفوظ   nom
محل nom
محمد    nom
محمود   nom
محيريز  nom
محيصة   nom
مخارق   nom
مخاشن   nom
مختار   nom
مخراق   nom
مخرش    nom
مخرمة   nom
مخزم    nom
مخلد    nom
مخمر    nom
مخنف    nom
مخول    nom
مدرك    nom
مدنى    nom
مدني    nom
مرار    nom
مرة nom
مرتثد   nom
مرثد    nom
مرجانة  nom
مرجى    nom
مرجي    nom
مرحب    nom
مرحوم   nom
مرداس   nom
مرزوق   nom
مرقع    nom
مروان   nom
مرى nom
مريم    nom
مزاحم   nom
مزيدة   nom
مسافر   nom
مسافع   nom
مساك    nom
مساور   nom
مسة nom
مستلم   nom
مستور   nom
مسحاج   nom
مسرة    nom
مسروح   nom
مسروق   nom
مسروقا  nom
مسعدة   nom
مسعر    nom
مسعود   nom
مسقلة   nom
مسكين   nom
مسلم    nom
مسلمة   nom
مسهر    nom
مسيكة   nom
مشاش    nom
مشرح    nom
مشعث    nom
مصبح    nom
مصدع    nom
مصدق    nom
مصرف    nom
مصعب    nom
مصفح    nom
مضارب   nom
مضر nom
مضرب    nom
مطر nom
مطرح    nom
مطرف    nom
مطعم    nom
مطهر    nom
مطير    nom
مطيع    nom
مظاهر   nom
مظفر    nom
معاذ    nom
معاذ بن جبل nom
معاذة   nom
معارك   nom
معان    nom
معاوية  nom
معبد    nom
معتب    nom
معتمر   nom
معدان   nom
معدى    nom
معدي    nom
معرف    nom
معروف   nom
معقل    nom
معلى    nom
معلي    nom
معمر    nom
معن nom
معيقيب  nom
معين    nom
مغراء   nom
مغراء العيذى    nom
مغراء العيذي    nom
مغفل    nom
مغول    nom
مغيث    nom
مغيرة   nom
مقاتل   nom
مقاعس   nom
مقدم    nom
مقسم    nom
مقلاص   nom
مكتوم   nom
مكحول   nom
مكحولا  nom
مكرم    nom
مكى nom
مكي nom
ملازم   nom
ملقام   nom
مليكة   nom
ممطور   nom
منبعث   nom
منبه    nom
منبوذ   nom
منجاب   nom
منجوف   nom
منذر    nom
منصور   nom
منظور   nom
منقذ    nom
منهال   nom
منية    nom
منير    nom
منيع    nom
مهاجر   nom
مهدى    nom
مهدي    nom
مهران   nom
مهنا    nom
مهند    nom
مورق    nom
موسى    nom
موسي    nom
موهب    nom
ميزان   nom
ميسر    nom
ميسرة   nom
ميمون   nom
ميمونة  nom
ميناء   nom
نائل    nom
نابت    nom
نابل    nom
ناتل    nom
ناجية   nom
ناشرة   nom
ناصح    nom
ناعم    nom
نافع    nom
نافعا   nom
ناهية   nom
نباتة   nom
نبهان   nom
نبيح    nom
نبيشة   nom
نبيط    nom
نبيه    nom
نجدة    nom
نجى nom
نجي nom
نجيح    nom
نجيد    nom
ندبة    nom
نذير    nom
نزار    nom
نسائى   nom
نسائي   nom
نسر nom
نسيب    nom
نسيبة   nom
نسير    nom
نشيط    nom
نصر nom
نصير    nom
نضربة   nom
نضرة    nom
نضلة    nom
نضير    nom
نعيم    nom
نفير    nom
نفيع    nom
نفيل    nom
نقادة   nom
نقيب    nom
نقيد    nom
نمران   nom
نملة    nom
نمير    nom
نميلة   nom
نهار    nom
نهشل    nom
نهيك    nom
نوح nom
نوف nom
نوفل    nom
نويفع   nom
نيار    nom
هارون   nom
هاشم    nom
هانىء   nom
هبيرة   nom
هجيمة   nom
هدبة    nom
هذيل    nom
هذيم    nom
هرقل    nom
هرم nom
هرمز    nom
هرمى    nom
هرمي    nom
هرير    nom
هريم    nom
هزال    nom
هزيل    nom
هشام    nom
هشيم    nom
هصان    nom
هلال    nom
هلقام   nom
همام    nom
هناد    nom
هنام    nom
هنان    nom
هند nom
هنى nom
هني nom
هنيدة   nom
هود nom
هوذة    nom
هولة    nom
هياج    nom
وائل    nom
وابصة   nom
واثلة   nom
وادع    nom
واسع    nom
واصل    nom
واقد    nom
واهب    nom
وبر nom
وبرة    nom
وحشى    nom
وحشي    nom
وراد    nom
ورازة   nom
ورد nom
ورقاء   nom
وزير    nom
وساج    nom
وعلة    nom
وفاء    nom
وقاء    nom
وقاص    nom
وقدان   nom
وكيع    nom
وليدة   nom
وهب nom
وهبان   nom
وهيب    nom
ياسين   nom
يحمد    nom
يحنس    nom
يحيى    nom
يحيي    nom
يريم    nom
يزداد   nom
يزيد    nom
يسار    nom
يساف    nom
يسرة    nom
يسير    nom
يسيرة   nom
يسيع    nom
يعقوب   nom
يعلى    nom
يعلي    nom
يعيش    nom
يقظان   nom
يمان    nom
يوسف    nom
يونس    nom
أبا القاسم صلى الله عليه و سلم  rasoul
أبا القاسم صلى الله عليه وسلم   rasoul
النبي   rasoul
النبي الصالح    rasoul
النبي صلى ا لله عليه و سلم  rasoul
النبي صلى ا لله عليه وسلم   rasoul
النبي صلى الله عليه و سلم   rasoul
النبي صلى الله عليه وسلم    rasoul
حبي صلى الله عليه و سلم rasoul
حبي صلى الله عليه وسلم  rasoul
رسول ا لله صلى الله عليه و سلم  rasoul
رسول ا لله صلى الله عليه وسلم   rasoul
رسول الله   rasoul
رسول الله صلى  الله عليه وسلم   rasoul
رسول الله صلى الله عليه rasoul
رسول الله صلى الله عليه و سلم   rasoul
رسول الله صلى الله عليه وسلم    rasoul
رسوله   rasoul
رسوله صلى الله عليه وسلم    rasoul
لنبي صلى الله عليه و سلم    rasoul
محمد صلى الله عليه وسلم rasoul
محمدا رسول الله rasoul
محمدا صلى الله عليه و سلم   rasoul
محمدا صلى الله عليه وسلم    rasoul
"""
TEXT1 = u"""
نبي الله    rasoul
نبي الله صلى الله عليه وسلم rasoul
نبيه صلى الله عليه وسلم rasoul
اسمه    Ma3rouf
اسمه :  Ma3rouf
اسمها   Ma3rouf
المعروف ب   Ma3rouf
قيل إنه Ma3rouf
قيل يقال له Ma3rouf
كان اسمه    Ma3rouf
لقبه    Ma3rouf
هو  Ma3rouf
هو :    Ma3rouf
هي  Ma3rouf
و اسمه  Ma3rouf
و لقبه  Ma3rouf
و هو    Ma3rouf
و يقال له   Ma3rouf
واسمه   Ma3rouf
وهو Ma3rouf
يعرف ب  Ma3rouf
يعنون   Ma3rouf
يعني    Ma3rouf
يقال له Ma3rouf
يقال لها    Ma3rouf
يلقب    Ma3rouf
يلقب ب  Ma3rouf

[ رضي الله عنه ]    Tardhia
[ رضي الله عنها ]   Tardhia
أم المؤمنين Tardhia
أم المؤمنين رضى الله تعالى عنها Tardhia
رضى الله   تعالى عنه    Tardhia
رضى الله تعالى عنه  Tardhia
رضى الله تعالى عنها Tardhia
رضى الله تعالى عنهم Tardhia
رضى الله تعالى عنهما    Tardhia
رضي الله عنه    Tardhia
رضي الله عنها   Tardhia
رضي الله عنهما  Tardhia
"""

TEXT2 = u"""
العلم   النوع
الأبيض  اسم علم - مكان - بحر / خليج / مضيق
الأبيض-المتوسط  اسم علم - مكان - بحر / خليج / مضيق
الأحساء اسم علم - مكان مدينة / مُقاطَعة / منطقة
الأحمدي اسم علم - مكان مدينة / مُقاطَعة / منطقة
الأحمر  اسم علم - مكان - بحر / خليج / مضيق
الأدرياتيكي اسم علم - مكان - بحر / خليج / مضيق
الأربعين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الأرجنتين   اسم علم - مكان - دولة
الأردن  اسم علم - مكان - دولة
الأزور  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الأسود  اسم علم - مكان - بحر / خليج / مضيق
الأصفر  اسم علم - مكان - بحر / خليج / مضيق
الأطلسي اسم علم - مكان - مُحيط
الأطلنطي    اسم علم - مكان - مُحيط
الأغواس اسم علم - مكان مدينة / مُقاطَعة / منطقة
الأغواط اسم علم - مكان مدينة / مُقاطَعة / منطقة
الأقصر  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الأمازون    اسم علم - مكان - نهر / بُحيرة - مُقاطَعة / منطقة
الأمم-الجنوبية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الأنبار اسم علم - مكان مدينة / مُقاطَعة / منطقة
الأندلس اسم علم - مكان مدينة / مُقاطَعة / منطقة
الأنصارية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الأوسط  اسم علم - مكان - بحر / خليج / مضيق
الأيرلندي   اسم علم - مكان - بحر / خليج / مضيق
الأيوني اسم علم - مكان - بحر / خليج / مضيق
الإبراهيمية اسم علم - مكان مدينة / مُقاطَعة / منطقة
الإسكندرية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الإسماعيلية اسم علم - مكان مدينة / مُقاطَعة / منطقة
الإكوادور   اسم علم - مكان - دولة
الإمارات    اسم علم - مكان - دولة
الباب   اسم علم - مكان مدينة / مُقاطَعة / منطقة
البابلية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الباجور اسم علم - مكان مدينة / مُقاطَعة / منطقة
الباحة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الباريزو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
البازورية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الباسك  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الباطنة اسم علم - مكان مدينة / مُقاطَعة / منطقة
البالياري   اسم علم - مكان - بحر / خليج / مضيق
البترون اسم علم - مكان مدينة / مُقاطَعة / منطقة
البحر-الأحمر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
البحرين اسم علم - مكان - دولة
البحيرة اسم علم - مكان مدينة / مُقاطَعة / منطقة
البداري اسم علم - مكان مدينة / مُقاطَعة / منطقة
البدرشين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
البديع  اسم علم - مكان مدينة / مُقاطَعة / منطقة
البرازيل    اسم علم - مكان - دولة
البرتغال    اسم علم - مكان - دولة
البرغلية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
البرلس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
البرهامة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
البريمي اسم علم - مكان مدينة / مُقاطَعة / منطقة
البساتين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
البصرة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
البطنان اسم علم - مكان مدينة / مُقاطَعة / منطقة
البطيشية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
البعلية اسم علم - مكان مدينة / مُقاطَعة / منطقة
البقاع  اسم علم - مكان مدينة / مُقاطَعة / منطقة
البقيعة اسم علم - مكان مدينة / مُقاطَعة / منطقة
البلطيق اسم علم - مكان - بحر / خليج / مضيق
البلينا اسم علم - مكان مدينة / مُقاطَعة / منطقة
البندقية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
البنغال اسم علم - مكان - بحر / خليج / مضيق
البهاما اسم علم - مكان - دولة
البوثنياني  اسم علم - مكان - بحر / خليج / مضيق
البوران اسم علم - مكان - بحر / خليج / مضيق
البوسنة-والهرسك اسم علم - مكان - دولة
البوكمال    اسم علم - مكان مدينة / مُقاطَعة / منطقة
البوليفار   اسم علم - مكان مدينة / مُقاطَعة / منطقة
البويرة اسم علم - مكان مدينة / مُقاطَعة / منطقة
البياض  اسم علم - مكان مدينة / مُقاطَعة / منطقة
البيسارية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
البيض   اسم علم - مكان مدينة / مُقاطَعة / منطقة
البيضاء اسم علم - مكان مدينة / مُقاطَعة / منطقة
التبت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
التبين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الترارزة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
التشيك  اسم علم - مكان - دولة
التشيلي اسم علم - مكان - بحر / خليج / مضيق
التل-الكبير اسم علم - مكان مدينة / مُقاطَعة / منطقة
التليل  اسم علم - مكان مدينة / مُقاطَعة / منطقة
التيراني    اسم علم - مكان - بحر / خليج / مضيق
الجبل-الأسود - مونتينيغرو   اسم علم - مكان - دولة
الجبيل  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الجبين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الجديدة اسم علم - مكان مدينة / مُقاطَعة / منطقة
الجزائر اسم علم - مكان - دولة - عاصمة
الجفارة اسم علم - مكان مدينة / مُقاطَعة / منطقة
الجفرة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الجفير  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الجلفة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الجمالية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الجمهورية-العربية-الصحراوية-الديمقراطية اسم علم - مكان - دولة
الجميجمة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الجميلية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الجناين اسم علم - مكان مدينة / مُقاطَعة / منطقة
الجنبية اسم علم - مكان مدينة / مُقاطَعة / منطقة
الجنينة اسم علم - مكان مدينة / مُقاطَعة / منطقة
الجهراء اسم علم - مكان مدينة / مُقاطَعة / منطقة
الجوف   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الجيزة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الحاج   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الحاصباني   اسم علم - مكان - نهر / بُحيرة
الحاكور اسم علم - مكان مدينة / مُقاطَعة / منطقة
الحامول اسم علم - مكان مدينة / مُقاطَعة / منطقة
الحامي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الحجاز  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الحجرية اسم علم - مكان مدينة / مُقاطَعة / منطقة
الحد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الحديدة اسم علم - مكان مدينة / مُقاطَعة / منطقة
الحرير  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الحزم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الحسكة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الحسنة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الحسيمة اسم علم - مكان مدينة / مُقاطَعة / منطقة
الحسينية    اسم علم - مكان - نهر / بُحيرة
الحفار  اسم علم - مكان - نهر / بُحيرة
الحلوسية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الحمصية اسم علم - مكان مدينة / مُقاطَعة / منطقة
الحميرة اسم علم - مكان مدينة / مُقاطَعة / منطقة
الحنيّة اسم علم - مكان مدينة / مُقاطَعة / منطقة
الحورة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الحوش   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الحوشب  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الحويش  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الخابور اسم علم - مكان - نهر / بُحيرة
الخارجة اسم علم - مكان مدينة / مُقاطَعة / منطقة
الخازر  اسم علم - مكان - نهر / بُحيرة
الخانكة اسم علم - مكان مدينة / مُقاطَعة / منطقة
الخبر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الخدرة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الخرايب اسم علم - مكان مدينة / مُقاطَعة / منطقة
الخربة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الخرسعة اسم علم - مكان مدينة / مُقاطَعة / منطقة
الخرطوم اسم علم - مكان - عاصِمة
الخريطيات   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الخضيرة اسم علم - مكان - نهر / بُحيرة - مُقاطَعة / منطقة
الخليفة اسم علم - مكان مدينة / مُقاطَعة / منطقة
الخليل  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الخميسات    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الخوخة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الخور   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الخوصر  اسم علم - مكان - نهر / بُحيرة
الخيام  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الداخلة اسم علم - مكان مدينة / مُقاطَعة / منطقة
الدار-البيضاء   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الدامر  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الدامور اسم علم - مكان مدينة / مُقاطَعة / منطقة
الداودية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الدبابية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الدحيل  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الدراز  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الدريب  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الدغلة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الدفنة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الدقهلية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الدقي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الدلب   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الدلنجات    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الدمازين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الدمام  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الدنمارك    اسم علم - مكان - دولة
الدوحة  اسم علم - مكان - عاصِمة
الدور   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الدوسة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الدومنيكان  اسم علم - مكان - دولة
الدوير  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الدويم  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الدير   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الذخيرة اسم علم - مكان مدينة / مُقاطَعة / منطقة
الراشيدية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الرأس-الأخضر - كاب-فيردي    اسم علم - مكان - دولة
الرباط  اسم علم - مكان - عاصِمة
الرحمانية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الرفاع  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الرقة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الرملة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الروضة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الرويس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الرياض  اسم علم - مكان - عاصِمة
الريان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الريحان اسم علم - مكان مدينة / مُقاطَعة / منطقة
الريحانية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الزاب   اسم علم - مكان - نهر / بُحيرة
الزاوية اسم علم - مكان مدينة / مُقاطَعة / منطقة
الزاوية-الحمراء اسم علم - مكان مدينة / مُقاطَعة / منطقة
الزبارة اسم علم - مكان مدينة / مُقاطَعة / منطقة
الزرارية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الزرقا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الزرقاء اسم علم - مكان مدينة / مُقاطَعة / منطقة
الزقازيق    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الزلاق  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الزلوطية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الزنج   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الزهراني    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الزواريب    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الزويرات    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الزيتون اسم علم - مكان مدينة / مُقاطَعة / منطقة
الساحل  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الساعد  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الساقية اسم علم - مكان مدينة / مُقاطَعة / منطقة
السد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
السراغنة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
السعودية    اسم علم - مكان - دولة
السفيرة اسم علم - مكان مدينة / مُقاطَعة / منطقة
السقحة  اسم علم - مكان - نهر / بُحيرة
السقية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
السكسكية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
السلام  اسم علم - مكان مدينة / مُقاطَعة / منطقة
السلط   اسم علم - مكان مدينة / مُقاطَعة / منطقة
السلطانية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
السلفادور   اسم علم - مكان - دولة
السلمانية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
السليمانية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
السنبلاوين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
السند   اسم علم - مكان مدينة / مُقاطَعة / منطقة
السنطة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
السنغال اسم علم - مكان - دولة
السهل   اسم علم - مكان مدينة / مُقاطَعة / منطقة
السوباط اسم علم - مكان - نهر / بُحيرة
السودان اسم علم - مكان - دولة
السويب  اسم علم - مكان - نهر / بُحيرة
السويد  اسم علم - مكان - دولة
السويس  اسم علم - مكان - بحر / خليج / مضيق - مُقاطَعة / منطقة
السويسة اسم علم - مكان مدينة / مُقاطَعة / منطقة
السويفية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
السيّاد اسم علم - مكان مدينة / مُقاطَعة / منطقة
السيدة-زينب اسم علم - مكان مدينة / مُقاطَعة / منطقة
السيف   اسم علم - مكان مدينة / مُقاطَعة / منطقة
السيم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الشارقة اسم علم - مكان مدينة / مُقاطَعة / منطقة
الشـحانية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الشحر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الشرابية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الشرقية اسم علم - مكان مدينة / مُقاطَعة / منطقة
الشعيتية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الشفت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الشلف   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الشمال  اسم علم - مكان - بحر / خليج / مضيق - مُقاطَعة / منطقة
الشهابية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الشهداء اسم علم - مكان مدينة / مُقاطَعة / منطقة
الشوف   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الشيخ-زويد  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الشيخ-محمد  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الصالحية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الصرفند اسم علم - مكان مدينة / مُقاطَعة / منطقة
الصف    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الصنوبر اسم علم - مكان مدينة / مُقاطَعة / منطقة
الصواني اسم علم - مكان مدينة / مُقاطَعة / منطقة
الصومال اسم علم - مكان - دولة
الصويرة اسم علم - مكان مدينة / مُقاطَعة / منطقة
الصين   اسم علم - مكان - دولة
الضالع  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الضعين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الضنية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الطائف  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الطارف  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الطفيلة اسم علم - مكان مدينة / مُقاطَعة / منطقة
الطور   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الطيبة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الطيرة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الطيري  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الظاهرة اسم علم - مكان مدينة / مُقاطَعة / منطقة
العاصي  اسم علم - مكان - نهر / بُحيرة
العامرية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
العبدة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
العدلية اسم علم - مكان مدينة / مُقاطَعة / منطقة
العدوة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
العرائش اسم علم - مكان مدينة / مُقاطَعة / منطقة
العراق  اسم علم - مكان - دولة
العرب   اسم علم - مكان - بحر / خليج / مضيق
العربي  اسم علم - مكان - بحر / خليج / مضيق - مُقاطَعة / منطقة
العريش  اسم علم - مكان مدينة / مُقاطَعة / منطقة
العزبة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
العزيزية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
العسيرات    اسم علم - مكان مدينة / مُقاطَعة / منطقة
العشار  اسم علم - مكان - نهر / بُحيرة
العقبة  اسم علم - مكان - بحر / خليج / مضيق - مُقاطَعة / منطقة
العكر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
العماير اسم علم - مكان مدينة / مُقاطَعة / منطقة
العمرة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
العوابل اسم علم - مكان مدينة / مُقاطَعة / منطقة
العوجا  اسم علم - مكان - نهر / بُحيرة
العوينات    اسم علم - مكان مدينة / مُقاطَعة / منطقة
العياط  اسم علم - مكان مدينة / مُقاطَعة / منطقة
العين-السخنة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
العيون  اسم علم - مكان - عاصِمة - مُقاطَعة / منطقة
الغابون اسم علم - مكان - دولة
الغازية اسم علم - مكان مدينة / مُقاطَعة / منطقة
الغانج  اسم علم - مكان - نهر / بُحيرة
الغراف  اسم علم - مكان - نهر / بُحيرة
الغرافة اسم علم - مكان مدينة / مُقاطَعة / منطقة
الغربية اسم علم - مكان مدينة / مُقاطَعة / منطقة
الغردقة اسم علم - مكان مدينة / مُقاطَعة / منطقة
الغريفة اسم علم - مكان مدينة / مُقاطَعة / منطقة
الغرينادينز اسم علم - مكان مدينة / مُقاطَعة / منطقة
الغزيلة اسم علم - مكان مدينة / مُقاطَعة / منطقة
الغنايم اسم علم - مكان مدينة / مُقاطَعة / منطقة
الغندورية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الغويرية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الغيضة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الفاتح  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الفاتيكان   اسم علم - مكان - دولة - عاصمة
الفاشر  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الفتح   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الفجيرة اسم علم - مكان مدينة / مُقاطَعة / منطقة
الفحيحيل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الفرات  اسم علم - مكان - نهر / بُحيرة
الفرافرة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الفرديس اسم علم - مكان مدينة / مُقاطَعة / منطقة
الفرض   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الفروانية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الفشن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الفقيه-بنصالح   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الفلبين اسم علم - مكان - دولة
الفنيدق اسم علم - مكان مدينة / مُقاطَعة / منطقة
الفيكة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الفيوم  اسم علم - مكان مدينة / مُقاطَعة / منطقة
القادسية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
القامشلي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
القاهرة اسم علم - مكان - عاصِمة
القبيات اسم علم - مكان مدينة / مُقاطَعة / منطقة
القدس   اسم علم - مكان - عاصِمة
القديس-توما اسم علم - مكان مدينة / مُقاطَعة / منطقة
القرقف  اسم علم - مكان مدينة / مُقاطَعة / منطقة
القرم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
القرنة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
القرية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
القشلق  اسم علم - مكان مدينة / مُقاطَعة / منطقة
القصاصين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
القصرين اسم علم - مكان مدينة / مُقاطَعة / منطقة
القصيبة اسم علم - مكان مدينة / مُقاطَعة / منطقة
القصير  اسم علم - مكان مدينة / مُقاطَعة / منطقة
القصيم  اسم علم - مكان مدينة / مُقاطَعة / منطقة
القضارف اسم علم - مكان مدينة / مُقاطَعة / منطقة
القضيبية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
القعقور اسم علم - مكان مدينة / مُقاطَعة / منطقة
القفول  اسم علم - مكان مدينة / مُقاطَعة / منطقة
القلمون اسم علم - مكان مدينة / مُقاطَعة / منطقة
القليعة اسم علم - مكان مدينة / مُقاطَعة / منطقة
القليلة اسم علم - مكان مدينة / مُقاطَعة / منطقة
القليوبية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
القناطر-الخيرية اسم علم - مكان مدينة / مُقاطَعة / منطقة
القنطرة اسم علم - مكان مدينة / مُقاطَعة / منطقة
القنيطرة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
القوزح  اسم علم - مكان مدينة / مُقاطَعة / منطقة
القيروان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
القيطع  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الكاريبي    اسم علم - مكان - بحر / خليج / مضيق
الكاف   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الكاميرون   اسم علم - مكان - دولة
الكحلاء اسم علم - مكان - نهر / بُحيرة
الكرخة  اسم علم - مكان - نهر / بُحيرة
الكرعانة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الكرك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الكرنتينا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الكسارة اسم علم - مكان - نهر / بُحيرة
الكفرة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الكفور  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الكفير  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الكلخة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الكواشرة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الكورة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الكورنيش    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الكوفة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الكونغو اسم علم - مكان - دولة
الكونغو-الديمقراطية - زائير اسم علم - مكان - دولة
الكويت  اسم علم - مكان - دولة - عاصمة
اللؤلؤ  اسم علم - مكان - نهر / بُحيرة
اللاذقية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
اللحية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
اللد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
اللعويسية   اسم علم - مكان - نهر / بُحيرة
الله-أباد   اسم علم - مكان مدينة / مُقاطَعة / منطقة
اللوبية اسم علم - مكان مدينة / مُقاطَعة / منطقة
الليغوري    اسم علم - مكان - بحر / خليج / مضيق
الليلكي اسم علم - مكان مدينة / مُقاطَعة / منطقة
الماحوز اسم علم - مكان مدينة / مُقاطَعة / منطقة
المالكية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
المانش  اسم علم - مكان - بحر / خليج / مضيق
المباركية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
المتن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
المثنى  اسم علم - مكان مدينة / مُقاطَعة / منطقة
المجادل اسم علم - مكان مدينة / مُقاطَعة / منطقة
المجدل  اسم علم - مكان مدينة / مُقاطَعة / منطقة
المجر - هنغاريا اسم علم - مكان - دولة
المجيدل اسم علم - مكان مدينة / مُقاطَعة / منطقة
المحابشة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
المحرق  اسم علم - مكان مدينة / مُقاطَعة / منطقة
المحطة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
المحفد  اسم علم - مكان مدينة / مُقاطَعة / منطقة
المحلة-الكبرى   اسم علم - مكان مدينة / مُقاطَعة / منطقة
المحمدية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
المحمرة اسم علم - مكان مدينة / مُقاطَعة / منطقة
المحمودية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
المحويت اسم علم - مكان مدينة / مُقاطَعة / منطقة
المحيدلة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
المدية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
المدينة-المنورة اسم علم - مكان مدينة / مُقاطَعة / منطقة
المراغة اسم علم - مكان مدينة / مُقاطَعة / منطقة
المرة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
المرج   اسم علم - مكان مدينة / مُقاطَعة / منطقة
المرجان اسم علم - مكان - بحر / خليج / مضيق
المرخ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
المرخية اسم علم - مكان مدينة / مُقاطَعة / منطقة
المرقب  اسم علم - مكان مدينة / مُقاطَعة / منطقة
المروانية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
المسيسبي    اسم علم - مكان - نهر / بُحيرة
المشرح  اسم علم - مكان - نهر / بُحيرة
المشهد  اسم علم - مكان مدينة / مُقاطَعة / منطقة
المطرفة اسم علم - مكان مدينة / مُقاطَعة / منطقة
المطرية اسم علم - مكان مدينة / مُقاطَعة / منطقة
المعادي اسم علم - مكان مدينة / مُقاطَعة / منطقة
المعامير    اسم علم - مكان مدينة / مُقاطَعة / منطقة
المعمرية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
المغار  اسم علم - مكان مدينة / مُقاطَعة / منطقة
المغرب  اسم علم - مكان - دولة
المفرق  اسم علم - مكان مدينة / مُقاطَعة / منطقة
المقطم  اسم علم - مكان مدينة / مُقاطَعة / منطقة
المكسيك اسم علم - مكان - دولة
المكلا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
المكنونية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
المملكة-المتحدة - بريطانيا - إنجلترا    اسم علم - مكان - دولة
المناقل اسم علم - مكان مدينة / مُقاطَعة / منطقة
المنامة اسم علم - مكان - عاصِمة
المنزلة اسم علم - مكان مدينة / مُقاطَعة / منطقة
المنستير    اسم علم - مكان مدينة / مُقاطَعة / منطقة
المنشاة اسم علم - مكان مدينة / مُقاطَعة / منطقة
المنصورة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
المنصوري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
المنوفية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
المنيا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
المهدية اسم علم - مكان مدينة / مُقاطَعة / منطقة
المهرة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
المهندسين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الموسكي اسم علم - مكان مدينة / مُقاطَعة / منطقة
الميت   اسم علم - مكان - بحر / خليج / مضيق
الميدان اسم علم - مكان مدينة / مُقاطَعة / منطقة
الميرة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الميسيسيبي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الناصرة اسم علم - مكان مدينة / مُقاطَعة / منطقة
الناصرية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الناظور اسم علم - مكان مدينة / مُقاطَعة / منطقة
الناقورة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
النبطية اسم علم - مكان مدينة / مُقاطَعة / منطقة
النبي-شيت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
النبيه-صالح اسم علم - مكان مدينة / مُقاطَعة / منطقة
النجارية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
النجف   اسم علم - مكان مدينة / مُقاطَعة / منطقة
النرويج اسم علم - مكان - دولة
النريجات    اسم علم - مكان مدينة / مُقاطَعة / منطقة
النزهة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
النصرانية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
النعامة اسم علم - مكان مدينة / مُقاطَعة / منطقة
النعيم  اسم علم - مكان مدينة / مُقاطَعة / منطقة
النفاخية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
النفيسة اسم علم - مكان مدينة / مُقاطَعة / منطقة
النمسا  اسم علم - مكان - دولة
النهر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
النوارة اسم علم - مكان مدينة / مُقاطَعة / منطقة
النوبارية-الجديدة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
النورة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
النويدرات   اسم علم - مكان مدينة / مُقاطَعة / منطقة
النيجر  اسم علم - مكان - دولة
النيل   اسم علم - مكان - نهر / بُحيرة
النيل-المندرس   اسم علم - مكان - نهر / بُحيرة
الهبريدز    اسم علم - مكان - بحر / خليج / مضيق
الهد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الهرمل  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الهضبات اسم علم - مكان مدينة / مُقاطَعة / منطقة
الهلالية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
الهملة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الهند   اسم علم - مكان - دولة
الواحات اسم علم - مكان مدينة / مُقاطَعة / منطقة
الواحات-البحرية اسم علم - مكان مدينة / مُقاطَعة / منطقة
الوادي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الوادي-الجديد   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الواسطى اسم علم - مكان مدينة / مُقاطَعة / منطقة
الوايلي اسم علم - مكان مدينة / مُقاطَعة / منطقة
الوزاني اسم علم - مكان مدينة / مُقاطَعة / منطقة
الوسطى  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الوعب   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الوقف   اسم علم - مكان مدينة / مُقاطَعة / منطقة
الوكرة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
الولايات-المتحدة - أمريكا   اسم علم - مكان - دولة
اليابان اسم علم - مكان - دولة
اليرموك اسم علم - مكان - نهر / بُحيرة
اليمن   اسم علم - مكان - دولة
اليوسفية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
اليونان اسم علم - مكان - دولة
آبلدورن اسم علم - مكان مدينة / مُقاطَعة / منطقة
آبوي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
آتشيه   اسم علم - مكان مدينة / مُقاطَعة / منطقة
آخال    اسم علم - مكان مدينة / مُقاطَعة / منطقة
آخن اسم علم - مكان مدينة / مُقاطَعة / منطقة
آرال    اسم علم - مكان - بحر / خليج / مضيق
آرتا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
آرهوس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
آزوف    اسم علم - مكان - بحر / خليج / مضيق
آسفي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
آسيا    اسم علم - مكان - قارَّة
آسيان   اسم علم - مكان - مُنَظَّمة دوليَّة / هيئة / اتِّحاد
آغلال   اسم علم - مكان مدينة / مُقاطَعة / منطقة
آقداش   اسم علم - مكان مدينة / مُقاطَعة / منطقة
آقدام   اسم علم - مكان مدينة / مُقاطَعة / منطقة
آقستافا اسم علم - مكان مدينة / مُقاطَعة / منطقة
آقسو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
آكرن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
آلبورغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
آمور    اسم علم - مكان - نهر / بُحيرة
آن-لا-راي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
آنا اسم علم - مكان مدينة / مُقاطَعة / منطقة
آنابار  اسم علم - مكان مدينة / مُقاطَعة / منطقة
آنسي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
آنهوي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
آوغسبورغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
آوموري  اسم علم - مكان مدينة / مُقاطَعة / منطقة
آيتشي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
آيجا-إي-لي-تاي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
آيراي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
آيزنشتات    اسم علم - مكان مدينة / مُقاطَعة / منطقة
آيسلندا اسم علم - مكان - دولة
آيندهوفن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
آيوا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
آيوو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أباتو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أباكو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبامبا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبخ اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبخازيا اسم علم - مكان - دولة
أبردين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبروتسو اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبشواي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبشوران اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبشى    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبلاهوي اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبلاوا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبنوب   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبها    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبو-المطامير    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبو-تشت اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبو-تيج اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبو-حماد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبو-حمص اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبو-شاش اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبو-صوير    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبو-قرقاص   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبو-كبير    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبو-لحية    اسم علم - مكان - نهر / بُحيرة
أبوجا   اسم علم - مكان - عاصِمة
أبوريماك    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبوظبي  اسم علم - مكان - عاصِمة
أبوفيان اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبوليما اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبومي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبونخلة اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبيا    اسم علم - مكان - عاصِمة
أبيدجان اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبينزيل-أوسيرهودن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أبينزيل-إينرهودن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أتابيو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أتاكاما اسم علم - مكان مدينة / مُقاطَعة / منطقة
أتاكورا اسم علم - مكان مدينة / مُقاطَعة / منطقة
أتاكونغا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أتسينانانا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أتشر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أتلانتيدا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أتلانتيك    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أتوا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أتيكا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أثيناآخايا  اسم علم - مكان - عاصِمة
أجا اسم علم - مكان مدينة / مُقاطَعة / منطقة
أجاديز  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أجان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أجانتا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أجد-عبرين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أجينبي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أحمد-أباد   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أحمد-بور-شرقية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أخالتسيخي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أخميم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أداماوا اسم علم - مكان مدينة / مُقاطَعة / منطقة
أدرار   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أدرار-سطف   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أدمور   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أدو اسم علم - مكان مدينة / مُقاطَعة / منطقة
أديس-أبابا  اسم علم - مكان - عاصِمة
أديليد  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أذربيجان    اسم علم - مكان - دولة
أذربيجان-الشرقية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أذربيجان-الغربية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أراتشينوفو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أراد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أرارات  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أراس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أراغاتسوتن  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أراغون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أرافورا اسم علم - مكان - بحر / خليج / مضيق
أراكاجو اسم علم - مكان مدينة / مُقاطَعة / منطقة
أراوكانيا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أربورغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أربيل   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أرتاشات اسم علم - مكان مدينة / مُقاطَعة / منطقة
أرتيبونيت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أرتيغاس اسم علم - مكان مدينة / مُقاطَعة / منطقة
أرتيك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أرجاو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أرجنتوي اسم علم - مكان مدينة / مُقاطَعة / منطقة
أرخبيل-غالاباغوس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أردبيل  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أرده    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أردوباد اسم علم - مكان مدينة / مُقاطَعة / منطقة
أردون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أرزون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أرزي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أرض-الصومال - صوماليلاند    اسم علم - مكان - دولة
أرعتا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أرغوستولي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أرغوليذا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أرغون   اسم علم - مكان - نهر / بُحيرة
أرفيل   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أركاديا اسم علم - مكان مدينة / مُقاطَعة / منطقة
أركنسو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أركونسكايا-موزدوك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أرلنغتون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أرلينغتون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أرمافير اسم علم - مكان مدينة / مُقاطَعة / منطقة
أرمينيا اسم علم - مكان - دولة
أرندال  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أرنهيم  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أرنون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أروزكان اسم علم - مكان مدينة / مُقاطَعة / منطقة
أروس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أروسا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أروشا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أرومية  اسم علم - مكان - بحر / خليج / مضيق
أرونجال-براديش  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أريانة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أريحا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أريزونا اسم علم - مكان مدينة / مُقاطَعة / منطقة
أريكيبا اسم علم - مكان مدينة / مُقاطَعة / منطقة
أزوا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أزوا-دي-كومبوستيلا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أزواي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أزوف    اسم علم - مكان - بحر / خليج / مضيق
أسام    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أساو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أسبرطة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أستارا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أستراخان-أوبلاست    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أستراليا    اسم علم - مكان - دولة
أستلي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أسطانا  اسم علم - مكان - عاصِمة
أسطون   اسم علم - مكان - نهر / بُحيرة
أسكيران اسم علم - مكان مدينة / مُقاطَعة / منطقة
أسلوت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أسماط   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أسمرة   اسم علم - مكان - عاصِمة
أسن اسم علم - مكان مدينة / مُقاطَعة / منطقة
أسنابروك    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أسواق-بيروت اسم علم - مكان مدينة / مُقاطَعة / منطقة
أسوان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أسونسيون    اسم علم - مكان - عاصِمة
أسيوط   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أشتاراك اسم علم - مكان مدينة / مُقاطَعة / منطقة
أشمون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أشيرول  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أضنة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أطار    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أطسا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أطفيح   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أطلانطس اسم علم - مكان - قارَّة
أطلنطا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أغادير  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أغواسكالينتس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أغوردات اسم علم - مكان مدينة / مُقاطَعة / منطقة
أغوز    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أغيوس-نيكولاوس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أفابت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أفجويي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أفرو-أوراسيا    اسم علم - مكان - قارَّة
أفريقيا اسم علم - مكان - قارَّة
أفريقيا-الوسطى  اسم علم - مكان - دولة
أفغانستان   اسم علم - مكان - دولة
أفقا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أفيرو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أفيغا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أفينيون اسم علم - مكان مدينة / مُقاطَعة / منطقة
أقجه-ادي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أكادير  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أكجوجت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أكرا    اسم علم - مكان - عاصِمة
أكرانيس اسم علم - مكان مدينة / مُقاطَعة / منطقة
أكرة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أكرشوس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أكروم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أكرون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أكري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أكسفورد اسم علم - مكان مدينة / مُقاطَعة / منطقة
أكلينز  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أكوا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أكوافيفا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أكوريري اسم علم - مكان مدينة / مُقاطَعة / منطقة
أكيتا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ألاباما اسم علم - مكان مدينة / مُقاطَعة / منطقة
ألاسكا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ألاغير  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ألاك    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ألانيا  اسم علم - مكان - دولة
ألايباتا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ألبا-يوليا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ألباني  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ألبانيا اسم علم - مكان - دولة
ألبختن  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ألبرتا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ألبرز   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ألبكركي اسم علم - مكان مدينة / مُقاطَعة / منطقة
ألبوكركه    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ألبي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ألبيرفيل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ألتا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ألتا-فيراباز    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ألتو-باراغواي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ألتو-بارانيا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ألطاي-كراي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ألكسو   اسم علم - مكان - مُنَظَّمة دوليَّة / هيئة / اتِّحاد
ألكمار  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ألماطي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ألمانيا اسم علم - مكان - دولة
ألميري  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ألوترا-مانغورو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ألور-سيتار  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أليبوري اسم علم - مكان مدينة / مُقاطَعة / منطقة
أليتس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أليكساندروبولي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أليكساندريا اسم علم - مكان مدينة / مُقاطَعة / منطقة
أم-الأفاعي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أم-البواقي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أم-الجماجم  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أم-الحصم    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أم-الرشراش  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أم-الزبار   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أم-الفحم    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أم-القيوين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أم-المرادم  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أم-المقارين اسم علم - مكان مدينة / مُقاطَعة / منطقة
أم-النمل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أم-أعبيرية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أم-باب  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أم-صلال-علي اسم علم - مكان مدينة / مُقاطَعة / منطقة
أم-صلال-محمد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أم-عوينة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أم-نخلة اسم علم - مكان - نهر / بُحيرة
أمابا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أمازوناس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أمامبيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
أمباتو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أمرسفورت    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أمريكا-الجنوبية اسم علم - مكان - قارَّة
أمريكا-الشمالية اسم علم - مكان - قارَّة
أمستردام    اسم علم - مكان - عاصِمة
أمعين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أمفيسا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أمنات-تشاروين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أمهرة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أمهرست  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أمور    اسم علم - مكان - نهر / بُحيرة
أموروني-مانيا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أموندسن اسم علم - مكان - بحر / خليج / مضيق
أميان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أمية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أميون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أن-جيانج    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنابوليس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنالامانجا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنالانجيروفو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أناهايم اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنتاركتيكا  اسم علم - مكان - قارَّة
أنتاناناريفو    اسم علم - مكان - عاصِمة
أنتسيرانانا اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنتوفاجاستا اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنتويرب اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنتيب   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنتيبوكا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنتيبولو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنتيغوا-وباربودا    اسم علم - مكان - دولة
أنجمينا اسم علم - مكان - عاصِمة
أنجوان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنجولا  اسم علم - مكان - دولة
أندامان اسم علم - مكان - بحر / خليج / مضيق
أندرا-براديش    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أندروس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أندلوسيا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أندمان-و-نيكوبار    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أندورا  اسم علم - مكان - دولة
أندورا-لافيلا   اسم علم - مكان - عاصِمة
أنديجان اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنسخدي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنصار   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنطاكيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنطاليا اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنطلياس اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنغ-ثونغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنغارا  اسم علم - مكان - نهر / بُحيرة
أنغاور  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنغوليم اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنقرة   اسم علم - مكان - عاصِمة
أنكاش   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنكوريج اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنكونا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنهالت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنوبون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنوسي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنيبيريانوران   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أنيتان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أهواشابان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوابك   اسم علم - مكان - مُنَظَّمة دوليَّة / هيئة / اتِّحاد
أواكساكا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوبانجي اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوبرهاوزن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوبسالا اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوبك    اسم علم - مكان - مُنَظَّمة دوليَّة / هيئة / اتِّحاد
أوبلاند اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوبولسكي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوبولو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوبي    اسم علم - مكان - نهر / بُحيرة
أوت-أوجوي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوتاجو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوتار-أنتشال    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوتار-براديش    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوتاراديت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوتاوا  اسم علم - مكان - عاصِمة
أوتحوزوندجوبا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوترخت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوتيم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوجادين اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوجار   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوجاين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوجوي-أفيندو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوجوي-لولو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوجيلانغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوخريد  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوخوتسك اسم علم - مكان - بحر / خليج / مضيق
أودار-ميانتشياي اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوداغست اسم علم - مكان مدينة / مُقاطَعة / منطقة
أودل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أودمورتيا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أودنسه  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أودومكساي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوديسا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوراديا اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوراسيا اسم علم - مكان - قارَّة
أورانج-واك  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أورتا-كور   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوردينو اسم علم - مكان مدينة / مُقاطَعة / منطقة
أورشوفا اسم علم - مكان مدينة / مُقاطَعة / منطقة
أورغانش اسم علم - مكان مدينة / مُقاطَعة / منطقة
أورغواي اسم علم - مكان - دولة
أورگنچ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أورلاندو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أورليون اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوروبا  اسم علم - مكان - قارَّة
أورورا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوروميا اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوريانا اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوريبرو اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوريسند اسم علم - مكان - بحر / خليج / مضيق
أوريغون اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوريليا اسم علم - مكان مدينة / مُقاطَعة / منطقة
أورينبرغ-أوبلاست    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أورينبورغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوزات-لو-كومبيلي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوزبكستان   اسم علم - مكان - دولة
أوساكا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوست-أغدار  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوستا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوسترافا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوسترغوتلاند    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوستفولد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوستن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوسلو   اسم علم - مكان - عاصِمة
أوسهيكوتو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوسولوتان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوسيتيا-الجنوبية    اسم علم - مكان - دولة
أوسير   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوسيما  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوش اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوشانا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوشاوا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوغندا  اسم علم - مكان - دولة
أوغوستا اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوفا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوفرآيزل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوقيانوسيا  اسم علم - مكان - قارَّة
أوكافانغو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوكايالي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوكاياما    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوكتيبيك    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوكرانيا    اسم علم - مكان - دولة
أوكلاند اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوكلاهوما   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوكوسي-أمبينو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوكيناوا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أولاد-التايمة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أولاد-صقر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أولان-باتور اسم علم - مكان - عاصِمة
أولاند  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أولانشو اسم علم - مكان مدينة / مُقاطَعة / منطقة
أولجي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أولدنبورغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أولدهام اسم علم - مكان مدينة / مُقاطَعة / منطقة
أولستر  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أولسن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أولم    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أولو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أولوموتس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوليسوند    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوليمبيا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أولينز  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوماها  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوماهيكي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أومبريا اسم علم - مكان مدينة / مُقاطَعة / منطقة
أومسك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أومسك-أوبلاست   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوموساتي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أونتاريو‏   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أونجوجا اسم علم - مكان مدينة / مُقاطَعة / منطقة
أونروا  اسم علم - مكان - مُنَظَّمة دوليَّة / هيئة / اتِّحاد
أونس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أونو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوهانغوينا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوهايو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوهريد  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أويتا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أويدا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أويسا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أويغه   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أويمي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
أوين-ساوند  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أياكوتشو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أيداهو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أيرلندا اسم علم - مكان - دولة
أيسلبن  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أيطو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أيلو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
أيميليك اسم علم - مكان مدينة / مُقاطَعة / منطقة
أينارو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
أيهة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إب  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إبسويتش اسم علم - مكان مدينة / مُقاطَعة / منطقة
إبفيل   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إبنبورن اسم علم - مكان مدينة / مُقاطَعة / منطقة
إبيروس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إبينال  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إتسيمو-اتسينانانا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إتسيمو-إندريفانا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إثيوبيا اسم علم - مكان - دولة
إجمياتسين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إجيفان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إدفو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إدكو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إدلب    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إدمنتون اسم علم - مكان مدينة / مُقاطَعة / منطقة
إدنبرة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إده اسم علم - مكان مدينة / مُقاطَعة / منطقة
إذيسا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إربد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إرتريا  اسم علم - مكان - دولة
إرفورت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إركوتسك-أوبلاست اسم علم - مكان مدينة / مُقاطَعة / منطقة
إركي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إرلنجن  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إرميرا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إرونغو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إريكوب  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إزمير   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إسبانيا اسم علم - مكان - دولة
إسبايات اسم علم - مكان مدينة / مُقاطَعة / منطقة
إسبو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إسبيريتو-سانتو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إستونيا اسم علم - مكان - دولة
إستوير  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إستيفن  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إسدود   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إسرائيل اسم علم - مكان - دولة
إسطنبول اسم علم - مكان مدينة / مُقاطَعة / منطقة
إسكالدس-إنجوردنى    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إسكتلندا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إسكندرونة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إسكيله  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إسلام-أباد  اسم علم - مكان - عاصِمة
إسماعيلي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إسميرالداس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إسن اسم علم - مكان مدينة / مُقاطَعة / منطقة
إسوجياس اسم علم - مكان مدينة / مُقاطَعة / منطقة
إسيك-كول    اسم علم - مكان - بحر / خليج / مضيق
إشبيلية اسم علم - مكان مدينة / مُقاطَعة / منطقة
إصفهان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إفروس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إفريتانيا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إكسوما  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إكسيانج-خوانج   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إكسيتر  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إكسينكورت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إل-إييرو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إل-باسو اسم علم - مكان مدينة / مُقاطَعة / منطقة
إل-بروغريسو اسم علم - مكان مدينة / مُقاطَعة / منطقة
إل-سيبو اسم علم - مكان مدينة / مُقاطَعة / منطقة
إلباسان اسم علم - مكان مدينة / مُقاطَعة / منطقة
إلغين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إلفسينا اسم علم - مكان مدينة / مُقاطَعة / منطقة
إلوكوس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إلياس-بينيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
إليزي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إليس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إلينوي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إليوت-لايك  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إليوثيرا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إمبابة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إمبابورا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إمبالمي اسم علم - مكان مدينة / مُقاطَعة / منطقة
إمدن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إميليا-رومانيا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إناغوا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إنتري-ريوس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إنجمينا اسم علم - مكان مدينة / مُقاطَعة / منطقة
إندبندنسيا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إندروي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إندونيسيا   اسم علم - مكان - دولة
إنديانا اسم علم - مكان مدينة / مُقاطَعة / منطقة
إنديانابوليس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إنسبروك اسم علم - مكان مدينة / مُقاطَعة / منطقة
إنسخيدي اسم علم - مكان مدينة / مُقاطَعة / منطقة
إنغا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إنغولشتات   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إنفركارجل   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إنفه    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إنكامب  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إنهامبين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إهدن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إهمج    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إهناسيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
إهيمه   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إوسترسوند   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيبادان اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيبارا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيباراكي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيبوه   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيبيزا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيبين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيتابوا اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيتاسي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيتاي-البارود   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيتوليا-أكارنانيا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيجة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيجوو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيجيفسك اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيدا-فيرو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيراكليون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيران   اسم علم - مكان - دولة
إيرتيش  اسم علم - مكان - نهر / بُحيرة
إيردراي اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيركوتسك    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيرينغا اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيزابال اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيزابيل اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيزابيلا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيسكينتلا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيسه    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيسولاسيو-دي-فيوموربوت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيسيسكو اسم علم - مكان - مُنَظَّمة دوليَّة / هيئة / اتِّحاد
إيسيك-كول   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيسيكويبو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيشيكاوا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيطاليا اسم علم - مكان - دولة
إيعات   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيعال   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيفانسفيل   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيفانوفارنكيفسك اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيفورا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيفيا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيفيان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيكا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيكالويت    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيل-أورو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيلات   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيلام   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيليا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيلينجينا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيماثيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيميشلي اسم علم - مكان مدينة / مُقاطَعة / منطقة
إينا    اسم علم - مكان - مُنَظَّمة دوليَّة / هيئة / اتِّحاد
إينشيري اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيوا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيواته  اسم علم - مكان مدينة / مُقاطَعة / منطقة
إيورومبي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
إييكولان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بئر-السبع   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بئر-العبد   اسم علم - مكان مدينة / مُقاطَعة / منطقة
با  اسم علم - مكان مدينة / مُقاطَعة / منطقة
باب-الشعرية اسم علم - مكان مدينة / مُقاطَعة / منطقة
بابل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بابلية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بابوا-غينيا-الجديدة اسم علم - مكان - دولة
بابونو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بابيك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بات-يام اسم علم - مكان مدينة / مُقاطَعة / منطقة
باتامبانغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
باتر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
باتراس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
باتراي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
باتشوكا اسم علم - مكان مدينة / مُقاطَعة / منطقة
باتكين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
باتنا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
باتنة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
باتوليه اسم علم - مكان مدينة / مُقاطَعة / منطقة
باتومي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
باتون-روج   اسم علم - مكان مدينة / مُقاطَعة / منطقة
باث اسم علم - مكان مدينة / مُقاطَعة / منطقة
باثوم-ثاني  اسم علم - مكان مدينة / مُقاطَعة / منطقة
باجة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
باجندا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
باخا-فيراباز    اسم علم - مكان مدينة / مُقاطَعة / منطقة
باخا-كاليفورنيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
باد-هاغزبورغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بادربورن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بادغيس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بادفايس اسم علم - مكان مدينة / مُقاطَعة / منطقة
بادن-بادن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بادن-فورتمبيرغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بار-لو-دوك  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بارا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
باراغواري   اسم علم - مكان مدينة / مُقاطَعة / منطقة
باراغواي    اسم علم - مكان - دولة
باراكو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
باراماريبو  اسم علم - مكان - عاصِمة
بارانا  اسم علم - مكان - نهر / بُحيرة - مُقاطَعة / منطقة
باراهونا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بارايبا اسم علم - مكان مدينة / مُقاطَعة / منطقة
باربار  اسم علم - مكان مدينة / مُقاطَعة / منطقة
باردا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
باركيفيل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بارنتس  اسم علم - مكان - بحر / خليج / مضيق
بارنتو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بارنزلي اسم علم - مكان مدينة / مُقاطَعة / منطقة
بارنو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بارنول  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بارو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
باروالي اسم علم - مكان مدينة / مُقاطَعة / منطقة
باروم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
باري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
باريا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
باريس   اسم علم - مكان - عاصِمة
باريسال اسم علم - مكان مدينة / مُقاطَعة / منطقة
باريش   اسم علم - مكان مدينة / مُقاطَعة / منطقة
باريلوتشي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بازل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بازيليكاتا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
باس اسم علم - مكان - بحر / خليج / مضيق
باس-ساسندرا اسم علم - مكان مدينة / مُقاطَعة / منطقة
باسارابياسكا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
باساري  اسم علم - مكان مدينة / مُقاطَعة / منطقة
باستازا اسم علم - مكان مدينة / مُقاطَعة / منطقة
باستيا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
باستير  اسم علم - مكان - عاصِمة
باسكو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
باسوجا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
باسي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
باسيغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
باشقورتوستان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بافاريا اسم علم - مكان مدينة / مُقاطَعة / منطقة
بافليه  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بافن    اسم علم - مكان - بحر / خليج / مضيق
بافوس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بافوسام اسم علم - مكان مدينة / مُقاطَعة / منطقة
بافينج  اسم علم - مكان مدينة / مُقاطَعة / منطقة
باقة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
باقة-الغربية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
باك اسم علم - مكان مدينة / مُقاطَعة / منطقة
باك-جيانج   اسم علم - مكان مدينة / مُقاطَعة / منطقة
باك-كان اسم علم - مكان مدينة / مُقاطَعة / منطقة
باك-ليو اسم علم - مكان مدينة / مُقاطَعة / منطقة
باكاو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
باكس-كسكن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
باكسان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
باكستان اسم علم - مكان - دولة
باكسي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
باكو    اسم علم - مكان - عاصِمة
باكول   اسم علم - مكان مدينة / مُقاطَعة / منطقة
باكيخانوف   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بالاتينات   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بالاكان اسم علم - مكان مدينة / مُقاطَعة / منطقة
بالاو   اسم علم - مكان - دولة
بالأولي اسم علم - مكان مدينة / مُقاطَعة / منطقة
بالتسي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بالحاف  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بالك    اسم علم - مكان - بحر / خليج / مضيق
بالما-دي-مايوركا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بالمرستون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بالي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
باليرمو اسم علم - مكان مدينة / مُقاطَعة / منطقة
باليزو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
باليكير اسم علم - مكان - عاصِمة
بالينكي اسم علم - مكان مدينة / مُقاطَعة / منطقة
باليني  اسم علم - مكان مدينة / مُقاطَعة / منطقة
باماكو  اسم علم - مكان - عاصِمة
باماندزي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بامبرغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بامندا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
باميان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بان-هوايكساي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بانتو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بانتياي-مينتشي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بانجول  اسم علم - مكان - عاصِمة
باندا   اسم علم - مكان - بحر / خليج / مضيق
باندرابوا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
باندريلي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بانسكا-بيستريتسا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بانغي   اسم علم - مكان - عاصِمة
بانكوك  اسم علم - مكان - عاصِمة
بانلونج اسم علم - مكان مدينة / مُقاطَعة / منطقة
باني    اسم علم - مكان مدينة / مُقاطَعة / منطقة
باهوروكو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
باهيا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
باي اسم علم - مكان مدينة / مُقاطَعة / منطقة
بايا-ماري   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بايات-هامي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بايامون اسم علم - مكان مدينة / مُقاطَعة / منطقة
بايتي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بايرويت اسم علم - مكان مدينة / مُقاطَعة / منطقة
بايسانديو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بايكال  اسم علم - مكان - بحر / خليج / مضيق
بايلين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بايمي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بايو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بايون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ببا اسم علم - مكان مدينة / مُقاطَعة / منطقة
ببنين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بتاح-تكفا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بتاحي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بتخني   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بتدين-اللقش اسم علم - مكان مدينة / مُقاطَعة / منطقة
بترومين اسم علم - مكان مدينة / مُقاطَعة / منطقة
بترون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بتعبورا اسم علم - مكان مدينة / مُقاطَعة / منطقة
بتغرين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بتوراتج اسم علم - مكان مدينة / مُقاطَعة / منطقة
بتول    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بتوي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بتيو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بجاية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بجه اسم علم - مكان مدينة / مُقاطَعة / منطقة
بجورا   اسم علم - مكان - بحر / خليج / مضيق
بحبوش   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بحرصاف  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بحصاص   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بحمدون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بحيرة-تنجانيقا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بخارى   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بدبهون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بدخشان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بدياس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بديبا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بر-إلياس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
برابنت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
براتشواب-خيري-خان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
براتيسلافا  اسم علم - مكان - عاصِمة
برادفورد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
برازافيل    اسم علم - مكان - عاصِمة
برازيليا    اسم علم - مكان - عاصِمة
براسلين اسم علم - مكان مدينة / مُقاطَعة / منطقة
براشوف  اسم علم - مكان مدينة / مُقاطَعة / منطقة
براشينبوري  اسم علم - مكان مدينة / مُقاطَعة / منطقة
براغ    اسم علم - مكان - عاصِمة
براغا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
براغانسا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
برافا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
براق    اسم علم - مكان مدينة / مُقاطَعة / منطقة
برامبتون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
براندنبورغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
برانيا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
براوناو-آم-إن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
براونشفايغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
برايا   اسم علم - مكان - عاصِمة
برايتون اسم علم - مكان مدينة / مُقاطَعة / منطقة
برايلا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بربادوس اسم علم - مكان - دولة
بربارة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بربر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بربرة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بربودا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
برج-العرب   اسم علم - مكان مدينة / مُقاطَعة / منطقة
برج-الملوك  اسم علم - مكان مدينة / مُقاطَعة / منطقة
برج-بو-عريريج   اسم علم - مكان مدينة / مُقاطَعة / منطقة
برج-حمود    اسم علم - مكان مدينة / مُقاطَعة / منطقة
برج-رحال    اسم علم - مكان مدينة / مُقاطَعة / منطقة
برج-قلاويه  اسم علم - مكان مدينة / مُقاطَعة / منطقة
برجن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
برجين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
برحليون اسم علم - مكان مدينة / مُقاطَعة / منطقة
بردع    اسم علم - مكان مدينة / مُقاطَعة / منطقة
برستون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
برشتينا اسم علم - مكان - عاصِمة
برشلونة اسم علم - مكان مدينة / مُقاطَعة / منطقة
برشيد   اسم علم - مكان مدينة / مُقاطَعة / منطقة
برصة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
برعشيت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
برعو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
برغن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
برفينيتسا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
برقايل  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بركاما  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بركان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بركة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بركة-السبع  اسم علم - مكان مدينة / مُقاطَعة / منطقة
برليس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
برلين   اسم علم - مكان - عاصِمة
برمانا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
برمبال-القديمة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
برمينغهام   اسم علم - مكان مدينة / مُقاطَعة / منطقة
برن اسم علم - مكان - عاصِمة
برنغ    اسم علم - مكان - بحر / خليج / مضيق
برنو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بروان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
برود    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بروسار  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بروفيدنس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بروكس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بروكسل  اسم علم - مكان - عاصِمة
بروكوبوندو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بروناي  اسم علم - مكان - دولة
بروناي-وموارا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بري-فينغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بريا-فيار   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بريتوريا    اسم علم - مكان - عاصِمة
برّيخ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بريدا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بريدة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بريدج-تاون  اسم علم - مكان - عاصِمة
بريزبين اسم علم - مكان مدينة / مُقاطَعة / منطقة
بريزرن  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بريزي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بريزيدنت-هايس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بريست   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بريستول‏    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بريشوف  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بريغنز  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بريفيزا اسم علم - مكان مدينة / مُقاطَعة / منطقة
بريقع   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بريليب  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بريمن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بريمورسكي-كراي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
برينس-ألبرت اسم علم - مكان مدينة / مُقاطَعة / منطقة
برينسيبي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بزبدين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بزعون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بزمار   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بزيزا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بسابا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بستان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بسكاي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بسكرة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بسكنتا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بسلان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بسمارك  اسم علم - مكان - بحر / خليج / مضيق - مُقاطَعة / منطقة
بسيتين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بسيون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بشار    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بشاور   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بشتلدا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بشري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بشكيك   اسم علم - مكان - عاصِمة
بشمزين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بشنوماتي    اسم علم - مكان - نهر / بُحيرة
بشنين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بصرما   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بطاران  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بطحا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بطرام   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بطرماز  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بطشي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بطمة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بعاصير  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بعبدا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بعبدات  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بعذران  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بعقلين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بعلبك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بعلول   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بغداد   اسم علم - مكان - عاصِمة
بغلان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بفالو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بفروة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بقاع-صفرين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بقرقاش  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بقسطة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بقسميّا اسم علم - مكان مدينة / مُقاطَعة / منطقة
بقعتات  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بقعكفرا اسم علم - مكان مدينة / مُقاطَعة / منطقة
بقنايا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بكا اسم علم - مكان مدينة / مُقاطَعة / منطقة
بكاسين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بكتيا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بكتيكا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بكركي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بكفتين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بكيفا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بكين    اسم علم - مكان - عاصِمة
بلاتيك  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلاط    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلاغويفغراد اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلاك-بوينت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلاكبول اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلانتيري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلانفيل اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلاوايو اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلباو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلبيس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلتيمور اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلجيكا  اسم علم - مكان - دولة
بلخ اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلخاش   اسم علم - مكان - بحر / خليج / مضيق
بلد-وين اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلطيق   اسم علم - مكان - بحر / خليج / مضيق
بلغاريا اسم علم - مكان - دولة
بلغراد  اسم علم - مكان - عاصِمة
بلفاست  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلفن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلفور   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلقاس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلقان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلقان-آباد  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلمس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلموبان اسم علم - مكان - عاصِمة
بلنتي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلنسية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلنغهاوزن   اسم علم - مكان - بحر / خليج / مضيق
بلوشستان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلوفديف اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلومفونتين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلومنقتون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلونة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلويشت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلويمفونتاين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بليتيو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بليدا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بليز - هندوراس-البريطانية   اسم علم - مكان - دولة
بليموث  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بلينو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بمحرين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بمريم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بن-عروس اسم علم - مكان مدينة / مُقاطَعة / منطقة
بنابل   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بنادر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بنانج   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بنت-جبيل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بنجاب   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بنجرير  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بنجشير  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بندر-سري-بكاوان اسم علم - مكان - عاصِمة
بنزرت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بنسونفيل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بنسيلفانيا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بنشعي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بنعفول  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بنغازي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بنغال   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بنغالور اسم علم - مكان مدينة / مُقاطَعة / منطقة
بنغلاديش    اسم علم - مكان - دولة
بنغو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بنغيلا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بنفورا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بنما    اسم علم - مكان - دولة - عاصمة
بنها    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بنهران  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بنواتي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بنوم-بنه    اسم علم - مكان - عاصِمة
بنون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بنى-عبيد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بني-براك    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بني-جمرة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بني-حسن اسم علم - مكان - نهر / بُحيرة
بني-حيان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بني-سويف    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بني-شنقول   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بني-مزار    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بني-ملال    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بنيالوكا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بنين    اسم علم - مكان - دولة - مُقاطَعة / منطقة
بهاولبور    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بهنج    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بهوبال  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بهيرهوا اسم علم - مكان مدينة / مُقاطَعة / منطقة
بو-عشيرة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بو-غزال اسم علم - مكان مدينة / مُقاطَعة / منطقة
بو-كواره    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بو-ماهر اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوا-فيستا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بواتييه اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوادا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوار    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوانت-نوار  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بواني   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوبريسك اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوبودية-لاسو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوبولو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوبونارو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوبيان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوبيه   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوتان   اسم علم - مكان - دولة
بوتراجايا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوتسدام اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوتسوانا    اسم علم - مكان - دولة
بوتنسا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوتوسيي اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوتوشاني    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوتي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوثا-بوث    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوثنيا  اسم علم - مكان - بحر / خليج / مضيق
بوجمبورا    اسم علم - مكان - عاصِمة
بوخارست اسم علم - مكان - عاصِمة
بوخوم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بودابست اسم علم - مكان - عاصِمة
بودغوريتشا  اسم علم - مكان - عاصِمة
بودلسكي اسم علم - مكان مدينة / مُقاطَعة / منطقة
بودو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بور اسم علم - مكان مدينة / مُقاطَعة / منطقة
بور-لويس    اسم علم - مكان - عاصِمة
بوربندر اسم علم - مكان مدينة / مُقاطَعة / منطقة
بورت-أو-برانس   اسم علم - مكان - عاصِمة
بورت-أوف-سبين   اسم علم - مكان - عاصِمة
بورت-إليزابيث   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بورت-بابكس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بورت-فيكتوريا   اسم علم - مكان - عاصِمة
بورت-فيلا   اسم علم - مكان - عاصِمة
بورت-مودي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بورت-مورسبي اسم علم - مكان - عاصِمة
بورتاليجري  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بورتسموث    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بورتسودان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بورتلاند    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بورتو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بورتو-أليغري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بورتو-ريكو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بورتو-فاليو اسم علم - مكان مدينة / مُقاطَعة / منطقة
بورتو-نوفو  اسم علم - مكان - عاصِمة
بورتوفيجو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بورجو-ماجيوري   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوردو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بورسات  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بورسد-أباوج-زمبلن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بورسعيد اسم علم - مكان مدينة / مُقاطَعة / منطقة
بورصة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بورغ-أتشارد اسم علم - مكان مدينة / مُقاطَعة / منطقة
بورغاس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بورغنلاند   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بورغو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بورغوان-جاليو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بورفؤاد اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوركينا-فاسو    اسم علم - مكان - دولة
بورما   اسم علم - مكان - دولة - مُقاطَعة / منطقة
بورنموث اسم علم - مكان مدينة / مُقاطَعة / منطقة
بورنيو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوروندي اسم علم - مكان - دولة
بوري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوريرام اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوزاو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوزنان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوساسو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوسان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوسطن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوسكيرود    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوسيلوفو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوشانان اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوشرية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوشهر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوضاي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوغدانتسي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوغوتا  اسم علم - مكان - عاصِمة
بوغوفينيي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوغوميلا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوفور   اسم علم - مكان - بحر / خليج / مضيق
بوكاس-ديل-تورو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوكاكا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوكَان-فيل  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوكهرا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوكي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوكيت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوكيرون اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوكيو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بول اسم علم - مكان مدينة / مُقاطَعة / منطقة
بولتافا اسم علم - مكان مدينة / مُقاطَعة / منطقة
بولتون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بولتيمور    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بولفا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بولندا  اسم علم - مكان - دولة
بولوكوان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بولون-بيانكور   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بولوني-سور-مير  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بولونيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوليا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوليخاماسي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوليفيا اسم علم - مكان - دولة
بولييروس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بومتانغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
بومرداس اسم علم - مكان مدينة / مُقاطَعة / منطقة
بومرسكي اسم علم - مكان مدينة / مُقاطَعة / منطقة
بومرن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بومي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بون اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوناخا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوناو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بونجولافا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بونديتشيري  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بونغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بونو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوني    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوهاي   اسم علم - مكان - بحر / خليج / مضيق
بوهنباي اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوهول   اسم علم - مكان - بحر / خليج / مضيق
بوهيانما    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بووا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوي اسم علم - مكان مدينة / مُقاطَعة / منطقة
بويا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بويبلا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بويرتو-بكويريزو-مورينو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بويرتو-بلاتا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بويرتو-جواسيو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بويرتو-فرانسيسكو-دي-ا-أوريانا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بويسي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بوينس-آيريس اسم علم - مكان - عاصِمة
بويني   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بياترا-نيامتس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بياقوت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيانكور اسم علم - مكان مدينة / مُقاطَعة / منطقة
بياوي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيت-الحاج   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيت-الدين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيت-الفقس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيت-الكيكو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيت-أيوب    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيت-حانون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيت-شباب    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيت-شعار    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيت-غطاس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيت-لاهيا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيت-لحم اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيت-لهيا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيت-ليف اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيت-مري اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيت-ملات    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيت-ياحون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيت-يونس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيترماريزبيرغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيتروشاني   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيتسبرغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيتسوندا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيتسيبوكا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيتولا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيتيشت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيتين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيخا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيدبورغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيدرو-خوان-كاباليرو اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيدوا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيديرنالس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بير اسم علم - مكان مدينة / مُقاطَعة / منطقة
بير-السناسل اسم علم - مكان مدينة / مُقاطَعة / منطقة
بير-غنج اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيرات   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيرات-نغر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيرافيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيراك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيراميد اسم علم - مكان - بحر / خليج / مضيق
بيرايوس اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيربيس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيربينيا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيرة-   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيرتوا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيرث    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيرجو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيرغوس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيركانما    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيركيركارا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيرلس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيرم    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيرم-كراي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيرمينغهام  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيرنامبوكو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيرناي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيرنغ   اسم علم - مكان - بحر / خليج / مضيق
بيرنيك  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيرو    اسم علم - مكان - دولة
بيروت   اسم علم - مكان - عاصِمة
بيروجيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيروفو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيريا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيريستيريون اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيزانسون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيزيرز  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيسان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيساو   اسم علم - مكان - عاصِمة
بيسايا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيست    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيستريتسا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيستريكا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيشو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيشوات  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيشينشا اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيضا-القاع  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيكار   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيكانور اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيكاو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيكرزفيلد   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيكورا  اسم علم - مكان - نهر / بُحيرة
بيكول   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيكيس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيكيني  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيلا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيلار   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيلاروسيا - روسيا-البيضاء   اسم علم - مكان - دولة
بيلاقان اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيلزن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيلسيستا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيلكينغه    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيله-جري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيله-سوار   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيلو-هوروزنتي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيلوبونيز   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيليت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيليفيل اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيليفيلد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيليليو اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيليم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيماغاتشيل  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيمبا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيميني  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بينار-دل-ريو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيناما  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بينانج  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيندر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بينغ-تانغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بينغ-وو اسم علم - مكان مدينة / مُقاطَعة / منطقة
بينو    اسم علم - مكان - نهر / بُحيرة
بيهار   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيو-بيو اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيوا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيوتيا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيورا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيوكو-سور   اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيوكو-نورته اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيونغ-يانغ  اسم علم - مكان - عاصِمة
بيونوس-آيرس اسم علم - مكان مدينة / مُقاطَعة / منطقة
بيي اسم علم - مكان مدينة / مُقاطَعة / منطقة
بييريا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
بييمونتي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
پخنونخوا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
پشاور   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاباجوس اسم علم - مكان - نهر / بُحيرة
تاباسكو اسم علم - مكان مدينة / مُقاطَعة / منطقة
تابورا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاجورة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاخماو-تا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاراباكا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاراناكي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاراوا  اسم علم - مكان - عاصِمة
تارتار  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تارتو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تارغوفيشته  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تارودانت    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تازة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تازمان  اسم علم - مكان - بحر / خليج / مضيق
تازمانيا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاسواريمبو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاغويغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تافوش   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تافووا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تافيا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاقلعي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاك اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاكنا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاكورادي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاكوما  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاكيو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تالاهاسي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاليا-  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تالين   اسم علم - مكان - عاصِمة
تامالي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاماوليباس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تامبا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تامباكوندا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تامبيري اسم علم - مكان مدينة / مُقاطَعة / منطقة
تامبيكو اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاميل-نادو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تانغا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاهلة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاهوا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاو-يوان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاورانغا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاوريرت اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاي-تانغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاي-شانغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاي-نن  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تايبي   اسم علم - مكان - عاصِمة
تايبيه  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تايلاند اسم علم - مكان - دولة
تايليفو اسم علم - مكان مدينة / مُقاطَعة / منطقة
تاينان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تايوان  اسم علم - مكان - دولة
تايين-جيانج اسم علم - مكان مدينة / مُقاطَعة / منطقة
تبسة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تبليسي  اسم علم - مكان - عاصِمة
تبنا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تبنين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تبوك    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تتارستان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تجكجة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تحويطة-الغدير   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تحويطة-النهر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تخار    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ترا-فين اسم علم - مكان مدينة / مُقاطَعة / منطقة
ترات    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تراشيايانغتسي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تراشيغانغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تراقيا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ترانسدانوبيا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ترانسنيستريا    اسم علم - مكان - دولة
ترانغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ترتيج   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ترجو-جيو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ترجو-موريش  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ترجوفيشت    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ترشيش   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تركمان-آباد اسم علم - مكان مدينة / مُقاطَعة / منطقة
تركمانستان  اسم علم - مكان - دولة
تركيا   اسم علم - مكان - دولة
ترمذ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ترنافا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ترنتون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ترنجانو اسم علم - مكان مدينة / مُقاطَعة / منطقة
تروا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تروا-ريفيير اسم علم - مكان مدينة / مُقاطَعة / منطقة
تروبردج اسم علم - مكان مدينة / مُقاطَعة / منطقة
ترومسو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تروندهايم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ترونغسا اسم علم - مكان مدينة / مُقاطَعة / منطقة
تريبورا اسم علم - مكان مدينة / مُقاطَعة / منطقة
تريبولي اسم علم - مكان مدينة / مُقاطَعة / منطقة
ترير    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تريكالا اسم علم - مكان مدينة / مُقاطَعة / منطقة
تريكومو اسم علم - مكان مدينة / مُقاطَعة / منطقة
تريلاوني    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تريم    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ترينتا-إي-تري   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ترينتشين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ترينتو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ترينتينو-ألتو-أديجي اسم علم - مكان مدينة / مُقاطَعة / منطقة
ترينيتي-بالميتو-بوينت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ترينيداد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ترينيداد-وتوباغو    اسم علم - مكان - دولة
ترييستي اسم علم - مكان مدينة / مُقاطَعة / منطقة
تزنيت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تسخينفالي   اسم علم - مكان - عاصِمة
تسمبيو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تسني    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تسيرانغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
تسيل-أم-زيه اسم علم - مكان مدينة / مُقاطَعة / منطقة
تسيليه  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تسيمغانغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تسينغوني    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشاد    اسم علم - مكان - دولة
تشارلستون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشارلوت اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشامباساك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشامبيري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشانثابوري  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشانجوون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشاندلر اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشانديكار   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشايافوم    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشاينات اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشبنهام اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشسابيك اسم علم - مكان - بحر / خليج / مضيق
تشستر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشهاتيسغار  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشوبو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشوبوت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشوخا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشوغوكو اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشوك    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشوكشي  اسم علم - مكان - بحر / خليج / مضيق
تشولا-فيستا اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشولوتيكا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشومفون اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشونبوري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشونغتشينغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشونغزين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشوي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشويسيول    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشياباس اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشيبا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشيباتا اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشيركاسي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشيرنيفتسي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشيريكي اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشيرينيهيف  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشيسابيك    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشيكيمولا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشيلبانسينغو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشيلي   اسم علم - مكان - دولة
تشيليابينسك اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشيليابينسك-أوبلاست اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشيلينا اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشيمالتيناغو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشيناي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشينشيبي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تشيواوا اسم علم - مكان مدينة / مُقاطَعة / منطقة
تصرونا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تطاوين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تطوان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تعز اسم علم - مكان مدينة / مُقاطَعة / منطقة
تفاحتا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تكانت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تكساس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تل-الربيع   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تل-أبيب اسم علم - مكان - عاصِمة
تلا اسم علم - مكان مدينة / مُقاطَعة / منطقة
تلاكسكالا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تلبرغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تلسا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تلمسان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تلنا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تلودي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تمارة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تمبكتو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تمنراست اسم علم - مكان مدينة / مُقاطَعة / منطقة
تمنين-التحتا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تمنين-الفوقا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تمى-الأمديد اسم علم - مكان مدينة / مُقاطَعة / منطقة
تناناريف    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تندوف   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تنريف   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تنزانيا اسم علم - مكان - دولة
تنسي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تنورة-  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تنورين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تنيكي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تواماساغا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تواماسينا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
توباجو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
توبلى   اسم علم - مكان مدينة / مُقاطَعة / منطقة
توبمانبورغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
توبيكا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
توتشيغي اسم علم - مكان مدينة / مُقاطَعة / منطقة
توتوري  اسم علم - مكان مدينة / مُقاطَعة / منطقة
توتونغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
توتونيكابان اسم علم - مكان مدينة / مُقاطَعة / منطقة
توجدير  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تور اسم علم - مكان مدينة / مُقاطَعة / منطقة
توربا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
توركانا اسم علم - مكان - بحر / خليج / مضيق
توركو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
توركوينغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تورنغن  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تورونتو اسم علم - مكان مدينة / مُقاطَعة / منطقة
تورينغيا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تورينو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
توزر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
توزولا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
توسكانا اسم علم - مكان مدينة / مُقاطَعة / منطقة
توسن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
توغو    اسم علم - مكان - دولة
توفالو  اسم علم - مكان - دولة
توفول   اسم علم - مكان مدينة / مُقاطَعة / منطقة
توكانتينس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
توكاي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
توكستلا-غوتييريز    اسم علم - مكان مدينة / مُقاطَعة / منطقة
توكوشيما    اسم علم - مكان مدينة / مُقاطَعة / منطقة
توكومان اسم علم - مكان مدينة / مُقاطَعة / منطقة
توكي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تول اسم علم - مكان مدينة / مُقاطَعة / منطقة
تولا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تولتشا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تولسا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تولكان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تولوز   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تولوكا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تولون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تولياتي اسم علم - مكان مدينة / مُقاطَعة / منطقة
توليارا اسم علم - مكان مدينة / مُقاطَعة / منطقة
توليدو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تولين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تومبا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تومبكتو اسم علم - مكان مدينة / مُقاطَعة / منطقة
تومبيس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تونجا - تونغا   اسم علم - مكان - دولة
تونجاتابو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تونس    اسم علم - مكان - دولة - عاصمة
تونسبيرغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تونغوراهوا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تونكين  اسم علم - مكان - بحر / خليج / مضيق
تونله-ساب‏‏ اسم علم - مكان - بحر / خليج / مضيق
توهوكو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تووز    اسم علم - مكان مدينة / مُقاطَعة / منطقة
توياما  اسم علم - مكان مدينة / مُقاطَعة / منطقة
توين-كانج   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيار-كوروشيو    اسم علم - مكان - بحر / خليج / مضيق
تيارت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيانجين اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيبازة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيبيك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيتي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيجراي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيجوسي-جالبا    اسم علم - مكان - عاصِمة
تيراسبول    اسم علم - مكان - عاصِمة
تيرانا  اسم علم - مكان - عاصِمة
تيربون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيرس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيرس-زمور   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيرنوبيل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيرول   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيريسينا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيزي-وزو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيسمسيلت    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيشيت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيفلت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيكيلا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيلابيري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيلافي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيلبورخ اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيليمارك    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيما    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيمبورونغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيمفو   اسم علم - مكان - عاصِمة
تيموتو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيمور   اسم علم - مكان - بحر / خليج / مضيق
تيمور-الشرقية   اسم علم - مكان - دولة
تيميشوارا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تينا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيناينانو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيوتيهواكان اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيومين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تيومين-أوبلاست  اسم علم - مكان مدينة / مُقاطَعة / منطقة
تييرا-ديل-فويغو اسم علم - مكان مدينة / مُقاطَعة / منطقة
ثابا-تسيكا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ثاخيك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ثانترال اسم علم - مكان مدينة / مُقاطَعة / منطقة
ثاي-بن  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ثاي-نوجوين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ثراسيا  اسم علم - مكان - بحر / خليج / مضيق
ثلا اسم علم - مكان مدينة / مُقاطَعة / منطقة
ثمود    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ثو-ثاين-هاو اسم علم - مكان مدينة / مُقاطَعة / منطقة
ثيساليا اسم علم - مكان مدينة / مُقاطَعة / منطقة
ثيسبروتيا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ثييس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جابوروني    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جاج اسم علم - مكان مدينة / مُقاطَعة / منطقة
جارخند  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جاردوني اسم علم - مكان مدينة / مُقاطَعة / منطقة
جازا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جازان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جاس-ناغيكن-زلنوك    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جافار   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جاكرتا  اسم علم - مكان - عاصِمة
جاكسون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جاكسونفيل   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جالكعيو اسم علم - مكان مدينة / مُقاطَعة / منطقة
جام-بور اسم علم - مكان مدينة / مُقاطَعة / منطقة
جامايكا اسم علم - مكان - دولة
جامبلا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جامو-وكشمير اسم علم - مكان مدينة / مُقاطَعة / منطقة
جانجانبوريه اسم علم - مكان مدينة / مُقاطَعة / منطقة
جاهلية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جاوا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جاوة    اسم علم - مكان - بحر / خليج / مضيق
جب-جنين اسم علم - مكان مدينة / مُقاطَعة / منطقة
جباع    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جبال-البطم  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جباليا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جبراييل اسم علم - مكان مدينة / مُقاطَعة / منطقة
جبشيت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جبل-القديس-ميشيل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جبل-أكروم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جبلة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جبيل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جبيه    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جدة اسم علم - مكان مدينة / مُقاطَعة / منطقة
جدرا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جدو اسم علم - مكان مدينة / مُقاطَعة / منطقة
جديدة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جديدة-القيطع    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جديدة-مرجعيون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جراسياس-أديوس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جراند-آنسي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جرجا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جرجوع   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جرداب   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جرسيف   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جرش اسم علم - مكان مدينة / مُقاطَعة / منطقة
جرمق    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جرناي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جرنايا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جرنة-أرصون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جروس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جرينادا اسم علم - مكان - دولة
جزاخ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جزر-البليار اسم علم - مكان مدينة / مُقاطَعة / منطقة
جزر-القمر   اسم علم - مكان - دولة
جزر-الكناري اسم علم - مكان مدينة / مُقاطَعة / منطقة
جزر-المالديف    اسم علم - مكان - دولة
جزر-سليمان  اسم علم - مكان - دولة
جزر-مارشال  اسم علم - مكان - دولة
جزين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جعيتا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جفرسون-سيتي اسم علم - مكان مدينة / مُقاطَعة / منطقة
جل-الديب    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جلال-أباد   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جلجدود  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جلفا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جلكافا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جليل-أباد   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جمامة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جمصة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جمهورية-مقدونيا اسم علم - مكان - دولة
جميجمة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جناتا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جنت اسم علم - مكان مدينة / مُقاطَعة / منطقة
جنتا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جنجلاية اسم علم - مكان مدينة / مُقاطَعة / منطقة
جنجن    اسم علم - مكان - نهر / بُحيرة
جندوبة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جنكفور-دهام اسم علم - مكان مدينة / مُقاطَعة / منطقة
جنوب-السودان    اسم علم - مكان - دولة
جنوب-أفريقيا    اسم علم - مكان - دولة
جنوب-بانداما    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جنوب-كوميه  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جنوة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جنيف    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جنين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جهينة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جوادالكانال اسم علم - مكان مدينة / مُقاطَعة / منطقة
جوادر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جوار-الحشيش اسم علم - مكان مدينة / مُقاطَعة / منطقة
جوار-الحوز  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جواو-بيسوا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جوبا    اسم علم - مكان - عاصِمة
جوباو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جوتنجن  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جورا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جورة-الحص   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جورة-بدران  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جورة-ترمس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جورة-محاد   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جورج-تاون   اسم علم - مكان - عاصِمة
جورجتون اسم علم - مكان مدينة / مُقاطَعة / منطقة
جورجيا  اسم علم - مكان - دولة - مُقاطَعة / منطقة
جورجيو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جورمالا اسم علم - مكان مدينة / مُقاطَعة / منطقة
جوزجان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جون اسم علم - مكان مدينة / مُقاطَعة / منطقة
جونقلي‏ اسم علم - مكان مدينة / مُقاطَعة / منطقة
جونو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جونيه   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جوهانسبورغ/جوهانسبيرغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جوهر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جوهور   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جوهور-بارو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جويّا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جيا-لي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جيارندا اسم علم - مكان مدينة / مُقاطَعة / منطقة
جيانغسو اسم علم - مكان مدينة / مُقاطَعة / منطقة
جيانغشي اسم علم - مكان مدينة / مُقاطَعة / منطقة
جيبوتي  اسم علم - مكان - دولة - عاصمة
جيتشيد  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جيجل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جيجو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جيجيانغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
جيحون   اسم علم - مكان - نهر / بُحيرة
جيراردوف    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جيرزي-سيتي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جيكابلس اسم علم - مكان مدينة / مُقاطَعة / منطقة
جيلان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جيلفورد اسم علم - مكان مدينة / مُقاطَعة / منطقة
جيلين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
جيلينا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جيلينو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
جيمس    اسم علم - مكان - بحر / خليج / مضيق
جيمو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
جينغ-هاي    اسم علم - مكان - بحر / خليج / مضيق
جيواننج اسم علم - مكان مدينة / مُقاطَعة / منطقة
جيونجو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
چهار-محال-وبختياري  اسم علم - مكان مدينة / مُقاطَعة / منطقة
حائل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حاجي-قبول   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حارة-البلانة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حارة-الخاصة اسم علم - مكان مدينة / مُقاطَعة / منطقة
حارة-الست   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حارة-الفاعور    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حارة-حريك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حارة-حمزة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حارة-صيدا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حارتيه  اسم علم - مكان مدينة / مُقاطَعة / منطقة
حاروف   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حاريص   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حاريصا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
حازمية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
حاصبيا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
حالات   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حامات   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حامول   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حانين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حبابة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حبان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حبوس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حبوش    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حتى اسم علم - مكان مدينة / مُقاطَعة / منطقة
حجة اسم علم - مكان مدينة / مُقاطَعة / منطقة
حجولا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حدائق-القبة اسم علم - مكان مدينة / مُقاطَعة / منطقة
حداثا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حدث-الجبة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حدشيت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حراجل   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حران    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حرحراي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
حرف-سياد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حرفيش   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حريصا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حصرايل  اسم علم - مكان مدينة / مُقاطَعة / منطقة
حصرون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حصون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حصين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حضرات   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حضرموت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
حقّاز   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حلب اسم علم - مكان مدينة / مُقاطَعة / منطقة
حلبا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حلحل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حلفا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حلوان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حلوة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حماة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حمانا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حمد اسم علم - مكان مدينة / مُقاطَعة / منطقة
حمص اسم علم - مكان مدينة / مُقاطَعة / منطقة
حميس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حميلة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حناويه  اسم علم - مكان مدينة / مُقاطَعة / منطقة
حنيدر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حوران   اسم علم - مكان - نهر / بُحيرة
حورة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حوش اسم علم - مكان مدينة / مُقاطَعة / منطقة
حوش-سنيد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حوش-عيسى    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حوض-ميلن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حوطة-لحج    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حولا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حولون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حولي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حومين-التحتا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حومين-الفوقا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حي-الفوقاني اسم علم - مكان مدينة / مُقاطَعة / منطقة
حيات    اسم علم - مكان مدينة / مُقاطَعة / منطقة
حيداب   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حيدر-أباد   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حيران   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حيزوق   اسم علم - مكان مدينة / مُقاطَعة / منطقة
حيطورة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
حيفا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
خاباروفسك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
خاباروفسك-كراي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
خاركوف  اسم علم - مكان مدينة / مُقاطَعة / منطقة
خاشماز  اسم علم - مكان مدينة / مُقاطَعة / منطقة
خاقماز  اسم علم - مكان مدينة / مُقاطَعة / منطقة
خالابا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
خالكيذا اسم علم - مكان مدينة / مُقاطَعة / منطقة
خالكيذيكي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
خاليسكو اسم علم - مكان مدينة / مُقاطَعة / منطقة
خامواني اسم علم - مكان مدينة / مُقاطَعة / منطقة
خانكندي اسم علم - مكان مدينة / مُقاطَعة / منطقة
خانه-هوا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
خانيا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
خانيونس اسم علم - مكان مدينة / مُقاطَعة / منطقة
خباري   اسم علم - مكان مدينة / مُقاطَعة / منطقة
خبي اسم علم - مكان مدينة / مُقاطَعة / منطقة
ختلان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
خراسان-الجنوبية اسم علم - مكان مدينة / مُقاطَعة / منطقة
خراسان-الرضوية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
خراسان-الشمالية اسم علم - مكان مدينة / مُقاطَعة / منطقة
خربة-البصل  اسم علم - مكان مدينة / مُقاطَعة / منطقة
خربة-الجرد  اسم علم - مكان مدينة / مُقاطَعة / منطقة
خربة-الدوير اسم علم - مكان مدينة / مُقاطَعة / منطقة
خربة-داوود  اسم علم - مكان مدينة / مُقاطَعة / منطقة
خربة-روحه   اسم علم - مكان مدينة / مُقاطَعة / منطقة
خربة-سلم    اسم علم - مكان مدينة / مُقاطَعة / منطقة
خرونينغن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
خريبة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
خريبة-الجندي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
خريبكة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
خسماتشال-براديش اسم علم - مكان مدينة / مُقاطَعة / منطقة
خصب اسم علم - مكان مدينة / مُقاطَعة / منطقة
خط-البترول  اسم علم - مكان مدينة / مُقاطَعة / منطقة
خليج    اسم علم - مكان - بحر / خليج / مضيق
خليفة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
خملنيتسكي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
خنان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
خنشارة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
خنشلة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
خنيفرة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
خوارزم  اسم علم - مكان مدينة / مُقاطَعة / منطقة
خوتيابا اسم علم - مكان مدينة / مُقاطَعة / منطقة
خوجالي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
خوجاوند اسم علم - مكان مدينة / مُقاطَعة / منطقة
خوخوي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
خوزستان اسم علم - مكان مدينة / مُقاطَعة / منطقة
خوست    اسم علم - مكان مدينة / مُقاطَعة / منطقة
خولنا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
خوماس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
خون-كاين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
خيرسون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
خيزي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
خيلدرلند    اسم علم - مكان مدينة / مُقاطَعة / منطقة
خيماني  اسم علم - مكان مدينة / مُقاطَعة / منطقة
خيوا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
خيوس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دا-نانج اسم علم - مكان مدينة / مُقاطَعة / منطقة
داخابون اسم علم - مكان مدينة / مُقاطَعة / منطقة
داخلة-نواذيبو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دادرا-ونكار-هاويلي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
دار-السلام  اسم علم - مكان مدينة / مُقاطَعة / منطقة
دار-بعشتار  اسم علم - مكان مدينة / مُقاطَعة / منطقة
دار-شنزين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دار-كليب    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دارفور  اسم علم - مكان مدينة / مُقاطَعة / منطقة
دارلنغ  اسم علم - مكان - نهر / بُحيرة
دارمشتات    اسم علم - مكان مدينة / مُقاطَعة / منطقة
داروِن  اسم علم - مكان مدينة / مُقاطَعة / منطقة
داريا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
داريا-زغرتا اسم علم - مكان مدينة / مُقاطَعة / منطقة
دارين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
داشكاسان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
داشوغوز اسم علم - مكان مدينة / مُقاطَعة / منطقة
داغانا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
داغستان اسم علم - مكان مدينة / مُقاطَعة / منطقة
دافاشي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
دافاو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
داك-لاك اسم علم - مكان مدينة / مُقاطَعة / منطقة
داك-نونج    اسم علم - مكان مدينة / مُقاطَعة / منطقة
داكار   اسم علم - مكان - عاصِمة
داكوتا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
دالارنا اسم علم - مكان مدينة / مُقاطَعة / منطقة
دالاس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دالهوندين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دامان-وديو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
دامبيني اسم علم - مكان مدينة / مُقاطَعة / منطقة
داوجافبلس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دايتن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دايجيون اسم علم - مكان مدينة / مُقاطَعة / منطقة
دايکندي اسم علم - مكان مدينة / مُقاطَعة / منطقة
دبا-روا اسم علم - مكان مدينة / مُقاطَعة / منطقة
دبعال   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دبل اسم علم - مكان مدينة / مُقاطَعة / منطقة
دبلن    اسم علم - مكان - عاصِمة
دبوباوي-مبراغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دبوباوي-معراب   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دبي اسم علم - مكان مدينة / مُقاطَعة / منطقة
دبين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دترويت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
دجلة    اسم علم - مكان - نهر / بُحيرة
دجوغو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دخان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دخيل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ددلي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دده اسم علم - مكان مدينة / مُقاطَعة / منطقة
درامن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دراو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
درب-السيم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دردغيا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
درعا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
درنة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
درهام   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دروبيتا-تورنو-سيفيرين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دروغوفو اسم علم - مكان مدينة / مُقاطَعة / منطقة
درومونفيل   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دريسدن  اسم علم - مكان مدينة / مُقاطَعة / منطقة
دزودزي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
دساو-روسلاو اسم علم - مكان مدينة / مُقاطَعة / منطقة
دسوق    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دشنا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دغيمحاري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دفن اسم علم - مكان مدينة / مُقاطَعة / منطقة
دقّيه   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دكا اسم علم - مكان - عاصِمة
دكرنس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دكوانة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
دلحون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دلهي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دمازين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
دمبارتون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دمستان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
دمشق    اسم علم - مكان - عاصِمة
دمفرلين اسم علم - مكان مدينة / مُقاطَعة / منطقة
دمنهور  اسم علم - مكان مدينة / مُقاطَعة / منطقة
دمياط   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دميت    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دنبو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دنجيلا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
دندي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دنفر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دنقلا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دنكاليا اسم علم - مكان مدينة / مُقاطَعة / منطقة
دنيبروبيتروفسك  اسم علم - مكان مدينة / مُقاطَعة / منطقة
دنيستر  اسم علم - مكان - نهر / بُحيرة
دهب اسم علم - مكان مدينة / مُقاطَعة / منطقة
دهران   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دهلك    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دهوك    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دوالا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دوبروسيفو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دوبروفنيك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دوبلون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
دوبيه   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دوبيونكي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دودلينغن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دودوما  اسم علم - مكان - عاصِمة
دوديكانيسيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
دوراتي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
دورازنو اسم علم - مكان مدينة / مُقاطَعة / منطقة
دورام   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دورانجو اسم علم - مكان مدينة / مُقاطَعة / منطقة
دورتموند    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دوروغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دوريس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دوسلدورف    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دوسن-كريك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دوسو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دوشنبه  اسم علم - مكان - عاصِمة
دوفان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دوفر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دولنا-بانجيكا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دولنوشلنسكي اسم علم - مكان مدينة / مُقاطَعة / منطقة
دولنيني اسم علم - مكان مدينة / مُقاطَعة / منطقة
دوما    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دومانيانو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دومبيير-سور-شالارون اسم علم - مكان مدينة / مُقاطَعة / منطقة
دوموني  اسم علم - مكان مدينة / مُقاطَعة / منطقة
دومينيكا    اسم علم - مكان - دولة
دون اسم علم - مكان - نهر / بُحيرة
دوناوشينغن  اسم علم - مكان مدينة / مُقاطَعة / منطقة
دونتشيري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دونج-ثاب    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دونج-ناي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دونسدين اسم علم - مكان مدينة / مُقاطَعة / منطقة
دونغا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دونكيرك اسم علم - مكان مدينة / مُقاطَعة / منطقة
دونيتسك اسم علم - مكان مدينة / مُقاطَعة / منطقة
دونيدين اسم علم - مكان مدينة / مُقاطَعة / منطقة
دوير    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دوير-عدوية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
دويسبورغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دويه    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دي-أو-مونتيج    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دي-لا-باهيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
دي-موين اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديار-بكر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديالي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديانا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديبار   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديبر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديترويت اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديجون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دير-الأحمر  اسم علم - مكان مدينة / مُقاطَعة / منطقة
دير-البلح   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دير-الحرف   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دير-الزهراني    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دير-الزور   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دير-القمر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دير-انطار   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دير-جنين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دير-دلوم    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دير-دوريت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دير-سريان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دير-عامص    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دير-عشاير   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دير-قانون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دير-كوش اسم علم - مكان مدينة / مُقاطَعة / منطقة
دير-مواس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دير-ميماس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
دير-نبوح    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديرا-غازي-خان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديرب-نجم    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديربي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديرة-داوا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديرعمار اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديروط   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديريامبا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديستريتو-كابيتال    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديسين-شاربيو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديشونية اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديغورا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديفا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديفردينغن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديفس    اسم علم - مكان - بحر / خليج / مضيق
ديفيس   اسم علم - مكان - بحر / خليج / مضيق
ديك-المحدي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديكرش   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديلاوير اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديلتشيفو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديلوغوجدي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديلي    اسم علم - مكان - عاصِمة
ديليجان اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديمونة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديميانكا    اسم علم - مكان - نهر / بُحيرة
ديمير-كابيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديمير-هيسار اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديميرارا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
دين-بين اسم علم - مكان مدينة / مُقاطَعة / منطقة
دينيري  اسم علم - مكان مدينة / مُقاطَعة / منطقة
دينيغومودو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ديوربيل اسم علم - مكان مدينة / مُقاطَعة / منطقة
ذراما   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ذمار    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ذوق-الحبالصة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ذوق-الحصنية اسم علم - مكان مدينة / مُقاطَعة / منطقة
ذوق-الخرب   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ذوق-مصبح    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ذوق-مكايل   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ذي-قار  اسم علم - مكان مدينة / مُقاطَعة / منطقة
را  اسم علم - مكان مدينة / مُقاطَعة / منطقة
رابلا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
رابية-  اسم علم - مكان مدينة / مُقاطَعة / منطقة
راتاناكيري  اسم علم - مكان مدينة / مُقاطَعة / منطقة
راتشابوري   اسم علم - مكان مدينة / مُقاطَعة / منطقة
راجستان اسم علم - مكان مدينة / مُقاطَعة / منطقة
راجشاهي اسم علم - مكان مدينة / مُقاطَعة / منطقة
راس-الحرف   اسم علم - مكان مدينة / مُقاطَعة / منطقة
راس-العين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
راس-أوسطة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
راس-بعلبك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
راس-كيفا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
راستات  اسم علم - مكان مدينة / مُقاطَعة / منطقة
راشيا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
راشيا-الفخار    اسم علم - مكان مدينة / مُقاطَعة / منطقة
رافد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
رافينيل اسم علم - مكان مدينة / مُقاطَعة / منطقة
رالي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
رام اسم علم - مكان مدينة / مُقاطَعة / منطقة
رام-الله    اسم علم - مكان مدينة / مُقاطَعة / منطقة
رامية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
راندستاد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
رانس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
رايخنبرغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
رايفيرا اسم علم - مكان مدينة / مُقاطَعة / منطقة
رايكيانسبير اسم علم - مكان مدينة / مُقاطَعة / منطقة
راينباخ اسم علم - مكان مدينة / مُقاطَعة / منطقة
راينلاند    اسم علم - مكان مدينة / مُقاطَعة / منطقة
راينه   اسم علم - مكان مدينة / مُقاطَعة / منطقة
رايونغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
رأس-الخيمة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
رأس-المتن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
رأس-سدر اسم علم - مكان مدينة / مُقاطَعة / منطقة
رأس-غارب    اسم علم - مكان مدينة / مُقاطَعة / منطقة
رأس-لفان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
رب-ثلاثين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ربَك    اسم علم - مكان مدينة / مُقاطَعة / منطقة
رجم-بيت-حسين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
رجم-بيت-خلف اسم علم - مكان مدينة / مُقاطَعة / منطقة
رجم-بيت-عيسى    اسم علم - مكان مدينة / مُقاطَعة / منطقة
رحوفوت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
رحيت    اسم علم - مكان مدينة / مُقاطَعة / منطقة
رحيم-يار-خان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
رد-دير  اسم علم - مكان مدينة / مُقاطَعة / منطقة
رسول-زاده   اسم علم - مكان مدينة / مُقاطَعة / منطقة
رشاف    اسم علم - مكان مدينة / مُقاطَعة / منطقة
رشعين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
رشكنانيه    اسم علم - مكان مدينة / مُقاطَعة / منطقة
رشيد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
رعشين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
رعنانا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
رفح اسم علم - مكان مدينة / مُقاطَعة / منطقة
رم-كاي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
رمات-غان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
رماح    اسم علم - مكان مدينة / مُقاطَعة / منطقة
رمادية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
رموسكي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
رميش    اسم علم - مكان مدينة / مُقاطَعة / منطقة
رميلة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
رمينكو-فيلتشا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
رنشون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
رهط اسم علم - مكان مدينة / مُقاطَعة / منطقة
روالبندي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
روان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
رواندا  اسم علم - مكان - دولة
روبرتسبورت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
روبيه   اسم علم - مكان مدينة / مُقاطَعة / منطقة
روتردام اسم علم - مكان مدينة / مُقاطَعة / منطقة
روتشيستر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
روتوروا اسم علم - مكان مدينة / مُقاطَعة / منطقة
روجالاند    اسم علم - مكان مدينة / مُقاطَعة / منطقة
رود-آيلاند  اسم علم - مكان مدينة / مُقاطَعة / منطقة
رودس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
روذوبي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
رورايما اسم علم - مكان مدينة / مُقاطَعة / منطقة
روس اسم علم - مكان - بحر / خليج / مضيق
روستافي اسم علم - مكان مدينة / مُقاطَعة / منطقة
روستوف-أوبلاست  اسم علم - مكان مدينة / مُقاطَعة / منطقة
روستوف-نا-دونو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
روستوك  اسم علم - مكان مدينة / مُقاطَعة / منطقة
روسكيلد اسم علم - مكان مدينة / مُقاطَعة / منطقة
روسكيلده    اسم علم - مكان مدينة / مُقاطَعة / منطقة
روسيا   اسم علم - مكان - دولة
روسياو  اسم علم - مكان - عاصِمة
روصو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
روض-الفرج   اسم علم - مكان مدينة / مُقاطَعة / منطقة
روفانييمي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
روفوما  اسم علم - مكان مدينة / مُقاطَعة / منطقة
روكا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
روكوا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
روكيسكيس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
رولي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
روما    اسم علم - مكان - عاصِمة
رومانيا اسم علم - مكان - دولة
رومية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
رومين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
رونجيرك اسم علم - مكان مدينة / مُقاطَعة / منطقة
روندونيا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
روي-إت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
رويتلينين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
رويسات-البلوط   اسم علم - مكان مدينة / مُقاطَعة / منطقة
رياق    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريبنتينيي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريبي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريتالهوليو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريتشموند    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريثيمنو اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريجاينا اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريدوندا اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريدينغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريرسر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريزيكني اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريسيفي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريشدبين اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريشون-لتسيون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريشيتسا اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريغا    اسم علم - مكان - عاصِمة
ريغنسبورغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريفرسايد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريفنه   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريكيافيك    اسم علم - مكان - عاصِمة
ريمات   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريمة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
رين اسم علم - مكان مدينة / مُقاطَعة / منطقة
رينجكوبنج   اسم علم - مكان مدينة / مُقاطَعة / منطقة
رينو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
رينيل-وبيلونا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريو-برانكو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريو-جراندي-دو-سول   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريو-دي-جانيرو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريو-غراندي-دو-نورتي اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريو-نيغرو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريوا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريوبامبا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريوكيو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ريوم    اسم علم - مكان مدينة / مُقاطَعة / منطقة
زائير   اسم علم - مكان مدينة / مُقاطَعة / منطقة
زابل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
زابورزيا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
زاجاس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
زاخودنيبومورسكي اسم علم - مكان مدينة / مُقاطَعة / منطقة
زاريا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
زاغرب   اسم علم - مكان - عاصِمة
زاقاتالا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
زاكابا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
زاكاتيكاس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
زاكارباتيا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
زاكينثوس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
زالا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
زالاو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
زالتسغيتر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
زالنجي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
زام-نو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
زامبوانغا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
زامبيا  اسم علم - مكان - دولة
زامبيزيا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
زامورا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
زان اسم علم - مكان مدينة / مُقاطَعة / منطقة
زان-زان اسم علم - مكان مدينة / مُقاطَعة / منطقة
زانستد  اسم علم - مكان مدينة / مُقاطَعة / منطقة
زبقين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
زحلة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
زحلتا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
زرداب   اسم علم - مكان مدينة / مُقاطَعة / منطقة
زرعون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
زعيتر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
زغدريا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
زغرتا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
زغوان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
زفتا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
زفتى    اسم علم - مكان مدينة / مُقاطَعة / منطقة
زقزوق   اسم علم - مكان مدينة / مُقاطَعة / منطقة
زكرون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
زكريت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
زلقا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
زليتوفو اسم علم - مكان مدينة / مُقاطَعة / منطقة
زمور    اسم علم - مكان مدينة / مُقاطَعة / منطقة
زنجان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
زنجبار  اسم علم - مكان مدينة / مُقاطَعة / منطقة
زنجيلان اسم علم - مكان مدينة / مُقاطَعة / منطقة
زنيتسا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
زهيرية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
زو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
زوترمير اسم علم - مكان مدينة / مُقاطَعة / منطقة
زوطر-الشرقية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
زوطر-الغربية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
زوغديدي اسم علم - مكان مدينة / مُقاطَعة / منطقة
زويدرو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
زويندريخت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
زي-مانزيني  اسم علم - مكان مدينة / مُقاطَعة / منطقة
زيتا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
زيتوسي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
زيتومير اسم علم - مكان مدينة / مُقاطَعة / منطقة
زيتون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
زيجمالي اسم علم - مكان مدينة / مُقاطَعة / منطقة
زيري    اسم علم - مكان - نهر / بُحيرة
زيغنشور اسم علم - مكان مدينة / مُقاطَعة / منطقة
زيلاند  اسم علم - مكان مدينة / مُقاطَعة / منطقة
زيلع    اسم علم - مكان مدينة / مُقاطَعة / منطقة
زيلينيكوفو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
زيمبابوي - روديسيا-الجنوبية اسم علم - مكان - دولة
زيندر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سا-كايو اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساباراغاموا اسم علم - مكان مدينة / مُقاطَعة / منطقة
سابوبان اسم علم - مكان مدينة / مُقاطَعة / منطقة
سابولكس-ساتمار-بيريغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساتاكونتا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساتو-ماري   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساتوبايتيا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساتون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساحل-سليم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سادا-مايوطي اسم علم - مكان مدينة / مُقاطَعة / منطقة
سار اسم علم - مكان مدينة / مُقاطَعة / منطقة
سارابوري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساراتوف اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساراتوف-أوبلاست اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساراماكا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساربانغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساربروكن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساربسبورغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سارجاسو اسم علم - مكان - بحر / خليج / مضيق
سارلاند اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساره    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساسكاتشوان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساسكاتون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساعتلي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساغا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساغينيه اسم علم - مكان مدينة / مُقاطَعة / منطقة
سافا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سافالو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سافاناكيت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سافانخت اسم علم - مكان مدينة / مُقاطَعة / منطقة
سافاي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سافرة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سافنا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سافو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سافوتو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سافوتولافاي اسم علم - مكان مدينة / مُقاطَعة / منطقة
سافوسافو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساقلتة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساكاتيباكيز اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساكرامنتو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساكسونيا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساكون-ناخون اسم علم - مكان مدينة / مُقاطَعة / منطقة
سال اسم علم - مكان مدينة / مُقاطَعة / منطقة
سالافان اسم علم - مكان مدينة / مُقاطَعة / منطقة
سالامومو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سالامومو-أوتو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سالتا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سالتو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سالتون‏‏    اسم علم - مكان - بحر / خليج / مضيق
سالتيو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سالزبورغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سالسيدو اسم علم - مكان مدينة / مُقاطَعة / منطقة
سالفادو اسم علم - مكان مدينة / مُقاطَعة / منطقة
سالفاليون-دي-هيغواي اسم علم - مكان مدينة / مُقاطَعة / منطقة
سالونيك اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساليان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سالياولا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساليسبري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سالينوس اسم علم - مكان مدينة / مُقاطَعة / منطقة
سامارا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساماميا اسم علم - مكان مدينة / مُقاطَعة / منطقة
سامانا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سامتريديا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سامتسي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سامدروب-جونغخار اسم علم - مكان مدينة / مُقاطَعة / منطقة
سامراونغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساموا   اسم علم - مكان - دولة
ساموت-براكان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساموت-ساخون اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساموت-سونغخرام  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساموخ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساموس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-أغناسيو-دي-سابانيتا اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-أنطونيو اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-باول    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-بيتر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-بيدرو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-بيدرو-دي-ماكونيس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-بيدرو-سولا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-تياغو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-جان-سور-ريشليو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-جورج    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-جون اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-جيروم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-خوان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-خوان-دي-لا-ماغوانا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-خوسيه   اسم علم - مكان - عاصِمة
سان-خوسيه-دي-أوكوا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-خوسيه-دي-مايو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-دمنجو   اسم علم - مكان - عاصِمة
سان-دوني    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-دينس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-دييغو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-سلفادور اسم علم - مكان - عاصِمة
سان-فرانسيسكو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-فرانسيسكو-دي-ماكوريس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-فرناندو-دي-مونتيكريستي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-فيسينتي اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-فيليب   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-فيليبي-دي-بويرتو-بلاتا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-كريستوبال   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-لورنزو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-لويس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-لويس-بوتوسي اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-مارتان-ديريس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-مارتن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-ماركوس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-ماري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-مارينو  اسم علم - مكان - دولة
سان-ميغيل   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-هوان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سان-هوزيه   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-آن اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-آن-ساندي-بوينت اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-ألبرت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-أندرو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-أوستاش اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-إتيان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-إليزابيث   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-باتريك اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-بريست  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-بريوك  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-بطرسبرغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-بول    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-بول-تشارلز-تاون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-بول-كابستير    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-بيتر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-بيتر-باستير    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-توماس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-توماس-لولاند   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-توماس-مدل-آيلاند   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-جورج   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-جورج-باستير    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-جورج-جنجرلاند  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-جورجز  اسم علم - مكان - عاصِمة
سانت-جوزيف  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-جوليا-دي-لوريا اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-جوليان-لابورس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-جون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-جون-فيغتري اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-جون-كابستير    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-جونز   اسم علم - مكان - عاصِمة
سانت-جيمس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-جيمس-ويندوارد  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-دافيد  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-ديفيد  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-رافاييل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-سير-إكول   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-فالير  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-فنسنت  اسم علم - مكان - بحر / خليج / مضيق
سانت-فيليب  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-كاترين اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-كيتس-ونيفيس    اسم علم - مكان - دولة
سانت-لورنس  اسم علم - مكان - بحر / خليج / مضيق
سانت-لوسي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-لوسيا  اسم علم - مكان - دولة
سانت-لوقا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-لويس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-مارك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-ماري   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-ماري-كايون اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-مايكل  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانت-هيلانة اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانتا-آنا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانتا-باربارا-دي-سامانا اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانتا-بربارا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانتا-روزا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانتا-فيه   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانتا-كاتارينا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانتا-كروز  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانتا-كروز-دل-سيبو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانتا-كروز-دي-باراهونا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانتا-كروز-دي-لا-سييرا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانتاريم    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانتاكروز   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانتس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانتو-أنتاو اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانتو-دومينجو-دي-غوزمان اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانتو-دومينغو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانتو-دومينغو-إيستي اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانتو-دومينغو-دي-لوس-كولورادوس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانتياغو    اسم علم - مكان - عاصِمة
سانتياغو-دي-كوبا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانتياغو-دي-لوس-كاباييروس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانتياغو-ديل-استيرو اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانتياغو-رودريغز    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساندفيورد   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانشيز-راميريز  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانكت-بولتن اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانكتي-سبيريتوس اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانما   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سانيكيلي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساو-باولو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساو-تومي    اسم علم - مكان - عاصِمة
ساو-تومي-وبرينسيبي  اسم علم - مكان - دولة
ساو-فيسونت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساو-لويز    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساو-نيكولو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساوث-كارولاينا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساوثامبتون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساوثند-أون-سي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ساوسيللو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سايتاما اسم علم - مكان مدينة / مُقاطَعة / منطقة
سايذيبولي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سايغون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سايلم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سبرنغفيلد   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سبروس-غرووف اسم علم - مكان مدينة / مُقاطَعة / منطقة
سبرينج-فيلد اسم علم - مكان مدينة / مُقاطَعة / منطقة
سبعل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سبنسر   اسم علم - مكان - بحر / خليج / مضيق
سبها    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سبيتاك  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ستارازاغورا اسم علم - مكان مدينة / مُقاطَعة / منطقة
ستافانغر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ستان-كريك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ستاينشير    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ستباناكيرت  اسم علم - مكان - عاصِمة
ستراسبورغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سترة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ستروغا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ستروميكا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ستورستروم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ستوك-أون-ترنت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ستوكتن  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ستوكهولم    اسم علم - مكان - عاصِمة
ستونغ-ترينغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
ستيبانافان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ستيوردال    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سخنين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سخومي   اسم علم - مكان - عاصِمة
سدرة    اسم علم - مكان - بحر / خليج / مضيق
سدرك    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سرار    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سرام    اسم علم - مكان - بحر / خليج / مضيق
سراوق   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سراييفو اسم علم - مكان - عاصِمة
سربل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سرت اسم علم - مكان مدينة / مُقاطَعة / منطقة
سرجغا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سرجودها اسم علم - مكان مدينة / مُقاطَعة / منطقة
سرحد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سرداريا اسم علم - مكان مدينة / مُقاطَعة / منطقة
سردينيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
سرس-الليان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سرعل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سرعين-التحتا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سرعين-الفوقا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سرغومين اسم علم - مكان مدينة / مُقاطَعة / منطقة
سرقسطة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سرقودة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سرمبان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سريلانكا    اسم علم - مكان - دولة
سريناغار    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سطات    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سطيف    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سعيدة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سفاجا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سفاي-رينغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سفنتو-جيورجي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سفيردلوفسك-أوبلاست  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سفينة-الدريب    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سفينة-القيطع    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سقنيتي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سكاكا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سكرامنتو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سكسونيا-أنهالت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سكوبجي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سكوبيه  اسم علم - مكان - عاصِمة
سكوتسديل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سكوتشيا اسم علم - مكان - بحر / خليج / مضيق
سكيكدة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سكين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سلا اسم علم - مكان مدينة / مُقاطَعة / منطقة
سلاتينا اسم علم - مكان مدينة / مُقاطَعة / منطقة
سلانغور اسم علم - مكان مدينة / مُقاطَعة / منطقة
سلتيك‏‏     اسم علم - مكان - بحر / خليج / مضيق
سلطان-بتيري اسم علم - مكان مدينة / مُقاطَعة / منطقة
سلطان-بور   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سلطان-يعقوب اسم علم - مكان مدينة / مُقاطَعة / منطقة
سلطنة-عمان  اسم علم - مكان - دولة
سلعا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سلعاتا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سلفاية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سلماباد اسم علم - مكان مدينة / مُقاطَعة / منطقة
سلمنكا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سلمية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سلنغا   اسم علم - مكان - نهر / بُحيرة
سلوفاكيا    اسم علم - مكان - دولة
سلوفينيا    اسم علم - مكان - دولة
سليانة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سمارا-أوبلاست   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سمالوط  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سماهيج  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سمرقند  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سمسطا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سمقانية اسم علم - مكان مدينة / مُقاطَعة / منطقة
سمنان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سمنكان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سمنود   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سموخة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سميلان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سن-الفيل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سنابس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سناج    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سنار    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سناق    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سنجة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سنجليا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سند اسم علم - مكان مدينة / مُقاطَعة / منطقة
سندرلاند    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سنسناتي اسم علم - مكان مدينة / مُقاطَعة / منطقة
سنغ-بوري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سنغافورة    اسم علم - مكان - دولة - عاصمة
سنغوا   اسم علم - مكان - نهر / بُحيرة
سنورس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سنيا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سهيلة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سوازيلاند   اسم علم - مكان - دولة
سواسون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سواكن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سوانزي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سوبكارباتيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
سوبوتيكا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سوتشافا اسم علم - مكان مدينة / مُقاطَعة / منطقة
سوتشيتيبيكيز    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سوخومي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سود اسم علم - مكان مدينة / مُقاطَعة / منطقة
سودرمانلاند اسم علم - مكان مدينة / مُقاطَعة / منطقة
سور-تروندلاغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سورات   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سورات-ثاني  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سوردس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سورو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سوريا   اسم علم - مكان - دولة
سوريانو اسم علم - مكان مدينة / مُقاطَعة / منطقة
سورين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سورينام اسم علم - مكان - دولة
سوسة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سوفا    اسم علم - مكان - عاصِمة
سوفالا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سوفانبوري   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سوفريير اسم علم - مكان مدينة / مُقاطَعة / منطقة
سوق-الغرب   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سوق-أهراس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سوكسكسارغن  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سوكوتاي اسم علم - مكان مدينة / مُقاطَعة / منطقة
سوكوده  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سوكومبيوس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سوكوى   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سول اسم علم - مكان مدينة / مُقاطَعة / منطقة
سولاوسي اسم علم - مكان مدينة / مُقاطَعة / منطقة
سولاويسي    اسم علم - مكان - بحر / خليج / مضيق
سولت-ليك-سيتي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سولو    اسم علم - مكان - بحر / خليج / مضيق
سولولا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سولينا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سولينغن اسم علم - مكان مدينة / مُقاطَعة / منطقة
سومطرة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سومقاييت    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سوموغي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سومي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سوميدا  اسم علم - مكان - نهر / بُحيرة
سون-وفيوردان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سونجكلا اسم علم - مكان مدينة / مُقاطَعة / منطقة
سوندرلاند   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سونسورول    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سونسوناته   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سونورا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سوهاج   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سويري   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سويسرا  اسم علم - مكان - دولة
سويفت-كورنت اسم علم - مكان مدينة / مُقاطَعة / منطقة
سويندون اسم علم - مكان مدينة / مُقاطَعة / منطقة
سي-سا-كت    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيئون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سياتل   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيارا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيازان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيال-كوت    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيام-ريب    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيانوكفيل   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيباتاك     اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيباليويني  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيبريا  اسم علم - مكان - بحر / خليج / مضيق
سيبوس   اسم علم - مكان - نهر / بُحيرة
سيبون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيبويان اسم علم - مكان - بحر / خليج / مضيق
سيبيك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيبيو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيتباناكيرت اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيتو    اسم علم - مكان - بحر / خليج / مضيق
سيتوبال اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيتيكي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيحون   اسم علم - مكان - نهر / بُحيرة
سيدادي دي مابوتو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيدني   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيدي-بلعباس اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيدي-بوزيد  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيدي-سالم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيدي-سليمان اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيدي-قاسم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سير-الضنية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سير-الغربية اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيرافالـي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيراليون - رومادونج اسم علم - مكان - دولة
سيرجبيل اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيرجيبي اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيرس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيرو-لارغو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيروا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيستان-وبلوتشستان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيسوفون اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيسوق   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيسيان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيشوان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيشيل   اسم علم - مكان - دولة
سيغن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيغو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيغو-دي-أفيلا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيغيشوارا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيفاستوبول  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيفان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيكَاتوكا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيكاسو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيكونغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيكيم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيلهت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيليبابي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيليبي-بيكوي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيلييه  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيمبو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيميشليا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيميناوي-مبراغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيميناوي-معراب  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سين-شو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيناء   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيناكي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سينالوا اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيناي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سينايا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سينت-بول    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سينت-بيترسبرغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سينت-دي اسم علم - مكان مدينة / مُقاطَعة / منطقة
سينت-لويس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سينترو-سور  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سينجيدا اسم علم - مكان مدينة / مُقاطَعة / منطقة
سينسيناتي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سينفويغوس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سينمونوروم  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سينوي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سينويجو اسم علم - مكان مدينة / مُقاطَعة / منطقة
سينيق   اسم علم - مكان - نهر / بُحيرة
سيوداد-خواريز   اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيوداد-دي-بوينس-آيرس-الاتحادية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيوداد-ديل-إستي اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيول    اسم علم - مكان - عاصِمة
سيونغنام    اسم علم - مكان مدينة / مُقاطَعة / منطقة
سيونيك  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شاتو-بيلير  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شارلوت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شارلوروا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شارينتاسافان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شاشوينجساو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شاكو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شاكي-زاقاتالا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شالا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شالاتينانغو اسم علم - مكان مدينة / مُقاطَعة / منطقة
شاله    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شاما    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شاماخي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شامبيشي اسم علم - مكان - نهر / بُحيرة
شامبيني-سور-مارني   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شان اسم علم - مكان مدينة / مُقاطَعة / منطقة
شاندونغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
شانغ-هوا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شانكشي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شاه-بوز اسم علم - مكان مدينة / مُقاطَعة / منطقة
شاه-علم اسم علم - مكان مدينة / مُقاطَعة / منطقة
شاهوميان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شاوينيغان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شايان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شبانية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شبرا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شبرا-الخيمة اسم علم - مكان مدينة / مُقاطَعة / منطقة
شبراخيت اسم علم - مكان مدينة / مُقاطَعة / منطقة
شبعا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شبلي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شبوة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شبيلي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شبين-القناطر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شبين-الكوم  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شتاتشن  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شتاده   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شتايرمارك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شتوتغارت    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شتورا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شحتول   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شحور    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شحيم    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شخلار   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شربين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شرم-الشيخ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شرور    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شط-العرب    اسم علم - مكان - نهر / بُحيرة
شط-الكوفة   اسم علم - مكان - نهر / بُحيرة
شط-ملغيغ    اسم علم - مكان - بحر / خليج / مضيق
شعب اسم علم - مكان مدينة / مُقاطَعة / منطقة
شفا-عمرو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شفاعمرو اسم علم - مكان مدينة / مُقاطَعة / منطقة
شفيرين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شفيلد   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شفينتوكشيسكي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شقاديف  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شقرا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شقيب-السلام اسم علم - مكان مدينة / مُقاطَعة / منطقة
شكودر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شكي اسم علم - مكان مدينة / مُقاطَعة / منطقة
شلاتين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شلتنهام‏    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شلنسكي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شليزين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شليسفغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شليفا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شمال-الراين اسم علم - مكان مدينة / مُقاطَعة / منطقة
شمال-قبرص-التركية - قبرص-الشمالية   اسم علم - مكان - دولة
شمبقّو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شمبورازو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شمسطار  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شمكير   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شناعير  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شنشي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شنغهاي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شنقولا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شنقيط   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شهارة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شهركان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شواسول  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شواغير-التحتا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شواغير-الفوقا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شوشا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شوشي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شوكية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شوكين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شومن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شونشيون اسم علم - مكان مدينة / مُقاطَعة / منطقة
شونين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شويا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شويت    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شويفات  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شياح    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شيانج-ري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شيانج-ماي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شيبيلي  اسم علم - مكان - نهر / بُحيرة
شيتاجونج    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شيتومال اسم علم - مكان مدينة / مُقاطَعة / منطقة
شيحين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شيرا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شيراك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شيربروك اسم علم - مكان مدينة / مُقاطَعة / منطقة
شيروان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شيرونغي اسم علم - مكان مدينة / مُقاطَعة / منطقة
شيزوكا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شيغا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شيكاغو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شيكوكو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شيكوني  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شيمانه  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شيملا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شين اسم علم - مكان مدينة / مُقاطَعة / منطقة
شين-سو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شينجيانغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شينيانغا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
شيواوا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
شييزانوفا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
شييفا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
صابر-أباد   اسم علم - مكان مدينة / مُقاطَعة / منطقة
صاليما  اسم علم - مكان مدينة / مُقاطَعة / منطقة
صباح    اسم علم - مكان مدينة / مُقاطَعة / منطقة
صحار    اسم علم - مكان مدينة / مُقاطَعة / منطقة
صخور-ليانكورت   اسم علم - مكان - بحر / خليج / مضيق
صدد اسم علم - مكان مدينة / مُقاطَعة / منطقة
صدفا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
صديقين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
صربا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
صربيا   اسم علم - مكان - دولة
صربين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
صُرخُنْداريا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
صرواح   اسم علم - مكان مدينة / مُقاطَعة / منطقة
صريفا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
صعدة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
صغبين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
صغد اسم علم - مكان مدينة / مُقاطَعة / منطقة
صفاريه  اسم علم - مكان مدينة / مُقاطَعة / منطقة
صفاقس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
صفد اسم علم - مكان مدينة / مُقاطَعة / منطقة
صفد-البطيخ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
صفرو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
صقلية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
صلالة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
صنعاء   اسم علم - مكان - عاصِمة
صنعفي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
صوانة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
صور اسم علم - مكان مدينة / مُقاطَعة / منطقة
صوفر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
صوفيا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
صوفيا-أنتيبوليس اسم علم - مكان مدينة / مُقاطَعة / منطقة
صول اسم علم - مكان مدينة / مُقاطَعة / منطقة
صيدا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
صيدون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ضبيه    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ضهر-الأحمر  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ضهر-الحسين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ضهر-الصوان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ضهر-العوادة اسم علم - مكان مدينة / مُقاطَعة / منطقة
ضهر-العين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ضهر-المغارة اسم علم - مكان مدينة / مُقاطَعة / منطقة
ضهر-حدارة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ضهور-الشوير اسم علم - مكان مدينة / مُقاطَعة / منطقة
طابا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
طاجيكستان   اسم علم - مكان - دولة
طاريا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
طامية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
طانطان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
طاووق-صو    اسم علم - مكان - نهر / بُحيرة
طبرجا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
طبرق    اسم علم - مكان مدينة / مُقاطَعة / منطقة
طبرقة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
طبريا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
طرابلس  اسم علم - مكان - عاصِمة - مُقاطَعة / منطقة
طرطوس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
طرعان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
طشقند   اسم علم - مكان - عاصِمة
طلاس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
طلخا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
طلوسة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
طما اسم علم - مكان مدينة / مُقاطَعة / منطقة
طنبوريت اسم علم - مكان مدينة / مُقاطَعة / منطقة
طنجة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
طنطا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
طهران   اسم علم - مكان - عاصِمة
طهطا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
طوخ اسم علم - مكان مدينة / مُقاطَعة / منطقة
طورا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
طورزا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
طوكيو   اسم علم - مكان - عاصِمة
طولكرم  اسم علم - مكان مدينة / مُقاطَعة / منطقة
طيبة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
طير-حرفا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
طير-دبا اسم علم - مكان مدينة / مُقاطَعة / منطقة
طيرفلسيه    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ظفار    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ظهيرة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عابا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عابدين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
عاريا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عازور   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عاقورة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
عالي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عاليه   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عانوت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عبا اسم علم - مكان مدينة / مُقاطَعة / منطقة
عبادية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
عباسيّة اسم علم - مكان مدينة / مُقاطَعة / منطقة
عبدين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عبرا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عبري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عبرين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عتاقة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عتق اسم علم - مكان مدينة / مُقاطَعة / منطقة
عجلتون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
عجلون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عجمان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عدبل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عدشيت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عدشيت-الشقيف    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عدل اسم علم - مكان مدينة / مُقاطَعة / منطقة
عدلون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عدن اسم علم - مكان مدينة / مُقاطَعة / منطقة
عدوسية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
عدي-تكليزان اسم علم - مكان مدينة / مُقاطَعة / منطقة
عدي-خوالا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عدي-قيّح    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عديسة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عراد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عرب-الجل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عرب-سكر اسم علم - مكان مدينة / مُقاطَعة / منطقة
عرب-طبايا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عربانية اسم علم - مكان مدينة / مُقاطَعة / منطقة
عربصاليم    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عرتا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عرجابو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
عرجس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عــرّزا اسم علم - مكان مدينة / مُقاطَعة / منطقة
عرزال   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عرسال   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عرضة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عرعر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عرقا    اسم علم - مكان - نهر / بُحيرة
عرمون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عزة اسم علم - مكان مدينة / مُقاطَعة / منطقة
عزر اسم علم - مكان مدينة / مُقاطَعة / منطقة
عزقي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عزور    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عسقلان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
عسكر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عسير    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عشق-آباد    اسم علم - مكان - عاصِمة
عشقوت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عصب اسم علم - مكان مدينة / مُقاطَعة / منطقة
عطار    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عطبرة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عطرين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عفار    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عفرين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عقتنيت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
عقيبة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عكا اسم علم - مكان مدينة / مُقاطَعة / منطقة
عكار    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عكفا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عكيكة   اسم علم - مكان - نهر / بُحيرة
علالية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
علما-الشعب  اسم علم - مكان مدينة / مُقاطَعة / منطقة
علمات   اسم علم - مكان مدينة / مُقاطَعة / منطقة
علمان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
على-سبح اسم علم - مكان مدينة / مُقاطَعة / منطقة
علي-الطاهر  اسم علم - مكان مدينة / مُقاطَعة / منطقة
عمار-البيكات    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عمارة-شلهوب اسم علم - مكان مدينة / مُقاطَعة / منطقة
عماطور  اسم علم - مكان مدينة / مُقاطَعة / منطقة
عمان    اسم علم - مكان - بحر / خليج / مضيق
عمّان   اسم علم - مكان - عاصِمة
عمران   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عمشيت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عميق    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عنا اسم علم - مكان مدينة / مُقاطَعة / منطقة
عنابة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عنتاب   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عنجر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عندقت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عنقون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عوالي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عوكر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عوهة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عيتا-الجبل  اسم علم - مكان مدينة / مُقاطَعة / منطقة
عيتا-الشعب  اسم علم - مكان مدينة / مُقاطَعة / منطقة
عيتا-الفخار اسم علم - مكان مدينة / مُقاطَعة / منطقة
عيتانيت اسم علم - مكان مدينة / مُقاطَعة / منطقة
عيترون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
عيتيت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عيدمون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
عيرون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عيسى    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عيلا-برعد   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عيما    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-التينة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-الدفلى  اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-الرمانة اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-الريحانة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-الزيت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-السنديانة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-الصفصاف اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-أبو-عبدالله اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-إبل اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-بعال    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-بوسوار  اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-تنتا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-تيموشنت اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-حرشا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-خالد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-زبدة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-زحلتا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-سعادة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-شمس اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-عار اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-عرب اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-عطا اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-عكرين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-قانا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-قاني    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-قنيا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-كفرزبد  اسم علم - مكان مدينة / مُقاطَعة / منطقة
عين-وزين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عينات   اسم علم - مكان مدينة / مُقاطَعة / منطقة
عيناتا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
عينبال  اسم علم - مكان مدينة / مُقاطَعة / منطقة
عينطورة اسم علم - مكان مدينة / مُقاطَعة / منطقة
عينطورين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عيون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
عيون-الغزلان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
غابة-بولونيا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
غابورون اسم علم - مكان - عاصِمة
غابون-قماطية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
غات اسم علم - مكان مدينة / مُقاطَعة / منطقة
غاردابير    اسم علم - مكان مدينة / مُقاطَعة / منطقة
غاردان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غارلاند اسم علم - مكان مدينة / مُقاطَعة / منطقة
غارميش-بارتنكيرخن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
غاروا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
غاروي‎  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غاسا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
غاغايفوماوغا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
غاغايماوغا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غاغرا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
غالاتس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غالواي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غامبيا  اسم علم - مكان - دولة
غانا    اسم علم - مكان - دولة
غانزي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
غانغان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غاو اسم علم - مكان مدينة / مُقاطَعة / منطقة
غاوتينج اسم علم - مكان مدينة / مُقاطَعة / منطقة
غباربولو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
غبارنغا اسم علم - مكان مدينة / مُقاطَعة / منطقة
غبالة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
غبيري   اسم علم - مكان مدينة / مُقاطَعة / منطقة
غدانسك  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غدراس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
غراتس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
غرادسكو اسم علم - مكان مدينة / مُقاطَعة / منطقة
غرانبي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غراند-باسا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غراند-براري اسم علم - مكان مدينة / مُقاطَعة / منطقة
غراند-غيدي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غراند-كاي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
غراند-كرو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
غرانما  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غراوبوندن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
غربي-بعلبك  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غرداية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غرفنماخر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
غرودنو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غرونوبل اسم علم - مكان مدينة / مُقاطَعة / منطقة
غريان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
غريفة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
غريفين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غريفينا اسم علم - مكان مدينة / مُقاطَعة / منطقة
غرينزبورو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
غرينفيل اسم علم - مكان مدينة / مُقاطَعة / منطقة
غرينلاند    اسم علم - مكان - بحر / خليج / مضيق
غزة اسم علم - مكان مدينة / مُقاطَعة / منطقة
غزني    اسم علم - مكان مدينة / مُقاطَعة / منطقة
غلاروس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غلاسغو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غلاسكو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غلستان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غلوستر  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غلوكسبورغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
غليزان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غلينديل اسم علم - مكان مدينة / مُقاطَعة / منطقة
غليوين  اسم علم - مكان - نهر / بُحيرة
غندوانا اسم علم - مكان - قارَّة
غوا اسم علم - مكان مدينة / مُقاطَعة / منطقة
غواتيمالا   اسم علم - مكان - دولة
غواتيمالا-سيتي  اسم علم - مكان - عاصِمة
غوادالاخارا اسم علم - مكان مدينة / مُقاطَعة / منطقة
غوام    اسم علم - مكان مدينة / مُقاطَعة / منطقة
غواناخواتو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غوانتانامو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غوانغجو اسم علم - مكان مدينة / مُقاطَعة / منطقة
غواياس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غواياكيل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
غوتلند  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غوتنبرغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
غودش    اسم علم - مكان مدينة / مُقاطَعة / منطقة
غور اسم علم - مكان مدينة / مُقاطَعة / منطقة
غورنو-باداخشان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غوري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
غوريس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
غوزيليورت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
غوستيفار    اسم علم - مكان مدينة / مُقاطَعة / منطقة
غوسطا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
غومل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
غونافيس اسم علم - مكان مدينة / مُقاطَعة / منطقة
غونما   اسم علم - مكان مدينة / مُقاطَعة / منطقة
غوياس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
غويانا  اسم علم - مكان - دولة
غويانغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غويانيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
غويغل   اسم علم - مكان مدينة / مُقاطَعة / منطقة
غويلف   اسم علم - مكان مدينة / مُقاطَعة / منطقة
غيديماغا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
غيروكاستر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
غيريرو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غيسن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
غيغاركونيك  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غيفغليا اسم علم - مكان مدينة / مُقاطَعة / منطقة
غيفلبورغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
غيفو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
غيفورز  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غيكيدو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غيلان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
غيلسنكيرشن  اسم علم - مكان مدينة / مُقاطَعة / منطقة
غينيا   اسم علم - مكان - دولة
غينيا-الاستوائية    اسم علم - مكان - دولة
غينيا-بيساو اسم علم - مكان - دولة
غينيه   اسم علم - مكان مدينة / مُقاطَعة / منطقة
غيور-موسون-سبرون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
غيومري  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فاتالونغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فاتر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فاتس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فاتوفافي-فيتوفيناني اسم علم - مكان مدينة / مُقاطَعة / منطقة
فاتيك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فاثي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فادسو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فادوز   اسم علم - مكان - عاصِمة
فارس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فارسكور اسم علم - مكان مدينة / مُقاطَعة / منطقة
فارسينايس-سوومي اسم علم - مكان مدينة / مُقاطَعة / منطقة
فارمينسكو-مازورسكي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فارنا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فارو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فاريا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فارياب  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فاس اسم علم - مكان مدينة / مُقاطَعة / منطقة
فاستيراس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فاسلوي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فاسيليفو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فاغارشابات  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فافاو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فاقوس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فاك اسم علم - مكان مدينة / مُقاطَعة / منطقة
فاكينانكارترا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فالاندوفو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فالباريسو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فالغا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فالفيردي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فالميرا اسم علم - مكان مدينة / مُقاطَعة / منطقة
فالنسيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
فالوغا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فالي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فاليتا  اسم علم - مكان - عاصِمة
فاليز   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فالينزويلا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فالينس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فاماغوستا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فانادزور    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فانانو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فانتا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فانج-تاو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فانسين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فانغ-فينغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فانغ-نغا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فانكوفر اسم علم - مكان مدينة / مُقاطَعة / منطقة
فانواتو اسم علم - مكان - دولة
فاو اسم علم - مكان - مُنَظَّمة دوليَّة / هيئة / اتِّحاد
فاياو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فايتانو اسم علم - مكان مدينة / مُقاطَعة / منطقة
فايد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فايسيجانو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فايله   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فايلوا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فايمر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فآساليليغا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فآو-فونوتي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فتسلار  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فتقة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فثيوتيس اسم علم - مكان مدينة / مُقاطَعة / منطقة
فخش اسم علم - مكان - نهر / بُحيرة
فرا-ناخون-سي-أيوتثايا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فرابسيستي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فراتنيكا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فراكسرن اسم علم - مكان مدينة / مُقاطَعة / منطقة
فرانسيستاون اسم علم - مكان مدينة / مُقاطَعة / منطقة
فرانسيسكو-مورازان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فرانكفورت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فرانيستيكا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فراه    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فراي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فراي-بينتوس اسم علم - مكان مدينة / مُقاطَعة / منطقة
فرايبورغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فرجينيا-بيتش    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فرزل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فرزنو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فرساي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فرشوط   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فرغانة? اسم علم - مكان مدينة / مُقاطَعة / منطقة
فرن-الشباك  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فرناندو-دي-لا-مورا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فرنسا   اسم علم - مكان - دولة
فروتسلاو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فروتوك  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فرون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فري-ستيت    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فريبورت اسم علم - مكان مدينة / مُقاطَعة / منطقة
فريبورغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
فريتاون اسم علم - مكان - عاصِمة
فريدريكتون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فريدريكسبورج    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فريدريكستاد اسم علم - مكان مدينة / مُقاطَعة / منطقة
فريدس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فريديس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فريسنو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فريمونت اسم علم - مكان مدينة / مُقاطَعة / منطقة
فريولي-فينيتسيا-جوليا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فزبرم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فسايا   اسم علم - مكان - بحر / خليج / مضيق
فستفولد اسم علم - مكان مدينة / مُقاطَعة / منطقة
فضولي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فطاني   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فكتوريا اسم علم - مكان مدينة / مُقاطَعة / منطقة
فلاديفوستوك اسم علم - مكان مدينة / مُقاطَعة / منطقة
فلاديقوقاز  اسم علم - مكان - عاصِمة
فلاندرز اسم علم - مكان مدينة / مُقاطَعة / منطقة
فلسطين  اسم علم - مكان - دولة
فلنسبورغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فلورس   اسم علم - مكان - بحر / خليج / مضيق
فلورنسا اسم علم - مكان مدينة / مُقاطَعة / منطقة
فلوري   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فلوريانوبوليس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فلوريدا اسم علم - مكان مدينة / مُقاطَعة / منطقة
فلوريس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فلورينا اسم علم - مكان مدينة / مُقاطَعة / منطقة
فليفولند    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فليوه   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فن-فوك  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فن-لونج اسم علم - مكان مدينة / مُقاطَعة / منطقة
فنار    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فندرانج اسم علم - مكان مدينة / مُقاطَعة / منطقة
فندى    اسم علم - مكان - بحر / خليج / مضيق
فنزويلا اسم علم - مكان - دولة
فنلندا  اسم علم - مكان - دولة
فنلو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فنمارك  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فنيدق   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فو-ثو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فو-ين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فوارون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فوبرتال اسم علم - مكان مدينة / مُقاطَعة / منطقة
فوجيان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فور-دو-فرانس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فورامجيه    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فورآرلبرغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فوربومرن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فورت-ساسكاتشوان اسم علم - مكان مدينة / مُقاطَعة / منطقة
فورت-ورث    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فورت-وورث   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فورت-وين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فورتاليزا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فورتسبورغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فورتو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فوردا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فورمس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فورمنتيرا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فورموسا اسم علم - مكان مدينة / مُقاطَعة / منطقة
فورو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فورونيج اسم علم - مكان مدينة / مُقاطَعة / منطقة
فورونيج-أوبلاست اسم علم - مكان مدينة / مُقاطَعة / منطقة
فوعارة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فوغو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فوكشاني اسم علم - مكان مدينة / مُقاطَعة / منطقة
فوكوشيما    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فوكوكا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فوكوي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فوكيت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فوكيس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فولدا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فولغا   اسم علم - مكان - نهر / بُحيرة
فولغوغراد   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فولغوغراد-أوبلاست   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فولفسبورغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فولوس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فولين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فومبوني اسم علم - مكان مدينة / مُقاطَعة / منطقة
فونافوتي    اسم علم - مكان - عاصِمة
فونتين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فونسافان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فونغسالي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فوه اسم علم - مكان مدينة / مُقاطَعة / منطقة
فويرتيفنتورا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فويرط   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فويفودينا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فوينجاما    اسم علم - مكان مدينة / مُقاطَعة / منطقة
في-في   اسم علم - مكان مدينة / مُقاطَعة / منطقة
في-ناخيتشيفان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فياردابيغد  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيانا-دو-كاستيلو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيانارانتسوا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيبورغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيتري   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيتسانولوك  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيتسبك  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيتشابون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيتشيت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيتن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيتنام  اسم علم - مكان - دولة
فيتنبرغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيتوريا اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيتوليستي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيجاياوادا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيجل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيجي    اسم علم - مكان - دولة
فيجير   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيدار   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيدزمي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيراغواس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيراكروز    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيرجينيا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيرجينيا-الغربية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيرجينيا-بيتش   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيردان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيرملاند    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيرمونت اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيريا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيسان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيسبادن اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيسبي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيست-أغدار  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيسترا-غوتالاند اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيستربوتن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيسترنورلاند    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيستسجلاند  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيستمانلاند اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيسيو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيش-تاون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيشي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيصل-آباد   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيطرون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيع اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيفتشاني    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيفيرز  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيكتوريا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيكيكي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيلا-ريال   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيلا-كلارا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيلادلفيا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيلاريكا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيلاهيرموسا اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيلبينتي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيلفرانش-سور-مير    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيلفونتين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيلكا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيلنيوس اسم علم - مكان - عاصِمة
فيلهلمسهافن اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيلوربان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيلياندي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيليس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيليشتا اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيليكو-ترنوفو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيلينيه اسم علم - مكان مدينة / مُقاطَعة / منطقة
فين اسم علم - مكان مدينة / مُقاطَعة / منطقة
فينالي  اسم علم - مكان - نهر / بُحيرة
فينتسبلس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فينكس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فينو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فينيتسا اسم علم - مكان مدينة / مُقاطَعة / منطقة
فينيتسيا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فينيتو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فينيكا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فينيكس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيو-فورت    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيورنتينو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيير    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
فيينا   اسم علم - مكان - عاصِمة
فيينتيان    اسم علم - مكان - عاصِمة
قابس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
قاخ اسم علم - مكان مدينة / مُقاطَعة / منطقة
قاخاز-نك    اسم علم - مكان مدينة / مُقاطَعة / منطقة
قاراجوخور   اسم علم - مكان مدينة / مُقاطَعة / منطقة
قاروه   اسم علم - مكان مدينة / مُقاطَعة / منطقة
قازاخ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
قازان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
قاع-الريم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
قالّا-نفحي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قالمة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
قالويه  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قانا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
قانسو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
قب-الياس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
قبادلي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قبة-بشمرا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
قبرص    اسم علم - مكان - دولة
قبريخا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قبله    اسم علم - مكان مدينة / مُقاطَعة / منطقة
قبلي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
قبوستان اسم علم - مكان مدينة / مُقاطَعة / منطقة
قبيع    اسم علم - مكان مدينة / مُقاطَعة / منطقة
قدابيك  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قدح     اسم علم - مكان مدينة / مُقاطَعة / منطقة
قراقورم اسم علم - مكان مدينة / مُقاطَعة / منطقة
قرة-باغ اسم علم - مكان - دولة
قرحة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
قردحو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
قرشي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
قرصون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
قرصيتا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قرطاجنة اسم علم - مكان مدينة / مُقاطَعة / منطقة
قرطاضة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قرطبا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
قرطبة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
قرعون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
قرغيزستان   اسم علم - مكان - دولة
قرقشونه اسم علم - مكان مدينة / مُقاطَعة / منطقة
قُرَقَل-باغستان اسم علم - مكان مدينة / مُقاطَعة / منطقة
قرنايل  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قرنة-شهوان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قره-باش اسم علم - مكان مدينة / مُقاطَعة / منطقة
قرورة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
قرية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
قرية-الحجة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قرية-بعبدا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قزوين   اسم علم - مكان - بحر / خليج / مضيق - مُقاطَعة / منطقة
قسنطينة اسم علم - مكان مدينة / مُقاطَعة / منطقة
قشقدار  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قشن اسم علم - مكان مدينة / مُقاطَعة / منطقة
قصير    اسم علم - مكان مدينة / مُقاطَعة / منطقة
قضاء-الضنية اسم علم - مكان مدينة / مُقاطَعة / منطقة
قطر اسم علم - مكان - دولة
قطمون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
قطور    اسم علم - مكان مدينة / مُقاطَعة / منطقة
قطين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
قعطبة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
قعقعية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قعقعية-الجسر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
قعقعية-الصنوبر  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قعقعية-للجسر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
قفصة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
قفط اسم علم - مكان مدينة / مُقاطَعة / منطقة
قلالي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
قلاويه  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قلب اسم علم - مكان مدينة / مُقاطَعة / منطقة
قلحات   اسم علم - مكان مدينة / مُقاطَعة / منطقة
قلعالو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قلعة-بعبدا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قلقيلية اسم علم - مكان مدينة / مُقاطَعة / منطقة
قلنسوة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قلوج    اسم علم - مكان مدينة / مُقاطَعة / منطقة
قلود-الباقية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
قليعات  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قلين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
قليوب   اسم علم - مكان مدينة / مُقاطَعة / منطقة
قم  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قماز    اسم علم - مكان مدينة / مُقاطَعة / منطقة
قنا اسم علم - مكان مدينة / مُقاطَعة / منطقة
قناة-   اسم علم - مكان مدينة / مُقاطَعة / منطقة
قناريت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قنبات-برمانا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
قندع    اسم علم - مكان مدينة / مُقاطَعة / منطقة
قندهار  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قنية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
قنيطرة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قوانغشي اسم علم - مكان مدينة / مُقاطَعة / منطقة
قوبا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
قوبا-خاشماز اسم علم - مكان مدينة / مُقاطَعة / منطقة
قوثنغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
قوريولي‎    اسم علم - مكان مدينة / مُقاطَعة / منطقة
قوسايا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قوسقو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
قوص اسم علم - مكان مدينة / مُقاطَعة / منطقة
قوصية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
قوقند   اسم علم - مكان مدينة / مُقاطَعة / منطقة
قونية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
قويتشو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قويجاي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قويسنا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قيتولي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
قيرنا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كابان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كابانياس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كابريفي اسم علم - مكان مدينة / مُقاطَعة / منطقة
كابو-دلجادجو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كابول   اسم علم - مكان - عاصِمة
كابوي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كابيسا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كابيندا اسم علم - مكان مدينة / مُقاطَعة / منطقة
كات اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاتاماركا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاتريني اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاتفنج  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاتماندو    اسم علم - مكان - عاصِمة
كاتنزارو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاتي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاثابا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاجيرا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاخاماركا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كادافو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كارا    اسم علم - مكان - بحر / خليج / مضيق
كارازو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاراس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاراغا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كارانسيبيش  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كارباز  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاربنتاريا  اسم علم - مكان - بحر / خليج / مضيق
كاربنيسي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كارتشى  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كارديف  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كارذيتسا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كارسون-سيتي اسم علم - مكان مدينة / مُقاطَعة / منطقة
كارلسروه    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كارناتاكا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كارنوليس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كارون   اسم علم - مكان - نهر / بُحيرة
كارياكو اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاريليا اسم علم - مكان مدينة / مُقاطَعة / منطقة
كازاخستان   اسم علم - مكان - دولة
كاساما  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاستريس اسم علم - مكان - عاصِمة
كاستوريا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاستيلو-برانكو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاسل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاشاتاغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاغاوا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاغايان اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاغواثو اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاغوشيما    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كافالا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كافرين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاكاتا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاكاودروف   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كالابارزون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كالابريا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كالاسين اسم علم - مكان مدينة / مُقاطَعة / منطقة
كالاماتا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كالاو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كالغاري اسم علم - مكان مدينة / مُقاطَعة / منطقة
كالمار  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كالوكان اسم علم - مكان مدينة / مُقاطَعة / منطقة
كالي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كالياري اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاليفورنيا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاليه   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاما    اسم علم - مكان - نهر / بُحيرة
كاماغوي اسم علم - مكان مدينة / مُقاطَعة / منطقة
كامبانيا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كامبتشه اسم علم - مكان - بحر / خليج / مضيق
كامبراي اسم علم - مكان مدينة / مُقاطَعة / منطقة
كامبريدج    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كامبو-غراندي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كامبوباسو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كامبوت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كامبونغ-تشام    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كامبونغ-تشينانغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
كامبونغ-توم اسم علم - مكان مدينة / مُقاطَعة / منطقة
كامبونغ-سبو اسم علم - مكان مدينة / مُقاطَعة / منطقة
كامبيتشي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كامد-اللوز  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كامروز  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كامفاينغ-فيت    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاموتس  اسم علم - مكان - بحر / خليج / مضيق
كان اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاناغاوا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كانبرا  اسم علم - مكان - عاصِمة
كانتا-هامي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كانتربري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كانتربيري   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كانتشانابوري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كانتن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كانتو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاندال  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاندهلة اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاندي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاندية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كانزاس-سيتي اسم علم - مكان مدينة / مُقاطَعة / منطقة
كانزس-سيتي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كانساس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كانساي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كانغار  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كانكان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كانكون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاني-كيلي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كانيلو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كانينديو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاوناس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كايانغيل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كايس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كايسونج اسم علم - مكان مدينة / مُقاطَعة / منطقة
كاينو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كايو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كبر اسم علم - مكان مدينة / مُقاطَعة / منطقة
كترة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كترمايا اسم علم - مكان مدينة / مُقاطَعة / منطقة
كتلونيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
كجاتلينج    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كجالاجادي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كجرات   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كح  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كحلونية اسم علم - مكان مدينة / مُقاطَعة / منطقة
كرابوبو اسم علم - مكان مدينة / مُقاطَعة / منطقة
كرابي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كراتشي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كراتييه اسم علم - مكان مدينة / مُقاطَعة / منطقة
كراجوي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كراسنودار   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كراسنودار-كراي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كراسنويارسك اسم علم - مكان مدينة / مُقاطَعة / منطقة
كراسنويارسك-كراي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كراكاس  اسم علم - مكان - عاصِمة
كراكاو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كرانيي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كرايست-تشرتش    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كرايستشيرش  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كرايوفا اسم علم - مكان مدينة / مُقاطَعة / منطقة
كرباباد اسم علم - مكان مدينة / مُقاطَعة / منطقة
كربلاء  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كرخا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كردامير اسم علم - مكان مدينة / مُقاطَعة / منطقة
كردستان اسم علم - مكان مدينة / مُقاطَعة / منطقة
كردستان-العراق  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كردفان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كرزكان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كركبت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كركوك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كرم-زبدين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كرم-سدة اسم علم - مكان مدينة / مُقاطَعة / منطقة
كرمة-بني-سعيد   اسم علم - مكان - نهر / بُحيرة
كرمة-علي    اسم علم - مكان - نهر / بُحيرة
كرن اسم علم - مكان مدينة / مُقاطَعة / منطقة
كرواتيا اسم علم - مكان - دولة
كروز    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كروسيفو اسم علم - مكان مدينة / مُقاطَعة / منطقة
كروم-عرب    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كرونوبيرغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كريات-آتا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كريات-شمونة اسم علم - مكان مدينة / مُقاطَعة / منطقة
كريات-موصقين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كريت    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كريتر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كريتيل  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كريستيان-سان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كريفلد  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كسانثي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كسرنبا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كسروان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كسلا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كسليك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كسونغراد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كشمير   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفار-سابا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفتون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفر اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفر-الدوار  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفر-الزيات  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفر-الزيت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفر-الشيخ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفر-بيت اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفر-جرة اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفر-حتى اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفر-حرة اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفر-حزير    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفر-دنيس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفر-دونين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفر-سعد اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفر-شكر اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفر-شيما    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفر-صقر اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفر-عقاب    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفر-فوق اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفر-مشكي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفربدا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفربعل  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفربنين اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرتاي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرتبنيت    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرتون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرجوز  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرحاتا اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرحبو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرحتى  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرحمام اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفردبيان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفردجال اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفردلاقوس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفررمان اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرزبد  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرزينا اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرسرون اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرسلوان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرسير  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرشلال اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرشلان اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرصارون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرصغاب اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرعقا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرعميه اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرفاقود    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرفالوس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرفو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرفيلا اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرقاهل اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفركحيل اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفركلا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرملكي اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرنبرخ اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرنيس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفروة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفريا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرياسين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفرياشيت    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفلاقطرة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كفور    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كلارندون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كلاغنفورت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كلانتان اسم علم - مكان مدينة / مُقاطَعة / منطقة
كلباتا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كلبجر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كلكتا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كلوج-نابوكا اسم علم - مكان مدينة / مُقاطَعة / منطقة
كلوني   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كليرمون-فيران   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كليفلاند    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كليمنجارو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كمبالا  اسم علم - مكان - عاصِمة
كمبهات  اسم علم - مكان - بحر / خليج / مضيق
كمبوديا اسم علم - مكان - دولة
كمونة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كمينز   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كنار    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كناريا-الكبرى   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كنتاكي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كنجة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كنجة-قازاخ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كنجرلي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كندا    اسم علم - مكان - دولة
كندز    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كنر اسم علم - مكان مدينة / مُقاطَعة / منطقة
كو-تابو اسم علم - مكان مدينة / مُقاطَعة / منطقة
كو-في-في-لي اسم علم - مكان مدينة / مُقاطَعة / منطقة
كو-كونغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
كواخ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوازولو-ناتال   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كواسي-يونغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوالا-ترنجانو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوالا-ترنغانو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوالالمبور  اسم علم - مكان - عاصِمة
كوانتان اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوانج-بن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوانج-نام   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كواندو-كوبانغو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوانزا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كواهويلا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوبا    اسم علم - مكان - دولة
كوبافوغور   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوبان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوبر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوبلنس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوبنهاغن/كوبنهاجن   اسم علم - مكان - عاصِمة
كوبورغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوت-ديفوار - ساحل-العاج اسم علم - مكان - دولة
كوتا-بارو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوتا-كينابالو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوتايسي اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوتايك  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوتبوس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوتش    اسم علم - مكان - بحر / خليج / مضيق
كوتشابامبا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوتشاني اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوتشوسون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوتشي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوتشينغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوتنجبرن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوتوباكسي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوتونو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوتوي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوثرية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كورال   اسم علم - مكان - بحر / خليج / مضيق
كورانبوي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوربس-كريستي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوربفوا اسم علم - مكان مدينة / مُقاطَعة / منطقة
كورة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كورتا-دي-أرجيش  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كورتشي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كورتيز  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوردوبا اسم علم - مكان مدينة / مُقاطَعة / منطقة
كورديليرا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كورزيمي اسم علم - مكان مدينة / مُقاطَعة / منطقة
كورفو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كورك    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوركول  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كورنث   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كورو    اسم علم - مكان - بحر / خليج / مضيق
كورور   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوروزال اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوروني  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كورونيل-أوفيدو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوريا-الجنوبية  اسم علم - مكان - دولة
كوريا-الشمالية  اسم علم - مكان - دولة
كوريتيبا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كورينثيا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوريينتس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوزاني  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوسار   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوسبا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوسبيكو اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوستاريكا   اسم علم - مكان - دولة
كوستي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوسراي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوسكاتلان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوسوفا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوسوفو  اسم علم - مكان - دولة
كوشا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوشيتسه اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوفا-ليما   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوفاسنا اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوفنتري اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوفو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوفولا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوكبا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوكسهافن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوكلي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوكيس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوكيمبو اسم علم - مكان مدينة / مُقاطَعة / منطقة
كولاك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كولاينيس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كولتشاك اسم علم - مكان - بحر / خليج / مضيق
كولد-لايك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كولدا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كولشيستر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كولمار  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كولمبوس اسم علم - مكان مدينة / مُقاطَعة / منطقة
كولمبيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
كولورادو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كولورادو-سبرينغس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كولومبو اسم علم - مكان - عاصِمة
كولومبوس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كولومبيا    اسم علم - مكان - دولة
كولومبيا-البريطانية اسم علم - مكان مدينة / مُقاطَعة / منطقة
كولون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كولونيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
كولونيا-بوهنباي اسم علم - مكان مدينة / مُقاطَعة / منطقة
كولونيا-ديل-ساكرمينتو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كولونيا-ياب اسم علم - مكان مدينة / مُقاطَعة / منطقة
كولياكن اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوليكورو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوليما  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوم-أمبو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوم-حمادة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوماروم-إزترغون اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوماسي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوماموتو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوماياجوا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوماياغوا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كومبي-صالح  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كومرات  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كومنلاكسو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كومنولث اسم علم - مكان - مُنَظَّمة دوليَّة / هيئة / اتِّحاد
كوموتيني    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوميكون اسم علم - مكان - مُنَظَّمة دوليَّة / هيئة / اتِّحاد
كوميندادور  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوميويجني   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كون-توم اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوناكت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوناكري اسم علم - مكان - عاصِمة
كونتيكت اسم علم - مكان مدينة / مُقاطَعة / منطقة
كونسبثيون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كونستانتسا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كونستانس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كونسيبسيون-لا-فيغا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كونغدنغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
كونغسبيرغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كونغو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كونكورد اسم علم - مكان مدينة / مُقاطَعة / منطقة
كونين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوه-تشانغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوه-ساموي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوه-سميت    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كووبيو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كويابا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كَويارا اسم علم - مكان مدينة / مُقاطَعة / منطقة
كويافسكو-بومورسكي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كويتا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كويته   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كويدو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كويرنافاكا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كويريتارو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كويست   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كويمبرا اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوينزلاند   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوينكا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كوينينج اسم علم - مكان مدينة / مُقاطَعة / منطقة
كي-لانغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيب اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيب-تاون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيب-هابيتان اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيبك    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيت اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيتا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيتزالتينانغو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيتو    اسم علم - مكان - عاصِمة
كيتوي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيدا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيدال   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيدوغو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيرالا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيرام   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيرنتن  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيروفوغراد  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيرونا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيريباتي - كيريباس  اسم علم - مكان - دولة
كيرينيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيريوان اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيزون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيزيمو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيسمايو اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيسيفو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيشي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيشيناو اسم علم - مكان - عاصِمة
كيغالي  اسم علم - مكان - عاصِمة
كيغوما  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيفالونيا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيفة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيكلادس اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيل اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيلانتان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيلكيس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيلونا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيما    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيمبيرلي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيمنتس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيميروفو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيميروفو-أوبلاست    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كين-جيانج   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كين-مين اسم علم - مكان مدينة / مُقاطَعة / منطقة
كينتانا-رو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كينجستون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كينديا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كينشاسا اسم علم - مكان - عاصِمة
كينغستاون   اسم علم - مكان - عاصِمة
كينغستن اسم علم - مكان مدينة / مُقاطَعة / منطقة
كينغستون    اسم علم - مكان - عاصِمة
كينغستون-أبون-هل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كينكي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كينيا   اسم علم - مكان - دولة
كيه-نتيم    اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيهيدي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيوتو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيوشو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
كيونزير اسم علم - مكان مدينة / مُقاطَعة / منطقة
كييف    اسم علم - مكان - عاصِمة
كييل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
کرمان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
کرمانشاه    اسم علم - مكان مدينة / مُقاطَعة / منطقة
کهکيلويه-وبوير-أحمد اسم علم - مكان مدينة / مُقاطَعة / منطقة
گولستان اسم علم - مكان مدينة / مُقاطَعة / منطقة
لا-التاغراسيا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لا-بالما    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لا-خوفينتود اسم علم - مكان مدينة / مُقاطَعة / منطقة
لا-روشيل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لا-رومانا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لا-غراسيوسا اسم علم - مكان مدينة / مُقاطَعة / منطقة
لا-غوميرا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لا-فيغا اسم علم - مكان مدينة / مُقاطَعة / منطقة
لا-ليبرتاد  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لا-ليبرتاد  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لا-يونيون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاباز   اسم علم - مكان - عاصِمة
لاباسا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لابتف   اسم علم - مكان - بحر / خليج / مضيق
لابرادور    اسم علم - مكان - بحر / خليج / مضيق
لابوان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لابوري  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لابي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لابينرنتا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاتجالي اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاتسيو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاتفيا  اسم علم - مكان - دولة
لاجونيه اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاجين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاديغو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لارنكا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاريدو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاريسا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاريوخا اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاس-بالماس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاس-بالماس-دي-جران-كناريا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاس-توناس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاس-فيغاس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاسا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاسيثي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاصعانود    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاغوس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لافال   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لافيليا اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاك اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاكشادويب   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاكومب  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاكونيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاكويلا اسم علم - مكان مدينة / مُقاطَعة / منطقة
لالا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لام-دونج    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لامبانغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
لامسانا اسم علم - مكان مدينة / مُقاطَعة / منطقة
لامفون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لامي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاميا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لانج-سون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاندسهوت    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لانزاروته   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لانسينغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
لانكاران    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لانكاران-أستارا اسم علم - مكان مدينة / مُقاطَعة / منطقة
لانه    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لانه-فيرو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لانيون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاهاي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاهور   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاو اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاو-كاي اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاوس - لاو  اسم علم - مكان - دولة
لاي-شو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لايبزيغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
لايك-بلاسيد اسم علم - مكان مدينة / مُقاطَعة / منطقة
لايكود  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لاينستر اسم علم - مكان مدينة / مُقاطَعة / منطقة
لايو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لباب    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لبايا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لبراكنة اسم علم - مكان مدينة / مُقاطَعة / منطقة
لبعا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لبك اسم علم - مكان مدينة / مُقاطَعة / منطقة
لبنان   اسم علم - مكان - دولة
لبوة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لجرات   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لحج اسم علم - مكان مدينة / مُقاطَعة / منطقة
لحفد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لرستان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لريب    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لريك    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لستر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لشبونة  اسم علم - مكان - عاصِمة
لعت اسم علم - مكان مدينة / مُقاطَعة / منطقة
لعصابة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لعلاي-قاش   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لعيون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لغمان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لفيف    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لقلوق   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لقّو-عنسبا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لكديف   اسم علم - مكان - بحر / خليج / مضيق
لكنو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لمباييكه    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لمبوبو  اسم علم - مكان - نهر / بُحيرة
لندن    اسم علم - مكان - عاصِمة
لنس اسم علم - مكان مدينة / مُقاطَعة / منطقة
لنكولن  اسم علم - مكان - بحر / خليج / مضيق
لهتي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لو-مان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لو-هافر اسم علم - مكان مدينة / مُقاطَعة / منطقة
لواندا  اسم علم - مكان - عاصِمة
لوانغ-برابانغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوباتسي اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوبامبا اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوبلانا اسم علم - مكان - عاصِمة
لوبوري  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوبوسكي اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوبيك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوبيلسكي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوتون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لودفيغسهافن اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوراسيا اسم علم - مكان - قارَّة
لوراين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لورد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوردز   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوريتو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لورينسكوغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوزون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوس-أنجلس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوس-ريوس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوس-سانتوس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوس-لاجوس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوساكا  اسم علم - مكان - عاصِمة
لوسيرن  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوغا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوغانسك اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوغوج   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوفا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوفيلوفي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوقا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوكر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوكربي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوكسمبورغ   اسم علم - مكان - دولة - عاصمة
لوكوتو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوكوسا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لومايفيتي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لومبارديا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لومي    اسم علم - مكان - عاصِمة
لونتسي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لونج-آن اسم علم - مكان مدينة / مُقاطَعة / منطقة
لونغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لونغ-بيتش   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لونغوي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لونغياربيين اسم علم - مكان مدينة / مُقاطَعة / منطقة
لونيبورغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوه اسم علم - مكان - نهر / بُحيرة
لويدمنستر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لويزيانا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لويفيل  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لويي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لوييفيل اسم علم - مكان مدينة / مُقاطَعة / منطقة
لي-ين-شيانغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
لياوفا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لياونينغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليباجا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليبراتادور-جنرال-بيرناردو-أوهيجينز  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليبرفيل اسم علم - مكان - عاصِمة
ليبيا   اسم علم - مكان - دولة
ليبيريا اسم علم - مكان - دولة
ليبيريتس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليتل-روك    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليتوانيا    اسم علم - مكان - دولة
ليتورال اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليثبريدج    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليختنشتاين  اسم علم - مكان - دولة
ليدز    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليدن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليدوك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليريا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليزهي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليسبوس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليستر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليسوتو  اسم علم - مكان - دولة
ليغوريا اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليفاذيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليفربول اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليفركوزن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليفكاذا اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليفكوشا اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليفوكا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليفيس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليفينغستون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليكانجر اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليكسينغتون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليكويسا اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليل اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليلهامر اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليلو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليلونغوي    اسم علم - مكان - عاصِمة
ليما    اسم علم - مكان - عاصِمة
ليماسول اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليمبوبو اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليمبورغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليموج   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليموريا اسم علم - مكان - قارَّة
ليميريك اسم علم - مكان مدينة / مُقاطَعة / منطقة
لينا    اسم علم - مكان - نهر / بُحيرة
لينتز   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليندي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
لينس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لينشيا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
لينكون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليولومويغا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ليوواردن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
لييج    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مابوتو  اسم علم - مكان - عاصِمة
ماتام   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماتانزاس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماتشالا اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماتو-غروسو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماتو-غروسو-دو-سول   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماجلان-دي-لا-أنتركتيكا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماجنكا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماجورو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مادبا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مادري-دي-ديوس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مادستو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماديا-براديش    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماديرا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماديسون اسم علم - مكان مدينة / مُقاطَعة / منطقة
مار-روكز    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مار-مخايل   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مار-موسى    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مارا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مارادي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مارانهاو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماربورغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
مارتاكيرت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مارتن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مارتوما اسم علم - مكان مدينة / مُقاطَعة / منطقة
مارتوني اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماردة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماردة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مارغاو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مارغي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماركي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مارنون  اسم علم - مكان - نهر / بُحيرة
ماروا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مارون-الراس اسم علم - مكان مدينة / مُقاطَعة / منطقة
مارويجيني   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مارويه  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماريا-ترينيداد-سانشيز   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماريانا اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماريانو-روكي-ألونسو اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماريبور اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماريلاند    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مازندران    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مازوفيتسكي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماسا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماساتشوستس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماسالي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماسايو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماسترخت‏    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماسن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماسياس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماسيرو  اسم علم - مكان - عاصِمة
ماسينو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماغديبورغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماغنيسيا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماغورو  اسم علم - مكان - عاصِمة
مافتنغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مافيكينج    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماكابا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماكاو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماكواتا اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماكون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماكيرا-ولوا اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماكينزي اسم علم - مكان - نهر / بُحيرة
مالابو  اسم علم - مكان - عاصِمة
مالاكا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مالامبا اسم علم - مكان مدينة / مُقاطَعة / منطقة
مالانجي اسم علم - مكان مدينة / مُقاطَعة / منطقة
مالاوي  اسم علم - مكان - دولة
مالدونادو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مالطا   اسم علم - مكان - دولة
مالكشم  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مالكية-الساحل   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مالمو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مالوكو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مالي    اسم علم - مكان - دولة
ماليتا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماليزيا اسم علم - مكان - دولة
ماليندي اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماليه   اسم علم - مكان - عاصِمة
مامو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مامودزو اسم علم - مكان مدينة / مُقاطَعة / منطقة
مانابى  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماناتوتو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماناغوا اسم علم - مكان - عاصِمة
ماناواتو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماناوس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مانسا-كونكو اسم علم - مكان مدينة / مُقاطَعة / منطقة
مانسفيلد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مانشستر‏    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مانشيستر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مانغلور اسم علم - مكان مدينة / مُقاطَعة / منطقة
مانكونكو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مانهايم اسم علم - مكان مدينة / مُقاطَعة / منطقة
مانوس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مانوفاهي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مانونو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مانيبور اسم علم - مكان مدينة / مُقاطَعة / منطقة
مانيتوبا‏   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مانيكا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مانيلا  اسم علم - مكان - عاصِمة
ماها-ساراخام    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماهاجانغا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماهاراشترا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماهي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماو اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماي-عيني    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماي-منيه    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماي-هونج-سون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماياغوانا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مايدوغوري   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مايسور  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ماينتس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مايو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مايوت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مأرب    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مبابان  اسم علم - مكان - عاصِمة
مبومالانجا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مبيا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مبيريك  اسم علم - مكان مدينة / مُقاطَعة / منطقة
متريت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
متز اسم علم - مكان مدينة / مُقاطَعة / منطقة
متسامبورو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
متسامودو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
متسانغاموجي اسم علم - مكان مدينة / مُقاطَعة / منطقة
متوارا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
متين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مجدل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مجدل-بلحيس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مجدل-ترشيش  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مجدل-زون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مجدل-عنجر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مجدل-معوش   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مجدلا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مجدلون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مجدليا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مجزوب   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مجيدية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
محج-قلعة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
محرونة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
محيبيب  اسم علم - مكان مدينة / مُقاطَعة / منطقة
محيدش   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مختارة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مدانك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مدريد   اسم علم - مكان - عاصِمة
مدسين-هات   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مدغشقر  اسم علم - مكان - دولة
مدق اسم علم - مكان مدينة / مُقاطَعة / منطقة
مدلين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مدنين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مدوخة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مذيخرة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مراح-الخوخ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مراح-السراج اسم علم - مكان مدينة / مُقاطَعة / منطقة
مراكش   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مرج-الزهور  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مرجبا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مرجعيون اسم علم - مكان مدينة / مُقاطَعة / منطقة
مرزق    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مرسته   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مرسى-علم    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مرسى-مطروح  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مرسية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مرسيليا اسم علم - مكان مدينة / مُقاطَعة / منطقة
مرسين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مركبا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مركة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مركزي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مركيبو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مرمرة   اسم علم - مكان - بحر / خليج / مضيق
مرو اسم علم - مكان مدينة / مُقاطَعة / منطقة
مروج    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مروحين  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مرياطة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مريجات  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مريجة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزبود   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-الاوساميات    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-البويضة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-التفاح    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-الجرين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-الحسينية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-الحمرا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-الخريبة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-السيد اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-الشوف اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-الضهر اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-المصيلح   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-الواسطة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-بصفور اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-بلدة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-بوراشد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-تولا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-جميجم اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-دمول  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-دير-تقلا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-زقية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-سردة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-سنيبر اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-شلبعل اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-طير-سمحات اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-عية   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-مشرف  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزرعة-يشوع  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزكة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزهر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزوزو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مزيارة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مستغانم اسم علم - مكان مدينة / مُقاطَعة / منطقة
مسقط    اسم علم - مكان - عاصِمة
مسكان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مسندم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مسيعيد  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مسيلة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مشتاغا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مشتول-السوق اسم علم - مكان مدينة / مُقاطَعة / منطقة
مشتى-حسن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مشتى-حمود   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مشحة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مشرف    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مشغرة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مشمش    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مشموشة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مشيخا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مصر اسم علم - مكان - دولة
مصراتة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مصوع    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مطاي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مطروح   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مطرية-الشومر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مطماطة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مطوبس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
معاد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
معاصر-الشوف اسم علم - مكان مدينة / مُقاطَعة / منطقة
معاصر-بيت-الدين اسم علم - مكان مدينة / مُقاطَعة / منطقة
معافر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
معاليه-أدوميم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
معان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
معركة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
معروب   اسم علم - مكان مدينة / مُقاطَعة / منطقة
معسكر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
معلقة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
معيذر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
معيصرة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مغاغة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مغدوشة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مغيرية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مقابة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مقدونيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
مقديشو  اسم علم - مكان - عاصِمة
مقوسا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مقولو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مقيبلة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مكة-المكرمة اسم علم - مكان مدينة / مُقاطَعة / منطقة
مكسي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مكسيكالي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مكسيكو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مكسيكو-سيتي اسم علم - مكان - عاصِمة
مكلس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مكنا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مكناس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مِلبورن اسم علم - مكان مدينة / مُقاطَعة / منطقة
ملتان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ملقا    اسم علم - مكان - بحر / خليج / مضيق
ملقة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ملكوال  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ملكي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ملوي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مليحة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ممفيس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
منارة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
منتون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
منجز    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مندفرا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مندن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مندناو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مندوسا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
منروفيا اسم علم - مكان - عاصِمة
منشأة-ناصر  اسم علم - مكان مدينة / مُقاطَعة / منطقة
منصف    اسم علم - مكان مدينة / مُقاطَعة / منطقة
منصورة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
منصوريه اسم علم - مكان مدينة / مُقاطَعة / منطقة
منغروف-كاي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
منغوليا اسم علم - مكان - دولة - مُقاطَعة / منطقة
منفلوط  اسم علم - مكان مدينة / مُقاطَعة / منطقة
منوبة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
منورقة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
منوف    اسم علم - مكان مدينة / مُقاطَعة / منطقة
منيا-القمح  اسم علم - مكان مدينة / مُقاطَعة / منطقة
منيابوليس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
منيارة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
منية-النصر  اسم علم - مكان مدينة / مُقاطَعة / منطقة
موانزا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
موانغ-خاي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
موانغ-فون-هونغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
موبتي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
موخوتلنغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مودوغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مور اسم علم - مكان مدينة / مُقاطَعة / منطقة
مورا-ورومسدال   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مورازان اسم علم - مكان مدينة / مُقاطَعة / منطقة
موراي   اسم علم - مكان - نهر / بُحيرة
مورتس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مورفو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
موروب   اسم علم - مكان مدينة / مُقاطَعة / منطقة
موروغورو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مورونا-سانتياغو اسم علم - مكان مدينة / مُقاطَعة / منطقة
موروني  اسم علم - مكان - عاصِمة
موريتانيا   اسم علم - مكان - دولة
موريشيوس    اسم علم - مكان - دولة
موريلوس اسم علم - مكان مدينة / مُقاطَعة / منطقة
موريليا اسم علم - مكان مدينة / مُقاطَعة / منطقة
موزمبيق اسم علم - مكان - دولة
موسجاو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
موسفلسبير   اسم علم - مكان مدينة / مُقاطَعة / منطقة
موسكوأستراخان   اسم علم - مكان - عاصِمة
موسكوفسكاجا-أوبلاست اسم علم - مكان مدينة / مُقاطَعة / منطقة
موسيا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
موغيليوف    اسم علم - مكان مدينة / مُقاطَعة / منطقة
موكا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
موكداهان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
موكسيكو اسم علم - مكان مدينة / مُقاطَعة / منطقة
موكيوا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مولدا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مولدوفا اسم علم - مكان - دولة
مولدوفا-نوا اسم علم - مكان مدينة / مُقاطَعة / منطقة
مولقي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مولهاوزن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مولهايم اسم علم - مكان مدينة / مُقاطَعة / منطقة
مولي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
موليزي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
موليفانوا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مومباسا اسم علم - مكان مدينة / مُقاطَعة / منطقة
مومباي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
موناكو  اسم علم - مكان - دولة
موناكو-فيل  اسم علم - مكان - عاصِمة
مونبيلييه   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مونتارغيس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مونتانا اسم علم - مكان مدينة / مُقاطَعة / منطقة
مونتبليير   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مونتريال    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مونتسيرادو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مونتغومري   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مونتفيرميل  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مونتي-بلاتا اسم علم - مكان مدينة / مُقاطَعة / منطقة
مونتيبيليارد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مونتيجياردينو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مونتيري اسم علم - مكان مدينة / مُقاطَعة / منطقة
مونتيفيديو  اسم علم - مكان - عاصِمة
مونتيكريستي اسم علم - مكان مدينة / مُقاطَعة / منطقة
موندولكيري  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مونروي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مونسة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مونستر  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مونسترمايفلد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مونسنيور-نويل   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مونشنغلادباخ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مونغار  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مونكتون اسم علم - مكان مدينة / مُقاطَعة / منطقة
مونمورانسي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مونو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
موهون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
موهيلز-هوك  اسم علم - مكان مدينة / مُقاطَعة / منطقة
موهيلي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
موين-أوجوي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
موين-سافالي اسم علم - مكان مدينة / مُقاطَعة / منطقة
موين-كوميه  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميازاكي اسم علم - مكان مدينة / مُقاطَعة / منطقة
مياغي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميامي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مياو-لي اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميت-سلسيل   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميت-غمر اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميتز    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميتشواكان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميتيليني    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميدلزبره    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميرتون  اسم علم - مكان - بحر / خليج / مضيق
ميرسيديس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميركورا-تشيوك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميروبا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميريامبولي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميريدا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميزورام اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميزوري  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميزون-ألفور اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميزيوناس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميس-الجبل   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميسا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميسان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميسن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميسوري  اسم علم - مكان - نهر / بُحيرة
ميسولونغي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميسيساغا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميسينيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميسيونس اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميشيغان اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميغالايا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميفدون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميفلارا اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميفوق   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميكرونيسيا  اسم علم - مكان - دولة
ميكلينبورغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميكو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميكوليف اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميكونغ  اسم علم - مكان - نهر / بُحيرة
ميلاكي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميلانو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميلة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميلكيوك اسم علم - مكان - عاصِمة
ميلو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميلواكي اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميلوز   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميلووكي اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميماروبا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميمس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميمفس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
مين اسم علم - مكان مدينة / مُقاطَعة / منطقة
مينا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مينابي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميناس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميناس-جيرايس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مينسك   اسم علم - مكان - عاصِمة
مينشي-تبينج اسم علم - مكان مدينة / مُقاطَعة / منطقة
مينغا-جوير  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مينغه-شوير  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مينيابوليس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
مينيسوتا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
مينينغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميه اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميورقة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ميونخ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نابل    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نابلس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نابو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نابولي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نابيه   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نابيير-هاستينغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ناتال   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ناتيتانغو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ناجالاند    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ناخون-باتوم اسم علم - مكان مدينة / مُقاطَعة / منطقة
ناخون-راتشاسيما اسم علم - مكان مدينة / مُقاطَعة / منطقة
ناخون-ساوان اسم علم - مكان مدينة / مُقاطَعة / منطقة
ناخون-سي-تاممارات   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ناخون-فانوم اسم علم - مكان مدينة / مُقاطَعة / منطقة
ناخون-نايوك اسم علم - مكان مدينة / مُقاطَعة / منطقة
ناخيتشيفان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نادروكَا-نافوسا اسم علم - مكان مدينة / مُقاطَعة / منطقة
نادي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ناديكادك    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نارا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ناراتيوات   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نارين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نازينو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ناساو   اسم علم - مكان - عاصِمة
ناشفيل  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ناعمة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ناغاساكي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ناغانو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ناغبور  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ناغوا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نافبليو اسم علم - مكان مدينة / مُقاطَعة / منطقة
نالوت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نام-دن  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نامبولا اسم علم - مكان مدينة / مُقاطَعة / منطقة
نامتسو  اسم علم - مكان - بحر / خليج / مضيق
ناموزي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ناميبي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ناميبيا اسم علم - مكان - دولة
نان اسم علم - مكان مدينة / مُقاطَعة / منطقة
نانت    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نانتو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نانتير  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نانسي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ناورو   اسم علم - مكان - دولة
ناوزوري اسم علم - مكان مدينة / مُقاطَعة / منطقة
ناياريت اسم علم - مكان مدينة / مُقاطَعة / منطقة
نايبيدو اسم علم - مكان - عاصِمة
نايتاسيري   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نايميخين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نبراسكا اسم علم - مكان مدينة / مُقاطَعة / منطقة
نبروه   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نبع-الصفا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نبي-أيلا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نبي-شيت اسم علم - مكان مدينة / مُقاطَعة / منطقة
نبي-عثمان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نتانيا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نجد اسم علم - مكان مدينة / مُقاطَعة / منطقة
نجد-عكار    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نجران   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نجري-سمبيلن اسم علم - مكان مدينة / مُقاطَعة / منطقة
نجع-حمادي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نجي-آن  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نجيري-سمبيلن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نخل اسم علم - مكان مدينة / مُقاطَعة / منطقة
نخلة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ندولا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نزوى    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نزيريكوري   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نصر-النوبة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نغاتبانغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نغارأرد اسم علم - مكان مدينة / مُقاطَعة / منطقة
نغارتشيلونغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
نغاردماو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نغاريملينغوي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نغاونديري   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نغونيه  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نغيوال  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نفتالان اسم علم - مكان مدينة / مُقاطَعة / منطقة
نفتجالا اسم علم - مكان مدينة / مُقاطَعة / منطقة
نقادة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نقفة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نكازيدجا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نكوص    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نمرين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نمنغان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نمنگان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نمور    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نميرية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نن-بن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نن-ثوان اسم علم - مكان مدينة / مُقاطَعة / منطقة
ننكرهار اسم علم - مكان مدينة / مُقاطَعة / منطقة
نهاريا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نهر-إبراهيم اسم علم - مكان مدينة / مُقاطَعة / منطقة
نهر-إيراوادي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نهر-حلوان   اسم علم - مكان - نهر / بُحيرة
نهر-سيس اسم علم - مكان مدينة / مُقاطَعة / منطقة
نهر-غي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نواذيبو اسم علم - مكان مدينة / مُقاطَعة / منطقة
نواكشوط اسم علم - مكان - عاصِمة
نواوي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نوتنغهام    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نوربوتن اسم علم - مكان مدينة / مُقاطَعة / منطقة
نورث-باتلفورد   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نورث-كارولاينا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نورثامبتون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نورثلاند    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نورد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نورد-تروندلاغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نوردلاند    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نورستان اسم علم - مكان مدينة / مُقاطَعة / منطقة
نورشوبينغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نورفولك اسم علم - مكان مدينة / مُقاطَعة / منطقة
نورويتش اسم علم - مكان مدينة / مُقاطَعة / منطقة
نوسا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نوغال   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نوغراد  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نوفا-سكوشيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
نوفو-ميستو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نوفوسيبيرسك اسم علم - مكان مدينة / مُقاطَعة / منطقة
نوفوسيبيرسك-أوبلاست اسم علم - مكان مدينة / مُقاطَعة / منطقة
نوفوكوزنتسك اسم علم - مكان مدينة / مُقاطَعة / منطقة
نوفي-ساد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نوكافيتاو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نوكو-ألوفا  اسم علم - مكان - عاصِمة
نونثابوري   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نونغ-خاي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نونغبوا-لامفو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نوني    اسم علم - مكان - نهر / بُحيرة
نووسافي اسم علم - مكان مدينة / مُقاطَعة / منطقة
نوولوبا اسم علم - مكان مدينة / مُقاطَعة / منطقة
نويبع   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نويس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نويفا-وخا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نويفو-ليون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نياسا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيالا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيامي   اسم علم - مكان - عاصِمة
نيانزا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيانغا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيبا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيبال   اسم علم - مكان - دولة
نيبس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيبوك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيترا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيتزي-كوميه اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيجني-نوفغورود  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيجني-نوفغورود-أوبلاست  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيجيريا اسم علم - مكان - دولة
نيحا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيروبي  اسم علم - مكان - عاصِمة
نيس اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيغتشيسار   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيفادا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيفاشا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيقوسيا اسم علم - مكان - عاصِمة
نيكاراجوا   اسم علم - مكان - دولة
نيكارسولم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيكولا-تاون اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيكيري  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيلسون  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيم اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيمبا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيمبوكو اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيمروز  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نين اسم علم - مكان مدينة / مُقاطَعة / منطقة
نينغشيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
نينوى   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيو-ساوث-ويلز   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيواس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيوأورلينز  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيوبليموث   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيوجرسي اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيودلهي اسم علم - مكان - عاصِمة
نيور    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيورك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيوزيلندا - أوتياروا - ماوري    اسم علم - مكان - دولة
نيوشاتل اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيوكاسل-أبون-تاين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيوكوين اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيومكسيكو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيوهامبشير  اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيويلي-سور-مارني    اسم علم - مكان مدينة / مُقاطَعة / منطقة
نيويورك اسم علم - مكان مدينة / مُقاطَعة / منطقة
نييغاتا اسم علم - مكان مدينة / مُقاطَعة / منطقة
ها  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ها-ألف  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ها-تينا اسم علم - مكان مدينة / مُقاطَعة / منطقة
ها-جيانج    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ها-دال  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ها-نام  اسم علم - مكان مدينة / مُقاطَعة / منطقة
هاباي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هاتو-مايور  اسم علم - مكان مدينة / مُقاطَعة / منطقة
هاتو-مايور-دل-راي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هاتوهوبي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هاجدو-بيهار اسم علم - مكان مدينة / مُقاطَعة / منطقة
هادروت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
هاربر   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هارتفورد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هارداب  اسم علم - مكان مدينة / مُقاطَعة / منطقة
هاردرفيك    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هارلم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هاروغيت اسم علم - مكان مدينة / مُقاطَعة / منطقة
هاريانا اسم علم - مكان مدينة / مُقاطَعة / منطقة
هاريسبرغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هاريو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هاغن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هافانا  اسم علم - مكان - عاصِمة
هافنارفيوردور   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هالاند  اسم علم - مكان مدينة / مُقاطَعة / منطقة
هالفيرده    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هاله    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هاليفاكس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هام اسم علم - مكان مدينة / مُقاطَعة / منطقة
هامار   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هامبورغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
هامشي   اسم علم - مكان - بحر / خليج / مضيق
هاميلتون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هامينلينا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هانج-ين اسم علم - مكان مدينة / مُقاطَعة / منطقة
هانوفر  اسم علم - مكان مدينة / مُقاطَعة / منطقة
هانوي   اسم علم - مكان - عاصِمة
هاو-جينج    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هاواي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هاي-دونج    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هاي-فونج    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هاياليا اسم علم - مكان مدينة / مُقاطَعة / منطقة
هايتي   اسم علم - مكان - دولة
هايدلبرغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هايدنهايم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هايفونغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
هايلبرون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هبارية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
هبرو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هدرسفيلد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هدسون   اسم علم - مكان - بحر / خليج / مضيق
هرات    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هراري   اسم علم - مكان - عاصِمة
هرازدان اسم علم - مكان مدينة / مُقاطَعة / منطقة
هرتزيلية    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هرجيسا  اسم علم - مكان - عاصِمة
هرري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هرلمرمير    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هرمزکان اسم علم - مكان مدينة / مُقاطَعة / منطقة
هرموبوليس   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هري اسم علم - مكان مدينة / مُقاطَعة / منطقة
هسن اسم علم - مكان مدينة / مُقاطَعة / منطقة
هلسنجبورج   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هلسنكي  اسم علم - مكان - عاصِمة
هلماهرا اسم علم - مكان - بحر / خليج / مضيق
هلمند   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هلينا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
همدان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هندوراس اسم علم - مكان - دولة
هنلي-أون-تيمز   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ههيا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هو-ساسندار  اسم علم - مكان مدينة / مُقاطَعة / منطقة
هوا-بن  اسم علم - مكان مدينة / مُقاطَعة / منطقة
هوا-فان اسم علم - مكان مدينة / مُقاطَعة / منطقة
هوالي-ين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هوامبو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
هوب-تاون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هوبارت  اسم علم - مكان مدينة / مُقاطَعة / منطقة
هوباي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هوبستن  اسم علم - مكان مدينة / مُقاطَعة / منطقة
هوت-ماتسياترا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هورالاند    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هورة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هوسان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هوشاي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هوشي-منه    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هوف اسم علم - مكان مدينة / مُقاطَعة / منطقة
هوك باي اسم علم - مكان مدينة / مُقاطَعة / منطقة
هوكايدو اسم علم - مكان مدينة / مُقاطَعة / منطقة
هولسشتاين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هولغوين اسم علم - مكان مدينة / مُقاطَعة / منطقة
هولندا  اسم علم - مكان - دولة
هومبورج اسم علم - مكان مدينة / مُقاطَعة / منطقة
هومنباد اسم علم - مكان مدينة / مُقاطَعة / منطقة
هونان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هونغ-كونغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هونغ-هي اسم علم - مكان - نهر / بُحيرة
هونغتشون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هونولولو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هونيارا اسم علم - مكان - عاصِمة
هونيدوارا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هونين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هويلا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هويهويتينانغو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هيتلا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هيدالجو اسم علم - مكان مدينة / مُقاطَعة / منطقة
هيدمارك اسم علم - مكان مدينة / مُقاطَعة / منطقة
هيرماناس-ميرابال    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هيرموسيلو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هيرنه   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هيروشيما    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هيريرا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
هيرينفين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هيستنغس اسم علم - مكان مدينة / مُقاطَعة / منطقة
هيفيز   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هيكوتة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
هيلدسهايم   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هيلفرسوم    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هيلونغجيانغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
هيليرود اسم علم - مكان مدينة / مُقاطَعة / منطقة
هيما    اسم علم - مكان مدينة / مُقاطَعة / منطقة
هينان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هيندرسن اسم علم - مكان مدينة / مُقاطَعة / منطقة
هينسشتي اسم علم - مكان مدينة / مُقاطَعة / منطقة
هيو اسم علم - مكان مدينة / مُقاطَعة / منطقة
هيوستن  اسم علم - مكان مدينة / مُقاطَعة / منطقة
هيوغو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
هيومان-رايتس-ووتش   اسم علم - مكان - مُنَظَّمة دوليَّة / هيئة / اتِّحاد
هييريس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
واترفورد    اسم علم - مكان مدينة / مُقاطَعة / منطقة
واترلو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
وادان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
وادي-الحور  اسم علم - مكان مدينة / مُقاطَعة / منطقة
وادي-الدلم  اسم علم - مكان مدينة / مُقاطَعة / منطقة
وادي-الست   اسم علم - مكان مدينة / مُقاطَعة / منطقة
وادي-النطرون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
وادي-بانداما    اسم علم - مكان مدينة / مُقاطَعة / منطقة
وادي-جاموس  اسم علم - مكان مدينة / مُقاطَعة / منطقة
وادي-جزين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
وادي-جيلو   اسم علم - مكان مدينة / مُقاطَعة / منطقة
وادي-خالد   اسم علم - مكان مدينة / مُقاطَعة / منطقة
وادي-زم اسم علم - مكان مدينة / مُقاطَعة / منطقة
وادي-شحرور  اسم علم - مكان مدينة / مُقاطَعة / منطقة
وادي-فعرا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
واراب   اسم علم - مكان مدينة / مُقاطَعة / منطقة
وارسو   اسم علم - مكان - عاصِمة
وارن    اسم علم - مكان مدينة / مُقاطَعة / منطقة
واري    اسم علم - مكان مدينة / مُقاطَعة / منطقة
واسط    اسم علم - مكان مدينة / مُقاطَعة / منطقة
واشنطن  اسم علم - مكان - عاصِمة
واشنطن-دي-سي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
واغادوغو    اسم علم - مكان - عاصِمة
واكاياما    اسم علم - مكان مدينة / مُقاطَعة / منطقة
والونيا اسم علم - مكان مدينة / مُقاطَعة / منطقة
وان     اسم علم - مكان - بحر / خليج / مضيق
وانجانوي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
وانغ-نامثا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
وانغاري اسم علم - مكان مدينة / مُقاطَعة / منطقة
وانغاني اسم علم - مكان مدينة / مُقاطَعة / منطقة
وانغدو-فودرانغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
وانكافيليكا اسم علم - مكان مدينة / مُقاطَعة / منطقة
وانوكو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
وانيكا  اسم علم - مكان مدينة / مُقاطَعة / منطقة
وايكاتو اسم علم - مكان مدينة / مُقاطَعة / منطقة
واينر-نوستادت   اسم علم - مكان مدينة / مُقاطَعة / منطقة
وايومينغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
وبون-راتشاثاني  اسم علم - مكان مدينة / مُقاطَعة / منطقة
وتاسكوين    اسم علم - مكان مدينة / مُقاطَعة / منطقة
وجدة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ودتش    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ودزكي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ودل اسم علم - مكان - بحر / خليج / مضيق
ودمدني  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ودون-تاني   اسم علم - مكان مدينة / مُقاطَعة / منطقة
وربة    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ورحانية اسم علم - مكان مدينة / مُقاطَعة / منطقة
وردانية اسم علم - مكان مدينة / مُقاطَعة / منطقة
وردك    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ورزازات اسم علم - مكان مدينة / مُقاطَعة / منطقة
ورقلة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ورودكو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
وزامورا اسم علم - مكان مدينة / مُقاطَعة / منطقة
وزان    اسم علم - مكان مدينة / مُقاطَعة / منطقة
وستفاليا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
وصاب-السافل اسم علم - مكان مدينة / مُقاطَعة / منطقة
وطى-الجوز   اسم علم - مكان مدينة / مُقاطَعة / منطقة
وطى-المروج  اسم علم - مكان مدينة / مُقاطَعة / منطقة
وطى-فارس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
وقويي-غلبيد اسم علم - مكان مدينة / مُقاطَعة / منطقة
ولاتة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ولسينج  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ولكرل   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ونسان   اسم علم - مكان مدينة / مُقاطَعة / منطقة
وهاي    اسم علم - مكان - بحر / خليج / مضيق
وهران   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ووريك   اسم علم - مكان مدينة / مُقاطَعة / منطقة
وولسول  اسم علم - مكان مدينة / مُقاطَعة / منطقة
وولف    اسم علم - مكان مدينة / مُقاطَعة / منطقة
وولفرهامبتون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ووليو-نتام  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ويبرن   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ويتشيتا اسم علم - مكان مدينة / مُقاطَعة / منطقة
ويسبري  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ويست-أورنج  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ويستمورلاند اسم علم - مكان مدينة / مُقاطَعة / منطقة
ويسكنسن اسم علم - مكان مدينة / مُقاطَعة / منطقة
ويكيبيديا   اسم علم - مكان - مُنَظَّمة دوليَّة / هيئة / اتِّحاد
ويكيليكس    اسم علم - مكان - مُنَظَّمة دوليَّة / هيئة / اتِّحاد
ويل-نزاس    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ويلتشير اسم علم - مكان مدينة / مُقاطَعة / منطقة
ويلز‏   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ويلينغتون   اسم علم - مكان - عاصِمة
ويندزر  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ويندهوك اسم علم - مكان - عاصِمة
وينو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
وينيبيغ اسم علم - مكان مدينة / مُقاطَعة / منطقة
ويورسلن اسم علم - مكان مدينة / مُقاطَعة / منطقة
ياب اسم علم - مكان مدينة / مُقاطَعة / منطقة
يارديملي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
يارفا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ياروسلافل   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ياروسلافل-أوبلاست   اسم علم - مكان مدينة / مُقاطَعة / منطقة
يارون   اسم علم - مكان مدينة / مُقاطَعة / منطقة
يارين   اسم علم - مكان - عاصِمة
ياسوثون اسم علم - مكان مدينة / مُقاطَعة / منطقة
ياش اسم علم - مكان مدينة / مُقاطَعة / منطقة
ياطر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
يافا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
يالا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
يالو    اسم علم - مكان - نهر / بُحيرة
ياماغاتا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ياماغوتشي   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ياماناشي    اسم علم - مكان مدينة / مُقاطَعة / منطقة
ياموسوكرو   اسم علم - مكان - عاصِمة
يانطا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
يانغتسي اسم علم - مكان - نهر / بُحيرة
يانوح   اسم علم - مكان مدينة / مُقاطَعة / منطقة
يانينة  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ياوندي  اسم علم - مكان - عاصِمة
يحشوش   اسم علم - مكان مدينة / مُقاطَعة / منطقة
يحمر    اسم علم - مكان مدينة / مُقاطَعة / منطقة
يحمر-الشقيف اسم علم - مكان مدينة / مُقاطَعة / منطقة
يريفان  اسم علم - مكان - عاصِمة
يزد اسم علم - مكان مدينة / مُقاطَعة / منطقة
يلسبرويت    اسم علم - مكان مدينة / مُقاطَعة / منطقة
يلونايف اسم علم - مكان مدينة / مُقاطَعة / منطقة
يمتلاند اسم علم - مكان مدينة / مُقاطَعة / منطقة
يمونة   اسم علم - مكان مدينة / مُقاطَعة / منطقة
ين-باي  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ينسي    اسم علم - مكان - نهر / بُحيرة
ينغستاون    اسم علم - مكان مدينة / مُقاطَعة / منطقة
يني اسم علم - مكان مدينة / مُقاطَعة / منطقة
يهودية  اسم علم - مكان مدينة / مُقاطَعة / منطقة
يو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
يوتا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
يوثاي-ثاني  اسم علم - مكان مدينة / مُقاطَعة / منطقة
يوجياكرتا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
يوخاري-قره-باغ  اسم علم - مكان مدينة / مُقاطَعة / منطقة
يوراسيك اسم علم - مكان - مُنَظَّمة دوليَّة / هيئة / اتِّحاد
يورك    اسم علم - مكان مدينة / مُقاطَعة / منطقة
يوركتن  اسم علم - مكان مدينة / مُقاطَعة / منطقة
يورو    اسم علم - مكان مدينة / مُقاطَعة / منطقة
يوغفا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
يوفا    اسم علم - مكان مدينة / مُقاطَعة / منطقة
يوفاسكولا   اسم علم - مكان مدينة / مُقاطَعة / منطقة
يوكاتان اسم علم - مكان مدينة / مُقاطَعة / منطقة
يولاخ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
يولاند  اسم علم - مكان مدينة / مُقاطَعة / منطقة
يون-لين اسم علم - مكان مدينة / مُقاطَعة / منطقة
يونسكو‏ اسم علم - مكان - مُنَظَّمة دوليَّة / هيئة / اتِّحاد
يونسيف  اسم علم - مكان - مُنَظَّمة دوليَّة / هيئة / اتِّحاد
يونشوبينغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
يونكتاد اسم علم - مكان - مُنَظَّمة دوليَّة / هيئة / اتِّحاد
يونكوبينغ   اسم علم - مكان مدينة / مُقاطَعة / منطقة
يونيسيف اسم علم - مكان - مُنَظَّمة دوليَّة / هيئة / اتِّحاد
يونين   اسم علم - مكان مدينة / مُقاطَعة / منطقة
يوينسو  اسم علم - مكان مدينة / مُقاطَعة / منطقة
يي  اسم علم - مكان - نهر / بُحيرة
يي-لان  اسم علم - مكان مدينة / مُقاطَعة / منطقة
ييكاتيرينبرغ    اسم علم - مكان مدينة / مُقاطَعة / منطقة
السيسي  konia
"""


# text+=text2;
PROPER_NOUNS = {}
for line in TEXT.split('\n'):
    if not line.startswith('#'):
        line = line.split('\t')
        if len(line) >= 2:
            lexeme = line[0]
            label = line[1]
            PROPER_NOUNS[lexeme] = label
# print ProperNoun;
