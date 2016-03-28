#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import sys
import os
os.chdir(sys.path[0])
if sys.version_info.major == 2:
    import urllib
if sys.version_info.major == 3:
    import urllib.request
import math
sys.path.append("LTsv")
from LTsv_printf import *
from LTsv_file   import *
#from LTsv_time   import *
#from LTsv_calc   import *
#from LTsv_joy    import *
#from LTsv_kbd    import *
from LTsv_gui    import *

kanzip_kanzip_tsv="kanzip.tsv"
kanzip_workdir="./kanzip/"
kanzip_fontsize=10
kanzip_prefectureMAX=48
kanzip_prefectureCVID=kanzip_prefectureMAX
kanzip_font="{0},{1}".format("kantray5x5comic",kanzip_fontsize)
kanzip_DLlabel_W,kanzip_DLlabel_H=kanzip_fontsize*9,kanzip_fontsize*3;                     kanzip_DLlabel=[""]*(kanzip_prefectureMAX+2)
kanzip_DLbutton_W,kanzip_DLbutton_H=kanzip_fontsize*12,kanzip_DLlabel_H;                   kanzip_DLbutton=[""]*(kanzip_prefectureMAX+2)
kanzip_DLprogres_W,kanzip_DLprogres_H=kanzip_DLbutton_W-kanzip_DLlabel_W,kanzip_DLlabel_H; kanzip_DLprogres=[""]*(kanzip_prefectureMAX+2)
kanzip_DLbuzy={}; kanzip_DLconvert={}
kanzip_prefecture_W,kanzip_prefecture_H=max(kanzip_DLlabel_W,kanzip_DLbutton_W),kanzip_DLlabel_H+kanzip_DLbutton_H
kanzip_FXbutton_W,kanzip_FXbutton_H=kanzip_prefecture_W*8-kanzip_DLprogres_W,kanzip_DLbutton_H; kanzip_FXbutton=None
kanzip_window_W,kanzip_window_H=kanzip_prefecture_W*8,kanzip_prefecture_H*6+kanzip_FXbutton_H
kanzip_prefecturesKAN=["事業所","北海道","青森県","岩手県","宮城県","秋田県","山形県","福島県",
                       "茨城県","栃木県","群馬県","埼玉県","千葉県","東京都","神奈川県","新潟県",
                       "富山県","石川県","福井県","山梨県","長野県","岐阜県","静岡県","愛知県",
                       "三重県","滋賀県","京都府","大阪府","兵庫県","奈良県","和歌山県","鳥取県",
                       "島根県","岡山県","広島県","山口県","徳島県","香川県","愛媛県","高知県",
                       "福岡県","佐賀県","長崎県","熊本県","大分県","宮崎県","鹿児島県","沖縄県","全国一括"]
kanzip_japanpostURL="http://www.post.japanpost.jp/zipcode/dl/"
kanzip_prefecturesNAME=["jigyosyo","01hokkai","02aomori","03iwate","04miyagi","05akita","06yamaga","07fukush",
                        "08ibarak","09tochig","10gumma","11saitam","12chiba","13tokyo","14kanaga","15niigat",
                        "16toyama","17ishika","18fukui","19yamana","20nagano","21gifu","22shizuo","23aichi",
                        "24mie","25shiga","26kyouto","27osaka","28hyogo","29nara","30wakaya","31tottor",
                        "32shiman","33okayam","34hirosh","35yamagu","36tokush","37kagawa","38ehime","39kochi",
                        "40fukuok","41saga","42nagasa","43kumamo","44oita","45miyaza","46kagosh","47okinaw","ken_all"]
