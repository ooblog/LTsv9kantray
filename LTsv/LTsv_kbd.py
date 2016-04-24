#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
from LTsv_file import *
import time
import os
import sys
import ctypes
import struct
if sys.platform.startswith("linux"):
    import fcntl
if sys.platform.startswith("win"):
    LTsv_user32=ctypes.windll.user32

LTsv_typenameL={ "1":2,"2":3,"3":4,"4":5,"5":6,"6":7,"7":8,"8":9,"9":10,"0":11,"=":12,"^":13,"|":124,
                 "Q":16,"W":17,"E":18,"R":19,"T":20,"Y":21,"U":22,"I":23,"O":24,"P":25,"@":26,"{":27,
                 "A":30,"S":31,"D":32,"F":33,"G":34,"H":35,"J":36,"K":37,"L":38,"+":39,"*":40,"}":43,
                 "Z":44,"X":45,"C":46,"V":47,"B":48,"N":49,"M":50,"<":51,">":52,"/":53,"_":89,
                 "NFER":94,"Space":57,"XFER":92,"KANA":93,"ShiftL":42,"ShiftR":54,"CtrlL":29,"CtrlR":97,"AltL":56,"AltR":100,
                 "Left":105,"Up":103,"Right":106,"Down":108,"Tab":15,"Esc":1,"PrtSc":99,
                 "Enter":28,"BS":14,"DEL":111,"Home":102,"End":107,"PgUp":104,"PgDn":109,
                 "F01":59,"F02":60,"F03":61,"F04":62,"F05":63,"F06":64,"F07":65,"F08":66,"F09":67,"F10":68,"F11":87,"F12":88,
                 "MouseL":250,"MouseR":251,"MouseC":252,"MouseF":253,"MouseB":254 }
LTsv_typecodeL=["${0:02x}".format(LTsv_code) for LTsv_code in range(256)]
for LTsv_key,LTsv_value in list(LTsv_typenameL.items()):
    LTsv_typecodeL[LTsv_typenameL[LTsv_key]]=LTsv_key
LTsv_typekanaL=[LTsv_code for LTsv_code in LTsv_typecodeL]

LTsv_typenameW={ "1":0x31,"2":0x32,"3":0x33,"4":0x34,"5":0x35,"6":0x36,"7":0x37,"8":0x38,"9":0x39,"0":0x30,"=":0xbd,"^":0xbb,"|":0xc0,
                 "Q":0x51,"W":0x57,"E":0x45,"R":0x52,"T":0x54,"Y":0x59,"U":0x55,"I":0x49,"O":0x4f,"P":0x50,"@":0xdb,"{":0xdd,
                 "A":0x41,"S":0x53,"D":0x44,"F":0x46,"G":0x47,"H":0x48,"J":0x4a,"K":0x4b,"L":0x4c,"+":0xba,"*":0xde,"}":0xdc,
                 "Z":0x5a,"X":0x58,"C":0x43,"V":0x56,"B":0x42,"N":0x4e,"M":0x4d,"<":0xbc,">":0xbe,"/":0xbf,"_":0xe2,
                 "NFER":0xe6,"Space":0x20,"XFER":0xe4,"KANA":0xe9,"CtrlL":0xa2,"CtrlR":0xa3,
                 "Left":0x25,"Up":0x26,"Right":0x27,"Down":0x28,"Tab":0x09,"Esc":0x1b,"PrtSc":0x2C,
                 "Enter":0x0d,"BS":0x08,"DEL":0x2e,"Home":0x24,"End":0x23,"PgUp":0x21,"PgDn":0x22,
                 "F01":0x70,"F02":0x71,"F03":0x72,"F04":0x73,"F05":0x74,"F06":0x75,"F07":0x76,"F08":0x77,"F09":0x78,"F10":0x79,"F11":0x7a,"F12":0x7b,
                 "MouseL":0x01,"MouseR":0x02,"MouseC":0x04,"MouseF":0x05,"MouseB":0x06 }
LTsv_typecodeW=["${0:02x}".format(LTsv_code) for LTsv_code in range(256)]
for LTsv_key,LTsv_value in list(LTsv_typenameW.items()):
    LTsv_typecodeW[LTsv_typenameW[LTsv_key]]=LTsv_key
LTsv_typekanaW=[LTsv_code for LTsv_code in LTsv_typecodeW]

LTsv_typegana={ "ぬ":"1","ふ":"2","あ":"3","う":"4","え":"5","お":"6","や":"7","ゆ":"8","よ":"9","わ":"0","ほ":"=","へ":"^","￥":"|",
                "た":"Q","て":"W","い":"E","す":"R","か":"T","ん":"Y","な":"U","に":"I","ら":"O","せ":"P","゛":"@","゜":"{",
                "ち":"A","と":"S","し":"D","は":"F","き":"G","く":"H","ま":"J","の":"K","り":"L","れ":"+","け":"*","む":"}",
                "つ":"Z","さ":"X","そ":"C","ひ":"V","こ":"B","み":"N","も":"M","ね":"<","る":">","め":"/","ろ":"_","　":"Space" }
for LTsv_key,LTsv_value in list(LTsv_typegana.items()):
    LTsv_typekanaL[LTsv_typenameL[LTsv_value]]=LTsv_key
    LTsv_typekanaW[LTsv_typenameW[LTsv_value]]=LTsv_key

LTsv_BTNnameL=["330","331","332","277","278"]
LTsv_BTNcodeL=[ 250,  251,  252,  253 , 254 ]
LTsv_BTNdic=dict(zip(LTsv_BTNnameL,LTsv_BTNcodeL))

