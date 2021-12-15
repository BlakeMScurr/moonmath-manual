## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file main-moonmath.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_87 = Integer(87); _sage_const_0 = Integer(0); _sage_const_97 = Integer(97); _sage_const_116 = Integer(116); _sage_const_1 = Integer(1); _sage_const_119 = Integer(119); _sage_const_187 = Integer(187); _sage_const_2 = Integer(2); _sage_const_192 = Integer(192); _sage_const_205 = Integer(205); _sage_const_3 = Integer(3); _sage_const_208 = Integer(208); _sage_const_265 = Integer(265); _sage_const_4 = Integer(4); _sage_const_267 = Integer(267); _sage_const_340 = Integer(340); _sage_const_5 = Integer(5); _sage_const_347 = Integer(347); _sage_const_376 = Integer(376); _sage_const_6 = Integer(6); _sage_const_379 = Integer(379); _sage_const_443 = Integer(443); _sage_const_7 = Integer(7); _sage_const_445 = Integer(445); _sage_const_519 = Integer(519); _sage_const_8 = Integer(8); _sage_const_523 = Integer(523); _sage_const_591 = Integer(591); _sage_const_9 = Integer(9); _sage_const_593 = Integer(593); _sage_const_639 = Integer(639); _sage_const_10 = Integer(10); _sage_const_644 = Integer(644); _sage_const_708 = Integer(708); _sage_const_11 = Integer(11); _sage_const_721 = Integer(721); _sage_const_742 = Integer(742); _sage_const_12 = Integer(12); _sage_const_751 = Integer(751); _sage_const_771 = Integer(771); _sage_const_13 = Integer(13); _sage_const_777 = Integer(777); _sage_const_788 = Integer(788); _sage_const_14 = Integer(14); _sage_const_793 = Integer(793); _sage_const_825 = Integer(825); _sage_const_15 = Integer(15); _sage_const_831 = Integer(831); _sage_const_844 = Integer(844); _sage_const_16 = Integer(16); _sage_const_850 = Integer(850); _sage_const_902 = Integer(902); _sage_const_17 = Integer(17); _sage_const_909 = Integer(909); _sage_const_934 = Integer(934); _sage_const_18 = Integer(18); _sage_const_939 = Integer(939); _sage_const_959 = Integer(959); _sage_const_19 = Integer(19); _sage_const_964 = Integer(964); _sage_const_300 = Integer(300); _sage_const_20 = Integer(20); _sage_const_313 = Integer(313); _sage_const_370 = Integer(370); _sage_const_21 = Integer(21); _sage_const_380 = Integer(380); _sage_const_382 = Integer(382); _sage_const_500 = Integer(500); _sage_const_384 = Integer(384); _sage_const_385 = Integer(385); _sage_const_387 = Integer(387); _sage_const_100000 = Integer(100000); _sage_const_10000 = Integer(10000); _sage_const_393 = Integer(393); _sage_const_395 = Integer(395); _sage_const_398 = Integer(398); _sage_const_31 = Integer(31); _sage_const_404 = Integer(404); _sage_const_406 = Integer(406); _sage_const_426 = Integer(426); _sage_const_22 = Integer(22); _sage_const_437 = Integer(437); _sage_const_439 = Integer(439); _sage_const_23 = Integer(23); _sage_const_460 = Integer(460); _sage_const_462 = Integer(462); _sage_const_651 = Integer(651); _sage_const_655 = Integer(655); _sage_const_675 = Integer(675); _sage_const_24 = Integer(24); _sage_const_680 = Integer(680); _sage_const_940 = Integer(940); _sage_const_25 = Integer(25); _sage_const_952 = Integer(952); _sage_const_35 = Integer(35); _sage_const_9973 = Integer(9973); _sage_const_41 = Integer(41); _sage_const_43 = Integer(43); _sage_const_44 = Integer(44); _sage_const_52 = Integer(52); _sage_const_26 = Integer(26); _sage_const_68 = Integer(68); _sage_const_81 = Integer(81); _sage_const_85 = Integer(85); _sage_const_101 = Integer(101); _sage_const_105 = Integer(105); _sage_const_107 = Integer(107); _sage_const_128 = Integer(128); _sage_const_27 = Integer(27); _sage_const_140 = Integer(140); _sage_const_168 = Integer(168); _sage_const_28 = Integer(28); _sage_const_182 = Integer(182); _sage_const_269 = Integer(269); _sage_const_29 = Integer(29); _sage_const_283 = Integer(283); _sage_const_291 = Integer(291); _sage_const_30 = Integer(30); _sage_const_298 = Integer(298); _sage_const_302 = Integer(302); _sage_const_315 = Integer(315); _sage_const_411 = Integer(411); _sage_const_32 = Integer(32); _sage_const_420 = Integer(420); _sage_const_660 = Integer(660); _sage_const_33 = Integer(33); _sage_const_669 = Integer(669); _sage_const_696 = Integer(696); _sage_const_34 = Integer(34); _sage_const_718 = Integer(718); _sage_const_808 = Integer(808); _sage_const_816 = Integer(816); _sage_const_907 = Integer(907); _sage_const_36 = Integer(36); _sage_const_921 = Integer(921); _sage_const_926 = Integer(926); _sage_const_37 = Integer(37); _sage_const_933 = Integer(933); _sage_const_947 = Integer(947); _sage_const_38 = Integer(38); _sage_const_955 = Integer(955); _sage_const_979 = Integer(979); _sage_const_39 = Integer(39); _sage_const_986 = Integer(986); _sage_const_998 = Integer(998); _sage_const_40 = Integer(40); _sage_const_1013 = Integer(1013); _sage_const_1015 = Integer(1015); _sage_const_1028 = Integer(1028); _sage_const_1073 = Integer(1073); _sage_const_42 = Integer(42); _sage_const_1080 = Integer(1080); _sage_const_1082 = Integer(1082); _sage_const_1090 = Integer(1090); _sage_const_1095 = Integer(1095); _sage_const_1102 = Integer(1102); _sage_const_1104 = Integer(1104); _sage_const_45 = Integer(45); _sage_const_1112 = Integer(1112); _sage_const_1278 = Integer(1278); _sage_const_46 = Integer(46); _sage_const_1291 = Integer(1291); _sage_const_1293 = Integer(1293); _sage_const_47 = Integer(47); _sage_const_1295 = Integer(1295); _sage_const_1297 = Integer(1297); _sage_const_48 = Integer(48); _sage_const_1300 = Integer(1300); _sage_const_1310 = Integer(1310); _sage_const_49 = Integer(49); _sage_const_1313 = Integer(1313); _sage_const_1367 = Integer(1367); _sage_const_50 = Integer(50); _sage_const_1373 = Integer(1373); _sage_const_1404 = Integer(1404); _sage_const_51 = Integer(51); _sage_const_1409 = Integer(1409); _sage_const_1453 = Integer(1453); _sage_const_1468 = Integer(1468); _sage_const_1629 = Integer(1629); _sage_const_53 = Integer(53); _sage_const_1640 = Integer(1640); _sage_const_1645 = Integer(1645); _sage_const_54 = Integer(54); _sage_const_1659 = Integer(1659); _sage_const_1661 = Integer(1661); _sage_const_55 = Integer(55); _sage_const_1674 = Integer(1674); _sage_const_1684 = Integer(1684); _sage_const_56 = Integer(56); _sage_const_1698 = Integer(1698); _sage_const_1745 = Integer(1745); _sage_const_57 = Integer(57); _sage_const_1750 = Integer(1750); _sage_const_1763 = Integer(1763); _sage_const_58 = Integer(58); _sage_const_1775 = Integer(1775); _sage_const_1779 = Integer(1779); _sage_const_59 = Integer(59); _sage_const_1793 = Integer(1793); _sage_const_1799 = Integer(1799); _sage_const_1801 = Integer(1801); _sage_const_1803 = Integer(1803); _sage_const_1822 = Integer(1822); _sage_const_60 = Integer(60); _sage_const_1830 = Integer(1830); _sage_const_1904 = Integer(1904); _sage_const_61 = Integer(61); _sage_const_1910 = Integer(1910); _sage_const_1916 = Integer(1916); _sage_const_62 = Integer(62); _sage_const_1927 = Integer(1927); _sage_const_1933 = Integer(1933); _sage_const_63 = Integer(63); _sage_const_1939 = Integer(1939); _sage_const_1974 = Integer(1974); _sage_const_64 = Integer(64); _sage_const_1978 = Integer(1978)## This file (main-moonmath.sagetex.sage) was *autogenerated* from main-moonmath.tex with sagetex.sty version 2020/08/12 v3.5.
import sagetex
_st_ = sagetex.SageTeXProcessor('main-moonmath', version='2020/08/12 v3.5', version_check=True)
try:
 _st_.current_tex_line = _sage_const_87 
 _st_.commandline(_sage_const_0 , r"""
sage: ZZ # A sage notation for the integer type
sage: NN # A sage notation for the counting number type
sage: ZZ(5) # Get an element from the Ring of integers
sage: ZZ(5) + ZZ(3)
sage: ZZ(5) * NN(3)
sage: ZZ.random_element(10**50)
sage: ZZ(27713).str(2) # Binary string representation
sage: NN(27713).str(2) # Binary string representation
sage: ZZ(27713).str(16) # Hexadecimal string representation
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_97 )
try:
 _st_.current_tex_line = _sage_const_116 
 _st_.commandline(_sage_const_1 , r"""
sage: n = NN(19214758032624000)
sage: factor(n)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_119 )
try:
 _st_.current_tex_line = _sage_const_187 
 _st_.commandline(_sage_const_2 , r"""
sage: ZZ(-17) // ZZ(4) # Integer quotient
sage: ZZ(-17) % ZZ(4) # remainder
sage: ZZ(4).divides(ZZ(-17)) # self divides other
sage: ZZ(4).divides(ZZ(12))
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_192 )
try:
 _st_.current_tex_line = _sage_const_205 
 _st_.commandline(_sage_const_3 , r"""
sage: ZZ(143785).quo_rem(ZZ(17)) # Euclidean Division
sage: ZZ(143785) == ZZ(8457)*ZZ(17) + ZZ(16) # check
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_208 )
try:
 _st_.current_tex_line = _sage_const_265 
 _st_.commandline(_sage_const_4 , r"""
sage: ZZ(12).xgcd(ZZ(5)) # (gcd(a,b),s,t)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_267 )
try:
 _st_.current_tex_line = _sage_const_340 
 _st_.commandline(_sage_const_5 , r"""
sage: ZZ(137).gcd(ZZ(64))
sage: ZZ(64)** ZZ(137) % ZZ(137) == ZZ(64) % ZZ(137)
sage: ZZ(64)** ZZ(137-1) % ZZ(137) == ZZ(1) % ZZ(137)
sage: ZZ(1918).gcd(ZZ(137))
sage: ZZ(1918)** ZZ(137) % ZZ(137) == ZZ(1918) % ZZ(137)
sage: ZZ(1918)** ZZ(137-1) % ZZ(137) == ZZ(1) % ZZ(137)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_347 )
try:
 _st_.current_tex_line = _sage_const_376 
 _st_.commandline(_sage_const_6 , r"""
sage: (ZZ(7)* (ZZ(2)*ZZ(4) + ZZ(21)) + ZZ(11))  % ZZ(6) == (ZZ(4) - ZZ(102))  % ZZ(6)
sage: (ZZ(7)* (ZZ(2)*ZZ(76) + ZZ(21)) + ZZ(11))  % ZZ(6) == (ZZ(76) - ZZ(102))  % ZZ(6)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_379 )
try:
 _st_.current_tex_line = _sage_const_443 
 _st_.commandline(_sage_const_7 , r"""
sage: CRT_list([4,1,3,0], [7,3,5,11])
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_445 )
try:
 _st_.current_tex_line = _sage_const_519 
 _st_.commandline(_sage_const_8 , r"""
sage: Z6 = Integers(6)
sage: Z6(2) + Z6(5)
sage: Z6(7)*(Z6(2)*Z6(4)+Z6(21))+Z6(11) == Z6(4) - Z6(102)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_523 )
try:
 _st_.current_tex_line = _sage_const_591 
 _st_.commandline(_sage_const_9 , r"""
sage: ZZ(6).xgcd(ZZ(5))
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_593 )
try:
 _st_.current_tex_line = _sage_const_639 
 _st_.commandline(_sage_const_10 , r"""
sage: Z5 = Integers(5)
sage: Z5(3)**(5-2)
sage: Z5(3)**(-1)
sage: Z5(3)**(5-2) == Z5(3)**(-1)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_644 )
try:
 _st_.current_tex_line = _sage_const_708 
 _st_.commandline(_sage_const_11 , r"""
sage: Zx = ZZ['x'] # integer polynomials with indeterminate x
sage: Zt.<t> = ZZ[] # integer polynomials with indeterminate t
sage: Zx
sage: Zt
sage: p1 = Zx([17,-4,2])
sage: p1
sage: p1.degree()
sage: p1.leading_coefficient()
sage: p2 = Zt(t^23)
sage: p2
sage: p6 = Zx([0])
sage: p6.degree()
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_721 )
try:
 _st_.current_tex_line = _sage_const_742 
 _st_.commandline(_sage_const_12 , r"""
sage: Z6 = Integers(6)
sage: Z6x = Z6['x']
sage: Z6x
sage: p1 = Z6x([5,-4,2])
sage: p1
sage: p1 = Z6x([17,-4,2])
sage: p1
sage: Z6x(x-2)*Z6x(x+3)*Z6x(x-5) == Z6x(x^3 + 2*x^2 + x)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_751 )
try:
 _st_.current_tex_line = _sage_const_771 
 _st_.commandline(_sage_const_13 , r"""
sage: Zx = ZZ['x']
sage: p1 = Zx([17,-4,2])
sage: p7 = Zx(x-2)*Zx(x+3)*Zx(x-5)
sage: p1(ZZ(2))
sage: p7(ZZ(-6)) == ZZ(-264)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_777 )
try:
 _st_.current_tex_line = _sage_const_788 
 _st_.commandline(_sage_const_14 , r"""
sage: Z6 = Integers(6)
sage: Z6x = Z6['x']
sage: p1 = Z6x([5,-4,2])
sage: p1(Z6(2)) == Z6(5)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_793 )
try:
 _st_.current_tex_line = _sage_const_825 
 _st_.commandline(_sage_const_15 , r"""
sage: Zx = ZZ['x']
sage: P = Zx([2,-4,5])
sage: Q = Zx([5,0,-2,1])
sage: P+Q == Zx(x^3 +3*x^2 -4*x +7)
sage: P*Q == Zx(5*x^5 -14*x^4 +10*x^3+21*x^2-20*x +10)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_831 )
try:
 _st_.current_tex_line = _sage_const_844 
 _st_.commandline(_sage_const_16 , r"""
sage: Z6x = Integers(6)['x']
sage: P = Z6x([2,-4,5])
sage: Q = Z6x([5,0,-2,1])
sage: P+Q == Z6x(x^3 +3*x^2 +2*x +1)
sage: P*Q == Z6x(5*x^5 +4*x^4 +4*x^3+3*x^2+4*x +4)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_850 )
try:
 _st_.current_tex_line = _sage_const_902 
 _st_.commandline(_sage_const_17 , r"""
sage: Zx = ZZ['x']
sage: A = Zx([-9,0,0,2,0,1])
sage: B = Zx([-1,4,1])
sage: M = Zx([-80,19,-4,1])
sage: R = Zx([-89,339])
sage: A == M*B + R
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_909 )
try:
 _st_.current_tex_line = _sage_const_934 
 _st_.commandline(_sage_const_18 , r"""
sage: Zx = ZZ['x']
sage: p = Zx(x^2-3)
sage: p.roots()
sage: p.factor()
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_939 )
try:
 _st_.current_tex_line = _sage_const_959 
 _st_.commandline(_sage_const_19 , r"""
sage: Zx = ZZ['x']
sage: p = Zx(x^7 + 3*x^6 + 3*x^5 + x^4 - x^3 - 3*x^2 - 3*x - 1)
sage: p.roots()
sage: p.factor()
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_964 )
try:
 _st_.current_tex_line = _sage_const_300 
 _st_.commandline(_sage_const_20 , r"""
sage: import Crypto
sage: from Crypto.Hash import SHA256
sage: test = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
sage: d = SHA256.new('')
sage: str = d.hexdigest()
sage: type(str)
sage: d = ZZ('0x'+ str) # conversion to integer type
sage: d.str(16) == str
sage: d.str(16) == test
sage: d.str(16)
sage: d.str(2)
sage: d.str(10)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_313 )
try:
 _st_.current_tex_line = _sage_const_370 
 _st_.commandline(_sage_const_21 , r"""
sage: import Crypto
sage: from Crypto.Hash import SHA256
sage: def Hash5(x):
....:     h = SHA256.new(x)
....:     d = h.hexdigest()
....:     d = ZZ(d, base=16)
....:     d = d.str(2)[-4:]
....:     return ZZ(d, base=2)
sage: Hash5('')
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_380 )
_st_.current_tex_line = _sage_const_382 
_st_.blockbegin()
try:
 H1 = list_plot([Hash5(ZZ(i).str(_sage_const_2 )) for i in range(_sage_const_500 )])