kanzip_prefectureURL,kanzip_prefectureDL,kanzip_prefectureCSV,kanzip_prefectureTSV=[""]*(kanzip_prefectureMAX+1),[""]*(kanzip_prefectureMAX+1),[""]*(kanzip_prefectureMAX+1),[""]*(kanzip_prefectureMAX+1)
for ken in range(kanzip_prefectureMAX+1):
    kanzip_prefectureURL[ken]=kanzip_japanpostURL+"kogaki/zip/"+kanzip_prefecturesNAME[ken]+".zip"
    kanzip_prefectureDL[ken]=kanzip_workdir+kanzip_prefecturesNAME[ken]+".zip"
    kanzip_prefectureCSV[ken]=kanzip_workdir+kanzip_prefecturesNAME[ken]+".csv"
    kanzip_prefectureTSV[ken]=kanzip_workdir+kanzip_prefecturesNAME[ken]+".tsv"
kanzip_prefectureURL[0]=kanzip_japanpostURL+"jigyosyo/zip/"+kanzip_prefecturesNAME[0]+".zip"
kanzip_prefecturedic=dict(zip(kanzip_prefecturesKAN,kanzip_prefectureURL))
kanzip_prefecturesICON={
  "事業所":  [1, 1, 28, 1, 28, 8, 18, 8, 18, 10, 28, 10, 28, 17, 18, 17, 18, 28, 11, 28, 11, 17, 1, 17, 1, 10, 11, 10, 11, 8, 1, 8],
  "北海道":  [16, 1, 26, 9, 17, 28, 9, 22, 10, 29, 5, 29, 1, 18, 8, 14],
  "青森県":  [10, 2, 23, 3, 24, 24, 5, 25, 4, 11, 9, 10, 10, 16, 16, 15, 16, 9, 11, 10],
  "岩手県":  [17, 2, 4, 11, 4, 23, 16, 27, 23, 21, 20, 17, 24, 16, 22, 13, 25, 12, 21, 9, 23, 7],
  "宮城県":  [3, 4, 11, 0, 16, 6, 24, 0, 25, 16, 21, 15, 17, 10, 14, 10, 12, 28, 4, 27, 1, 20, 4, 12, 4, 12, 4, 12],
  "秋田県":  [14, 0, 23, 1, 23, 1, 23, 1, 23, 1, 23, 1, 23, 16, 25, 27, 13, 23, 12, 12, 6, 11, 12, 6],
  "山形県":  [12, 0, 24, 1, 26, 1, 26, 1, 25, 9, 23, 28, 11, 24, 11, 16, 17, 16, 11, 11, 11, 11, 11, 11, 7, 10, 12, 4],
  "福島県":  [15, 19, 6, 25, 4, 9, 11, 5, 11, 0, 17, 4, 20, 0, 28, 17, 19, 25],
  "茨城県":  [13, 0, 17, 4, 24, 0, 19, 16, 29, 27, 18, 23, 10, 28, 2, 16, 13, 9],
  "栃木県":  [14, 0, 22, 1, 25, 8, 25, 22, 13, 27, 3, 21, 9, 13, 10, 11, 4, 9],
  "群馬県":  [11, 1, 20, 4, 18, 8, 23, 10, 21, 18, 28, 18, 28, 19, 18, 21, 17, 24, 17, 24, 17, 24, 17, 24, 17, 24, 7, 27, 9, 15, 3, 17, 4, 8, 10, 6],
  "埼玉県":  [2, 13, 9, 11, 13, 6, 22, 9, 27, 18, 18, 22, 6, 21, 0, 21, 0, 16, 0, 16, 0, 16, 0, 16, 0, 16],
  "千葉県":  [2, 0, 13, 8, 20, 1, 26, 5, 26, 5, 26, 5, 27, 5, 27, 5, 21, 12, 21, 12, 21, 12, 22, 20, 7, 29, 9, 12, 4, 10],
  "東京都":  [1, 9, 10, 13, 25, 11, 29, 17, 26, 23, 18, 18, 17, 25, 13, 19, 5, 17],
  "神奈川県":[2, 0, 9, 3, 18, 5, 19, 7, 21, 1, 26, 0, 30, 3, 28, 8, 29, 10, 26, 12, 24, 13, 28, 16, 26, 26, 22, 26, 20, 17, 8, 21, 8, 26, 4, 26, 2, 17, 2, 17, 2, 17, 7, 14, 2, 10, 8, 7],
  "新潟県":  [27, 1, 15, 13, 7, 14, 8, 9, 4, 10, 12, 4, 13, 5, 18, 6, 12, 16, 3, 21, 3, 28, 15, 24, 20, 28, 25, 20, 24, 13, 29, 9],
  "富山県":  [10, 1, 8, 11, 17, 11, 21, 6, 23, 3, 29, 7, 29, 14, 26, 25, 17, 20, 10, 25, 4, 24, 2, 13, 5, 1],
  "石川県":  [7, 5, 8, 1, 17, 0, 13, 5, 17, 7, 11, 13, 13, 29, 6, 27, 9, 13],
  "福井県":  [17, 1, 28, 6, 20, 12, 13, 20, 4, 27, 1, 18, 4, 20, 11, 19, 13, 11, 12, 4],
  "山梨県":  [6, 2, 13, 1, 27, 7, 29, 12, 29, 18, 18, 20, 11, 14, 12, 25, 6, 25, 3, 19, 2, 8],
  "長野県":  [5, 1, 5, 3, 11, 3, 15, 1, 19, 3, 17, 8, 21, 10, 21, 15, 14, 15, 13, 21, 9, 28, 4, 28, 7, 19, 2, 16, 6, 9],
  "岐阜県":  [9, 10, 11, 0, 26, 1, 28, 10, 23, 13, 29, 24, 26, 28, 17, 26, 11, 20, 9, 25, 4, 25, 4, 14, 14, 12],
  "静岡県":  [7, 0, 11, 8, 18, 1, 26, 3, 28, 10, 25, 24, 22, 13, 22, 5, 17, 7, 15, 23, 2, 18, 1, 10, 6, 8],
  "愛知県":  [15, 21, 17, 22, 10, 27, 22, 26, 26, 16, 29, 5, 20, 5, 10, 0, 3, 5, 1, 10, 6, 9, 4, 17, 2, 21, 9, 17, 10, 19, 11, 22],
  "三重県":  [16, 2, 22, 5, 16, 11, 25, 13, 24, 17, 16, 17, 8, 28, 6, 25, 10, 16, 9, 16, 12, 18, 12, 13, 9, 13, 9, 9],
  "滋賀県":  [18, 1, 22, 9, 26, 22, 16, 27, 16, 30, 8, 26, 6, 23, 18, 17, 15, 9, 6, 23, 4, 13, 1, 9, 8, 1],
  "京都府":  [3, 6, 12, 1, 15, 8, 22, 5, 18, 11, 26, 14, 26, 26, 30, 25, 24, 28, 13, 24, 10, 17, 3, 16, 6, 10],
  "大阪府":  [12, 3, 13, 15, 4, 27, 23, 27, 22, 14, 25, 6, 18, 0, 7, 0],
  "兵庫県":  [19, 20, 14, 29, 21, 29, 20, 21, 29, 18, 29, 7, 18, 8, 14, 1, 4, 0, 7, 9, 5, 18, 12, 15],
  "奈良県":  [4, 0, 9, 4, 18, 0, 25, 8, 21, 8, 23, 14, 16, 26, 4, 26, 6, 21, 4, 16, 10, 11],
  "和歌山県":[1, 3, 12, 1, 10, 8, 9, 16, 13, 16, 19, 8, 19, 16, 26, 18, 25, 26, 18, 27, 9, 27, 4, 20, 1, 18, 3, 8],
  "鳥取県":  [1, 2, 3, 10, 5, 19, 3, 27, 10, 24, 11, 11, 15, 13, 19, 10, 25, 12, 29, 6, 22, 1, 14, 5, 4, 6],
  "島根県":  [3, 27, 19, 16, 19, 7, 15, 2, 22, 0, 25, 3, 20, 7, 20, 15, 24, 18, 12, 29, 5, 29],
  "岡山県":  [6, 1, 13, 4, 18, 0, 28, 1, 24, 12, 28, 20, 28, 20, 28, 20, 21, 28, 13, 24, 5, 26, 2, 10],
  "広島県":  [3, 26, 4, 13, 15, 12, 16, 1, 28, 4, 29, 21, 25, 27, 25, 27, 25, 27, 9, 28, 9, 21],
  "山口県":  [1, 11, 10, 9, 11, 1, 14, 5, 17, 10, 21, 3, 24, 12, 24, 18, 28, 19, 22, 22, 13, 16, 9, 21, 5, 17, 2, 21],
  "徳島県":  [11, 18, 0, 18, 1, 10, 18, 3, 28, 12, 22, 28],
  "香川県":  [29, 23, 21, 17, 17, 23, 9, 25, 6, 19, 2, 26, 2, 11, 0, 1, 5, 8, 15, 4, 24, 8, 25, 1, 32, 3, 25, 7],
  "愛媛県":  [16, 4, 17, 10, 28, 9, 29, 14, 20, 16, 7, 28, 6, 23, 9, 16, 3, 10, 10, 13, 12, 4],
  "高知県":  [29, 13, 25, 6, 17, 2, 7, 3, 0, 13, 3, 27, 9, 25, 7, 14, 14, 11, 21, 16],
  "福岡県":  [11, 2, 8, 2, 16, 5, 24, 0, 21, 5, 24, 8, 26, 11, 17, 12, 16, 20, 23, 24, 20, 28, 12, 24, 6, 28, 3, 24, 12, 14, 3, 12, 3, 8, 9, 8],
  "佐賀県":  [6, 1, 12, 7, 22, 3, 29, 8, 29, 4, 29, 15, 34, 18, 21, 14, 14, 22, 19, 27, 7, 25, 2, 14, 7, 9],
  "長崎県":  [18, 14, 29, 26, 17, 26, 18, 15, 10, 20, 9, 26, 3, 30, 9, 19, 18, 15, 18, 9, 12, 6, 15, 0],
  "熊本県":  [13, 1, 21, 4, 24, 0, 27, 0, 25, 8, 21, 15, 27, 22, 18, 29, 11, 27, 14, 19, 1, 23, 2, 14, 6, 16, 13, 16, 4, 8, 6, 3],
  "大分県":  [3, 8, 14, 8, 19, 1, 29, 7, 25, 14, 29, 23, 22, 28, 13, 27, 11, 15, 6, 14, 3, 19, 1, 13],
  "宮崎県":  [22, 4, 8, 29, 3, 13, 9, 13, 9, 3, 16, 1, 18, 4],
  "鹿児島県":[4, 4, 14, 3, 29, 17, 24, 18, 27, 23, 10, 29, 16, 20, 14, 12, 11, 23, 12, 27, 5, 25, 2, 26, 5, 19, 1, 11],
  "沖縄県":  [6, 7, 13, 11, 25, 5, 26, 9, 18, 14, 10, 19, 6, 27, 1, 26, 6, 17],
  "全国一括":[14, 5, 21, 1, 26, 5, 21, 10, 25, 14, 24, 24, 21, 25, 14, 26, 10, 21, 11, 26, 7, 28, 6, 24, 9, 22, 3, 24, 5, 27, 3, 32, 1, 20, 17, 15, 19, 12]
}

