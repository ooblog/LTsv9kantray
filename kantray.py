#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import os
os.chdir(sys.path[0])
from LTsv_printf import *
from LTsv_file   import *
from LTsv_time   import *
from LTsv_calc   import *
from LTsv_joy    import *
from LTsv_kbd    import *
from LTsv_gui    import *

kantray_ltsv,kantray_config,kantray_keybind,kantray_keybindF="","","",""
kantray_setchar,kantray_setfind="",""
kantray_fontname,kantray_fontsize="kantray5x5comic",12; kantray_font="{0},{1}".format(kantray_fontname,kantray_fontsize)
kantray_findNX,kantray_findalpha,kantray_finddic,kantray_findchar="Σ","σ","名","ぬ"
kantray_directnotifys,kantray_directimage,kantray_directcellpos,kantray_directONOFF=0,"kanmap.png",{"N":76,"X":153,"NK":75,"XK":152,"P":76,"D":153,"S":154},0
kantray_inputpaste,kantray_inputcut,kantray_inputNFER,kantray_inputXFER,kantray_inputKANA="CtrlL\tV","CtrlL\tX","NFER","XFER","KANA"
kantray_input_OTHER="Left\tUp\tRight\tDown\tEnter\tTab\tEsc\tPrtSc\tBS\tDEL\tHome\tEnd\tPgUp\tPgDn"
kantray_evalentry,kantray_evalcalc,kantray_evalnow,kantray_evaloverhour,kantray_evalslash,kantray_evaldakuon,kantray_evalseion="","Σ","年-月-日(週曜)時:分:秒",24,"￥","Ｐ","Ｈ"
kantray_notifyicon=None
kantray_notifyID=[[],[3],[3,2],[2,1,0],[3,2,1,0]]
kantray_notifyOBJ=[[],[None],[None,None],[None,None,None],[None,None,None,None]]
kantray_notifyPD,kantray_notifyNX,kantray_notifyK,kantray_notifyS=["P","D"],{"True":"N","False":"X"},{"True":"NK","False":"XK"},"S"
kantray_title=["kantray「貼付モード(マウス)」","kantray「漢直モード(キーボード)」"]
kantray_cursorIR,kantray_cursorNX,kantray_kbdSwitch,kantray_kbdSandS,kantray_kbdSandSDraw=None,None,"","",""
kantray_IROHAs,kantray_IROHAsOLD="",""
kantray_KEYNAMEs,kantray_KEYNAMEsOLD="",""
kantray_kanword,kantray_kanzip="",""
keytray_evaltype="平片大小半全＼￥清ＨＭ濁ＢＰ今⑩⑯⑧⓪照探〒汎算"

def kantray_directswitch(callback_void=None,callback_ptr=None):
    global kantray_directONOFF
    if kantray_directnotifys > 0:
        kantray_directONOFF=0 if kantray_directONOFF else 1
        LTsv_kbdEVIOCGRAB(kantray_directONOFF)
        LTsv_widget_settext(kantray_window,kantray_title[kantray_directONOFF])
        for notifyLCRX in range(len(kantray_notifyID[kantray_directnotifys])):
            LTsv_widget_settext(kantray_notifyOBJ[kantray_directnotifys][notifyLCRX],kantray_title[kantray_directONOFF])
            LTsv_widget_seturi(kantray_notifyOBJ[kantray_directnotifys][notifyLCRX],widget_u="{0}[{1}]".format(kantray_directimage,kantray_directcellpos[kantray_notifyPD[kantray_directONOFF]]*4+kantray_notifyID[kantray_directnotifys][notifyLCRX]))
kantray_directswitch_cbk=LTsv_CALLBACLTYPE(kantray_directswitch)