LTsv_keyboard_iroha=  ["ぬ",     "ふ",     "あ",     "う",     "え",     "お",     "や",     "ゆ",     "よ",     "わ",     "ほ",     "へ",     "た",     "て",     "い",     "す"     ,"か",     "ん",     "な",     "に",     "ら",     "せ",     "゛",     "゜",     "ち",     "と",     "し",     "は",     "き",     "く",     "ま",     "の",     "り",     "れ",     "け",     "む",     "つ",     "さ",     "そ",     "ひ",     "こ",     "み",      "も",      "ね",      "る",      "め",     "ろ",     "￥",     "　"]
LTsv_keyboard_guideN= {"ぬ":"ﾇ", "ふ":"ﾌ", "あ":"ｱ", "う":"ｳ", "え":"ｴ", "お":"ｵ", "や":"ﾔ", "ゆ":"ﾕ", "よ":"ﾖ", "わ":"ﾜ", "ほ":"ﾎ", "へ":"ﾍﾎ","た":"ﾀ", "て":"ﾃ", "い":"ｲ", "す":"ｽ", "か":"ｶ", "ん":"ｶ", "な":"ﾅ", "に":"ﾅﾆ","ら":"ﾗ", "せ":"ｾ", "゛":"＠","゜":"ぷ","ち":"ﾁ", "と":"ﾄ", "し":"ｼ", "は":"ﾊ", "き":"ｷ", "く":"ｸ", "ま":"ﾏ", "の":"ﾉ", "り":"ﾘ", "れ":"ﾚ", "け":"ｹ", "む":"ﾑ", "つ":"ﾂ", "さ":"ｻ", "そ":"ｿ", "ひ":"ﾋ", "こ":"ｺ", "み":"ﾐ",  "も":"ﾓ",  "ね":"ﾈ",  "る":"ﾙ",  "め":"ﾒﾙ","ろ":"ﾛ", "￥":"\\","α":"α","β":"β","γ":"γ","δ":"δ","ε":"ε","ζ":"ζ","η":"η","θ":"θ","ι":"ι","κ":"κ","λ":"λ","μ":"μ","ν":"ν","ξ":"ξ","ο":"ο","π":"π","ρ":"ρ","σ":"σ","τ":"τ","υ":"υ","φ":"φ","χ":"χ","ψ":"ψ","ω":"ω","○":"○","△":"△","□":"□"}
LTsv_keyboard_guideX= {"ぬ":"ﾇ", "ふ":"ﾌ", "あ":"ｱ", "う":"ｳ", "え":"ｱ", "お":"ｵ", "や":"ｼｬ","ゆ":"ｼｭ","よ":"ｼｮ","わ":"ｼｮ","ほ":"ﾎ", "へ":"ﾀ", "た":"ﾀ", "て":"ﾀﾃ","い":"ｲ", "す":"ｽ", "か":"ｶ", "ん":"ｶ", "な":"ｶ", "に":"ﾆﾄ","ら":"ｼ", "せ":"ｾ", "゛":"｀","゜":"プ","ち":"ﾁ", "と":"ﾄ", "し":"ｼ", "は":"ﾊ", "き":"ｷ", "く":"ｸ", "ま":"ﾏ", "の":"ﾊ", "り":"ﾊ", "れ":"ｷ", "け":"ｹ", "む":"ﾑ", "つ":"ﾂ", "さ":"ｻ", "そ":"ｿ", "ひ":"ﾋ", "こ":"ｺ", "み":"ｻﾐ", "も":"ｿﾓ", "ね":"ﾋﾈ", "る":"ﾙｺ", "め":"ﾒ", "ろ":"ﾛ", "￥":"|" ,"α":"Α","β":"Β","γ":"Γ","δ":"Δ","ε":"Ε","ζ":"Ζ","η":"Η","θ":"Θ","ι":"Ι","κ":"Κ","λ":"Λ","μ":"Μ","ν":"Ν","ξ":"Ξ","ο":"Ο","π":"Π","ρ":"Ρ","σ":"Σ","τ":"Τ","υ":"Υ","φ":"Φ","χ":"Χ","ψ":"Ψ","ω":"Ω","○":"●","△":"▲","□":"■"}
LTsv_keyboard_guideK= ["名",     "音",     "訓",     "送",     "異",     "俗",     "簡",     "繁",     "越",     "地",     "逆",     "非",     "英",     "顔",     "ε",     "ρ",     "τ",     "υ",     "θ",     "ι",     "ο",     "π",     "゛",     "゜",     "α",     "σ",     "δ",     "φ",     "γ",     "η",     "ξ",     "κ",     "λ",     "代",     "鍵",     "ぬ",     "ζ",     "χ",     "ψ",     "ω",     "β",     "ν",      "μ",      "熙",      "○",      "△",     "□",     "￥",     "σ"]
LTsv_keyboard_guideKN={"ぬ":"名","ふ":"音","あ":"訓","う":"送","え":"異","お":"俗","や":"簡","ゆ":"繁","よ":"越","わ":"地","ほ":"逆","へ":"非","た":"英","て":"顔","い":"ε","す":"ρ","か":"τ","ん":"υ","な":"θ","に":"ι","ら":"ο","せ":"π","゛":"＠","゜":"ぷ","ち":"α","と":"σ","し":"δ","は":"φ","き":"γ","く":"η","ま":"ξ","の":"κ","り":"λ","れ":"代","け":"鍵","む":"ぬ","つ":"ζ","さ":"χ","そ":"ψ","ひ":"ω","こ":"β","み":"ν", "も":"μ", "ね":"熙", "る":"○", "め":"△","ろ":"□","￥":"\\","　":"σ"}
LTsv_keyboard_guideKX={"ぬ":"名","ふ":"音","あ":"訓","う":"送","え":"異","お":"俗","や":"簡","ゆ":"繁","よ":"越","わ":"地","ほ":"逆","へ":"非","た":"英","て":"顔","い":"Ε","す":"Ρ","か":"Τ","ん":"Υ","な":"Θ","に":"Ι","ら":"Ο","せ":"Π","゛":"｀","゜":"プ","ち":"Α","と":"Σ","し":"Δ","は":"Φ","き":"Γ","く":"Η","ま":"Ξ","の":"Κ","り":"Λ","れ":"代","け":"鍵","む":"ヌ","つ":"Ζ","さ":"Χ","そ":"Ψ","ひ":"Ω","こ":"Β","み":"Ν", "も":"Μ", "ね":"熙", "る":"○", "め":"△","ろ":"□","￥":"\\","　":"σ"}
LTsv_keyboard_findN=  {"ぬ":"ぬ","ふ":"ふ","あ":"あ","う":"う","え":"え","お":"お","や":"や","ゆ":"ゆ","よ":"よ","わ":"わ","ほ":"ほ","へ":"へ","た":"た","て":"て","い":"い","す":"す","か":"か","ん":"ん","な":"な","に":"に","ら":"ら","せ":"せ","゛":"゛","゜":"゜","ち":"ち","と":"と","し":"し","は":"は","き":"き","く":"く","ま":"ま","の":"の","り":"り","れ":"れ","け":"け","む":"む","つ":"つ","さ":"さ","そ":"そ","ひ":"ひ","こ":"こ","み":"み","も":"も","ね":"ね","る":"る","め":"め","ろ":"ろ","￥":"￥",    "α":"α","β":"β","γ":"γ","δ":"δ","ε":"ε","ζ":"ζ","η":"η","θ":"θ","ι":"ι","κ":"κ","λ":"λ","μ":"μ","ν":"ν","ξ":"ξ","ο":"ο","π":"π","ρ":"ρ","σ":"σ","τ":"τ","υ":"υ","φ":"φ","χ":"χ","ψ":"ψ","ω":"ω","○":"○","△":"△","□":"□"}
LTsv_keyboard_findX=  {"ヌ":"ぬ","フ":"ふ","ア":"あ","ウ":"う","エ":"え","オ":"お","ヤ":"や","ユ":"ゆ","ヨ":"よ","ワ":"わ","ホ":"ほ","ヘ":"へ","タ":"た","テ":"て","イ":"い","ス":"す","カ":"か","ン":"ん","ナ":"な","ニ":"に","ラ":"ら","セ":"せ","｀":"゛","｛":"゜","チ":"ち","ト":"と","シ":"し","ハ":"は","キ":"き","ク":"く","マ":"ま","ノ":"の","リ":"り","レ":"れ","ケ":"け","ム":"む","ツ":"つ","サ":"さ","ソ":"そ","ヒ":"ひ","コ":"こ","ミ":"み","モ":"も","ネ":"ね","ル":"る","メ":"め","ロ":"ろ","｜":"￥",    "Α":"α","Β":"β","Γ":"γ","Δ":"δ","Ε":"ε","Ζ":"ζ","Η":"η","Θ":"θ","Ι":"ι","Κ":"κ","Λ":"λ","Μ":"μ","Ν":"ν","Ξ":"ξ","Ο":"ο","Π":"π","Ρ":"ρ","Σ":"σ","Τ":"τ","Υ":"υ","Φ":"φ","Χ":"χ","Ψ":"ψ","Ω":"ω","●":"○","▲":"△","■":"□"}
LTsv_keyboard_findNr,LTsv_keyboard_findXr={val:key for key,val in LTsv_keyboard_findN.items()},{val:key for key,val in LTsv_keyboard_findX.items()}
LTsv_keyboard_dicinput= [" "]*len(LTsv_keyboard_iroha)
LTsv_keyboard_irohatype=["ぬ","ふ","あ","う","え","お","や","ゆ","よ","わ","ほ","へ","た","て","い","す","か","ん","な","に","ら","せ","゛","゜","ち","と","し","は","き","く","ま","の","り","れ","け","む","つ","さ","そ","ひ","こ","み","も","ね","る","め","ろ","￥"]
LTsv_keyboard_alphatype=["α","β","γ","δ","ε","ζ","η","θ","ι","κ","λ","μ","ν","ξ","ο","π","ρ","σ","τ","υ","φ","χ","ψ","ω","○","△","□"]
LTsv_keyboard_dictype=  ["英","名","音","訓","送","異","俗","熙","簡","繁","越","地","顔","鍵","代","逆","非","難","活","幅"]
LTsv_keyboard_tofu='✖'
LTsv_keyboard_irohamax,LTsv_keyboard_alphapos,LTsv_keyboard_guidepos,LTsv_keyboard_dicinppos,LTsv_keyboard_dicselpos=48,49,50,51,52
LTsv_keyboard_cursorMS,LTsv_keyboard_cursorIR,LTsv_keyboard_cursorAF,LTsv_keyboard_cursorOLD,LTsv_keyboard_cursorDIC,LTsv_keyboard_cursorNX,LTsv_keyboard_cursorK,LTsv_keyboard_cursorLCR=LTsv_keyboard_alphapos,0,0,LTsv_keyboard_alphapos,LTsv_keyboard_dictype[0],True,0,"000"
LTsv_keyboard_kanmapN,LTsv_keyboard_kanmapX,LTsv_keyboard_kandic={},{},""