def kanzip_fileexist(window_objvoid=None,window_objptr=None):
    tsvcount=0
    for ken in range(kanzip_prefectureMAX):
        kanzip_buzyicon(ken,True)
        if os.path.isfile(kanzip_prefectureTSV[ken]):
            LTsv_widget_disableenable(kanzip_DLbutton[ken],False)
            LTsv_widget_settext(kanzip_DLbutton[ken],widget_t=kanzip_prefecturesNAME[ken])
            tsvcount+=1
        elif os.path.isfile(kanzip_prefectureCSV[ken]):
            LTsv_widget_disableenable(kanzip_DLbutton[ken],True)
            LTsv_widget_settext(kanzip_DLbutton[ken],widget_t=kanzip_prefecturesNAME[ken]+".tsv")
        elif os.path.isfile(kanzip_prefectureDL[ken]):
            LTsv_widget_disableenable(kanzip_DLbutton[ken],True)
            LTsv_widget_settext(kanzip_DLbutton[ken],widget_t=kanzip_prefecturesNAME[ken]+".csv")
        else:
            LTsv_widget_disableenable(kanzip_DLbutton[ken],True)
            LTsv_widget_settext(kanzip_DLbutton[ken],widget_t=kanzip_prefecturesNAME[ken]+".zip")
    if tsvcount == kanzip_prefectureMAX and not os.path.isfile(kanzip_kanzip_tsv):
        LTsv_widget_disableenable(kanzip_DLbutton[kanzip_prefectureMAX],True)
    else:
        LTsv_widget_disableenable(kanzip_DLbutton[kanzip_prefectureMAX],False)
    kanzip_buzyicon(kanzip_prefectureMAX,True)
    LTsv_widget_showhide(kanzip_window,True)
    if os.path.isfile(kanzip_kanzip_tsv):
        LTsv_widget_settext(kanzip_window,widget_t="kanzip:completion:{0}".format(kanzip_kanzip_tsv))
    else:
        LTsv_widget_settext(kanzip_window,widget_t="kanzip")

