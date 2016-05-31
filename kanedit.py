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
tinykbd_irohatype=["ぬ","ふ","あ","う","え","お","や","ゆ","よ","わ","ほ","へ","た","て","い","す","か","ん","な","に","ら","せ","゛","゜","ち","と","し","は","き","く","ま","の","り","れ","け","む","つ","さ","そ","ひ","こ","み","も","ね","る","め","ろ","￥"]
tinykbd_alphatype=["α","β","γ","δ","ε","ζ","η","θ","ι","κ","λ","μ","ν","ξ","ο","π","ρ","σ","τ","υ","φ","χ","ψ","ω","○","△","□"]
tinykbd_dictype=  ["英","名","音","訓","送","異","俗","熙","簡","繁","越","地","顔","鍵","代","逆","非","難","活","幅"]
tinykbd_guideNX=  ["ぬ",     "ふ",     "あ",     "う",     "え",     "お",     "や",     "ゆ",     "よ",     "わ",     "ほ",     "へ",     "た",     "て",     "い",     "す"     ,"か",     "ん",     "な",     "に",     "ら",     "せ",     "゛",     "゜",     "ち",     "と",     "し",     "は",     "き",     "く",     "ま",     "の",     "り",     "れ",     "け",     "む",     "つ",     "さ",     "そ",     "ひ",     "こ",     "み",      "も",      "ね",      "る",      "め",     "ろ",     "￥",     "　"]
tinykbd_guideK= ["名",     "音",     "訓",     "送",     "異",     "俗",     "簡",     "繁",     "越",     "地",     "逆",     "非",     "英",     "顔",     "ε",     "ρ",     "τ",     "υ",     "θ",     "ι",     "ο",     "π",     "゛",     "゜",     "α",     "σ",     "δ",     "φ",     "γ",     "η",     "ξ",     "κ",     "λ",     "代",     "鍵",     "ぬ",     "ζ",     "χ",     "ψ",     "ω",     "β",     "ν",      "μ",      "熙",      "○",      "△",     "□",     "￥",     "σ"]
tinykbd_map,tinykbd_char,tinykbd_word,tinykbd_zip="","","",""
tinykbd_fontcolor,tinykbd_bgcolor="black","#CFE6CF"
tinykbd_fontsize,tinykbd_fontspace,tinykbd_fonthalf=5,6,3
tinykbd_menusize,tinykbd_menuspace,tinykbd_menuhalf=10,12,6
tinykbd_irohamax=12*4; tinykbd_SandS,tinykbd_NFER,tinykbd_XFER,tinykbd_KANA,tinykbd_None=48,49,50,51,52
tinykbd_cursorMS=tinykbd_None
tinykbd_fontX,tinykbd_fontY,tinykbd_spaceX,tinykbd_spaceY=[0]*(tinykbd_None),[0]*(tinykbd_None),[0]*(tinykbd_None),[0]*(tinykbd_None)
tinykbd_fontchar=[""]*(tinykbd_None)
tinykbd_fontchar[tinykbd_SandS],tinykbd_fontchar[tinykbd_NFER],tinykbd_fontchar[tinykbd_XFER],tinykbd_fontchar[tinykbd_KANA]="地","Ｎ","Ｘ","県"
def kanedit_tinykbd_new():
    global keyboard_irohamax,keyboard_alphapos,keyboard_guidepos,keyboard_dicinppos,keyboard_dicselpos,keyboard_iroha,keyboard_guideN,keyboard_guideX,keyboard_guideK,keyboard_guideKN,keyboard_guideKX
    global keyboard_irohatype,keyboard_alphatype,keyboard_dictype,keyboard_tofu
    keyboard_irohamax,keyboard_alphapos,keyboard_guidepos,keyboard_dicinppos,keyboard_dicselpos,keyboard_iroha,keyboard_guideN,keyboard_guideX,keyboard_guideK,keyboard_guideKN,keyboard_guideKX=LTsv_keyboard_iroha_guide()
    keyboard_irohatype,keyboard_alphatype,keyboard_dictype,keyboard_tofu=LTsv_keyboard_iroha_type()
    global tinykbd_fontX,tinykbd_fontY,tinykbd_fontchar
    tinykbd_fontX[tinykbd_SandS],tinykbd_fontY[tinykbd_SandS]=1,tinykbd_menuspace+1
    tinykbd_fontX[tinykbd_NFER],tinykbd_fontY[tinykbd_NFER]=1,1
    tinykbd_fontX[tinykbd_XFER],tinykbd_fontY[tinykbd_XFER]=1+tinykbd_fontspace*12+tinykbd_menuspace,1
    tinykbd_fontX[tinykbd_KANA],tinykbd_fontY[tinykbd_KANA]=1+tinykbd_fontspace*12+tinykbd_menuspace,tinykbd_menuspace+1
    for kbd_xy in range(tinykbd_irohamax):
        tinykbd_fontX[kbd_xy],tinykbd_fontY[kbd_xy]=tinykbd_fontspace*(kbd_xy%12)+tinykbd_menuspace,tinykbd_fontspace*(kbd_xy//12)+1
        tinykbd_spaceX[kbd_xy],tinykbd_spaceY[kbd_xy]=tinykbd_fontX[kbd_xy]+tinykbd_fonthalf,tinykbd_fontY[kbd_xy]+tinykbd_fonthalf
        tinykbd_fontchar[kbd_xy]=tinykbd_guideK[kbd_xy]
    for kbd_xy in range(tinykbd_irohamax,tinykbd_None):
        tinykbd_spaceX[kbd_xy],tinykbd_spaceY[kbd_xy]=tinykbd_fontX[kbd_xy]+tinykbd_menuhalf,tinykbd_fontY[kbd_xy]+tinykbd_menuhalf

kanedit_getkbdnames=""
kanedit_W,kanedit_H,kanedit_RS=tinykbd_W,tinykbd_H,False
kanedit_ltsv,kanedit_config="",""
kanedit_fontcolor,kanedit_bgcolor,kanedit_fontsize="black","#FFF3F5",10
kanedit_texteditvalue=""

def kanedit_kbddraw(kbd_x,kbd_y):
    global keyboard_kanmapN,keyboard_kanmapX,keyboard_dicinput
    keyboard_kanmapN,keyboard_kanmapX,keyboard_dicinput=LTsv_keyboard_map()
    LTsv_drawtk_color(kanedit_fontcolor);     LTsv_drawtk_glyphfill(kanedit_getkbdnames,draw_x=0,draw_y=kbd_y+1,draw_f=10,draw_w=1,draw_h=1)
    LTsv_drawtk_color(kanedit_fontcolor);     LTsv_drawtk_glyphfill(str(tinykbd_cursorMS),draw_x=0,draw_y=kbd_y+13,draw_f=10,draw_w=1,draw_h=1)
    LTsv_drawtk_color(tinykbd_bgcolor); LTsv_drawtk_polygonfill(kbd_x,kbd_y,kbd_x+tinykbd_W,kbd_y,kbd_x+tinykbd_W,kbd_y+tinykbd_H,kbd_x,kbd_y+tinykbd_H)
    LTsv_drawtk_bgcolor(tinykbd_bgcolor); LTsv_drawtk_color(tinykbd_fontcolor)
    for kbd_xy in range(tinykbd_irohamax):
        LTsv_drawtk_glyphfill(tinykbd_fontchar[kbd_xy],draw_x=kbd_x+tinykbd_fontX[kbd_xy],draw_y=kbd_y+tinykbd_fontY[kbd_xy],draw_f=tinykbd_fontsize)
    for kbd_xy in range(tinykbd_irohamax,tinykbd_None):
        LTsv_drawtk_glyphfill(tinykbd_fontchar[kbd_xy],draw_x=kbd_x+tinykbd_fontX[kbd_xy],draw_y=kbd_y+tinykbd_fontY[kbd_xy],draw_f=tinykbd_menusize)

def kanedit_redraw():
    global kanedit_getkbdnames
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

def kanedit_press(window_objvoid=None,window_objptr=None):
    global tinykbd_cursorMS
    tinykbd_cursorMS=tinykbd_None
    mouseX,mouseY=LTsv_global_canvasmotionX(),LTsv_global_canvasmotionY()
    print("kanedit_press",kanedit_getkbdnames)

def kanedit_motion(window_objvoid=None,window_objptr=None):
    global tinykbd_cursorMS
    tinykbd_cursorMS=tinykbd_None
    mouseX,mouseY=LTsv_global_canvasmotionX(),LTsv_global_canvasmotionY()
    kbd_x,kbd_y=kanedit_W-tinykbd_W,kanedit_H-tinykbd_H
    for kbd_xy in range(tinykbd_irohamax):
        if abs(kbd_x+tinykbd_spaceX[kbd_xy]-mouseX) <= tinykbd_fonthalf and abs(kbd_y+tinykbd_spaceY[kbd_xy]-mouseY) <= tinykbd_fonthalf:
            tinykbd_cursorMS=kbd_xy
    for kbd_xy in range(tinykbd_irohamax,tinykbd_None):
        if abs(kbd_x+tinykbd_spaceX[kbd_xy]-mouseX) <= tinykbd_menuhalf and abs(kbd_y+tinykbd_spaceY[kbd_xy]-mouseY) <= tinykbd_menuhalf:
            tinykbd_cursorMS=kbd_xy
    kanedit_redraw()

def kanedit_release(window_objvoid=None,window_objptr=None):
    global tinykbd_cursorMS
    tinykbd_cursorMS=tinykbd_None
    mouseX,mouseY=LTsv_global_canvasmotionX(),LTsv_global_canvasmotionY()
    print("kanedit_release",kanedit_getkbdnames)

def kanedit_keypress(window_objvoid=None,window_objptr=None):
    global kanedit_getkbdnames
    LTsv_setkbddata(10,0)
    kanedit_getkbdnames=LTsv_getkbdnames()
    kanedit_redraw()
    print("kanedit_keypress",kanedit_getkbdnames)

def kanedit_keyrelease(window_objvoid=None,window_objptr=None):
    global kanedit_getkbdnames
    if kanedit_getkbdnames == "Space":
        print("SandS")
        pass
    LTsv_setkbddata(10,0)
    kanedit_getkbdnames=LTsv_getkbdnames()
    kanedit_redraw()
    print("kanedit_keyrelease",kanedit_getkbdnames)

def kanedit_textload(filename):
    global kanedit_texteditvalue
    kanedit_texteditvalue=LTsv_loadfile(filename)

def kanedit_configload():
    global kanedit_fontcolor,kanedit_bgcolor,kanedit_fontsize
    global kanedit_ltsv,kanedit_config
    global tinykbd_map,tinykbd_char,tinykbd_word,tinykbd_zip
    global tinykbd_fontcolor,tinykbd_bgcolor
    kanedit_ltsv=LTsv_loadfile("kanedit.tsv")
    kanedit_config=LTsv_getpage(kanedit_ltsv,"kanedit")
    kanedit_fontcolor=LTsv_readlinerest(kanedit_config,"edit_fontcolor",kanedit_fontcolor)
    kanedit_bgcolor=LTsv_readlinerest(kanedit_config,"edit_bgcolor",kanedit_bgcolor)
    tinykbd_fontcolor=LTsv_readlinerest(kanedit_config,"kbd_fontcolor",tinykbd_fontcolor)
    tinykbd_bgcolor=LTsv_readlinerest(kanedit_config,"kbd_bgcolor",tinykbd_bgcolor)
    kanedit_fontsize=min(max(LTsv_intstr0x(LTsv_readlinerest(kanedit_config,"font_size",str(kanedit_fontsize))),5),100)
    tinykbd_map=LTsv_loadfile(LTsv_readlinerest(kanedit_config,"dic_mapname",tinykbd_map))
    tinykbd_char=LTsv_loadfile(LTsv_readlinerest(kanedit_config,"dic_charname",tinykbd_char))
    tinykbd_word=LTsv_loadfile(LTsv_readlinerest(kanedit_config,"dic_wordname",tinykbd_word))
    tinykbd_zip=LTsv_loadfile(LTsv_readlinerest(kanedit_config,"dic_zipname",tinykbd_zip))
    kanedit_textload("kanedit.txt")

LTsv_GUI=LTsv_guiinit()
kantray_max=0x2ffff if LTsv_GUI != "Tkinter" else 0xffff
if len(LTsv_GUI) > 0:
    LTsv_kbdinit()
    kanedit_configload()
    kanedit_tinykbd_new()
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
     event_p=kanedit_press,event_r=kanedit_release,event_m=kanedit_motion,event_w=50)
    kanedit_clipboard=LTsv_clipboard_new(kanedit_window)
    LTsv_widget_showhide(kanedit_window,True)
    kanedit_resize()
    kanedit_redraw()
    LTsv_window_main(kanedit_window)
else:
    LTsv_libc_printf("GUIの設定に失敗しました。")