LTsv_grabflagdef=0
LTsv_EVIOCGRAB        =0x40044590
LTsv_defkbddevpath    ="/dev/input/event0"; LTsv_kbddevpath=LTsv_defkbddevpath
LTsv_defmousedevpath  ="/dev/input/event0"; LTsv_mousedevpath=LTsv_defmousedevpath
LTsv_kbdhands         =None
LTsv_mousehands       =None
LTsv_INPUTEVENT_unpack=b"QhhL" if sys.version_info.major == 2 else "QhhL"
LTsv_kbdkeep          =[0]*256
LTsv_EV_KEY           =0x01
LTsv_EV_REL           =0x02
LTsv_EV_ABS           =0x03
class LTsv_timeval(ctypes.Structure):
    _fields_ = [
        ('tv_sec',        ctypes.c_ulong),
        ('tv_usec',       ctypes.c_ulong)
    ]
class LTsv_INPUTEVENT(ctypes.Structure):
    _fields_ = [
        ('time',          LTsv_timeval),
        ('type',          ctypes.c_short),
        ('code',          ctypes.c_short),
        ('value',         ctypes.c_uint)
    ]
                
LTsv_WH_KEYBOARD_LL=13
class LTsv_WINDOWSHOOK(ctypes.Structure):
    def __init__(self):
        self.keyboard_hook=False
        self.HookKeyboard()
    def HookKeyboard(self):
        print("LTsv_WINDOWSHOOK__init__")
