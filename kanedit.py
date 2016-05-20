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


def kanedit_redraw():
    global kanedit_W,kanedit_H
    LTsv_drawtk_selcanvas(kanedit_canvas); LTsv_drawtk_delete("lightgray")
    LTsv_drawtk_color("lightgray"); LTsv_drawtk_polygonfill(0,0,kanedit_W,0,kanedit_W,kanedit_H,0,kanedit_H)
    LTsv_drawtk_color("black");     LTsv_drawtk_glyphfill("test北海道",draw_x=kanedit_W-145,draw_y=kanedit_H-25,draw_f=20,draw_w=1,draw_h=1)
    LTsv_drawtk_queue()
 
def kanedit_resize(callback_void=None,callback_ptr=None):
    global kanedit_W,kanedit_H
    window_w,window_h=LTsv_window_wh(kanedit_window)
    if kanedit_W!=window_w or kanedit_H!=window_h:
        kanedit_W,kanedit_H=window_w,window_h
        LTsv_widget_settext(kanedit_window,widget_t="w,h={0},{1}".format(kanedit_W,kanedit_H))
        kanedit_redraw()

LTsv_GUI=LTsv_guiinit()
kantray_max=0x2ffff if LTsv_GUI != "Tkinter" else 0xffff
if len(LTsv_GUI) > 0:
    LTsv_kbdinit()
    kanedit_minW,kanedit_minH=200,100; kanedit_W,kanedit_H=kanedit_minW,kanedit_minH
    if LTsv_GUI == LTsv_GUI_GTK2:
        LTsv_drawtk_selcanvas,LTsv_drawtk_delete,LTsv_drawtk_queue=LTsv_drawGTK_selcanvas,LTsv_drawGTK_delete,LTsv_drawGTK_queue
        LTsv_drawtk_glyph,LTsv_drawtk_glyphfill,LTsv_drawtk_color=LTsv_drawGTK_glyph,LTsv_drawGTK_glyphfill,LTsv_drawGTK_color
        LTsv_drawtk_polygonfill=LTsv_drawGTK_polygonfill
    if LTsv_GUI == LTsv_GUI_Tkinter:
        LTsv_drawtk_selcanvas,LTsv_drawtk_delete,LTsv_drawtk_queue=LTsv_drawTkinter_selcanvas,LTsv_drawTkinter_delete,LTsv_drawTkinter_queue
        LTsv_drawtk_glyph,LTsv_drawtk_glyphfill,LTsv_drawtk_color=LTsv_drawTkinter_glyph,LTsv_drawTkinter_glyphfill,LTsv_drawTkinter_color
        LTsv_drawtk_polygonfill=LTsv_drawTkinter_polygonfill
    kanedit_window=LTsv_window_new(widget_t="L:Tsv GUI test and KeyCode Setup",event_b=LTsv_window_exit,widget_w=kanedit_W,widget_h=kanedit_H,event_z=kanedit_resize)
    kanedit_canvas=LTsv_canvas_new(kanedit_window,widget_x=0,widget_y=0,widget_w=LTsv_screen_w(kanedit_window),widget_h=LTsv_screen_h(kanedit_window),event_w=50)
    LTsv_widget_showhide(kanedit_window,True)
    kanedit_redraw()
    LTsv_window_main(kanedit_window)
else:
    LTsv_libc_printf("GUIの設定に失敗しました。")
