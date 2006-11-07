#!/usr/bin/env python

# Copyright (C) 2006 Adam Olsen
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 1, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import plugins, time, os, gtk, subprocess, xl.media

PLUGIN_NAME = "Serpentine Plugin"
PLUGIN_AUTHORS = ['Adam Olsen <arolsen@gmail.com>']
PLUGIN_VERSION = '0.1'
PLUGIN_DESCRIPTION = "Opens the songs in the current playlist for burning in" \
    " Serpentine"
PLUGIN_ENABLED = False
w = gtk.Window()

EXAILE = None
BUTTON = None

def launch_serpentine(button):
    tracks = EXAILE.tracks
    if tracks:
        songs = tracks.songs
        if songs:
            ar = [song.loc for song in songs if not isinstance(song,
                xl.media.StreamTrack)]
            if not ar: return
            args = ['serpentine', '-o']
            args.extend(ar)
            subprocess.Popen(args, stdout=-1,
                stderr=-1)

def initialize(exaile):
    global EXAILE, BUTTON
    try:
        ret = subprocess.call(['serpentine', '-h'], stdout=-1, stderr=-1)
    except OSError:
        raise Exception("Serpentine was not found")
        return False

    EXAILE = exaile
    BUTTON = gtk.Button()
    image = gtk.Image()
    image.set_from_pixbuf(PLUGIN_ICON)
    BUTTON.set_image(image)
    BUTTON.connect('clicked', launch_serpentine)

    EXAILE.xml.get_widget('rating_toolbar').pack_start(BUTTON)
    BUTTON.show()
    return True

def destroy():
    global BUTTON
    if not BUTTON: return
    EXAILE.xml.get_widget('rating_toolbar').remove(BUTTON)
    BUTTON.hide()
    BUTTON.destroy()
    BUTTON = None

