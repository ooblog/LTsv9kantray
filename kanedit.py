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

kanedit_getkbdnames=""
kanedit_iconimage,kanedit_iconimage_W,kanedit_iconimage_H="kanmap.png",24*4,24
kanedit_W,kanedit_H=kanedit_iconimage_W,kanedit_iconimage_H
kanedit_fontcolor,kanedit_bgcolor="#1A1A1A","#F8F8F8"

def kanedit_kbddraw(kbd_x,kbd_y):
    pass

def kanedit_input(window_objvoid=None,window_objptr=None):
    global kanedit_getkbdnames
    mouse_x,mouse_y=LTsv_global_canvasmotionX(),LTsv_global_canvasmotionY()
    LTsv_setkbddata(25,0)
    kanedit_getkbdnames=LTsv_getkbdnames()
    kanedit_redraw()
    LTsv_window_after(kanedit_window,event_b=kanedit_input,event_i="kanedit_input",event_w=50)

def kanedit_redraw():
    global kanedit_W,kanedit_H
    global kanedit_getkbdnames
    global kanedit_fontcolor,kanedit_bgcolor
    LTsv_drawtk_selcanvas(kanedit_canvas); LTsv_drawtk_delete(kanedit_bgcolor)
    LTsv_drawtk_color(kanedit_bgcolor); LTsv_drawtk_polygonfill(0,0,kanedit_W,0,kanedit_W,kanedit_H,0,kanedit_H)
    LTsv_drawtk_color(kanedit_fontcolor);     LTsv_drawtk_glyphfill("kanfont_grid25_199.png\n北青岩城秋形島茨栃群埼千東神潟富石井梨野岐静愛三滋京阪兵奈和鳥根岡広口徳川媛高福佐長熊分宮鹿沖",draw_x=0,draw_y=5,draw_f=5,draw_w=1,draw_h=1)
    LTsv_drawtk_color(kanedit_fontcolor);     LTsv_drawtk_glyphfill(kanedit_getkbdnames,draw_x=0,draw_y=20,draw_f=20,draw_w=1,draw_h=1)
    LTsv_drawtk_color(kanedit_fontcolor);     LTsv_drawtk_glyphfill("w,h={0},{1}".format(kanedit_W,kanedit_H),draw_x=0,draw_y=40,draw_f=20,draw_w=1,draw_h=1)
#    LTsv_drawtk_picture("{0}[{1}]".format(kanedit_iconimage,0),kanedit_W-kanedit_iconimage_W,kanedit_H-kanedit_iconimage_H)
    LTsv_drawtk_queue()

def kanedit_resize(callback_void=None,callback_ptr=None):
    global kanedit_W,kanedit_H
    window_w,window_h=LTsv_window_wh(kanedit_window)
    if kanedit_W!=window_w or kanedit_H!=window_h:
        kanedit_W,kanedit_H=window_w,window_h
#        kanedit_redraw()

def kanedit_configload():
    global kanedit_iconimage
    global kanedit_fontcolor,kanedit_bgcolor
    kanedit_ltsv=LTsv_loadfile("kanedit.tsv")
    kanedit_config=LTsv_getpage(kanedit_ltsv,"kantray")
    kanedit_iconimage=LTsv_readlinerest(kanedit_config,"icon_image",kanedit_iconimage)
#    if LTsv_draw_picture_load(kanedit_iconimage) != None:
#        LTsv_draw_picture_celldiv(kanedit_iconimage,7,25)
    kanedit_fontcolor=LTsv_readlinerest(kanedit_config,"icon_fontcolor",kanedit_fontcolor)
    kanedit_bgcolor=LTsv_readlinerest(kanedit_config,"icon_bgcolor",kanedit_bgcolor)


LTsv_GUI=LTsv_guiinit()
kantray_max=0x2ffff if LTsv_GUI != "Tkinter" else 0xffff
if len(LTsv_GUI) > 0:
    LTsv_kbdinit()
    kanedit_configload()
    if LTsv_GUI == LTsv_GUI_GTK2:
        LTsv_drawtk_selcanvas,LTsv_drawtk_delete,LTsv_drawtk_queue=LTsv_drawGTK_selcanvas,LTsv_drawGTK_delete,LTsv_drawGTK_queue
        LTsv_drawtk_glyph,LTsv_drawtk_glyphfill,LTsv_drawtk_color=LTsv_drawGTK_glyph,LTsv_drawGTK_glyphfill,LTsv_drawGTK_color
        LTsv_drawtk_polygonfill,LTsv_drawtk_picture=LTsv_drawGTK_polygonfill,LTsv_drawGTK_picture
    if LTsv_GUI == LTsv_GUI_Tkinter:
        LTsv_drawtk_selcanvas,LTsv_drawtk_delete,LTsv_drawtk_queue=LTsv_drawTkinter_selcanvas,LTsv_drawTkinter_delete,LTsv_drawTkinter_queue
        LTsv_drawtk_glyph,LTsv_drawtk_glyphfill,LTsv_drawtk_color=LTsv_drawTkinter_glyph,LTsv_drawTkinter_glyphfill,LTsv_drawTkinter_color
        LTsv_drawtk_polygonfill,LTsv_drawtk_picture=LTsv_drawTkinter_polygonfill,LTsv_drawTkinter_picture
    kanedit_window=LTsv_window_new(widget_t="L:Tsv GUI test and KeyCode Setup",event_b=LTsv_window_exit,widget_w=kanedit_W,widget_h=kanedit_H,event_z=kanedit_resize)
    LTsv_window_resize(kanedit_window,320,240)
    kanedit_canvas=LTsv_canvas_new(kanedit_window,widget_x=0,widget_y=0,widget_w=LTsv_screen_w(kanedit_window),widget_h=LTsv_screen_h(kanedit_window),event_w=50)
    kanedit_clipboard=LTsv_clipboard_new(kanedit_window)
    LTsv_widget_showhide(kanedit_window,True)
    kanedit_input()
    LTsv_window_main(kanedit_window)
else:
    LTsv_libc_printf("GUIの設定に失敗しました。")