#        self.keyboard_hook=True
    def __del__(self):
        self.UnhookKeyboard()
    def UnhookKeyboard(self):
        print("LTsv_WINDOWSHOOK __del__")
#        self.keyboard_hook=False
LTsv_WINDOWSHOOK_Class=None


LTsv_defkbdformat="ぬ\tふ\tあ\tう\tえ\tお\tや\tゆ\tよ\tわ\tほ\tへ\t￥\t" \
                 "た\tて\tい\tす\tか\tん\tな\tに\tら\tせ\t゛\t゜\t" \
                 "ち\tと\tし\tは\tき\tく\tま\tの\tり\tれ\tけ\tむ\t" \
                 "つ\tさ\tそ\tひ\tこ\tみ\tも\tね\tる\tめ\tろ\t" \
                 "NFER\tSpace\tXFER\tKANA\tMouseL\tMouseR\tMouseC"
def LTsv_kbdreset(LTsv_tsvpath):
    global LTsv_kbddevpath,LTsv_kbdhands,LTsv_mousedevpath,LTsv_mousehands
    global LTsv_typekanaW,LTsv_typekanaL,LTsv_typecodeW,LTsv_typecodeL
    global LTsv_typenameW,LTsv_typenameL,LTsv_typegana
    global LTsv_BTNnameL,LTsv_BTNcodeL,LTsv_BTNdic
    global LTsv_keyboard_iroha,LTsv_keyboard_guideN,LTsv_keyboard_guideX,LTsv_keyboard_guideK,LTsv_keyboard_guideKN,LTsv_keyboard_guideKX
    global LTsv_keyboard_kanmapN,LTsv_keyboard_kanmapX,LTsv_keyboard_tofu,LTsv_keyboard_kandic,LTsv_keyboard_irohatype,LTsv_keyboard_alphatype,LTsv_keyboard_dictype
    global LTsv_keyboard_findN,LTsv_keyboard_findX,LTsv_keyboard_findNr,LTsv_keyboard_findXr

    LTsv_tsvdir=os.path.normpath(os.path.dirname(LTsv_tsvpath))+"/"
    LTsv_kbdltsv=LTsv_loadfile(LTsv_tsvpath)
    LTsv_deviceL_page=LTsv_getpage(LTsv_kbdltsv,"LTsv_deviceL")
    if len(LTsv_deviceL_page) > 0:
        LTsv_kbddevpath=LTsv_readlinerest(LTsv_deviceL_page,"kbd")
        LTsv_mousedevpath=LTsv_readlinerest(LTsv_deviceL_page,"mouse")
    if not os.path.exists(LTsv_kbddevpath):
        LTsv_kbddevpath=LTsv_defkbddevpath
    if not os.path.exists(LTsv_mousedevpath):
        LTsv_mousedevpath=LTsv_defmousedevpath
    LTsv_typenameW_page=LTsv_getpage(LTsv_kbdltsv,"LTsv_typenameW")
    if len(LTsv_typenameW_page) > 0:
        for LTsv_code in range(256):
            LTsv_typecodeW[LTsv_code]="${0:02x}".format(LTsv_code)
        LTsv_typenameW=LTsv_label2dictint(LTsv_typenameW_page)
        for LTsv_key,LTsv_value in list(LTsv_typenameW.items()):
            LTsv_typecodeW[LTsv_typenameW[LTsv_key]]=LTsv_key
    LTsv_typenameL_page=LTsv_getpage(LTsv_kbdltsv,"LTsv_typenameL")
    if len(LTsv_typenameL_page) > 0:
        for LTsv_code in range(256):
            LTsv_typecodeL[LTsv_code]="${0:02x}".format(LTsv_code)
        LTsv_typenameL=LTsv_label2dictint(LTsv_typenameL_page)
        for LTsv_key,LTsv_value in list(LTsv_typenameL.items()):
            LTsv_typecodeL[LTsv_typenameL[LTsv_key]]=LTsv_key
    LTsv_typegana_page=LTsv_getpage(LTsv_kbdltsv,"LTsv_typegana")
    if len(LTsv_typegana_page) > 0:
        for LTsv_code in range(256):
            LTsv_typekanaW[LTsv_code]=LTsv_typecodeW[LTsv_code]
            LTsv_typekanaL[LTsv_code]=LTsv_typecodeL[LTsv_code]
        LTsv_typegana=LTsv_label2dictstr(LTsv_typegana_page)
        for LTsv_key,LTsv_value in list(LTsv_typegana.items()):
            if LTsv_value in LTsv_typenameL:
                LTsv_typekanaL[LTsv_typenameL[LTsv_value]]=LTsv_key
            if LTsv_value in LTsv_typenameW:
                LTsv_typekanaW[LTsv_typenameW[LTsv_value]]=LTsv_key
    LTsv_mouse_EV_KEY_page=LTsv_getpage(LTsv_kbdltsv,"LTsv_mouse_EV_KEY")
    if len(LTsv_mouse_EV_KEY_page) > 0:
        LTsv_BTNnameL,LTsv_BTNcodeL=[],[]
        for LTsv_mouse_EV_KEY_num in range(LTsv_readlinedeno(LTsv_mouse_EV_KEY_page)):
            LTsv_mouse_EV_KEY_line=LTsv_readlinenum(LTsv_mouse_EV_KEY_page,LTsv_mouse_EV_KEY_num)
            LTsv_BTNnameL.append(str(LTsv_intstr0x(LTsv_split_label_data(LTsv_pickdatanum(LTsv_mouse_EV_KEY_line,0),True))))
            LTsv_BTNcodeL.append(LTsv_intstr0x(LTsv_split_label_data(LTsv_pickdatanum(LTsv_mouse_EV_KEY_line,1),True)))
    LTsv_BTNdic=dict(zip(LTsv_BTNnameL,LTsv_BTNcodeL))
    LTsv_keydefault_page=LTsv_getpage(LTsv_kbdltsv,"LTsv_keydefault")
    if len(LTsv_keydefault_page) > 0:
        LTsv_defkbdformat=LTsv_keydefault_page
    keyboard_iroha_page=LTsv_getpage(LTsv_kbdltsv,"keyboard_iroha")
    if len(keyboard_iroha_page) > 0:
        LTsv_keyboard_iroha=LTsv_joindatanum(keyboard_iroha_page,0,"").strip('\n').split('\t')
    keyboard_guideN_page=LTsv_getpage(LTsv_kbdltsv,"keyboard_guideN")
    if len(keyboard_guideN_page) > 0:
        LTsv_keyboard_guideN=LTsv_label2dictstr(keyboard_guideN_page)
    keyboard_guideX_page=LTsv_getpage(LTsv_kbdltsv,"keyboard_guideX")
    if len(keyboard_guideX_page) > 0:
        LTsv_keyboard_guideX=LTsv_label2dictstr(keyboard_guideX_page)
    keyboard_guideK_page=LTsv_getpage(LTsv_kbdltsv,"keyboard_guideK")
    if len(keyboard_guideK_page) > 0:
        LTsv_keyboard_guideK=LTsv_joindatanum(keyboard_guideK_page,0,"").strip('\n').split('\t')
    keyboard_guideKN_page=LTsv_getpage(LTsv_kbdltsv,"keyboard_guideKN")
    if len(keyboard_guideKN_page) > 0:
        LTsv_keyboard_guideKN=LTsv_label2dictstr(keyboard_guideKN_page)
    keyboard_guideKX_page=LTsv_getpage(LTsv_kbdltsv,"keyboard_guideKX")
    if len(keyboard_guideKX_page) > 0:
        LTsv_keyboard_guideKX=LTsv_label2dictstr(keyboard_guideKX_page)
    keyboard_findN_page=LTsv_getpage(LTsv_kbdltsv,"keyboard_findN")
    if len(keyboard_findN_page) > 0:
       LTsv_keyboard_findN=LTsv_label2dictstr(keyboard_findN_page)
       LTsv_keyboard_findNr={val:key for key,val in LTsv_keyboard_findN.items()}
    keyboard_findX_page=LTsv_getpage(LTsv_kbdltsv,"keyboard_findX")
    if len(keyboard_findX_page) > 0:
       LTsv_keyboard_findX=LTsv_label2dictstr(keyboard_findX_page)
       LTsv_keyboard_findXr={val:key for key,val in LTsv_keyboard_findX.items()}
    keyboard_mapdic_page=LTsv_getpage(LTsv_kbdltsv,"keyboard_mapdic")
    if len(keyboard_mapdic_page) > 0:
        tofuT=LTsv_readlinerest(keyboard_mapdic_page,"tofu")
        LTsv_keyboard_tofu='✖' if len(tofuT) == 0 else tofuT[0] if len(tofuT) >= 2 else tofuT
        keyboard_alphatypeT=LTsv_readlinerest(keyboard_mapdic_page,"alphatype")
        LTsv_keyboard_alphatype=LTsv_joindatanum(keyboard_alphatypeT,0,"").strip('\n').split('\t') if len(keyboard_alphatypeT) > 0 else keyboard_alphatype
        keyboard_dictypeT=LTsv_readlinerest(keyboard_mapdic_page,"dictype")
        LTsv_keyboard_dictype=LTsv_joindatanum(keyboard_dictypeT,0,"").strip('\n').split('\t') if len(keyboard_dictypeT) > 0 else keyboard_dictype
        keyboard_kanmapT=LTsv_loadfile(LTsv_tsvdir+LTsv_readlinerest(keyboard_mapdic_page,"mapname"))
        LTsv_keyboard_guide=LTsv_keyboard_guideN.keys()
        for keyboard_guide in LTsv_keyboard_guide:
            keyboard_lineT=LTsv_readlinerest(keyboard_kanmapT,keyboard_guide)
            keyboard_line=keyboard_lineT.split('\t'); keyboard_line=keyboard_line+[" "]*(LTsv_keyboard_alphapos*2-len(keyboard_line))
            keyboard_line=[(char if len(char) else " ") for char in keyboard_line]
            LTsv_keyboard_kanmapN[keyboard_guide]=keyboard_line[:LTsv_keyboard_alphapos]
            LTsv_keyboard_kanmapX[keyboard_guide]=keyboard_line[LTsv_keyboard_alphapos:LTsv_keyboard_alphapos*2]
        LTsv_keyboard_kanmapN["　"],LTsv_keyboard_kanmapX["　"]=LTsv_keyboard_kanmapN[LTsv_keyboard_alphatype[0]],LTsv_keyboard_kanmapX[LTsv_keyboard_alphatype[0]]
        LTsv_keyboard_guideN["　"],LTsv_keyboard_guideX["　"]=LTsv_keyboard_guideN[LTsv_keyboard_alphatype[0]],LTsv_keyboard_guideX[LTsv_keyboard_alphatype[0]]
        LTsv_keyboard_kandic=LTsv_loadfile(LTsv_tsvdir+LTsv_readlinerest(keyboard_mapdic_page,"dicname"),LTsv_keyboard_kandic)