def kanzip_buzyicon(kanzip_ken,kanzip_buzy):
    LTsv_draw_delete(kanzip_DLprogres[kanzip_ken])
    LTsv_drawtk_selcanvas(kanzip_DLprogres[kanzip_ken])
    if kanzip_buzy:
        LTsv_drawtk_color(draw_c="gray"); LTsv_drawtk_polygon(*tuple(kanzip_prefecturesICON[kanzip_prefecturesKAN[kanzip_ken]]))
    else:
        for ken in range(kanzip_prefectureMAX+1):
            LTsv_widget_disableenable(kanzip_DLbutton[ken],False)
        LTsv_drawtk_color(draw_c="gray"); LTsv_drawtk_polygonfill(*tuple(kanzip_prefecturesICON[kanzip_prefecturesKAN[kanzip_ken]]))
        LTsv_drawtk_color(draw_c="black"); LTsv_drawtk_polygon(*tuple(kanzip_prefecturesICON[kanzip_prefecturesKAN[kanzip_ken]]))
    LTsv_draw_queue(kanzip_DLprogres[kanzip_ken])
    LTsv_widget_showhide(kanzip_DLprogres[kanzip_ken],True)

def kanzip_DL_report(kanzip_DL_cnt=None,kanzip_DL_size=None,kanzip_DL_total=None):
    pass