icon_data = [ "22 22 259 2",
"  	c None",
". 	c #6B6C69",
"+ 	c #A1A3A2",
"@ 	c #E8E8E8",
"# 	c #F6F7F8",
"$ 	c #FBFCFC",
"% 	c #FBFCFD",
"& 	c #F6F7F6",
"* 	c #E6E6E5",
"= 	c #AEAEAD",
"- 	c #F0F0F1",
"; 	c #EFF0F1",
"> 	c #DADCDD",
", 	c #CACCCF",
"' 	c #C9CBCD",
") 	c #D0D1D2",
"! 	c #D8D8D8",
"~ 	c #E9E8E7",
"{ 	c #F7F6F5",
"] 	c #F2F2F2",
"^ 	c #9A9B98",
"/ 	c #B3B4B3",
"( 	c #FAFBFC",
"_ 	c #D8DADB",
": 	c #C0C2C4",
"< 	c #BCBFC3",
"[ 	c #BFC3C7",
"} 	c #C6CACE",
"| 	c #D0D2D4",
"1 	c #D3D3D3",
"2 	c #DEDDDA",
"3 	c #E5E3E0",
"4 	c #EEECEA",
"5 	c #FCFBFA",
"6 	c #A4A5A3",
"7 	c #6D6E6B",
"8 	c #8E8E8C",
"9 	c #CECFD1",
"0 	c #B6B8BB",
"a 	c #B8BBBF",
"b 	c #B7BCC1",
"c 	c #BAC0C6",
"d 	c #C6CBD2",
"e 	c #D0D4D7",
"f 	c #D1D2D1",
"g 	c #DDDAD4",
"h 	c #E1DDD6",
"i 	c #E7E4DE",
"j 	c #EDEBE7",
"k 	c #F8F8F6",
"l 	c #929391",
"m 	c #EEEFEF",
"n 	c #E2E3E3",
"o 	c #C5C7C8",
"p 	c #C4C6C9",
"q 	c #B7BDC2",
"r 	c #B7BEC5",
"s 	c #C1C9D0",
"t 	c #CACED2",
"u 	c #CFCECD",
"v 	c #D9D4CB",
"w 	c #E0D9CD",
"x 	c #E7E2D7",
"y 	c #ECE8E2",
"z 	c #F1F0ED",
"A 	c #E4E4E3",
"B 	c #6F706D",
"C 	c #ADAEAC",
"D 	c #F6F6F6",
"E 	c #D2D2D3",
"F 	c #CACBCB",
"G 	c #CACBCC",
"H 	c #C5C8C9",
"I 	c #BBBFC3",
"J 	c #CBD2D8",
"K 	c #CED6DC",
"L 	c #D5DADE",
"M 	c #D5D4D0",
"N 	c #D8D0C1",
"O 	c #E0D6C5",
"P 	c #E6DDCF",
"Q 	c #E7E1D8",
"R 	c #E1DEDA",
"S 	c #000000",
"T 	c #6C6D6A",
"U 	c #E5E6E5",
"V 	c #D3D3D2",
"W 	c #CCCCC9",
"X 	c #CAC9C5",
"Y 	c #D2D4D4",
"Z 	c #B4B6B7",
"` 	c #777776",
" .	c #757774",
"..	c #A9A8A2",
"+.	c #E3DAC0",
"@.	c #DDD1BB",
"#.	c #DDD2C2",
"$.	c #D5CFC5",
"%.	c #FBE73B",
"&.	c #F2B64D",
"*.	c #F9F9F9",
"=.	c #E3E3E1",
"-.	c #D8D6D4",
";.	c #D0CCC4",
">.	c #C9C3B8",
",.	c #D3CEC1",
"'.	c #BCBAB5",
").	c #858584",
"!.	c #999999",
"~.	c #9E9E9E",
"{.	c #929291",
"].	c #B2AFA6",
"^.	c #E7DDCD",
"/.	c #CEC5B6",
"(.	c #FCEB3D",
"_.	c #F7B544",
":.	c #645732",
"<.	c #6B6C6A",
"[.	c #FDFDFD",
"}.	c #E7E6E4",
"|.	c #DEDAD3",
"1.	c #D6CFBC",
"2.	c #CCC2A8",
"3.	c #D9CEB3",
"4.	c #74746E",
"5.	c #9D9D9D",
"6.	c #777875",
"7.	c #262626",
"8.	c #FCE93B",
"9.	c #F7B545",
"0.	c #6C5F34",
"a.	c #EAE9E7",
"b.	c #E2DDD3",
"c.	c #DAD0B3",
"d.	c #CEC09D",
"e.	c #D9CCAC",
"f.	c #80807B",
"g.	c #777874",
"h.	c #FAE43A",
"i.	c #F4B244",
"j.	c #504627",
"k.	c #F1F1F1",
"l.	c #70716F",
"m.	c #FAFAFA",
"n.	c #F0EEEC",
"o.	c #E7E3DC",
"p.	c #DED6C5",
"q.	c #D3C8B3",
"r.	c #D5CBB7",
"s.	c #ABA9A1",
"t.	c #888887",
"u.	c #777876",
"v.	c #F9DF39",
"w.	c #F3AF42",
"x.	c #61552E",
"y.	c #EBEBEA",
"z.	c #727270",
"A.	c #777775",
"B.	c #E9E9E9",
"C.	c #F5F4F2",
"D.	c #ECE9E6",
"E.	c #E3DDD5",
"F.	c #D9D3C8",
"G.	c #D3CEC5",
"H.	c #DBDCD9",
"I.	c #BDBFBF",
"J.	c #868785",
"K.	c #858784",
"L.	c #F9DC38",
"M.	c #EFB44D",
"N.	c #665A32",
"O.	c #CACACA",
"P.	c #DADADA",
"Q.	c #D7D7D6",
"R.	c #7B7C7A",
"S.	c #ACADAC",
"T.	c #FAFAF9",
"U.	c #F0EFEE",
"V.	c #EAE9E6",
"W.	c #E7E5E0",
"X.	c #DEDDDB",
"Y.	c #D1D6D8",
"Z.	c #D1D9E1",
"`.	c #D1DCE6",
" +	c #F8D837",
".+	c #F0A93F",
"++	c #655930",
"@+	c #C8C8C8",
"#+	c #C6C6C6",
"$+	c #E6E6E6",
"%+	c #A1A1A0",
"&+	c #838482",
"*+	c #727370",
"=+	c #F7F7F7",
"-+	c #F1F2F2",
";+	c #EAEBEB",
">+	c #E0E4E6",
",+	c #D5DBE1",
"'+	c #BFC9D2",
")+	c #F6D236",
"!+	c #EDA43E",
"~+	c #5B512D",
"{+	c #CFCEC0",
"]+	c #C9C9C6",
"^+	c #D6D6D6",
"/+	c #E1E1E0",
"(+	c #7E7F7D",
"_+	c #949593",
":+	c #F9FAFB",
"<+	c #F5F6F7",
"[+	c #EEF0F2",
"}+	c #E5E9ED",
"|+	c #DCE2E8",
"1+	c #C9D1DB",
"2+	c #D7AE74",
"3+	c #61562F",
"4+	c #C4C5C1",
"5+	c #C4C3B7",
"6+	c #D4D4D1",
"7+	c #EAEAEA",
"8+	c #939491",
"9+	c #80817F",
"0+	c #797977",
"a+	c #AFB0AE",
"b+	c #F9F9FA",
"c+	c #F3F5F7",
"d+	c #EDEFF2",
"e+	c #E3E8ED",
"f+	c #4F4115",
"g+	c #C4C8CC",
"h+	c #C2C3C4",
"i+	c #D3D3D1",
"j+	c #E8E8E7",
"k+	c #A3A3A2",
"l+	c #7C7C7A",
"m+	c #959795",
"n+	c #F6F7F9",
"o+	c #E9ECEF",
"p+	c #D1D5DA",
"q+	c #D6D8DA",
"r+	c #E4E5E6",
"s+	c #D7D8D7",
"t+	c #939492",
"u+	c #787876",
"v+	c #666665",
"w+	c #747572",
"x+	c #B0B1B0",
"y+	c #D5D6D7",
"z+	c #E3E5E7",
"A+	c #E8EBEE",
"B+	c #E9EBEF",
"C+	c #E6E7E9",
"D+	c #D7D8D9",
"E+	c #A4A6A4",
"F+	c #767775",
"G+	c #818180",
"H+	c #7F7F7D",
"I+	c #7E7E7C",
"J+	c #828382",
"                                            ",
"                . . . . . .                 ",
"            . + @ # $ % & * = .             ",
"        . + - ; > , ' ) ! ~ { ] ^ .         ",
"      . / ( _ : < [ } | 1 2 3 4 5 6 7       ",
"      8 $ 9 0 a b c d e f g h i j k l       ",
"    . m n o p < q r s t u v w x y z A B     ",
"    C D E F G H I J K L M N O P Q R S S     ",
"  T U @ V W X X Y Z `  ...+.@.#.$.S %.&.S   ",
"  B *.=.-.;.>.,.'.).!.~.{.].^./.S (._.:.S   ",
"  <.[.}.|.1.2.3.4.5.      6.7.S 8.9.0.S T   ",
"  T [.a.b.c.d.e.f.        g.S h.i.j.S k.T   ",
"  l.m.n.o.p.q.r.s.t.    u.S v.w.x.S 1 y.z.  ",
"  A.B.C.D.E.F.G.H.I.J.K.S L.M.N.S O.P.Q.R.  ",
"    S.T.U.V.W.X.Y.Z.`.S  +.+++S @+#+$+%+&+  ",
"    *+k.=+-+;+>+,+'+S )+!+~+S {+]+^+/+(+    ",
"      _+:+<+[+}+|+1+S 2+3+S 4+5+6+7+8+9+    ",
"      0+a+b+c+d+e+S f+S S g+h+i+j+k+l+      ",
"        R.m+;+n+o+S S ,+p+q+r+s+t+u+        ",
"          v+w+x+y+z+A+B+C+D+E+z.F+          ",
"              G+H+w+7 7 w+I+J+              ",
"                                            "]
PLUGIN_ICON = gtk.gdk.pixbuf_new_from_xpm_data(icon_data)