def kantray_direct(callback_void=None,callback_ptr=None):
    global kantray_cursorIR,kantray_cursorNX,kantray_kbdSwitch,kantray_kbdSandS,kantray_kbdSandSDraw
    global kantray_IROHAs,kantray_IROHAsOLD,kantray_KEYNAMEs,kantray_KEYNAMEsOLD
    global kantray_inputpaste,kantray_inputcut,kantray_inputNFER,kantray_inputXFER,kantray_inputKANA,kantray_input_OTHER
    keyboard_cursorMS,keyboard_cursorIR,keyboard_cursorAF,keyboard_cursorOLD,keyboard_cursorDIC,keyboard_cursorNX,keyboard_cursorK,keyboard_cursorLCR=LTsv_keyboard_NXK()
    keyboard_irohatype,keyboard_alphatype,keyboard_dictype,keyboard_tofu=LTsv_keyboard_iroha_type()
    keyboard_irohamax,keyboard_alphapos,keyboard_guidepos,keyboard_dicinppos,keyboard_dicselpos,keyboard_iroha,keyboard_guideN,keyboard_guideX,keyboard_guideK,keyboard_guideKN,keyboard_guideKX=LTsv_keyboard_iroha_guide()
    LTsv_setkbddata(25,0); kantray_getkbdstr=LTsv_getkbdlabels("{0}\t{1}\t{2}\tSpace\tMouseL\tMouseR\tMouseC".format(kantray_inputNFER,kantray_inputXFER,kantray_inputKANA))
    keyboard_kanmapN,keyboard_kanmapX,keyboard_dicinput=LTsv_keyboard_map()
    if kantray_directnotifys > 0:
        kantray_NFER= int(LTsv_pickdatalabel(kantray_getkbdstr,kantray_inputNFER))
        kantray_XFER= int(LTsv_pickdatalabel(kantray_getkbdstr,kantray_inputXFER))
        if kantray_NFER != 0 and kantray_XFER != 0:
            if kantray_kbdSwitch != "NFERXFER":
                kantray_kbdSwitch="NFERXFER"; kantray_directswitch()
        elif kantray_NFER == 0 and kantray_XFER == 0:
            kantray_kbdSwitch=""
        if kantray_directONOFF > 0:
            kantray_KANA= int(LTsv_pickdatalabel(kantray_getkbdstr,kantray_inputKANA))
            kantray_SPACE=int(LTsv_pickdatalabel(kantray_getkbdstr,"Space"))
            kantray_kbdkanas,kantray_kbdnames=LTsv_getkbdkanas(),LTsv_getkbdnames()
            kantray_IROHAs=kantray_kbdkanas.split('\t') if len(kantray_kbdkanas) > 0 else []
            kantray_KEYNAMEs=kantray_kbdnames.split('\t') if len(kantray_kbdnames) > 0 else []
            if kantray_NFER != 0 and kantray_XFER == 0:
                keyboard_cursorNX=True
                for IROHAs in kantray_IROHAs:
                    if IROHAs in keyboard_iroha:
                        keyboard_cursorIR=keyboard_iroha.index(IROHAs); keyboard_cursorMS=keyboard_cursorIR
                LTsv_keyboard_NXK(cursorMS=keyboard_cursorMS,cursorNX=keyboard_cursorNX,cursorIR=keyboard_cursorIR); LTsv_keyboard_find(kantray_canvas)
            elif kantray_NFER == 0 and kantray_XFER != 0:
                keyboard_cursorNX=False
                for IROHAs in kantray_IROHAs:
                    if IROHAs in keyboard_iroha:
                        keyboard_cursorIR=keyboard_iroha.index(IROHAs); keyboard_cursorMS=keyboard_cursorIR
                LTsv_keyboard_NXK(cursorMS=keyboard_cursorMS,cursorNX=keyboard_cursorNX,cursorIR=keyboard_cursorIR); LTsv_keyboard_find(kantray_canvas)
            elif kantray_KANA != 0:
                keyboard_cursorK=-1; kantray_kbdSandS="alpha"
                if kantray_IROHAsOLD != kantray_IROHAs:
                    for IROHAs in kantray_IROHAs:
                        if IROHAs in keyboard_iroha:
                            keyboard_cursorMS=keyboard_iroha.index(IROHAs)
                            keyboard_cursor_alpha=keyboard_guideK[keyboard_cursorMS]
                            if keyboard_cursor_alpha in keyboard_irohatype:
                                keyboard_cursorIR=keyboard_irohatype.index(keyboard_cursor_alpha); LTsv_keyboard_NXK(cursorIR=keyboard_cursorIR)
                            elif keyboard_cursor_alpha in keyboard_alphatype:
                                keyboard_cursorIR,keyboard_cursorAF=LTsv_keyboard_irohamax,keyboard_alphatype.index(keyboard_cursor_alpha)
                                LTsv_keyboard_NXK(cursorIR=keyboard_cursorIR,cursorAF=keyboard_cursorAF)
                            elif keyboard_cursor_alpha in keyboard_dictype:
                                keyboard_cursorDIC=keyboard_cursor_alpha; LTsv_keyboard_NXK(cursorDIC=keyboard_cursorDIC)
                LTsv_keyboard_NXK(cursorMS=keyboard_cursorMS,cursorK=keyboard_cursorK); LTsv_keyboard_find(kantray_canvas)
            elif kantray_SPACE != 0:
                if kantray_kbdSandS == "":
                    LTsv_keyboard_dicinput()
                    keyboard_cursorK=1; kantray_kbdSandS="SandS"
                if kantray_IROHAsOLD != kantray_IROHAs:
                    for IROHAs in kantray_IROHAs:
                        if IROHAs in keyboard_irohatype:
                            keyboard_cursorMS=LTsv_keyboard_iroha.index(IROHAs)
                            kantray_direct_char(keyboard_dicinput[keyboard_cursorMS]); kantray_kbdSandS="dicinput"
                LTsv_keyboard_NXK(cursorMS=keyboard_cursorMS,cursorK=keyboard_cursorK); LTsv_keyboard_find(kantray_canvas)
            else:
                if kantray_kbdSandS != "":
                    if kantray_kbdSandS == "SandS":
                        if keyboard_cursorNX:
                            kantray_direct_char(keyboard_kanmapN[keyboard_iroha[keyboard_cursorIR]][keyboard_irohamax])
                        else:
                            kantray_direct_char(keyboard_kanmapX[keyboard_iroha[keyboard_cursorIR]][keyboard_irohamax])
                    keyboard_cursorK=0; kantray_kbdSandS=""
                    LTsv_keyboard_NXK(cursorK=keyboard_cursorK); LTsv_keyboard_find(kantray_canvas)
                if kantray_IROHAsOLD != kantray_IROHAs:
                    for IROHAs in kantray_IROHAs:
                        if IROHAs in keyboard_irohatype:
                            if keyboard_cursorNX:
                                kantray_direct_char(keyboard_kanmapN[keyboard_iroha[keyboard_cursorIR]][LTsv_keyboard_iroha.index(IROHAs)])
                            else:
                                kantray_direct_char(keyboard_kanmapX[keyboard_iroha[keyboard_cursorIR]][LTsv_keyboard_iroha.index(IROHAs)])
                if kantray_KEYNAMEsOLD != kantray_KEYNAMEs:
                    for KEYNAMEs in kantray_KEYNAMEsOLD:
                        if KEYNAMEs in kantray_input_OTHER.split('\t'):
                            LTsv_kbdEVIOCGRAB(0)
                            LTsv_kbdwriteCtrl(KEYNAMEs)
                            LTsv_kbdEVIOCGRAB(1)
            kantray_IROHAsOLD,kantray_KEYNAMEsOLD=kantray_IROHAs,kantray_KEYNAMEs
    if kantray_kbdSandSDraw != kantray_kbdSandS:
        kantray_kbdSandSDraw=kantray_kbdSandS
        if kantray_kbdSandS == "alpha":
            for notifyLCRX in range(len(kantray_notifyID[kantray_directnotifys])):
                LTsv_widget_seturi(kantray_notifyOBJ[kantray_directnotifys][notifyLCRX],widget_u="{0}[{1}]".format(kantray_directimage,kantray_directcellpos[kantray_notifyK[str(kantray_cursorNX)]]*4+kantray_notifyID[kantray_directnotifys][notifyLCRX]))
        elif kantray_kbdSandS == "SandS":
            if keyboard_cursorDIC in keyboard_dictype:
                for notifyLCRX in range(len(kantray_notifyID[kantray_directnotifys])):
                    LTsv_widget_seturi(kantray_notifyOBJ[kantray_directnotifys][notifyLCRX],widget_u="{0}[{1}]".format(kantray_directimage,kantray_directcellpos[kantray_notifyS]*4+keyboard_dictype.index(keyboard_cursorDIC)*4+kantray_notifyID[kantray_directnotifys][notifyLCRX]))
        else:
            for notifyLCRX in range(len(kantray_notifyID[kantray_directnotifys])):
                LTsv_widget_seturi(kantray_notifyOBJ[kantray_directnotifys][notifyLCRX],widget_u="{0}[{1}]".format(kantray_directimage,kantray_directcellpos[kantray_notifyNX[str(kantray_cursorNX)]]*4+(kantray_cursorIR if keyboard_cursorIR < LTsv_keyboard_irohamax else keyboard_cursorIR+keyboard_cursorAF)*4+kantray_notifyID[kantray_directnotifys][notifyLCRX]))
    if kantray_cursorIR != keyboard_cursorIR or kantray_cursorNX != keyboard_cursorNX:
        kantray_cursorNX,kantray_cursorIR=keyboard_cursorNX,keyboard_cursorIR
        for notifyLCRX in range(len(kantray_notifyID[kantray_directnotifys])):
            LTsv_widget_seturi(kantray_notifyOBJ[kantray_directnotifys][notifyLCRX],widget_u="{0}[{1}]".format(kantray_directimage,kantray_directcellpos[kantray_notifyNX[str(kantray_cursorNX)]]*4+(kantray_cursorIR if keyboard_cursorIR < LTsv_keyboard_irohamax else keyboard_cursorIR+keyboard_cursorAF)*4+kantray_notifyID[kantray_directnotifys][notifyLCRX]))
    LTsv_window_after(kantray_window,event_b=kantray_direct,event_i="kantray_direct",event_w=50)

