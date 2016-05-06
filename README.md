# 「LTsv9kantray(tsvtool9)」は「L:Tsv」の読み書きを中心としたモジュール群と漢字入力「kantray」のPythonによる実装です。

## 「kantray」は日本語入力ソフトです。漢字を直接入力する(変換サジェストが存在しない)ので漢直のジャンルです。

    ┏kantray「貼付モード(マウス) ┓┏kantray「貼付モード(マウス) ┓┏kantray「貼付モード(マウス) ┓
    ┃ ぬふあうえおやゆよわほへﾇ  ┃┃ 1 2 3 4 5 6 7 8 9 0 - ^ Σ ┃┃ 名音訓送異俗簡繁越地逆非￥ ┃
    ┃  たていすかんなにらせ沼濡  ┃┃  ! 全# ｅ＋－×÷√π| (    ┃┃  英顔ερτυθιοπ゛゜  ┃
    ┃ﾇ  ちとしはきくまのりれけむ ┃┃Σ 半小大⑩⑯平枝片干+ * )  ┃┃   ασδφγηξκλ代鍵ぬ ┃
    ┃＿代つさそひこみもねるめろα┃┃＿名濁清c L G 今m , . / ＼Σ┃┃σ越ζχψωβνμ熙○△□Σ┃
    ┃[代ま⇔ぱ          ]Ｃ← ⇔ ┃┃[算1/3⇔1|3        ]Ｃ← ⇔ ┃┃[照_⇔&#95;        ]Ｃ← ⇔ ┃
    ┗━━━━━━━━━━━━━━┛┗━━━━━━━━━━━━━━┛┗━━━━━━━━━━━━━━┛

通知タスクトレイ&#40;Notify&#41;に鍵盤アイコンを表示するので、漢字配列を丸暗記しなくても使えます。  
※「[鍵盤アイコン(kanmap.png)](kanmap.png "https://github.com/ooblog/LTsv9kantray/blob/master/kanmap.png")」には描画途中の箇所があります。  
※アイコン描画されてない&#40;α鍵盤&#41;にも未整頓ではありますが「[漢字配列(kanmap.tsv)](kanmap.tsv "https://github.com/ooblog/LTsv9kantray/blob/master/kanmap.tsv")」上に漢字があります。  
※配列に無い漢字も「[単漢字辞書(kanchar.tsv)](kanchar.tsv "https://github.com/ooblog/LTsv9kantray/blob/master/kanchar.tsv")」からの字引入力で異体字なども漢直できます。  


### 漢直の操作方法

Tkinter環境&#40;Windows&#41;ならマウス操作「貼付モード」のみですが、  
GTK2の通知タスクトレイ&#40;Notify&#41;が使える環境ならキーボード操作「漢直モード」も使用可能になります。  
親指で&#91;NFER&#40;無変換&#41;&#93;,&#91;XFER&#40;変換&#41;&#93;,&#91;Space&#40;SandS&#41;&#93;,&#91;KANA&#93;キーを操作して鍵盤を交換しながら漢字を直接入力します。  

漢直の実装はキーフック(EVIOCGRAB)でキーボード操作を吸収してクリップボード経由で文字入力するので、  
&#91;Ctrl&#93;+&#91;V&#93;で貼り付けができないエディタでは漢直できません。逆にVim以外のエディタでもhjkl移動を可能にします。  

「貼付モード(マウス)」の操作方法は「[LTsv.txt](LTsv.txt "https://github.com/ooblog/LTsv9kantray/blob/master/LTsv.txt")」の方に書いてます。  
「漢直モード(キーボード)」の操作方法は「[kantray.txt](kantray.txt "https://github.com/ooblog/LTsv9kantray/blob/master/kantray.txt")」の方に書いてます。  

## 「kanfont」は単漢字辞書&#91;kanchar.tsv&#93;の管理するソフトです。辞書の項目にはフォントのグリフデザインも含まれます。

    ┏kanfont ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃┌──┐│　　　　　　　　　　　　　　　　─────　　　　　│英[PA Japanese hiragana                  ]┃
    ┃│    ││　　　　　　　　　　　　　　　／　　　　　＼　　　　│名[ぱ                                    ]┃
    ┃│ぱ  ││　　　　　　　　　　　　　　／　　　　　　　＼　　　│音[                                      ]┃
    ┃└──┘│　　　　　　　　　　　　　／　　　　　　　　　＼　　│訓[                                      ]┃
    ┃  12401 │　　　　　　　　　　　　／　　　　　　　　　　　＼　│送[                                      ]┃
    ┃ 　┃　 │┌───────────　　　　■───●　　　　││異[パ                                    ]┃
    ┃ 　□　 ││　　　　　　　　　　　　　　　│X300Y100　　　　││俗[半濁音                                ]┃
    ┃ 　┃　 ││　　　　　　　　　　　　　　　│　　　│　　　　││熙[                                      ]┃
    ┃ 　┃　 ││　　　　　　　　　　　　　　　│　　　│　　　　││簡[                                      ]┃
    ┃ 　┃　 ││　　　　　　　　　　　　　　　●───●　　　　││繁[                                      ]┃
    ┃ 　┃　 ││　　　　┌─────　　　　　　　　　　　　　／　│地[                                      ]┃
    ┃ 　┃　 ││　　　　│　　　／　　　　　　　　　　　　　／　　│顔[                                      ]┃
    ┃ 　┃　 ││　　　　│　　／　　　　　　　　　　　　　／　　　│鍵[                                      ]┃
    ┃ 　┃　 ││　　　　│　／　　　　　　　　　　　　　／　　　　│代[ま                                    ]┃
    ┃ 　┃　 ││　　　　│／　　　　　　　　　　　　　／　　　　　│逆[ﾊﾟ                                    ]┃
    ┃ 　┃　 ││　　　　│　　　　　┌───┐　　　　─────┐│非[は/ば                                 ]┃
    ┃ 　┃　 ││　　　　│　　　　　│　　　│　　　　　　　　　││難[                                      ]┃
    ┃ 　┃　 ││　　　　│　　　　　│　　　│　　　　　　　　　││活[M 0,800 400,800 600,1000 8]幅[        ]┃
    ┃ 　┃　 ││　　　　│　　　　　│　　　│　　　　　　　　　││　　　　　　　　2 　　　　grid　　　　　　┃
    ┃ 　┃　 ││　　　　│　　　　　└───┘　　　　　　　　　││　━━━━━━━□━━━━[25日 　　[    ]┃
    ┃ 　┃　 ││　　　　│＼　　　　　　　　　　　　　─────┘│　　　　　　　　　　　　　　　　　　｢ ↓ ｣┃
    ┃ 　┃　 ││　　　　│　＼　　　　　　　　　　　／　　　　　　│｢kanchar.tsv｣  ゔぶぁぅぇぉゃゅょをぼべヶ ┃
    ┃ 　┃　 ││　　　　│　　＼　　　　　　　　　／　　　　　　　│｢kanmap.tsv ｣   だでぃずがゎゐっゑぜ゛゜  ┃
    ┃[12401日││　　　　│　　　＼　　　　　　　／　　　　　　　　│｢kanfont.svg｣ ぷ ぢどじばぎぐぱ…「」げぷ ┃
    ┃ 0x3071 │└────┘　　　　───────　　　　　　　　　│　　　　　　  ＿名づざぞびごぴぽ、。ぺ〜σ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

「kanfont.svg」を「kantray5x5comic.ttf」に変換するには「[FontForge](http://fontforge.github.io/ja/ "FontForge")」が別途必要です。  
FontForgeの導入が困難なWindowsの場合、「kantray5x5comic.woff」を「[WOFFコンバータ](http://opentype.jp/woffconv.htm "WOFFコンバータ")」でTTFに変換してください。  


### グリフキャンバスの座標とSVGパスの座標の違い。

グリフキャンバスのサイズは512ですがフォントの想定サイズは1024です。  
グリフキャンバスは左上が&#40;0,0&#41;ですがフォントは左下が&#40;0,0&#41;です。  
「活」の項目には上下と縮尺二倍を修正したSVGパスが入ります。  
「kanfont」は直線しか編集できない&#40;ポリゴン限定「M」と「z」しか対応してない&#41;ので注意。  


## 「kanzip」は郵便番号辞書&#91;kanzip.tsv&#93;を作成するソフトです。

    ┏kanzip━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃  事業所  □  北海道  □  青森県  □  岩手県  □  宮城県  □  秋田県  □  山形県  □  福島県  □┃
    ┃｢ jigyosyo ｣｢ 01hokkai ｣｢ 02aomori ｣｢ 03iwate  ｣｢ 04miyagi ｣｢ 05akita  ｣｢ 06yamaga ｣｢ 07fukush ｣┃
    ┃  茨城県  □  栃木県  □  群馬県  □  埼玉県  □  千葉県  □  東京都  □ 神奈川県 □  新潟県  □┃
    ┃｢ 08ibarak ｣｢ 09tochig ｣｢ 10gumma  ｣｢ 11saitam ｣｢ 12chiba  ｣｢ 13tokyo  ｣｢ 14kanaga ｣｢ 15niiga  ｣┃
    ┃  富山県  □  石川県  □  福井県  □  山梨県  □  長野県  □  岐阜県  □  静岡県  □  愛知県  □┃
    ┃｢ 16toyama ｣｢ 17ishika ｣｢ 18fukui  ｣｢ 19yamana ｣｢ 20nagano ｣｢  21gifu  ｣｢ 22shizuo｣ ｢ 23aichi  ｣┃
    ┃  三重県  □  滋賀県  □  京都府  □  大阪府  □  兵庫県  □  奈良県  □ 和歌山県 □  鳥取県  □┃
    ┃｢  24mie   ｣｢ 25shiga  ｣｢ 26kyouto ｣｢ 27osaka  ｣｢ 28hyogo  ｣｢  29nara  ｣｢ 30wakaya ｣｢ 31tottor ｣┃
    ┃  島根県  □  岡山県  □  広島県  □  山口県  □  徳島県  □  香川県  □  愛媛県  □  高知県  □┃
    ┃｢ 32shiman ｣｢ 33okayam ｣｢ 34hirosh ｣｢ 35yamagu ｣｢ 36tokush ｣｢ 37kagawa ｣｢ 38ehime  ｣｢ 39kochi  ｣┃
    ┃  福岡県  □  佐賀県  □  長崎県  □  熊本県  □  大分県  □  宮崎県  □ 鹿児島県 □  沖縄県  □┃
    ┃｢ 40fukuok ｣｢  41saga  ｣｢ 42nagasa ｣｢ 43kumamo ｣｢  44oita  ｣｢ 45miyaza ｣｢ 46kagosh ｣｢ 47okinaw ｣┃
    ┃｢        都道府県と事業所をダウンロード＆コンバートし終えてから[kanzip.tsv]にマージ。        ｣□┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

「[〒郵便番号](http://www.post.japanpost.jp/zipcode/dl/readme.html "郵便番号データの説明 - 日本郵便")」からzipをダウンロードして郵便番号辞書「kanzip.tsv」を作成します。  

## 「LTsv」はアプリを作るためのモジュール群です。

モジュールの仕様や「kantray」の電卓で使う日時フォーマット・電卓フォーマットの仕様とかは[LTsv.txt](LTsv.txt)の方に書いてます。  


## 動作環境。

Python 2.7.6(Tahrpup6.0.5)でも動作を確認しています。  
Python2.7.3(PuppyLinux571JP)およびPython3.4.3(Wine1.7.18)でも動作してたと思います(開発環境移行中)。  


## ライセンス・著作権など。

Copyright (c) 2016 ooblog  
License: MIT  
[https://github.com/ooblog/LTsv9kantray/blob/master/LICENSE](https://github.com/ooblog/LTsv9kantray/blob/master/LICENSE "https://github.com/ooblog/LTsv9kantray/blob/master/LICENSE")  