#    LTsv_libc_printf("{0}({1}/{2})".format(kanzip_prefectureDL[kanzip_ken],min(kanzip_DL_cnt*kanzip_DL_size,kanzip_DL_total),kanzip_DL_total))

def kanzip_DL_shell(kanzip_ken):
    def kanzip_DL_convert(window_objvoid=None,window_objptr=None):
        kanzip_buzyicon(kanzip_ken,True)
        if os.path.isfile(kanzip_prefectureTSV[kanzip_ken]):
            pass
        elif os.path.isfile(kanzip_prefectureCSV[kanzip_ken]):
            kanzip_csv=LTsv_loadcp932file(kanzip_prefectureCSV[kanzip_ken]); kanzip_tsv=""
            kanzip_splits=kanzip_csv.strip('\n').split('\n')
            kantsv_splits=[]; kantsv_splitsfirst=[];
            if kanzip_prefecturesKAN[kanzip_ken] == "事業所":
                for kanzip_CV_cnt,kanzip_split in enumerate(kanzip_splits):
                    kanzip_csvsplits=kanzip_split.split(',')
                    kanzip_tsvfirst=kanzip_csvsplits[7].strip('"')
                    kanzip_tsvrest=kanzip_csvsplits[3].strip('"')+kanzip_csvsplits[4].strip('"')+kanzip_csvsplits[5].strip('"')+kanzip_csvsplits[6].strip('"')+"　"+kanzip_csvsplits[2].strip('"')
                    kantsv_splits.append(kanzip_tsvfirst+'\t'+kanzip_tsvrest+'\n')
            else:
                for kanzip_CV_cnt,kanzip_split in enumerate(kanzip_splits):
                    kanzip_csvsplits=kanzip_split.split(',')
                    kanzip_tsvfirst=kanzip_csvsplits[2].strip('"')
                    if kanzip_tsvfirst in kantsv_splitsfirst:
                        kanzip_tsvrestjoin=kantsv_splits[kantsv_splitsfirst.index(kanzip_tsvfirst)]
                        kanzip_tsvrest=kanzip_csvsplits[8].strip('"') if kanzip_csvsplits[7].strip('"') in kanzip_tsvrestjoin else kanzip_csvsplits[7].strip('"')+kanzip_csvsplits[8].strip('"')
                        kantsv_splits[kantsv_splitsfirst.index(kanzip_tsvfirst)]=kanzip_tsvrestjoin.strip('\n')+' '+kanzip_tsvrest+'\n'
                    else:
                        kantsv_splitsfirst.append(kanzip_tsvfirst)
                        kanzip_tsvrest=kanzip_csvsplits[6].strip('"')+kanzip_csvsplits[7].strip('"')+kanzip_csvsplits[8].strip('"')
                        kantsv_splits.append(kanzip_tsvfirst+'\t'+kanzip_tsvrest+'\n')
            kanzip_tsv="".join(kantsv_splits)
            LTsv_saveplain(kanzip_prefectureTSV[kanzip_ken],kanzip_tsv)
        elif os.path.isfile(kanzip_prefectureDL[kanzip_ken]):
            LTsv_zipload(kanzip_prefectureDL[kanzip_ken],kanzip_prefecturesNAME[kanzip_ken]+".csv",kanzip_prefectureCSV[kanzip_ken])
        else:
            LTsv_download(kanzip_prefectureURL[kanzip_ken],kanzip_prefectureDL[kanzip_ken],kanzip_DL_report)
        LTsv_window_after(kanzip_window,event_b=kanzip_fileexist,event_i="kanzip_fileexist",event_w=10)
    def kanzip_DL_buzy(window_objvoid=None,window_objptr=None):
        kanzip_buzyicon(kanzip_ken,False)
        if kanzip_ken < kanzip_prefectureMAX:
            if os.path.isfile(kanzip_prefectureTSV[kanzip_ken]):
                pass
            elif os.path.isfile(kanzip_prefectureCSV[kanzip_ken]):
                LTsv_widget_settext(kanzip_window,widget_t="kanzip:convert:{0}→{1}".format(kanzip_prefectureCSV[kanzip_ken],kanzip_prefectureTSV[kanzip_ken]))
            elif os.path.isfile(kanzip_prefectureDL[kanzip_ken]):
                LTsv_widget_settext(kanzip_window,widget_t="kanzip:unpack:{0}→{1}".format(kanzip_prefectureDL[kanzip_ken],kanzip_prefectureCSV[kanzip_ken]))
            else:
                LTsv_widget_settext(kanzip_window,widget_t="kanzip:DownLoad:{0}".format(kanzip_prefectureDL[kanzip_ken]))
            LTsv_window_after(kanzip_window,event_b=kanzip_DL_convert,event_i="kanzip_DL_convert",event_w=10)
        else:
            LTsv_widget_settext(kanzip_window,widget_t="kanzip:merge:{0}".format(kanzip_kanzip_tsv))
            LTsv_window_after(kanzip_window,event_b=kanzip_FX_merge,event_i="kanzip_FX_merge",event_w=10)
    return kanzip_DL_buzy,kanzip_DL_convert