def kantray_direct_char(direct_char=""):
    global kantray_keybindF
    if direct_char in kantray_keybindF:
        kantray_keybindR=LTsv_readlinerest(kantray_keybind,direct_char)
        if direct_char == "Window!":
            LTsv_widget_showhide(kantray_window,True)
        elif direct_char == "QuickWindow!":
            LTsv_kantray_windowshow()
        elif direct_char == "Eval!":
            LTsv_kbdEVIOCGRAB(0)
            LTsv_kbdwriteCtrl(kantray_inputcut)     #"CtrlL\tX"
            LTsv_kbdEVIOCGRAB(1)
            calc_value=LTsv_widget_gettext(kantray_clipboard)
            calc_value=kantray_entryeval_kernel(value=calc_value)
            LTsv_widget_settext(kantray_clipboard,widget_t=calc_value)
            LTsv_kbdEVIOCGRAB(0)
            LTsv_kbdwriteCtrl(kantray_inputpaste)   #"CtrlL\tV"
            LTsv_kbdEVIOCGRAB(1)
        elif direct_char == "tab!":
            LTsv_widget_settext(kantray_clipboard,widget_t="\t")
            LTsv_kbdEVIOCGRAB(0)
            LTsv_kbdwriteCtrl(kantray_inputpaste)
            LTsv_kbdEVIOCGRAB(1)
        elif direct_char == "4Space!":
            LTsv_widget_settext(kantray_clipboard,widget_t="    ")
            LTsv_kbdEVIOCGRAB(0)
            LTsv_kbdwriteCtrl(kantray_inputpaste)
            LTsv_kbdEVIOCGRAB(1)
        else:
            LTsv_kbdEVIOCGRAB(0)
            LTsv_kbdwriteCtrl(kantray_keybindR)     #"hjkl"
            LTsv_kbdEVIOCGRAB(1)
    else:
        LTsv_widget_settext(kantray_clipboard,widget_t=direct_char)
        LTsv_kbdEVIOCGRAB(0)
        LTsv_kbdwriteCtrl(kantray_inputpaste)       #"CtrlL\tV"
        LTsv_kbdEVIOCGRAB(1)