def LTsv_kbdgettypename(LTsv_code):
    LTsv_name=""
    LTsv_codeff=LTsv_code if 0 <= LTsv_code <=0xff else 0
    if sys.platform.startswith("win"):
        LTsv_name=LTsv_typecodeW[LTsv_codeff]
    if sys.platform.startswith("linux"):
        LTsv_name=LTsv_typecodeL[LTsv_codeff]
    return LTsv_name

def LTsv_kbdgettypekana(LTsv_code):
    LTsv_name=""
    LTsv_codeff=LTsv_code if 0 <= LTsv_code <=0xff else 0
    if sys.platform.startswith("win"):
        LTsv_name=LTsv_typekanaW[LTsv_codeff]
    if sys.platform.startswith("linux"):
        LTsv_name=LTsv_typekanaL[LTsv_codeff]
    return LTsv_name

def LTsv_kbdgettypecode(LTsv_name):
    LTsv_code=0
    if sys.platform.startswith("win"):
        if LTsv_name in LTsv_typenameW:
            LTsv_code=LTsv_typenameW[LTsv_name]
    if sys.platform.startswith("linux"):
        if LTsv_name in LTsv_typenameL:
            LTsv_code=LTsv_typenameL[LTsv_name]
    return LTsv_code

def LTsv_kbdgettypegana(LTsv_gana):
    LTsv_code=LTsv_kbdgettypecode(LTsv_typegana[LTsv_gana] if LTsv_gana in LTsv_typegana else LTsv_gana)
    return LTsv_code

