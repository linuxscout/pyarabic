unshaping_table={
u'\uFEA1':u'\u062D',
u'\uFEA3':u'\u062D',
u'\uFEA4':u'\u062D',
u'\uFEA2':u'\u062D',
u'\uFEA5':u'\u062E',
u'\uFEA7':u'\u062E',
u'\uFEA8':u'\u062E',
u'\uFEA6':u'\u062E',
u'\uFEA9':u'\u062F',
u'\uFEAA':u'\u062F',
u'\uFE95':u'\u062A',
u'\uFE97':u'\u062A',
u'\uFE98':u'\u062A',
u'\uFE96':u'\u062A',
u'\uFE99':u'\u062B',
u'\uFE9B':u'\u062B',
u'\uFE9C':u'\u062B',
u'\uFE9A':u'\u062B',
u'\uFE9D':u'\u062C',
u'\uFE9F':u'\u062C',
u'\uFEA0':u'\u062C',
u'\uFE9E':u'\u062C',
u'\uFEC5':u'\u0638',
u'\uFEC7':u'\u0638',
u'\uFEC8':u'\u0638',
u'\uFEC6':u'\u0638',
u'\uFEE9':u'\u0647',
u'\uFEEB':u'\u0647',
u'\uFEEC':u'\u0647',
u'\uFEEA':u'\u0647',
u'\uFEAB':u'\u0630',
u'\uFEAC':u'\u0630',
u'\uFED9':u'\u0643',
u'\uFEDB':u'\u0643',
u'\uFEDC':u'\u0643',
u'\uFEDA':u'\u0643',
u'\uFEC1':u'\u0637',
u'\uFEC3':u'\u0637',
u'\uFEC4':u'\u0637',
u'\uFEC2':u'\u0637',
u'\uFEE5':u'\u0646',
u'\uFEE7':u'\u0646',
u'\uFEE8':u'\u0646',
u'\uFEE6':u'\u0646',
u'\uFEB5':u'\u0634',
u'\uFEB7':u'\u0634',
u'\uFEB8':u'\u0634',
u'\uFEB6':u'\u0634',
u'\uFEDD':u'\u0644',
u'\uFEDF':u'\u0644',
u'\uFEE0':u'\u0644',
u'\uFEDE':u'\u0644',
u'\uFEE1':u'\u0645',
u'\uFEE3':u'\u0645',
u'\uFEE4':u'\u0645',
u'\uFEE2':u'\u0645',
u'\uFED5':u'\u0642',
u'\uFED7':u'\u0642',
u'\uFED8':u'\u0642',
u'\uFED6':u'\u0642',
u'\uFECD':u'\u063A',
u'\uFECF':u'\u063A',
u'\uFED0':u'\u063A',
u'\uFECE':u'\u063A',
u'\u0640':u'\u0640',
u'\uFEBD':u'\u0636',
u'\uFEBF':u'\u0636',
u'\uFEC0':u'\u0636',
u'\uFEBE':u'\u0636',
u'\uFED1':u'\u0641',
u'\uFED3':u'\u0641',
u'\uFED4':u'\u0641',
u'\uFED2':u'\u0641',
u'\uFEB9':u'\u0635',
u'\uFEBB':u'\u0635',
u'\uFEBC':u'\u0635',
u'\uFEBA':u'\u0635',
u'\uFEED':u'\u0648',
u'\uFEEE':u'\u0648',
u'\uFEEF':u'\u0649',
u'\uFEF0':u'\u0649',
u'\uFE85':u'\u0624',
u'\uFE86':u'\u0624',
u'\uFE87':u'\u0625',
u'\uFE88':u'\u0625',
u'\uFE89':u'\u0626',
u'\uFE8B':u'\u0626',
u'\uFE8C':u'\u0626',
u'\uFE8A':u'\u0626',
u'\uFE8D':u'\u0627',
u'\uFE8E':u'\u0627',
u'\uFEB1':u'\u0633',
u'\uFEB3':u'\u0633',
u'\uFEB4':u'\u0633',
u'\uFEB2':u'\u0633',
u'\uFE80':u'\u0621',
u'\uFE81':u'\u0622',
u'\uFE82':u'\u0622',
u'\uFE83':u'\u0623',
u'\uFE84':u'\u0623',
u'\uFEF1':u'\u064A',
u'\uFEF3':u'\u064A',
u'\uFEF4':u'\u064A',
u'\uFEF2':u'\u064A',
u'\uFEAD':u'\u0631',
u'\uFEAE':u'\u0631',
u'\uFE8F':u'\u0628',
u'\uFE91':u'\u0628',
u'\uFE92':u'\u0628',
u'\uFE90':u'\u0628',
u'\uFE93':u'\u0629',
u'\uFE94':u'\u0629',
u'\uFEC9':u'\u0639',
u'\uFECB':u'\u0639',
u'\uFECC':u'\u0639',
u'\uFECA':u'\u0639',
u'\uFEAF':u'\u0632',
u'\uFEB0':u'\u0632',
u'\uFEF5':u'\u0644\u0622',#LAM_ALEF_MADDA_ABOVE
u'\uFEF7':u'\u0644\u0623',#LAM_ALEF_HAMZA_ABOVE
u'\uFEF9':u'\u0644\u0625',#LAM_ALEF_HAMZA_BELOW
u'\uFEFC':u'\u0644\u0627',# LAM ALEF

}
def unshaping_text(text):
    unshaping_text="";
    list_line=text.splitlines();
    for line in list_line:
        unshaping_text+="\n"+unshaping_line(line);
    return unshaping_text;


import pyarabic.araby as arab
#arab=arabic.araby();
def unshaping_line(line):
    unshaping_line="";
    currentword=u"";
    words=line.split();
    newwordlist=[];
    for word in words:
       newwordlist.append(unshaping_word(word));
    newwordlist.reverse()
    return ' '.join(newwordlist)



def unshaping_word(word):
    unshaping_word="";
##    if not arab.isArabicrange(word):
##        return word;
    for c in word:
        if c in unshaping_table.keys():
            unshaping_word=unshaping_table[c]+unshaping_word;
        else:
            unshaping_word=c+unshaping_word;
    return unshaping_word;