def kantray_getkey():
    LTsv_setkbddata(25,0); kantray_getkbdstr=LTsv_getkbdlabels("MouseL\tMouseR\tMouseC")
    return kantray_getkbdstr

def kantray_setkey(setkey=None,setfind=True):
    global kantray_setchar,kantray_setfind
    global kantray_findNX,kantray_findalpha,kantray_finddic,kantray_findchar
    global kantray_evalentry
    kantray_setchar=setkey
    kantray_setfind=setfind
    kantray_findchar=kantray_findchar if len(kantray_setchar) !=1  else kantray_setchar
    LTsv_widget_settext(kantray_entry,LTsv_widget_gettext(kantray_entry)+kantray_setchar)
    kantray_evalentry=LTsv_widget_gettext(kantray_entry)

def kantray_entrydel(callback_void=None,callback_ptr=None):
    global kantray_evalentry
    kantray_evalentry=LTsv_widget_gettext(kantray_entry)
    LTsv_widget_settext(kantray_entry,kantray_evalentry[:len(kantray_evalentry)-1])
    kantray_evalentry=LTsv_widget_gettext(kantray_entry)

def kantray_entryclear(callback_void=None,callback_ptr=None):
    global kantray_evalentry
    LTsv_widget_settext(kantray_entry,"")
    kantray_evalentry=LTsv_widget_gettext(kantray_entry)

def kantray_entryeval_shell(callback_void=None,callback_ptr=None):
    global kantray_evalentry
    calc_value=LTsv_widget_gettext(kantray_entry)
    calc_value=kantray_entryeval_kernel(value=calc_value)
    LTsv_widget_settext(kantray_entry,calc_value)
    kantray_evalentry=LTsv_widget_gettext(kantray_entry)