def kanzip_FX_merge(window_objvoid=None,window_objptr=None):
    kanzip_tsv,kanzip_preTSV="",""
    for ken in range(kanzip_prefectureMAX):
        kanzip_preTSV=LTsv_loadfile(kanzip_prefectureTSV[ken])
        kanzip_tsv+=kanzip_preTSV
    LTsv_saveplain(kanzip_kanzip_tsv,kanzip_tsv)
    LTsv_window_after(kanzip_window,event_b=kanzip_fileexist,event_i="kanzip_fileexist",event_w=10)

LTsv_GUI=LTsv_guiinit()
if len(LTsv_GUI) > 0:
    if LTsv_GUI == LTsv_GUI_GTK2:
        LTsv_drawtk_selcanvas,LTsv_drawtk_color,LTsv_drawtk_polygon,LTsv_drawtk_polygonfill=LTsv_drawGTK_selcanvas,LTsv_drawGTK_color,LTsv_drawGTK_polygon,LTsv_drawGTK_polygonfill
    if LTsv_GUI == LTsv_GUI_Tkinter:
        LTsv_drawtk_selcanvas,LTsv_drawtk_color,LTsv_drawtk_polygon,LTsv_drawtk_polygonfill=LTsv_drawTkinter_selcanvas,LTsv_drawTkinter_color,LTsv_drawTkinter_polygon,LTsv_drawTkinter_polygonfill
    kanzip_window=LTsv_window_new(widget_t="kanzip",event_b=LTsv_window_exit,widget_w=kanzip_window_W,widget_h=kanzip_window_H)
    if not os.path.isdir(kanzip_workdir): os.mkdir(kanzip_workdir)
    for ken in range(kanzip_prefectureMAX):
        prefecture_x,prefecture_y=kanzip_prefecture_W*(ken%8),kanzip_prefecture_H*(ken//8)
        kanzip_DLlabel[ken]=LTsv_label_new(kanzip_window,widget_t=kanzip_prefecturesKAN[ken],widget_x=prefecture_x,widget_y=prefecture_y,widget_w=kanzip_DLlabel_W,widget_h=kanzip_DLlabel_H,widget_f=kanzip_font)
        kanzip_DLbuzy[str(ken)],kanzip_DLconvert[str(ken)]=kanzip_DL_shell(ken)
        kanzip_DLbutton[ken]=LTsv_button_new(kanzip_window,event_b=kanzip_DLbuzy[str(ken)],widget_t=kanzip_prefecturesNAME[ken],widget_x=prefecture_x,widget_y=prefecture_y+kanzip_DLlabel_H,widget_w=kanzip_DLbutton_W,widget_h=kanzip_DLbutton_H,widget_f=kanzip_font)
        kanzip_DLprogres[ken]=LTsv_canvas_new(kanzip_window,widget_x=prefecture_x+kanzip_DLlabel_W,widget_y=prefecture_y,widget_w=kanzip_DLprogres_W,widget_h=kanzip_DLprogres_H)
    kanzip_DLbuzy[str(kanzip_prefectureMAX)],kanzip_DLconvert[str(kanzip_prefectureMAX)]=kanzip_DL_shell(kanzip_prefectureMAX)
    kanzip_DLbutton[kanzip_prefectureMAX]=LTsv_button_new(kanzip_window,event_b=kanzip_DLbuzy[str(kanzip_prefectureMAX)],widget_t="都道府県と事業所をダウンロード＆コンバートし終えてから[{0}]にマージ。".format(kanzip_kanzip_tsv),widget_x=0,widget_y=kanzip_prefecture_H*6,widget_w=kanzip_FXbutton_W,widget_h=kanzip_FXbutton_H,widget_f=kanzip_font)
    kanzip_DLprogres[kanzip_prefectureMAX]=LTsv_canvas_new(kanzip_window,widget_x=kanzip_window_W-kanzip_DLprogres_W,widget_y=kanzip_prefecture_H*6,widget_w=kanzip_DLprogres_W,widget_h=kanzip_DLprogres_H)
    LTsv_widget_showhide(kanzip_window,True)
    kanzip_fileexist()
    LTsv_window_main(kanzip_window)


# Copyright (c) 2016 ooblog
# License: MIT
# https://github.com/ooblog/LTsv9kantray/blob/master/LICENSE