def LTsv_kbdexit():
    global LTsv_kbddevpath,LTsv_kbdhands,LTsv_mousedevpath,LTsv_mousehands
    for LTsv_code in range(256):
        LTsv_kbdkeep[LTsv_code]=0
    if sys.platform.startswith("win"):
        pass
    if sys.platform.startswith("linux"):
        if LTsv_kbdhands != None:
            try:
                os.close(LTsv_kbdhands); LTsv_kbdhands=None
            except OSError as err:
                print("OSError({0}):{1}".format(err.errno,err.strerror))
        if LTsv_mousehands != None:
            try:
                os.close(LTsv_mousehands); LTsv_mousehands=None
            except OSError as err:
                print("OSError({0}):{1}".format(err.errno,err.strerror))

def LTsv_kbdinit(LTsv_tsvpath="LTsv/LTsv_kbd.tsv",LTsv_initmouse=False):
    global LTsv_kbddevpath,LTsv_kbdhands,LTsv_mousedevpath,LTsv_mousehands
    LTsv_kbdexit()
    LTsv_kbdreset(LTsv_tsvpath)
    if sys.platform.startswith("win"):
        pass
    if sys.platform.startswith("linux"):
        try:
            LTsv_kbdhands=os.open(LTsv_kbddevpath,os.O_RDWR|os.O_NONBLOCK)
        except OSError as err:
            print("LTsv_kbdhands,OSError({0}):{1}".format(err.errno,err.strerror))
        if LTsv_initmouse:
            try:
                LTsv_mousehands=os.open(LTsv_mousedevpath,os.O_RDWR|os.O_NONBLOCK)
            except OSError as err:
                print("LTsv_mousehands,OSError({0}):{1}".format(err.errno,err.strerror))

def LTsv_kbdEVIOCGRAB(LTsv_grabflag):
    global LTsv_grabflagdef,LTsv_kbddevpath,LTsv_kbdhands,LTsv_WINDOWSHOOK_Class
    if sys.platform.startswith("win"):
        pass
#        print("win;LTsv_kbdEVIOCGRAB")
#        LTsv_WINDOWSHOOK_Class=LTsv_WINDOWSHOOK() if LTsv_grabflag !=0 else None
    if sys.platform.startswith("linux"):
        if LTsv_kbdhands != 0:
            LTsv_grabflag=1 if LTsv_grabflag else 0
            if LTsv_grabflagdef != LTsv_grabflag:
                LTsv_grabflagdef = LTsv_grabflag
                fcntl.ioctl(LTsv_kbdhands,LTsv_EVIOCGRAB,LTsv_grabflag)

def LTsv_kbdwrite(LTsv_code,LTsv_value):
    global LTsv_kbdhands,LTsv_INPUTEVENT,LTsv_timeval
    if sys.platform.startswith("win"):
        pass
    if sys.platform.startswith("linux"):
        if LTsv_kbdhands != 0 and LTsv_code != 0:
            LTsv_kbdeve,LTsv_kbdtim=LTsv_INPUTEVENT,LTsv_timeval
            LTsv_meridian_now=datetime.datetime.now()
            LTsv_kbdtim.tv_sec,LTsv_kbdtim.tv_usec=LTsv_meridian_now.second,LTsv_meridian_now.microsecond
            LTsv_kbdeve.time,LTsv_kbdeve.type,LTsv_kbdeve.code,LTsv_kbdeve.value=LTsv_kbdtim,LTsv_EV_KEY,min(max(LTsv_code,0),255),min(max(LTsv_value,0),1)
            LTsv_kbdeve_pack=bytearray([])
#            LTsv_kbdeve_pack.extend(struct.pack("Q",Tsv_kbdtim))
            LTsv_kbdeve_pack.extend(struct.pack("L",LTsv_kbdtim.tv_sec))
            LTsv_kbdeve_pack.extend(struct.pack("L",LTsv_kbdtim.tv_usec))
            LTsv_kbdeve_pack.extend(struct.pack("h",LTsv_kbdeve.type))
            LTsv_kbdeve_pack.extend(struct.pack("h",LTsv_kbdeve.code))
            LTsv_kbdeve_pack.extend(struct.pack("L",LTsv_kbdeve.value))
            os.write(LTsv_kbdhands,LTsv_kbdeve_pack)