def kantray_entryeval_kernel(value=""):
    global kantray_evalentry
    global kantray_kanword,kantray_kanzip
    keyboard_cursorMS,keyboard_cursorIR,keyboard_cursorAF,keyboard_cursorOLD,keyboard_cursorDIC,keyboard_cursorNX,keyboard_cursorK,keyboard_cursorLCR=LTsv_keyboard_NXK()
    keyboard_irohatype,keyboard_alphatype,keyboard_dictype,keyboard_tofu=LTsv_keyboard_iroha_type()
    calc_value=value
    calc_K,calc_Q,calc_A="","",""
    keyboard_kandic=LTsv_keyboard_dic()
    if len(calc_value) == 0:
        LTsv_keyboard_find(kantray_canvas,find_t="",find_max=kantray_max,NX_t=kantray_evalcalc)
    elif calc_value.find('⇔') < 0:
        calc_value+='⇔'
    if calc_value.find('⇔') == 0:
        if calc_value[:2] == "⇔⇔":
            calc_Q=calc_value[0]
            calc_A=LTsv_pickdatalabel(LTsv_readlinerest(keyboard_kandic,calc_Q),keyboard_cursorDIC)
            if len(calc_A) > 0:
                calc_K=keyboard_cursorDIC
            else:
                calc_K,calc_A="照",""
        else:
            if len(calc_value) == 1:
                if len(LTsv_pickdatalabel(LTsv_readlinerest(keyboard_kandic,calc_value[0]),keyboard_cursorDIC)) > 0:
                    calc_K,calc_Q=keyboard_cursorDIC,calc_value[0]
                else:
                    calc_K,calc_Q="照",calc_value[0]
            else:
                calc_K,calc_Q="算",""
    elif calc_value.find('⇔') == 1:
        calc_Q=calc_value[0]
        if len(calc_value) > 2:
            if calc_value[2] == ('⇔'):
                if calc_Q in keytray_evaltype or calc_Q in keyboard_dictype:
                    calc_K=calc_Q
        if calc_K == "":
            calc_A=LTsv_pickdatalabel(LTsv_readlinerest(keyboard_kandic,calc_Q),keyboard_cursorDIC)
            if len(calc_A) > 0:
                calc_K=keyboard_cursorDIC
            else:
                calc_K,calc_A="照",""
        LTsv_keyboard_find(kantray_canvas,find_t=calc_Q,find_max=kantray_max)
    elif calc_value.find('⇔') == 2:
        if calc_value[0] in keytray_evaltype or calc_value[0] in keyboard_dictype:
            calc_K,calc_Q=calc_value[0],calc_value[1]
        else:
            calc_K,calc_Q="汎",calc_value[:2]
    else:
        if len(calc_value) > 0:
            calc_Q=calc_value[:calc_value.find('⇔')]
            if (calc_Q.startswith("&#") or calc_Q.startswith("&")) and calc_Q.endswith(";"):
                calc_K="照"
            elif calc_Q[0] in keytray_evaltype:
                calc_K,calc_Q=calc_Q[0],calc_Q[1:]
            else:
                calc_K="汎"
    if calc_K == "全":
        calc_K="￥" if kantray_evalslash == "￥" else "＼"
    if calc_K == "濁":
        calc_K="Ｐ" if kantray_evaldakuon == "Ｐ" else "Ｂ"
    if calc_K == "清":
        calc_K="Ｈ" if kantray_evalseion == "Ｈ" else "Ｍ"
    if calc_K in keyboard_dictype:
        calc_A=LTsv_pickdatalabel(LTsv_readlinerest(keyboard_kandic,calc_Q),calc_K)
    elif calc_K == "平":
        calc_A=LTsv_kanare(calc_Q,"Kata2Hira")
    elif calc_K == "片":
        calc_A=LTsv_kanare(calc_Q,"Hira2Kata")
    elif calc_K == "大":
        calc_A=LTsv_kanare(calc_Q,"Alpha2BIG")
    elif calc_K == "小":
        calc_A=LTsv_kanare(calc_Q,"Alpha2SML")
    elif calc_K == "半":
        calc_A=LTsv_kanare(calc_Q,"HiraKana2HanKaKe"); calc_A=LTsv_kanare(calc_A,"Alpha2HAN")
    elif calc_K == "＼":
        calc_A=LTsv_kanare(calc_Q,"Han2Kata");         calc_A=LTsv_kanare(calc_A,"Alpha2ZENBS")
    elif calc_K == "￥":
        calc_A=LTsv_kanare(calc_Q,"Han2Kata");         calc_A=LTsv_kanare(calc_A,"Alpha2ZENYen")
    elif calc_K == "Ｈ":
        calc_A=LTsv_kanare(calc_Q,"HiraKana2SeiH")
    elif calc_K == "Ｍ":
        calc_A=LTsv_kanare(calc_Q,"HiraKana2SeiM")
    elif calc_K == "Ｂ":
        calc_A=LTsv_kanare(calc_Q,"HiraKana2DakB")
    elif calc_K == "Ｐ":
        calc_A=LTsv_kanare(calc_Q,"HiraKana2DakP")
    elif calc_K == "今":
        LTsv_putdaytimenow(overhour=kantray_evaloverhour)
        calc_Q=calc_Q.replace("今",kantray_evalnow)
        calc_Q=calc_Q.replace("干","@yzj").replace("年","@000y").replace("月","@0m").replace("日","@0dm").replace("週","@0wnyi").replace("曜","@wdj").replace("時","@0h").replace("分","@0n").replace("秒","@0s")
        calc_Q=calc_Q.replace("版",LTsv_time_ver())
        calc_Q=calc_Q.replace("印","@000y@0m@0dm@wdec@0h@0n@0s")
        calc_A=LTsv_getdaytimestr(calc_Q)
    elif calc_K == "⑩":
        calc_A=str(LTsv_intstr0x(calc_Q))
    elif calc_K == "⑯":
        calc_A=hex(LTsv_intstr0x(calc_Q.lstrip('0x').strip('$')))
    elif calc_K == "⑧":
        calc_A=LTsv_utf2ink(calc_Q)
    elif calc_K == "⓪":
        calc_A=LTsv_ink2utf(calc_Q)
    elif calc_K == "照":
        if (calc_Q.startswith("&#") or calc_Q.startswith("&")) and calc_Q.endswith(";"):
            calc_A=LTsv_xml2utf(calc_Q)
        else:
            calc_A=LTsv_utf2xml(calc_Q)
    elif calc_K == "〒":
        kantray_kanzip=LTsv_loadfile(LTsv_readlinerest(kantray_config,"dic_zipname"),kantray_kanzip)
        calc_Q=LTsv_kanare(calc_Q,"HiraKana2HanKaKe"); calc_Q=LTsv_kanare(calc_Q,"Alpha2HAN")
        calc_Q=(calc_Q.replace('-','').replace('ｰ','')+'0'*7)[:7]
        calc_A=LTsv_readlinerest(kantray_kanzip,calc_Q)
    elif calc_K == "探":
        for calc_F in calc_Q:
            calc_EX=""
            calc_EXdic=LTsv_pickdatalabel(LTsv_readlinerest(keyboard_kandic,calc_F),'異')+ \
              LTsv_pickdatalabel(LTsv_readlinerest(keyboard_kandic,calc_F),'簡')+ \
              LTsv_pickdatalabel(LTsv_readlinerest(keyboard_kandic,calc_F),'繁')+ \
              LTsv_pickdatalabel(LTsv_readlinerest(keyboard_kandic,calc_F),'代')
            for calc_e in calc_EXdic:
                calc_EX=calc_EX if ord(calc_e) < 128 else calc_EX+calc_e
            find_existpos=LTsv_keyboard_find(kantray_canvas,find_t=calc_F+calc_EX,find_max=kantray_max)
            if find_existpos >= 0:
                calc_A=calc_F
                break
    elif calc_K == "汎":
        kantray_kanword=LTsv_loadfile(LTsv_readlinerest(kantray_config,"dic_wordname"),kantray_kanword)
        calc_A=LTsv_readlinerest(kantray_kanword,calc_Q)
        if calc_A == "":
            calc_A=LTsv_readlinerest(kantray_kanword,LTsv_kanare(calc_Q,"Kata2Hira"))
            calc_Q=LTsv_kanare(calc_Q,"Kata2Hira") if calc_A != "" else calc_Q
        if calc_A == "":
            calc_A=LTsv_readlinerest(kantray_kanword,LTsv_kanare(calc_Q,"Hira2Kata"))
            calc_Q=LTsv_kanare(calc_Q,"Kata2Hira") if calc_A != "" else calc_Q
        if calc_A == "":
            calc_K="算"
    if calc_K == "算":
        calc_A=LTsv_calc(calc_Q)
    if calc_K != "":
