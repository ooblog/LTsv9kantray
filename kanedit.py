#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import os
os.chdir(sys.path[0])
sys.path.append("LTsv")
from LTsv_printf import *
from LTsv_file   import *
from LTsv_time   import *
from LTsv_calc   import *
#from LTsv_joy    import *
from LTsv_kbd    import *
from LTsv_gui    import *

tinykbd_W,tinykbd_H=24*4,24
tinykbd_inputSandS,tinykbd_inputNFER,tinykbd_inputXFER,tinykbd_inputKANA="Space","NFER","XFER","KANA"
tinykbd_irohatype= ["ぬ","ふ","あ","う","え","お","や","ゆ","よ","わ","ほ","へ","た","て","い","す","か","ん","な","に","ら","せ","゛","゜","ち","と","し","は","き","く","ま","の","り","れ","け","む","つ","さ","そ","ひ","こ","み","も","ね","る","め","ろ","￥"]
tinykbd_irohatypeN=["ぬ","ふ","あ","う","え","お","や","ゆ","よ","わ","ほ","へ","た","て","い","す","か","ん","な","に","ら","せ","＠","ぷ","ち","と","し","は","き","く","ま","の","り","れ","け","む","つ","さ","そ","ひ","こ","み","も","ね","る","め","ろ","￥"]
tinykbd_irohatypeX=["ヌ","フ","ア","ウ","エ","オ","ヤ","ユ","ヨ","ワ","ホ","ヘ","タ","テ","イ","ス","カ","ン","ナ","ニ","ラ","セ","｀","プ","チ","ト","シ","ハ","キ","ク","マ","ノ","リ","レ","ケ","ム","ツ","サ","ソ","ヒ","コ","ミ","モ","ネ","ル","メ","ロ","｜"]
tinykbd_choiceN=   ["名","音","訓","送","異","俗","簡","繁","越","地","逆","非","英","顔","ε","ρ","τ","υ","θ","ι","ο","π","＠","ぷ","α","σ","δ","φ","γ","η","ξ","κ","λ","代","鍵","ぬ","ζ","χ","ψ","ω","β","ν","μ","熙","○","△","□","￥","σ"]
tinykbd_choiceX=   ["名","音","訓","送","異","俗","簡","繁","越","地","逆","非","英","顔","Ε","Ρ","Τ","Υ","Θ","Ι","Ο","Π","｀","プ","Α","Σ","Δ","Φ","Γ","Η","Ξ","Κ","Λ","代","鍵","ぬ","Ζ","Χ","Ψ","Ω","Β","Ν","Μ","熙","○","△","□","￥","Σ"]
tinykbd_alphatype= ["α","β","γ","δ","ε","ζ","η","θ","ι","κ","λ","μ","ν","ξ","ο","π","ρ","σ","τ","υ","φ","χ","ψ","ω","○","△","□"]
tinykbd_alphatypeN=["α","β","γ","δ","ε","ζ","η","θ","ι","κ","λ","μ","ν","ξ","ο","π","ρ","σ","τ","υ","φ","χ","ψ","ω","○","△","□"]
tinykbd_alphatypeX=["Α","Β","Γ","Δ","Ε","Ζ","Η","Θ","Ι","Κ","Λ","Μ","Ν","Ξ","Ο","Π","Ρ","Σ","Τ","Υ","Φ","Χ","Ψ","Ω","●","▲","■"]
tinykbd_irohaalpha=tinykbd_irohatype+tinykbd_alphatype
tinykbd_dictype=    ["英","名","音","訓","送","異","俗","熙","簡","繁","越","地","顔","鍵","代","逆","非","難","活","幅"]
tinykbd_map,tinykbd_char,tinykbd_word,tinykbd_zip="","","",""
tinykbd_kanmapN,tinykbd_kanmapX,tinykbd_kanmapD={},{},{}
#tinykbd_kanmapchoice=tinykbd_irohatype[0]
tinykbd_fontcolor,tinykbd_bgcolor="black","#CFE6CF"
tinykbd_fontsize,tinykbd_fontspace,tinykbd_fonthalf=5,6,3
tinykbd_menusize,tinykbd_menuspace,tinykbd_menuhalf=10,12,6
tinykbd_irohamax=12*4; tinykbd_SandS,tinykbd_NFER,tinykbd_XFER,tinykbd_KANA,tinykbd_None=48,49,50,51,52
tinykbd_cursorMSbf,tinykbd_cursorMSaf,tinykbd_cursorLCR,tinykbd_cursorTSF=tinykbd_None,tinykbd_None,"000",{"000":"Tap","100":"Tap","010":"Swipe","001":"Flick"}
tinykbd_fontX,tinykbd_fontY,tinykbd_spaceX,tinykbd_spaceY=[0]*(tinykbd_None),[0]*(tinykbd_None),[0]*(tinykbd_None),[0]*(tinykbd_None)
tinykbd_fontchar=[""]*(tinykbd_None); tinykbd_fontchar[tinykbd_SandS],tinykbd_fontchar[tinykbd_NFER],tinykbd_fontchar[tinykbd_XFER],tinykbd_fontchar[tinykbd_KANA]="地","Ｎ","Ｘ",tinykbd_irohatype[0]