def LTsv_kbdwriteCtrl(LTsv_ganastsv):
    LTsv_ganas=LTsv_ganastsv.split('\t') if len(LTsv_ganastsv) > 0 else []
    for LTsv_gana in LTsv_ganas:
        LTsv_kbdwrite(LTsv_kbdgettypegana(LTsv_gana),0)
        LTsv_kbdwrite(LTsv_kbdgettypegana(LTsv_gana),1)
    for LTsv_gana in reversed(LTsv_ganas):
        LTsv_kbdwrite(LTsv_kbdgettypegana(LTsv_gana),0)

def LTsv_setkbddata(LTsv_kbdstacks,LTsv_mousestacks):
    global LTsv_kbddevpath,LTsv_kbdhands,LTsv_mousedevpath,LTsv_mousehands
    if sys.platform.startswith("win"):
        for LTsv_code in range(256):
            LTsv_kbdkeep[LTsv_code]=1 if LTsv_user32.GetAsyncKeyState(LTsv_code)!=0 else 0
    if sys.platform.startswith("linux"):
        LTsv_kbdbyte=""
        LTsv_kbdeve=LTsv_INPUTEVENT
        for LTsv_stack in range(LTsv_kbdstacks):
            try:
                LTsv_kbdbyte=os.read(LTsv_kbdhands,ctypes.sizeof(LTsv_INPUTEVENT))
            except OSError as err:
#                print("LTsv_setkbddata,OSError({0}):{1}".format(err.errno,err.strerror))
                break
            if LTsv_kbdbyte:
                LTsv_kbdeve.time,LTsv_kbdeve.type,LTsv_kbdeve.code,LTsv_kbdeve.value=struct.unpack(LTsv_INPUTEVENT_unpack,LTsv_kbdbyte)
                if LTsv_kbdeve.type == LTsv_EV_KEY:
                    LTsv_kbdkeep[LTsv_kbdeve.code]=LTsv_kbdeve.value
        LTsv_mousebyte=""
        LTsv_mouseve=LTsv_INPUTEVENT
        for LTsv_stack in range(LTsv_mousestacks) if LTsv_mousehands != None else range(0):
            try:
                LTsv_mousebyte=os.read(LTsv_mousehands,ctypes.sizeof(LTsv_INPUTEVENT))
            except OSError as err:
                print("LTsv_setkbddata,OSError({0}):{1}".format(err.errno,err.strerror))
                break
            if LTsv_mousebyte:
                LTsv_mouseve.time,LTsv_mouseve.type,LTsv_mouseve.code,LTsv_mouseve.value=struct.unpack(LTsv_INPUTEVENT_unpack,LTsv_mousebyte)
                if LTsv_mouseve.type == LTsv_EV_KEY:
                    if str(LTsv_mouseve.code) in LTsv_BTNnameL:
                        LTsv_kbdkeep[LTsv_BTNdic[str(LTsv_mouseve.code)]]=LTsv_kbdeve.value
                if LTsv_mouseve.type == LTsv_EV_REL:
                    pass
                if LTsv_mouseve.type == LTsv_EV_ABS:
                    pass
    return LTsv_kbdkeep

def LTsv_getkbdlabels(kbdformat=LTsv_defkbdformat):
    LTsv_splits=kbdformat.split('\t'); LTsv_codes=""
    if sys.platform.startswith("win"):
        for LTsv_gana in LTsv_splits:
            LTsv_name=LTsv_typegana[LTsv_gana] if LTsv_gana in LTsv_typegana else LTsv_gana
            LTsv_code=LTsv_typenameW[LTsv_name] if LTsv_name in LTsv_typenameW else 0
            LTsv_codes+=LTsv_gana+':'+str(LTsv_kbdkeep[LTsv_code])+'\t'
    if sys.platform.startswith("linux"):
        for LTsv_gana in LTsv_splits:
            LTsv_name=LTsv_typegana[LTsv_gana] if LTsv_gana in LTsv_typegana else LTsv_gana
            LTsv_code=LTsv_typenameL[LTsv_name] if LTsv_name in LTsv_typenameL else 0
            LTsv_codes+=LTsv_gana+':'+str(LTsv_kbdkeep[LTsv_code])+'\t'
    return LTsv_codes.rstrip('\t')

def LTsv_getkbdnames():
    LTsv_names=""
    if sys.platform.startswith("win"):
        for LTsv_name in LTsv_typenameW:
            if LTsv_kbdkeep[LTsv_typenameW[LTsv_name]]:
                LTsv_names+=LTsv_name+'\t'
    if sys.platform.startswith("linux"):
        for LTsv_name in LTsv_typenameL:
            if LTsv_kbdkeep[LTsv_typenameL[LTsv_name]]:
                LTsv_names+=LTsv_name+'\t'
    return LTsv_names.rstrip('\t')

def LTsv_getkbdcodes():
    LTsv_names=""
    if sys.platform.startswith("win"):
        for LTsv_code in range(256):
            if LTsv_kbdkeep[LTsv_code]:
                LTsv_names+="${0:02x}\t".format(LTsv_code)
    if sys.platform.startswith("linux"):
        for LTsv_code in range(256):
            if LTsv_kbdkeep[LTsv_code]:
                LTsv_names+="${0:02x}\t".format(LTsv_code)
    return LTsv_names.rstrip('\t')

def LTsv_getkbdkanas():
    LTsv_kanas=""
    if sys.platform.startswith("win"):
        for LTsv_key,LTsv_value in list(LTsv_typegana.items()):
            if LTsv_kbdkeep[LTsv_typenameW[LTsv_value]]:
                LTsv_kanas+=LTsv_key+'\t'
    if sys.platform.startswith("linux"):
        for LTsv_key,LTsv_value in list(LTsv_typegana.items()):
            if LTsv_kbdkeep[LTsv_typenameL[LTsv_value]]:
                LTsv_kanas+=LTsv_key+'\t'
    return LTsv_kanas.rstrip('\t')