#        LTsv_widget_settext(kantray_entry,"{0}{1}⇔{2}".format(calc_K,calc_Q,calc_A))
        calc_value="{0}{1}⇔{2}".format(calc_K,calc_Q,calc_A)
    else:
        calc_value=value
    return calc_value

def kantray_notify_menu():
    yield ("「kantray」の終了",kantray_exit_configsave_cbk)
    yield ("",None)
    yield ("「漢直モード(キーボード)」と「貼付モード(マウス)」の切替",kantray_directswitch_cbk)
    yield ("",None)
    yield ("「kantray」を強引に表示",LTsv_kantray_windowshow_cbk)

def LTsv_kantray_windowshow(window_objvoid=None,window_objptr=None):
    LTsv_widget_showhide(kantray_window,False)
    LTsv_widget_showhide(kantray_window,True)
LTsv_kantray_windowshow_cbk=LTsv_CALLBACLTYPE(LTsv_kantray_windowshow)

def kantray_configload():
    global kantray_ltsv,kantray_config,kantray_keybind,kantray_keybindF
    global kantray_setchar,kantray_setfind
    global kantray_fontname,kantray_fontsize
    global kantray_findNX,kantray_findalpha,kantray_finddic,kantray_findchar
    global kantray_directnotifys,kantray_directimage,kantray_directcellpos,kantray_directONOFF
    global kantray_inputpaste,kantray_inputcut,kantray_inputNFER,kantray_inputXFER,kantray_inputKANA,kantray_input_OTHER
    global kantray_evalentry,kantray_evalcalc,kantray_evalnow,kantray_evaloverhour,kantray_evalslash,kantray_evaldakuon,kantray_evalseion
    kantray_ltsv=LTsv_loadfile("kantray.tsv")
    kantray_config=LTsv_getpage(kantray_ltsv,"kantray")
    kantray_findNX=LTsv_readlinerest(kantray_config,"find_NX",kantray_findNX)
    kantray_findalpha=LTsv_readlinerest(kantray_config,"find_alpha",kantray_findalpha)
    kantray_finddic=LTsv_readlinerest(kantray_config,"find_dic",kantray_finddic)
    kantray_findchar=LTsv_readlinerest(kantray_config,"find_char",kantray_findchar)
    kantray_directnotifys=min(max(LTsv_intstr0x(LTsv_readlinerest(kantray_config,"direct_notifys")),0),4) if LTsv_GUI != "Tkinter" else 0
    if kantray_directnotifys > 0:
        kantray_directimage=LTsv_readlinerest(kantray_config,"direct_image",kantray_directimage)
        if LTsv_draw_picture_load(kantray_directimage) != None:
            LTsv_draw_picture_celldiv(kantray_directimage,28,25)
            kantray_directONOFF=min(max(LTsv_intstr0x(LTsv_readlinerest(kantray_config,"direct_ONOFF")),0),1)
        else:
            kantray_directnotifys=0
            kantray_directONOFF=0
        kantray_directcellpos=LTsv_label2dictint(LTsv_readlinerest(kantray_config,"direct_cellpos",kantray_directcellpos))
    kantray_inputpaste=LTsv_readlinerest(kantray_config,"input_paste",kantray_inputpaste)
    kantray_inputcut=LTsv_readlinerest(kantray_config,"input_cut",kantray_inputcut)
    kantray_inputNFER=LTsv_readlinerest(kantray_config,"input_NFER",kantray_inputNFER)
    kantray_inputXFER=LTsv_readlinerest(kantray_config,"input_XFER",kantray_inputXFER)
    kantray_inputKANA=LTsv_readlinerest(kantray_config,"input_KANA",kantray_inputKANA)
    kantray_input_OTHER=LTsv_readlinerest(kantray_config,"input_OTHER",kantray_input_OTHER)
    kantray_evalcalc=LTsv_readlinerest(kantray_config,"eval_calc",kantray_evalcalc)
    kantray_evalentry=LTsv_readlinerest(kantray_config,"eval_entry","")
    kantray_evalnow=LTsv_readlinerest(kantray_config,"eval_now",kantray_evalnow)
    kantray_evaloverhour=min(max(LTsv_intstr0x(LTsv_readlinerest(kantray_config,"eval_overhour")),24),48)
    kantray_evalslash=LTsv_readlinerest(kantray_config,"eval_slash",kantray_evalslash)
    kantray_evaldakuon=LTsv_readlinerest(kantray_config,"eval_dakuon",kantray_evaldakuon)
    kantray_evalseion=LTsv_readlinerest(kantray_config,"eval_seion",kantray_evalseion)
    kantray_fontname=LTsv_readlinerest(kantray_config,"font_name",kantray_fontname)
    kantray_fontsize=min(max(LTsv_intstr0x(LTsv_readlinerest(kantray_config,"font_size")),5),99)
    kantray_keybind=LTsv_getpage(kantray_ltsv,"keybind")
    kantray_keybindF=LTsv_readlinefirsts(kantray_keybind).split('\t')