def kanedit_tinykbd_new():
    global keyboard_irohamax,keyboard_alphapos,keyboard_guidepos,keyboard_dicinppos,keyboard_dicselpos,keyboard_iroha,keyboard_guideN,keyboard_guideX,keyboard_guideK,keyboard_guideKN,keyboard_guideKX
    global keyboard_irohatype,keyboard_alphatype,keyboard_dictype,keyboard_tofu
    global tinykbd_fontX,tinykbd_fontY,tinykbd_spaceX,tinykbd_spaceY
    global tinykbd_fontchar
    tinykbd_fontX[tinykbd_SandS],tinykbd_fontY[tinykbd_SandS]=1,tinykbd_menuspace+1
    tinykbd_fontX[tinykbd_NFER],tinykbd_fontY[tinykbd_NFER]=1,1
    tinykbd_fontX[tinykbd_XFER],tinykbd_fontY[tinykbd_XFER]=1+tinykbd_fontspace*12+tinykbd_menuspace,1
    tinykbd_fontX[tinykbd_KANA],tinykbd_fontY[tinykbd_KANA]=1+tinykbd_fontspace*12+tinykbd_menuspace,tinykbd_menuspace+1
    for kbd_xy in range(tinykbd_irohamax):
        tinykbd_fontX[kbd_xy],tinykbd_fontY[kbd_xy]=tinykbd_fontspace*(kbd_xy%12)+tinykbd_menuspace,tinykbd_fontspace*(kbd_xy//12)+1
        tinykbd_spaceX[kbd_xy],tinykbd_spaceY[kbd_xy]=tinykbd_fontX[kbd_xy]+tinykbd_fonthalf,tinykbd_fontY[kbd_xy]+tinykbd_fonthalf
    for kbd_xy in range(tinykbd_irohamax,tinykbd_None):
        tinykbd_spaceX[kbd_xy],tinykbd_spaceY[kbd_xy]=tinykbd_fontX[kbd_xy]+tinykbd_menuhalf,tinykbd_fontY[kbd_xy]+tinykbd_menuhalf

kanedit_getkbdnames,kanedit_getkbdkanas="",""
kanedit_W,kanedit_H,kanedit_RS=tinykbd_W,tinykbd_H,False
kanedit_ltsv,kanedit_config="",""
kanedit_fontcolor,kanedit_bgcolor,kanedit_fontsize="black","#FFF3F5",10
kanedit_texteditvalue,kanedit_texteditlines="",[]
kanedit_texteditcursor=0

def kanedit_kbddraw(kbd_x,kbd_y):
    global keyboard_kanmapN,keyboard_kanmapX,keyboard_dicinput
    keyboard_kanmapN,keyboard_kanmapX,keyboard_dicinput=LTsv_keyboard_map()
    LTsv_drawtk_color(kanedit_fontcolor);     LTsv_drawtk_glyphfill(kanedit_getkbdnames,draw_x=0,draw_y=kbd_y+1,draw_f=10,draw_w=1,draw_h=1)
    LTsv_drawtk_color(kanedit_fontcolor);     LTsv_drawtk_glyphfill(str(tinykbd_cursorMSaf),draw_x=0,draw_y=kbd_y+13,draw_f=10,draw_w=1,draw_h=1)
    LTsv_drawtk_color(tinykbd_bgcolor); LTsv_drawtk_polygonfill(kbd_x,kbd_y,kbd_x+tinykbd_W,kbd_y,kbd_x+tinykbd_W,kbd_y+tinykbd_H,kbd_x,kbd_y+tinykbd_H)
    LTsv_drawtk_bgcolor(tinykbd_bgcolor); LTsv_drawtk_color(tinykbd_fontcolor)
    for kbd_xy in range(tinykbd_irohamax):
        LTsv_drawtk_glyphfill(tinykbd_fontchar[kbd_xy],draw_x=kbd_x+tinykbd_fontX[kbd_xy],draw_y=kbd_y+tinykbd_fontY[kbd_xy],draw_f=tinykbd_fontsize)
    for kbd_xy in range(tinykbd_irohamax,tinykbd_None):
        LTsv_drawtk_glyphfill(tinykbd_fontchar[kbd_xy],draw_x=kbd_x+tinykbd_fontX[kbd_xy],draw_y=kbd_y+tinykbd_fontY[kbd_xy],draw_f=tinykbd_menusize)

def kanedit_redraw():
    global kanedit_getkbdnames,kanedit_getkbdkanas
    global kanedit_fontcolor,kanedit_bgcolor,kanedit_fontsize
    LTsv_drawtk_selcanvas(kanedit_canvas); LTsv_drawtk_delete(kanedit_bgcolor)
    LTsv_drawtk_color(kanedit_bgcolor); LTsv_drawtk_polygonfill(0,0,kanedit_W,0,kanedit_W,kanedit_H,0,kanedit_H)
    LTsv_drawtk_color(kanedit_fontcolor); LTsv_drawtk_glyphfill(kanedit_texteditvalue,draw_x=5,draw_y=5,draw_f=kanedit_fontsize,draw_w=1,draw_h=1)
    kanedit_kbddraw(kanedit_W-tinykbd_W,kanedit_H-tinykbd_H)
    LTsv_drawtk_queue()

def kanedit_resizeredraw(window_objvoid=None,window_objptr=None):
    global kanedit_W,kanedit_H,kanedit_RS
    window_w,window_h=LTsv_window_wh(kanedit_window)
    if kanedit_W!=window_w or kanedit_H!=window_h:
        kanedit_W,kanedit_H=window_w,window_h
        kanedit_redraw()
        LTsv_window_after(kanedit_window,event_b=kanedit_resizeredraw,event_i="kanedit_resizeredraw",event_w=50)
    else:
        kanedit_W,kanedit_H=window_w,window_h
        kanedit_RS=False

def kanedit_resize(callback_void=None,callback_ptr=None):
    global kanedit_W,kanedit_H,kanedit_RS
    if kanedit_RS == False:
        kanedit_RS=True
        kanedit_resizeredraw()

def kanedit_tinykbd_select(choice):
    global tinykbd_fontchar
    choiceNX=choice
    if choice in tinykbd_irohatypeN:
        choiceNX=tinykbd_irohatype[tinykbd_irohatypeN.index(choice)]
        tinykbd_fontchar[0:tinykbd_irohamax]=tinykbd_kanmapN[choiceNX][0:tinykbd_irohamax]
    if choice in tinykbd_irohatypeX:
        choiceNX=tinykbd_irohatype[tinykbd_irohatypeX.index(choice)]
        tinykbd_fontchar[0:tinykbd_irohamax]=tinykbd_kanmapX[choiceNX][0:tinykbd_irohamax]

def kanedit_inputchar(choice,kbd_xy):
    global kanedit_texteditvalue
    if choice in tinykbd_irohatypeN:
        kanedit_texteditvalue+=tinykbd_kanmapN[tinykbd_irohatype[tinykbd_irohatypeN.index(choice)]][kbd_xy]
    if choice in tinykbd_irohatypeX:
        kanedit_texteditvalue+=tinykbd_kanmapX[tinykbd_irohatype[tinykbd_irohatypeX.index(choice)]][kbd_xy]

def kanedit_mousecursor():
    global tinykbd_cursorMSbf,tinykbd_cursorMSaf,tinykbd_cursorLCR,tinykbd_cursorTSF
    tinykbd_cursorMSbf=tinykbd_cursorMSaf; tinykbd_cursorMSaf=tinykbd_None
    mouseX,mouseY=LTsv_global_canvasmotionX(),LTsv_global_canvasmotionY()
    kbd_x,kbd_y=kanedit_W-tinykbd_W,kanedit_H-tinykbd_H
    for kbd_xy in range(tinykbd_irohamax):
        if abs(kbd_x+tinykbd_spaceX[kbd_xy]-mouseX) <= tinykbd_fonthalf and abs(kbd_y+tinykbd_spaceY[kbd_xy]-mouseY) <= tinykbd_fonthalf:
            tinykbd_cursorMSaf=kbd_xy
    for kbd_xy in range(tinykbd_irohamax,tinykbd_None):
        if abs(kbd_x+tinykbd_spaceX[kbd_xy]-mouseX) <= tinykbd_menuhalf and abs(kbd_y+tinykbd_spaceY[kbd_xy]-mouseY) <= tinykbd_menuhalf:
            tinykbd_cursorMSaf=kbd_xy
    return tinykbd_cursorMSaf

def kanedit_mousepress(window_objvoid=None,window_objptr=None):
    global tinykbd_cursorMSbf,tinykbd_cursorMSaf,tinykbd_cursorLCR,tinykbd_cursorTSF
    tinykbd_cursorMSaf=kanedit_mousecursor()
    global kanedit_getkbdnames,kanedit_getkbdkanas
    LTsv_setkbddata(10,10); kanedit_getmouse=LTsv_getkbdlabels("MouseL\tMouseR\tMouseC")
    tinykbd_cursorLCR="{0}{1}{2}".format(LTsv_pickdatalabel(kanedit_getmouse,"MouseL"),LTsv_pickdatalabel(kanedit_getmouse,"MouseC"),LTsv_pickdatalabel(kanedit_getmouse,"MouseR"))
    LTsv_libc_printf("kanedit_mousepress「{0}」".format(tinykbd_cursorLCR))
    if tinykbd_cursorLCR in tinykbd_cursorTSF:
        tinykbd_cursorLCR=tinykbd_cursorTSF[tinykbd_cursorLCR]
    if tinykbd_cursorMSaf == tinykbd_SandS:
        tinykbd_cursorLCR="Flick"
    if tinykbd_cursorMSaf == tinykbd_NFER:
        tinykbd_cursorLCR="SwipeN"
    if tinykbd_cursorMSaf == tinykbd_XFER:
        tinykbd_cursorLCR="SwipeX"
    if tinykbd_cursorMSaf == tinykbd_KANA:
        tinykbd_cursorLCR="SwipeK"
    if tinykbd_cursorLCR == "Tap":
        if tinykbd_cursorMSaf < tinykbd_None:
#            kanedit_inputchar(tinykbd_kanmapchoice,tinykbd_cursorMSaf)
            kanedit_inputchar(tinykbd_fontchar[tinykbd_KANA],tinykbd_cursorMSaf)
    if tinykbd_cursorLCR == "SwipeN":
        pass
    if tinykbd_cursorLCR == "SwipeX":
        pass
    if tinykbd_cursorLCR == "SwipeK":
        kanedit_tinykbd_select("α")
    if tinykbd_cursorLCR == "Flick":
        pass
    kanedit_redraw()

def kanedit_mousemotion(window_objvoid=None,window_objptr=None):
    tinykbd_cursorMSaf=kanedit_mousecursor()
    if tinykbd_cursorMSaf < tinykbd_irohamax:
        if tinykbd_cursorLCR == "SwipeN":
            tinykbd_fontchar[tinykbd_KANA]=tinykbd_irohatypeN[tinykbd_cursorMSaf]
        if tinykbd_cursorLCR == "SwipeX":
            tinykbd_fontchar[tinykbd_KANA]=tinykbd_irohatypeX[tinykbd_cursorMSaf]
        if tinykbd_cursorMSbf != tinykbd_cursorMSaf:
            kanedit_tinykbd_select(tinykbd_fontchar[tinykbd_KANA])
            kanedit_redraw()

def kanedit_mouserelease(window_objvoid=None,window_objptr=None):
    global tinykbd_cursorMSbf,tinykbd_cursorMSaf,tinykbd_cursorLCR,tinykbd_cursorTSF
    tinykbd_cursorMSaf=kanedit_mousecursor()
    if tinykbd_cursorLCR == "SwipeK":
        kanedit_tinykbd_select(tinykbd_fontchar[tinykbd_KANA])
    tinykbd_cursorLCR=""
    kanedit_redraw()
    LTsv_libc_printf("kanedit_mouserelease「{0}」「{1}」".format(kanedit_getkbdnames,kanedit_getkbdkanas))

def kanedit_keypress(window_objvoid=None,window_objptr=None):
    global kanedit_getkbdnames,kanedit_getkbdkanas
    LTsv_setkbddata(10,0)
    kanedit_getkbdnames,kanedit_getkbdkanas=LTsv_getkbdnames(),LTsv_getkbdkanas()
    if kanedit_getkbdkanas in tinykbd_irohatype:
#        kanedit_inputchar(tinykbd_kanmapchoice,tinykbd_irohatype.index(kanedit_getkbdkanas))
        kanedit_inputchar(tinykbd_fontchar[tinykbd_KANA],tinykbd_irohatype.index(kanedit_getkbdkanas))
    kanedit_redraw()
    LTsv_libc_printf("kanedit_keypress「{0}」「{1}」".format(kanedit_getkbdnames,kanedit_getkbdkanas))

def kanedit_keyrelease(window_objvoid=None,window_objptr=None):
    global kanedit_getkbdnames,kanedit_getkbdkanas
    if kanedit_getkbdnames == "Space":
#        kanedit_inputchar(tinykbd_kanmapchoice,tinykbd_SandS)
        kanedit_inputchar(tinykbd_fontchar[tinykbd_KANA],tinykbd_SandS)
    LTsv_setkbddata(10,0)
    kanedit_redraw()
    LTsv_libc_printf("kanedit_keypress「{0}」「{1}」".format(kanedit_getkbdnames,kanedit_getkbdkanas))

def kanedit_textload(filename):
    global kanedit_texteditvalue
    kanedit_texteditvalue=LTsv_loadfile(filename)

def kanedit_configload():
    global kanedit_fontcolor,kanedit_bgcolor,kanedit_fontsize
    global kanedit_ltsv,kanedit_config
    global tinykbd_map,tinykbd_char,tinykbd_word,tinykbd_zip
    global tinykbd_kanmapN,tinykbd_kanmapX,tinykbd_kanmapD
    global tinykbd_fontcolor,tinykbd_bgcolor
    kanedit_ltsv=LTsv_loadfile("kanedit.tsv")
    kanedit_config=LTsv_getpage(kanedit_ltsv,"kanedit")
    kanedit_fontcolor=LTsv_readlinerest(kanedit_config,"edit_fontcolor",kanedit_fontcolor)
    kanedit_bgcolor=LTsv_readlinerest(kanedit_config,"edit_bgcolor",kanedit_bgcolor)
    tinykbd_fontcolor=LTsv_readlinerest(kanedit_config,"kbd_fontcolor",tinykbd_fontcolor)
    tinykbd_bgcolor=LTsv_readlinerest(kanedit_config,"kbd_bgcolor",tinykbd_bgcolor)
    kanedit_fontsize=min(max(LTsv_intstr0x(LTsv_readlinerest(kanedit_config,"font_size",str(kanedit_fontsize))),5),100)
    tinykbd_map=LTsv_loadfile(LTsv_readlinerest(kanedit_config,"dic_mapname",tinykbd_map))
    for irohaalpha in tinykbd_irohaalpha:
        kbd_lineT=LTsv_readlinerest(tinykbd_map,irohaalpha)
        kbd_lineL=kbd_lineT.split('\t'); kbd_lineL=kbd_lineL+[" "]*(tinykbd_SandS*2-len(kbd_lineL))
        tinykbd_kanmapN[irohaalpha],tinykbd_kanmapX[irohaalpha]=kbd_lineL[0:tinykbd_SandS+1],kbd_lineL[tinykbd_SandS+1:tinykbd_SandS+1+tinykbd_SandS+1]
    tinykbd_char=LTsv_loadfile(LTsv_readlinerest(kanedit_config,"dic_charname",tinykbd_char))
    tinykbd_word=LTsv_loadfile(LTsv_readlinerest(kanedit_config,"dic_wordname",tinykbd_word))
    tinykbd_zip=LTsv_loadfile(LTsv_readlinerest(kanedit_config,"dic_zipname",tinykbd_zip))
#    kanedit_tinykbd_select(tinykbd_kanmapchoice)
    kanedit_tinykbd_select(tinykbd_fontchar[tinykbd_KANA])
    kanedit_textload("kanedit.txt")

LTsv_GUI=LTsv_guiinit()
kantray_max=0x2ffff if LTsv_GUI != "Tkinter" else 0xffff
if len(LTsv_GUI) > 0:
    LTsv_kbdinit(LTsv_initmouse=False)
    kanedit_tinykbd_new()
    kanedit_configload()
    if LTsv_GUI == LTsv_GUI_GTK2:
        LTsv_drawtk_selcanvas,LTsv_drawtk_delete,LTsv_drawtk_queue=LTsv_drawGTK_selcanvas,LTsv_drawGTK_delete,LTsv_drawGTK_queue
        LTsv_drawtk_glyph,LTsv_drawtk_glyphfill,LTsv_drawtk_color,LTsv_drawtk_bgcolor=LTsv_drawGTK_glyph,LTsv_drawGTK_glyphfill,LTsv_drawGTK_color,LTsv_drawGTK_bgcolor
        LTsv_drawtk_polygonfill,LTsv_drawtk_picture=LTsv_drawGTK_polygonfill,LTsv_drawGTK_picture
        LTsv_drawtk_font,LTsv_drawtk_text=LTsv_drawGTK_font,LTsv_drawGTK_text
    if LTsv_GUI == LTsv_GUI_Tkinter:
        LTsv_drawtk_selcanvas,LTsv_drawtk_delete,LTsv_drawtk_queue=LTsv_drawTkinter_selcanvas,LTsv_drawTkinter_delete,LTsv_drawTkinter_queue
        LTsv_drawtk_glyph,LTsv_drawtk_glyphfill,LTsv_drawtk_color,LTsv_drawtk_bgcolor=LTsv_drawTkinter_glyph,LTsv_drawTkinter_glyphfill,LTsv_drawTkinter_color,LTsv_drawTkinter_bgcolor
        LTsv_drawtk_polygonfill,LTsv_drawtk_picture=LTsv_drawTkinter_polygonfill,LTsv_drawTkinter_picture
        LTsv_drawtk_font,LTsv_drawtk_text=LTsv_drawTkinter_font,LTsv_drawTkinter_text
    kanedit_window=LTsv_window_new(widget_t="L:Tsv GUI test and KeyCode Setup",event_b=LTsv_window_exit,widget_w=kanedit_W,widget_h=kanedit_H,event_z=kanedit_resize,event_k=kanedit_keypress,event_y=kanedit_keyrelease)
    LTsv_window_resize(kanedit_window,320,240)
    kanedit_canvas=LTsv_canvas_new(kanedit_window,widget_x=0,widget_y=0,widget_w=LTsv_screen_w(kanedit_window),widget_h=LTsv_screen_h(kanedit_window),
     event_p=kanedit_mousepress,event_r=kanedit_mouserelease,event_m=kanedit_mousemotion,event_w=50)
    kanedit_clipboard=LTsv_clipboard_new(kanedit_window)
    LTsv_widget_showhide(kanedit_window,True)
    kanedit_resize()
    kanedit_redraw()
    LTsv_window_main(kanedit_window)
else:
    LTsv_libc_printf("GUIの設定に失敗しました。")