except:
 _st_.goboom(_sage_const_384 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_385 
 _st_.plot(_sage_const_0 , format='notprovided', _p_=H1)
except:
 _st_.goboom(_sage_const_385 )
_st_.current_tex_line = _sage_const_387 
_st_.blockbegin()
try:
 arr = []
 arr = [_sage_const_0  for i in range(_sage_const_16 )]
 for i in range(_sage_const_100000 ):
     arr[Hash5(ZZ(i).str(_sage_const_2 ))] +=_sage_const_1 
 H2 = list_plot(arr, ymin=_sage_const_0 ,ymax=_sage_const_10000 )
except:
 _st_.goboom(_sage_const_393 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_395 
 _st_.plot(_sage_const_1 , format='notprovided', _p_=H2)
except:
 _st_.goboom(_sage_const_395 )
_st_.current_tex_line = _sage_const_398 
_st_.blockbegin()
try:
 arr = []
 arr = [_sage_const_0  for i in range(_sage_const_31 )]
 for i in range(_sage_const_100000 ):
     arr[Hash5(ZZ(i).str(_sage_const_2 ))] +=_sage_const_1 
 H3 = list_plot(arr, ymin=_sage_const_0 ,ymax=_sage_const_10000 )
except:
 _st_.goboom(_sage_const_404 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_406 
 _st_.plot(_sage_const_2 , format='notprovided', _p_=H3)
except:
 _st_.goboom(_sage_const_406 )
try:
 _st_.current_tex_line = _sage_const_426 
 _st_.commandline(_sage_const_22 , r"""
sage: import Crypto
sage: from Crypto.Hash import SHA256
sage: Z23 = Integers(23)
sage: def Hash_mod23(x, k2):
....:     h = SHA256.new(x)
....:     d = h.hexdigest()
....:     d = ZZ(d, base=16)
....:     d = d.str(2)[-k2:]
....:     d = ZZ(d, base=2)
....:     return Z23(d)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_437 )
_st_.current_tex_line = _sage_const_439 
_st_.blockbegin()
try:
 arr1 = []
 arr1 = [_sage_const_0  for i in range(_sage_const_23 )]
 for i in range(_sage_const_100000 ):
     arr1[Hash_mod23(ZZ(i).str(_sage_const_2 ),_sage_const_5 )] +=_sage_const_1 
 H3 = list_plot(arr1, ymin=_sage_const_0 ,ymax=_sage_const_10000 ,color='red', legend_label='k=5')
 arr2 = []
 arr2 = [_sage_const_0  for i in range(_sage_const_23 )]
 for i in range(_sage_const_100000 ):
     arr2[Hash_mod23(ZZ(i).str(_sage_const_2 ),_sage_const_7 )] +=_sage_const_1 
 H4 = list_plot(arr2, ymin=_sage_const_0 ,ymax=_sage_const_10000 ,color='blue', legend_label='k=7')
 arr3 = []
 arr3 = [_sage_const_0  for i in range(_sage_const_23 )]
 for i in range(_sage_const_100000 ):
     arr3[Hash_mod23(ZZ(i).str(_sage_const_2 ),_sage_const_9 )] +=_sage_const_1 
 H5 = list_plot(arr3, ymin=_sage_const_0 ,ymax=_sage_const_10000 ,color='yellow', legend_label='k=9')
 arr4 = []
 arr4 = [_sage_const_0  for i in range(_sage_const_23 )]
 for i in range(_sage_const_100000 ):
     arr4[Hash_mod23(ZZ(i).str(_sage_const_2 ),_sage_const_16 )] +=_sage_const_1 
 H6 = list_plot(arr4, ymin=_sage_const_0 ,ymax=_sage_const_10000 ,color='black', legend_label='k=16')
except:
 _st_.goboom(_sage_const_460 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_462 
 _st_.plot(_sage_const_3 , format='notprovided', _p_=H3+H4+H5+H6)
except:
 _st_.goboom(_sage_const_462 )
try:
 _st_.current_tex_line = _sage_const_651 
 _st_.commandline(_sage_const_23 , r"""
sage: QQ
sage: QQ(1/5) # Get an element from the field of rational numbers
sage: QQ(1/5) / QQ(3) # Division
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_655 )
try:
 _st_.current_tex_line = _sage_const_675 
 _st_.commandline(_sage_const_24 , r"""
sage: F2 = GF(2)
sage: F2(1) # Get an element from GF(2)
sage: F2(1) + F2(1) # Addition
sage: F2(1) / F2(1) # Division
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_680 )
try:
 _st_.current_tex_line = _sage_const_940 
 _st_.commandline(_sage_const_25 , r"""
sage: Z3 = GF(3) # prime field
sage: Z3t.<t> = Z3[] # polynomials over Z3
sage: P = Z3t(t^2+1)
sage: P.is_irreducible()
sage: F3_2.<t> = GF(3^2, name='t', modulus=P)
sage: F3_2
sage: F3_2(t+2)*F3_2(2*t+2) == F3_2(2)
sage: F3_2(2*t+2)^(-1) # multiplicative inverse
sage: # verify our solution to (t+1)(x^2 + (2t+2)) = 2
sage: F3_2(t+1)*(F3_2(t)**2 + F3_2(2*t+2)) == F3_2(2)
sage: F3_2(t+1)*(F3_2(2*t)**2 + F3_2(2*t+2)) == F3_2(2)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_952 )
_st_.current_tex_line = _sage_const_35 
_st_.blockbegin()
try:
 E1 = EllipticCurve([-_sage_const_2 ,_sage_const_1 ])
 C1 = E1.plot()
 F = GF(_sage_const_9973 )
 E2 = EllipticCurve(F, [-_sage_const_2 ,_sage_const_1 ])
 C2 = E2.plot()
except:
 _st_.goboom(_sage_const_41 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_43 
 _st_.plot(_sage_const_4 , format='notprovided', _p_=C1)
except:
 _st_.goboom(_sage_const_43 )
try:
 _st_.current_tex_line = _sage_const_44 
 _st_.plot(_sage_const_5 , format='notprovided', _p_=C2)
except:
 _st_.goboom(_sage_const_44 )
try:
 _st_.current_tex_line = _sage_const_52 
 _st_.commandline(_sage_const_26 , r"""
sage: F5 = GF(5) # define the base field
sage: a = F5(2) # parameter a
sage: b = F5(4) # parameter b
sage: # check non-sigularity
sage: F5(6)*(F5(4)*a^3+F5(27)*b^2) != F5(0)
sage: # short Weierstrass curve
sage: E = EllipticCurve(F5,[a,b]) # y^2 == x^3 + ax +b
sage: P = E(0,2) # 2^2 == 0^3 + 2*0 + 4
sage: P.xy() # affine coordinates
sage: INF = E(0) # point at infinity
sage: try:  # point at infinity has no affine coordinates
....:     INF.xy()
....: except ZeroDivisionError:
....:     pass
sage: P = E.plot() # create a plotted version
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_68 )
_st_.current_tex_line = _sage_const_81 
_st_.blockbegin()
try:
 F5 = GF(_sage_const_5 )
 E1 = EllipticCurve(F5, [_sage_const_1 ,_sage_const_1 ])
 C1 = E1.plot()
except:
 _st_.goboom(_sage_const_85 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_87 
 _st_.plot(_sage_const_6 , format='notprovided', _p_=C1)
except:
 _st_.goboom(_sage_const_87 )
_st_.current_tex_line = _sage_const_101 
_st_.blockbegin()
try:
 F13 = GF(_sage_const_13 )
 PJJ_13 = EllipticCurve(F13, [_sage_const_8 ,_sage_const_8 ])
 CPJJ_13 = PJJ_13.plot()
except:
 _st_.goboom(_sage_const_105 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_107 
 _st_.plot(_sage_const_7 , format='notprovided', _p_=CPJJ_13)
except:
 _st_.goboom(_sage_const_107 )
try:
 _st_.current_tex_line = _sage_const_128 
 _st_.commandline(_sage_const_27 , r"""
sage: p = 115792089237316195423570985008687907853269984665640564039457584007908834671663
sage: # Hexadecimal representation
sage: p.str(16)
sage: p.is_prime()
sage: p.nbits()
sage: Fp = GF(p)
sage: Secp256k1 = EllipticCurve(Fp,[0,7])
sage: r = Secp256k1.order() # number of elements
sage: r.str(16)
sage: r.is_prime()
sage: r.nbits()
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_140 )
try:
 _st_.current_tex_line = _sage_const_168 
 _st_.commandline(_sage_const_28 , r"""
sage: P = Secp256k1.random_point().xy()
sage: P
sage: # uncompressed affine point size
sage: ZZ(P[0]).nbits()+ZZ(P[1]).nbits()
sage: # compute the compression
sage: if P[1] > Fp(-1)/Fp(2):
....:     PARITY = 1
....: else:
....:     PARITY = 0
sage: PCOMPRESSED = [P[0],PARITY]
sage: PCOMPRESSED
sage: # compressed affine point size
sage: ZZ(PCOMPRESSED[0]).nbits()+ZZ(PCOMPRESSED[1]).nbits()
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_182 )
try:
 _st_.current_tex_line = _sage_const_269 
 _st_.commandline(_sage_const_29 , r"""
sage: F5 = GF(5)
sage: E1 = EllipticCurve(F5,[1,1])
sage: INF = E1(0) # point at infinity
sage: P1 = E1(0,1)
sage: P2 = E1(4,2)
sage: P3 = E1(0,4)
sage: R1 = E1(2,1)
sage: R2 = E1(3,4)
sage: R1 == P1+P2
sage: INF == P1+P3
sage: R2 == P2+P2
sage: R2 == 2*P2
sage: P3 == P3 + INF
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_283 )
try:
 _st_.current_tex_line = _sage_const_291 
 _st_.commandline(_sage_const_30 , r"""
sage: F13 = GF(13)
sage: MJJ = EllipticCurve(F13,[8,8])
sage: P = MJJ(4,0)
sage: INF = MJJ(0) # Point at infinity
sage: INF == P+P
sage: INF == 2*P
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_298 )
try:
 _st_.current_tex_line = _sage_const_302 
 _st_.commandline(_sage_const_31 , r"""
sage: P = Secp256k1.random_point()
sage: Q = Secp256k1.random_point()
sage: INF = Secp256k1(0)
sage: R1 = -P
sage: R2 = P + Q
sage: R3 = Secp256k1.order()*P
sage: P.xy()
sage: Q.xy()
sage: (ZZ(R1[0]).str(16), ZZ(R1[1]).str(16))
sage: R2.xy()
sage: R3 == INF
sage: P[1]+R1[1] == Fp(0) # -(x,y) = (x,-y)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_315 )
try:
 _st_.current_tex_line = _sage_const_411 
 _st_.commandline(_sage_const_32 , r"""
sage: F13 = GF(13)
sage: PJJ = EllipticCurve(F13,[8,8])
sage: P = PJJ(5,11)
sage: INF = PJJ(0)
sage: 10*P == INF
sage: Q = PJJ(9,4)
sage: R = PJJ(4,0)
sage: 10*Q == R
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_420 )
try:
 _st_.current_tex_line = _sage_const_660 
 _st_.commandline(_sage_const_33 , r"""
sage: F13 = GF(13)
sage: L_MPJJ = []
....: for x in F13:
....:     for y in F13:
....:         if F13(7)*y^2 == x^3 + F13(6)*x^2 +x:
....:             L_MPJJ.append((x,y))
sage: MPJJ = Set(L_MPJJ)
sage: # does not compute the point at infinity
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_669 )
try:
 _st_.current_tex_line = _sage_const_696 
 _st_.commandline(_sage_const_34 , r"""
sage: # Compute PHI of Montgomery form:
sage: L_PHI_MPJJ = []
sage: for (x,y) in L_MPJJ: # LMJJ as defined previously
....:     v = (F13(3)*x + F13(6))/(F13(3)*F13(7))
....:     w = y/F13(7)
....:     L_PHI_MPJJ.append((v,w))
sage: PHI_MPJJ = Set(L_PHI_MPJJ)
sage: # Computation Weierstrass form
sage: C_WPJJ = EllipticCurve(F13,[8,8])
sage: L_WPJJ = [P.xy() for P in C_WPJJ.points() if P.order() > 1]
sage: WPJJ = Set(L_WPJJ)
sage: # check PHI(Montgomery) == Weierstrass
sage: WPJJ == PHI_MPJJ
sage: # check the inverse map PHI^(-1)
sage: L_PHIINV_WPJJ = []
sage: for (v,w) in L_WPJJ:
....:     x = F13(7)*(v-F13(4))
....:     y = F13(7)*w
....:     L_PHIINV_WPJJ.append((x,y))
sage: PHIINV_WPJJ = Set(L_PHIINV_WPJJ)
sage: MPJJ == PHIINV_WPJJ
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_718 )
try:
 _st_.current_tex_line = _sage_const_808 
 _st_.commandline(_sage_const_35 , r"""
sage: F13 = GF(13)
sage: L_EPJJ = []
....: for x in F13:
....:     for y in F13:
....:         if F13(3)*x^2 + y^2 == 1+ F13(8)*x^2*y^2:
....:             L_EPJJ.append((x,y))
sage: EPJJ = Set(L_EPJJ)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_816 )
try:
 _st_.current_tex_line = _sage_const_907 
 _st_.commandline(_sage_const_36 , r"""
sage: p = 13
sage: # large prime factor
sage: n = 5
sage: for k in range(1,5): # Fermat's little theorem
....:     if (p^k-1)%n == 0:
....:         break
sage: k
sage: # small prime factor
sage: n = 2
sage: for k in range(1,2): # Fermat's little theorem
....:     if (p^k-1)%n == 0:
....:         break
sage: k
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_921 )
try:
 _st_.current_tex_line = _sage_const_926 
 _st_.commandline(_sage_const_37 , r"""
sage: p = 115792089237316195423570985008687907853269984665640564039457584007908834671663
sage: n = 115792089237316195423570985008687907852837564279074904382605163141518161494337
sage: for k in range(1,1000):
....:     if (p^k-1)%n == 0:
....:         break
sage: k
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_933 )
try:
 _st_.current_tex_line = _sage_const_947 
 _st_.commandline(_sage_const_38 , r"""
sage: F5= GF(5)
sage: F5t.<t> = F5[]
sage: P = F5t(t^2+2)
sage: P.is_irreducible()
sage: F5_2.<t> = GF(5^2, name='t', modulus=P)
sage: E1F5_2 = EllipticCurve(F5_2,[1,1])
sage: E1F5_2.order()
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_955 )
try:
 _st_.current_tex_line = _sage_const_979 
 _st_.commandline(_sage_const_39 , r"""
sage: INF = E1F5_2(0) # Point at infinity
sage: L_E1_3 = []
sage: for p in E1F5_2:
....:     if 3*p == INF:
....:         L_E1_3.append(p)
sage: E1_3 = Set(L_E1_3) # Full 3-torsion set
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_986 )
try:
 _st_.current_tex_line = _sage_const_998 
 _st_.commandline(_sage_const_40 , r"""
sage: # define the extension field
sage: F13= GF(13) # prime field
sage: F13t.<t> = F13[] # polynomials over t
sage: P = F13t(t^4+2) # irreducible polynomial of degree 4
sage: P.is_irreducible()
sage: F13_4.<t> = GF(13^4, name='t', modulus=P) # F_{13^4}
sage: TJJF13_4 = EllipticCurve(F13_4,[8,8]) # tiny jubjub extension
sage: # compute the full 5-torsion
sage: L_TJJF13_4_5 = []
sage: INF = TJJF13_4(0)
sage: for P in INF.division_points(5): # [5]P == INF
....:     L_TJJF13_4_5.append(P)
sage: len(L_TJJF13_4_5)
sage: TJJF13_4_5 = Set(L_TJJF13_4_5)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1013 )
try:
 _st_.current_tex_line = _sage_const_1015 
 _st_.commandline(_sage_const_41 , r"""
sage: # define the extension field
sage: P = F13t(t^3+2) # irreducible polynomial of degree 3
sage: P.is_irreducible()
sage: F13_3.<t> = GF(13^3, name='t', modulus=P) # F_{13^3}
sage: TJJF13_3 = EllipticCurve(F13_3,[8,8]) # tiny jubjub extension
sage: # compute the 5-torsion
sage: L_TJJF13_3_5 = []
sage: INF = TJJF13_3(0)
sage: for P in INF.division_points(5): # [5]P == INF
....:     L_TJJF13_3_5.append(P)
sage: len(L_TJJF13_3_5)
sage: TJJF13_3_5 = Set(L_TJJF13_3_5) # full $5$-torsion
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1028 )
try:
 _st_.current_tex_line = _sage_const_1073 
 _st_.commandline(_sage_const_42 , r"""
sage: L_G1 = []
sage: for P in E1_3:
....:     PiP = E1F5_2([a.frobenius() for a in P]) # pi(P)
....:     if P == PiP:
....:         L_G1.append(P)
sage: G1 = Set(L_G1)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1080 )
try:
 _st_.current_tex_line = _sage_const_1082 
 _st_.commandline(_sage_const_43 , r"""
sage: L_G2 = []
sage: for P in E1_3:
....:     PiP = E1F5_2([a.frobenius() for a in P]) # pi(P)
....:     pP = 5*P # [5]P
....:     if pP == PiP:
....:         L_G2.append(P)
sage: G2 = Set(L_G2)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1090 )
try:
 _st_.current_tex_line = _sage_const_1095 
 _st_.commandline(_sage_const_44 , r"""
sage: L_TJJ_G1 = []
sage: for P in TJJF13_4_5:
....:     PiP = TJJF13_4([a.frobenius() for a in P]) # pi(P)
....:     if P == PiP:
....:         L_TJJ_G1.append(P)
sage: TJJ_G1 = Set(L_TJJ_G1)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1102 )
try:
 _st_.current_tex_line = _sage_const_1104 
 _st_.commandline(_sage_const_45 , r"""
sage: L_TJJ_G1 = []
sage: for P in TJJF13_4_5:
....:     PiP = TJJF13_4([a.frobenius() for a in P]) # pi(P)
....:     pP = 13*P # [5]P
....:     if pP == PiP:
....:         L_TJJ_G1.append(P)
sage: TJJ_G1 = Set(L_TJJ_G1)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1112 )
try:
 _st_.current_tex_line = _sage_const_1278 
 _st_.commandline(_sage_const_46 , r"""
sage: import Crypto
sage: from Crypto.Hash import SHA256
sage: def try_hash(s,c):
....:     s_1 = s+c
....:     h = SHA256.new(s_1)
....:     d = h.hexdigest()
....:     d = Integer(d,base=16)
....:     sign = d.str(2)[-5:-4]
....:     d = d.str(2)[-4:]
....:     z = Integer(d,base=2)
....:     return (z,sign)
sage: try_hash('10011001111010110100000111','0000')
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1291 )
try:
 _st_.current_tex_line = _sage_const_1293 
 _st_.commandline(_sage_const_47 , r"""
sage: try_hash('10011001111010110100000111','0001')
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1295 )
try:
 _st_.current_tex_line = _sage_const_1297 
 _st_.commandline(_sage_const_48 , r"""
sage: try_hash('10011001111010110100000111','0010')
sage: try_hash('10011001111010110100000111','0011')
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1300 )
try:
 _st_.current_tex_line = _sage_const_1310 
 _st_.commandline(_sage_const_49 , r"""
sage: try_hash('10011001111010110100000111','0100')
sage: try_hash('10011001111010110100000111','0101')
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1313 )
try:
 _st_.current_tex_line = _sage_const_1367 
 _st_.commandline(_sage_const_50 , r"""
sage: p = 115792089237316195423570985008687907853269984665640564039457584007908834671663
sage: r = 115792089237316195423570985008687907852837564279074904382605163141518161494337
sage: t = p + 1 -r
sage: t.nbits()
sage: abs(RR(t)) <= 2*sqrt(RR(p))
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1373 )
try:
 _st_.current_tex_line = _sage_const_1404 
 _st_.commandline(_sage_const_51 , r"""
sage: p = 115792089237316195423570985008687907853269984665640564039457584007908834671663
sage: F = GF(p)
sage: j = F(1728)*((F(4)*F(0)^3)/(F(4)*F(0)^3+F(27)*F(7)^2))
sage: j == F(0)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1409 )
try:
 _st_.current_tex_line = _sage_const_1453 
 _st_.commandline(_sage_const_52 , r"""
sage: z = ComplexField(100)(0,1)
sage: z # (0+1i)
sage: elliptic_j(z)
sage: # j-function only defined for positive imaginary arguments
sage: z = ComplexField(100)(1,-1)
sage: try:
....:     elliptic_j(z)
....: except PariError:
....:     pass
sage: # root at (-1+i sqrt(3))/2
sage: z = ComplexField(100)(-1,sqrt(3))/2
sage: elliptic_j(z)
sage: elliptic_j(z).imag().round()
sage: elliptic_j(z).real().round()
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1468 )
try:
 _st_.current_tex_line = _sage_const_1629 
 _st_.commandline(_sage_const_53 , r"""
sage: D = -3
sage: p = 115792089237316195423570985008687907853269984665640564039457584007908834671663
sage: r = 115792089237316195423570985008687907852837564279074904382605163141518161494337
sage: t = p+1-r
sage: v_sqr = (4*p - t^2)/abs(D)
sage: v_sqr.is_integer()
sage: v = sqrt(v_sqr)
sage: v.is_integer()
sage: 4*p == t^2 + abs(D)*v^2
sage: v
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1640 )
try:
 _st_.current_tex_line = _sage_const_1645 
 _st_.commandline(_sage_const_54 , r"""
sage: F = GF(p)
sage: for c2 in F:
....:     try: # quadratic residue
....:         _ = c2.nth_root(2)
....:     except ValueError: # quadratic non residue
....:         break
sage: c2
sage: for c3 in F:
....:     try:
....:         _ = c3.nth_root(3)
....:     except ValueError:
....:         break
sage: c3
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1659 )
try:
 _st_.current_tex_line = _sage_const_1661 
 _st_.commandline(_sage_const_55 , r"""
sage: C1 = EllipticCurve(F,[0,1])
sage: C1.order() == r
sage: C2 = EllipticCurve(F,[0,c2^3])
sage: C2.order() == r
sage: C3 = EllipticCurve(F,[0,c3^2])
sage: C3.order() == r
sage: C4 = EllipticCurve(F,[0,c3^2*c2^3])
sage: C4.order() == r
sage: C5 = EllipticCurve(F,[0,c3^(-2)])
sage: C5.order() == r
sage: C6 = EllipticCurve(F,[0,c3^(-2)*c2^3])
sage: C6.order() == r
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1674 )
try:
 _st_.current_tex_line = _sage_const_1684 
 _st_.commandline(_sage_const_56 , r"""
sage: b1=86844066927987146567678238756515930889952488499230423029593188005931626003754
sage: for b2 in F:
....:     try:
....:         d = (b2/b1).nth_root(3)
....:         try:
....:             _ = d.nth_root(2)
....:             if d != 0:
....:                 break
....:         except ValueError:
....:             pass
....:     except ValueError:
....:         pass
sage: b2
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1698 )
try:
 _st_.current_tex_line = _sage_const_1745 
 _st_.commandline(_sage_const_57 , r"""
sage: for k in range(1,42): # Fermat's little theorem
....:     if (43^k-1)%13 == 0:
....:         break
sage: k
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1750 )
try:
 _st_.current_tex_line = _sage_const_1763 
 _st_.commandline(_sage_const_58 , r"""
sage: F43 = GF(43)
sage: c2 = F43(5)
....: try: # quadratic residue
....:     c2.nth_root(2)
....: except ValueError: # quadratic non residue
....:     c2
sage: c3 =F43(36)
....: try:
....:     c3.nth_root(3)
....: except ValueError:
....:     c3
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1775 )
try:
 _st_.current_tex_line = _sage_const_1779 
 _st_.commandline(_sage_const_59 , r"""
sage: BLS61 = EllipticCurve(F43,[0,1])
sage: BLS61.order() == 39
sage: BLS62 = EllipticCurve(F43,[0,c2^3])
sage: BLS62.order() == 39
sage: BLS63 = EllipticCurve(F43,[0,c3^2])
sage: BLS63.order() == 39
sage: BLS64 = EllipticCurve(F43,[0,c3^2*c2^3])
sage: BLS64.order() == 39
sage: BLS65 = EllipticCurve(F43,[0,c3^(-2)])
sage: BLS65.order() == 39
sage: BLS66 = EllipticCurve(F43,[0,c3^(-2)*c2^3])
sage: BLS66.order() == 39
sage: BLS6 = BLS63 # our BLS6 curve in the book
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1793 )
_st_.current_tex_line = _sage_const_1799 
_st_.blockbegin()
try:
 BLS63p = BLS63.plot()
except:
 _st_.goboom(_sage_const_1801 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_1803 
 _st_.plot(_sage_const_8 , format='notprovided', _p_=BLS63p)
except:
 _st_.goboom(_sage_const_1803 )
try:
 _st_.current_tex_line = _sage_const_1822 
 _st_.commandline(_sage_const_60 , r"""
sage: P = BLS6(9,2)
sage: Q = 3*P
sage: Q.xy()
sage: BLS6_13 = []
sage: for x in range(0,13): # cyclic of order 13
....:     P = x*Q
....:     BLS6_13.append(P)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1830 )
try:
 _st_.current_tex_line = _sage_const_1904 
 _st_.commandline(_sage_const_61 , r"""
sage: F43 = GF(43)
sage: F43t.<t> = F43[]
sage: p = F43t(t^6+6)
sage: p.is_irreducible()
sage: F43_6.<v> = GF(43^6, name='v', modulus=p)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1910 )
try:
 _st_.current_tex_line = _sage_const_1916 
 _st_.commandline(_sage_const_62 , r"""
sage: BLS6 = EllipticCurve (F43_6,[0 ,6]) # curve extension
sage: INF = BLS6(0) # point at infinity
sage: for P in INF.division_points(13): # full 13-torsion
....: # PI(P) == [q]P
....:     if P.order() == 13: # exclude point at infinity
....:         PiP = BLS6([a.frobenius() for a in P])
....:         qP = 43*P
....:         if PiP == qP:
....:             break
sage: P.xy()
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1927 )
try:
 _st_.current_tex_line = _sage_const_1933 
 _st_.commandline(_sage_const_63 , r"""
sage: Q = BLS6(7*v^2,16*v^3)
sage: BLS6_13_2 = []
sage: for x in range(0,13):
....:     P = x*Q
....:     BLS6_13_2.append(P)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1939 )
try:
 _st_.current_tex_line = _sage_const_1974 
 _st_.commandline(_sage_const_64 , r"""
sage: g1 = BLS6([13,15])
sage: g2 = BLS6([7*v^2, 16*v^3])
sage: g1.weil_pairing(g2,13)
""", globals(), locals(), True)
except:
 _st_.goboom(_sage_const_1978 )
_st_.endofdoc()