def kantray_exit_configsave(window_objvoid=None,window_objptr=None):
    global kantray_ltsv,kantray_config
    global kantray_findNX,kantray_findalpha,kantray_finddic,kantray_findchar
    keyboard_irohamax,keyboard_alphapos,keyboard_guidepos,keyboard_dicinppos,keyboard_dicselpos,keyboard_iroha,keyboard_guideN,keyboard_guideX,keyboard_guideK,keyboard_guideKN,keyboard_guideKX=LTsv_keyboard_iroha_guide()
    keyboard_cursorMS,keyboard_cursorIR,keyboard_cursorAF,keyboard_cursorOLD,keyboard_cursorDIC,keyboard_cursorNX,keyboard_cursorK,keyboard_cursorLCR=LTsv_keyboard_NXK()
    keyboard_irohatype,keyboard_alphatype,keyboard_dictype,keyboard_tofu=LTsv_keyboard_iroha_type()
    kantray_findalpha,kantray_finddic=keyboard_alphatype[keyboard_cursorAF],keyboard_cursorDIC
    kantray_ltsv=LTsv_loadfile("kantray.tsv")
    if keyboard_cursorOLD < keyboard_alphapos:
        kantray_findNX=""
    else:
        kantray_findchar=""
        keyboard_findN,keyboard_findX,keyboard_findNr,keyboard_findXr=LTsv_keyboard_findNX()
        if keyboard_cursorIR < keyboard_irohamax:
            kantray_findNX=keyboard_findNr[keyboard_irohatype[keyboard_cursorIR]] if keyboard_cursorNX else keyboard_findXr[keyboard_irohatype[keyboard_cursorIR]]
        else:
            kantray_findNX=keyboard_findNr[keyboard_alphatype[keyboard_cursorAF]] if keyboard_cursorNX else keyboard_findXr[keyboard_alphatype[keyboard_cursorAF]]
    kantray_config=LTsv_pushlinerest(kantray_config,"find_NX",kantray_findNX)
    kantray_config=LTsv_pushlinerest(kantray_config,"find_alpha",kantray_findalpha)
    kantray_config=LTsv_pushlinerest(kantray_config,"find_dic",kantray_finddic)
    kantray_config=LTsv_pushlinerest(kantray_config,"find_char",kantray_findchar)
    kantray_config=LTsv_pushlinerest(kantray_config,"direct_ONOFF",str(kantray_directONOFF))
    kantray_config=LTsv_pushlinerest(kantray_config,"eval_entry",kantray_evalentry)
    kantray_ltsv=LTsv_putpage(kantray_ltsv,"kantray",kantray_config)
    LTsv_savefile("kantray.tsv",kantray_ltsv)
    LTsv_window_exit()