def LTsv_keyboard_iroha_guide():
    return LTsv_keyboard_irohamax,LTsv_keyboard_alphapos,LTsv_keyboard_guidepos,LTsv_keyboard_dicinppos,LTsv_keyboard_dicselpos,LTsv_keyboard_iroha,LTsv_keyboard_guideN,LTsv_keyboard_guideX,LTsv_keyboard_guideK,LTsv_keyboard_guideKN,LTsv_keyboard_guideKX

def LTsv_keyboard_iroha_type():
    return LTsv_keyboard_irohatype,LTsv_keyboard_alphatype,LTsv_keyboard_dictype,LTsv_keyboard_tofu

def LTsv_keyboard_map(kanmapN=None,kanmapX=None,dicinput=None):
    global LTsv_keyboard_kanmapN,LTsv_keyboard_kanmapX,LTsv_keyboard_dicinput
    LTsv_keyboard_kanmapN=LTsv_keyboard_kanmapN     if kanmapN  == None else kanmapN
    LTsv_keyboard_kanmapX=LTsv_keyboard_kanmapX     if kanmapX  == None else kanmapX
    LTsv_keyboard_dicinput=LTsv_keyboard_dicinput   if dicinput == None else dicinput
    return LTsv_keyboard_kanmapN,LTsv_keyboard_kanmapX,LTsv_keyboard_dicinput

def LTsv_keyboard_dic(kandic=None):
    global LTsv_keyboard_kandic
    LTsv_keyboard_kandic=LTsv_keyboard_kandic   if kandic == None else kandic
    return LTsv_keyboard_kandic

def LTsv_keyboard_NXK(cursorMS=None,cursorIR=None,cursorAF=None,cursorOLD=None,cursorDIC=None,cursorNX=None,cursorK=None,cursorLCR=None):
    global LTsv_keyboard_cursorMS,LTsv_keyboard_cursorIR,LTsv_keyboard_cursorAF,LTsv_keyboard_cursorOLD,LTsv_keyboard_cursorDIC,LTsv_keyboard_cursorNX,LTsv_keyboard_cursorK,LTsv_keyboard_cursorLCR
    LTsv_keyboard_cursorMS=LTsv_keyboard_cursorMS   if cursorMS  == None else cursorMS
    LTsv_keyboard_cursorIR=LTsv_keyboard_cursorIR   if cursorIR  == None else cursorIR
    LTsv_keyboard_cursorAF=LTsv_keyboard_cursorAF   if cursorAF  == None else cursorAF
    LTsv_keyboard_cursorOLD=LTsv_keyboard_cursorOLD if cursorOLD == None else cursorOLD
    LTsv_keyboard_cursorDIC=LTsv_keyboard_cursorDIC if cursorDIC == None else cursorDIC
    LTsv_keyboard_cursorNX=LTsv_keyboard_cursorNX   if cursorNX  == None else cursorNX
    LTsv_keyboard_cursorK=LTsv_keyboard_cursorK     if cursorK   == None else cursorK
    LTsv_keyboard_cursorLCR=LTsv_keyboard_cursorLCR if cursorLCR == None else cursorLCR
    return LTsv_keyboard_cursorMS,LTsv_keyboard_cursorIR,LTsv_keyboard_cursorAF,LTsv_keyboard_cursorOLD,LTsv_keyboard_cursorDIC,LTsv_keyboard_cursorNX,LTsv_keyboard_cursorK,LTsv_keyboard_cursorLCR

def LTsv_keyboard_findNX():
    global LTsv_keyboard_findN,LTsv_keyboard_findX,LTsv_keyboard_findNr,LTsv_keyboard_findXr
    return LTsv_keyboard_findN,LTsv_keyboard_findX,LTsv_keyboard_findNr,LTsv_keyboard_findXr


if __name__=="__main__":
    from LTsv_printf import *
    from LTsv_file   import *
    print("__main__ Python{0.major}.{0.minor}.{0.micro},{1},{2}".format(sys.version_info,sys.platform,sys.stdout.encoding))
    print("")
    LTsv_libc_printcat("\nLTsv_kbdgettypename()")
    for col in range(256):
        LTsv_libc_printcat("{0}{1}".format(',' if col%16 !=0 else '\n',LTsv_kbdgettypename(col)))
    LTsv_libc_printcat("\nLTsv_kbdgettypekana()")
    for col in range(256):
        LTsv_libc_printcat("{0}{1}".format(',' if col%16 !=0 else '\n',LTsv_kbdgettypekana(col)))
    LTsv_libc_printcat("\nLTsv_kbdgettypecode()")
    for col,val in enumerate(LTsv_typenameL):
        LTsv_libc_printcat("{0}{1}:{2}".format(',' if col%16 !=0 else '\n',val,LTsv_kbdgettypecode(val)))
    LTsv_libc_printcat("\nLTsv_kbdgettypegana()")
    for col,val in enumerate(LTsv_typegana.keys()):
        LTsv_libc_printcat("{0}{1}:{2}".format(',' if col%16 !=0 else '\n',val,LTsv_kbdgettypegana(val)))
    print("")
    LTsv_kbdinit()
    print("LTsv_kbdinit()")
    LTsv_kbdEVIOCGRAB(10)
    for j in range(10):
        LTsv_setkbddata(25,0)
        LTsv_kf=LTsv_getkbdlabels().replace('\t',' ').replace('た','\nた').replace('ち','\nち').replace('つ','\nつ').replace('NFER','\nNFER')
        LTsv_libc_printf("\n{0}".format(LTsv_kf))
        LTsv_libc_printf("LTsv_getkbdnames()={0}".format(LTsv_getkbdnames().replace('\t',',')))
        LTsv_libc_printf("LTsv_getkbdcodes()={0}".format(LTsv_getkbdcodes().replace('\t',',')))
        LTsv_libc_printf("LTsv_getkbdkanas()={0}".format(LTsv_getkbdkanas().replace('\t',',')))
        time.sleep(0.2)
    LTsv_kbdEVIOCGRAB(0)
    print("")
    print("__main__",LTsv_file_ver())


# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv9kantray/blob/master/LICENSE