kantray_exit_configsave_cbk=LTsv_CALLBACLTYPE(kantray_exit_configsave)

LTsv_GUI=LTsv_guiinit(LTsv_GUI_Tkinter)
kantray_max=0x2ffff if LTsv_GUI != "Tkinter" else 0xffff
if len(LTsv_GUI) > 0:
    LTsv_kbdinit(); kantray_kanchar=LTsv_keyboard_dic()
    kantray_configload()
    kantray_font="{0},{1}".format(kantray_fontname,kantray_fontsize)
    kantray_buttonWH=kantray_fontsize*5//3
    kantray_canvasWH=LTsv_keyboard_size(kantray_fontsize); kantray_canvasW,kantray_canvasH=LTsv_intstr0x(LTsv_pickdatanum(kantray_canvasWH,0)),LTsv_intstr0x(LTsv_pickdatanum(kantray_canvasWH,1))
    kantray_entryW=kantray_canvasW-int(kantray_buttonWH*3.5)
    kantray_window=LTsv_window_new(widget_t=kantray_title[kantray_directONOFF],event_b=kantray_exit_configsave if kantray_directnotifys == 0 else None,widget_w=kantray_canvasW,widget_h=kantray_canvasH+kantray_buttonWH)
    kantray_canvas=LTsv_keyboard_new(kantray_window,widget_x=0,widget_y=0,keyboard_getkey=kantray_getkey,keyboard_setkey=kantray_setkey,widget_f=kantray_font)
    LTsv_keyboard_find(kantray_canvas,find_t=kantray_findchar,find_max=kantray_max,dic_t=kantray_finddic,alpha_t=kantray_findalpha,NX_t=kantray_findNX)
    LTsv_keyboard_find(kantray_canvas,find_max=kantray_max,NX_t=kantray_findNX)
    kantray_entry=LTsv_entry_new(kantray_window,event_b=kantray_entryeval_shell,widget_t=kantray_evalentry,widget_x=0,widget_y=kantray_canvasH,widget_w=kantray_entryW,widget_h=kantray_buttonWH,widget_f=kantray_font)
    kantray_clipboard=LTsv_clipboard_new(kantray_window)
    kantray_delbutton=LTsv_button_new(kantray_window,event_b=kantray_entrydel,widget_t="←",widget_x=kantray_entryW+kantray_buttonWH*0,widget_y=kantray_canvasH,widget_w=kantray_buttonWH,widget_h=kantray_buttonWH,widget_f=kantray_font)
    kantray_clearbutton=LTsv_button_new(kantray_window,event_b=kantray_entryclear,widget_t="c",widget_x=kantray_entryW+kantray_buttonWH*1,widget_y=kantray_canvasH,widget_w=kantray_buttonWH,widget_h=kantray_buttonWH,widget_f=kantray_font)
    kantray_evalbutton=LTsv_button_new(kantray_window,event_b=kantray_entryeval_shell,widget_t="⇔",widget_x=kantray_entryW+kantray_buttonWH*2,widget_y=kantray_canvasH,widget_w=int(kantray_buttonWH*1.5),widget_h=kantray_buttonWH,widget_f=kantray_font)
    if kantray_directnotifys > 0:
        for notifyLCRX in range(len(kantray_notifyID[kantray_directnotifys])):
            kantray_notifyOBJ[kantray_directnotifys][notifyLCRX]=LTsv_notifyicon_new(kantray_window,widget_t="kantray",widget_u="{0}[{1}]".format(kantray_directimage,kantray_directcellpos[kantray_notifyPD[kantray_directONOFF]]*4+kantray_notifyID[kantray_directnotifys][notifyLCRX]),menu_b=kantray_notify_menu())
            LTsv_widget_settext(kantray_notifyOBJ[kantray_directnotifys][notifyLCRX],kantray_title[kantray_directONOFF])
        LTsv_kbdEVIOCGRAB(kantray_directONOFF)
    LTsv_widget_showhide(kantray_window,True)
    kantray_direct()
    LTsv_window_main(kantray_window)


# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv9kantray/blob/master/LICENSE

