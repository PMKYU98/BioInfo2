sInput1 = '''
4
1
0   13  21  22
13  0   12  13
21  12  0   13
22  13  13  0
'''

sInput2 = '''
25
2
0 6806 3415 3666 8467 1175 6105 4705 1537 5183 4463 2616 2156 9275 3315 7970 4217 2632 7561 8857 4047 9129 4972 3729 8378
6806 0 9639 9890 3615 7399 2689 10929 6371 11407 2849 5972 8380 4423 4905 3118 3723 8856 2709 4005 3737 4277 11196 9953 3526
3415 9639 0 1319 11300 2886 8938 2358 4370 2836 7296 5449 2541 12108 6148 10803 7050 1061 10394 11690 6880 11962 2625 1382 11211
3666 9890 1319 0 11551 3137 9189 2035 4621 2513 7547 5700 2792 12359 6399 11054 7301 1312 10645 11941 7131 12213 2302 1059 11462
8467 3615 11300 11551 0 9060 4350 12590 8032 13068 4510 7633 10041 1978 6566 2249 5384 10517 2904 1560 5398 1832 12857 11614 1207
1175 7399 2886 3137 9060 0 6698 4176 2130 4654 5056 3209 1627 9868 3908 8563 4810 2103 8154 9450 4640 9722 4443 3200 8971
6105 2689 8938 9189 4350 6698 0 10228 5670 10706 2148 5271 7679 5158 4204 3853 3022 8155 3444 4740 3036 5012 10495 9252 4261
4705 10929 2358 2035 12590 4176 10228 0 5660 2166 8586 6739 3831 13398 7438 12093 8340 2351 11684 12980 8170 13252 1955 1736 12501
1537 6371 4370 4621 8032 2130 5670 5660 0 6138 4028 2181 3111 8840 2880 7535 3782 3587 7126 8422 3612 8694 5927 4684 7943
5183 11407 2836 2513 13068 4654 10706 2166 6138 0 9064 7217 4309 13876 7916 12571 8818 2829 12162 13458 8648 13730 1033 2214 12979
4463 2849 7296 7547 4510 5056 2148 8586 4028 9064 0 3629 6037 5318 2562 4013 1380 6513 3604 4900 1394 5172 8853 7610 4421
2616 5972 5449 5700 7633 3209 5271 6739 2181 7217 3629 0 4190 8441 2481 7136 3383 4666 6727 8023 3213 8295 7006 5763 7544
2156 8380 2541 2792 10041 1627 7679 3831 3111 4309 6037 4190 0 10849 4889 9544 5791 1758 9135 10431 5621 10703 4098 2855 9952
9275 4423 12108 12359 1978 9868 5158 13398 8840 13876 5318 8441 10849 0 7374 3057 6192 11325 3712 716 6206 1332 13665 12422 2015
3315 4905 6148 6399 6566 3908 4204 7438 2880 7916 2562 2481 4889 7374 0 6069 2316 5365 5660 6956 2146 7228 7705 6462 6477
7970 3118 10803 11054 2249 8563 3853 12093 7535 12571 4013 7136 9544 3057 6069 0 4887 10020 2407 2639 4901 2911 12360 11117 2160
4217 3723 7050 7301 5384 4810 3022 8340 3782 8818 1380 3383 5791 6192 2316 4887 0 6267 4478 5774 1148 6046 8607 7364 5295
2632 8856 1061 1312 10517 2103 8155 2351 3587 2829 6513 4666 1758 11325 5365 10020 6267 0 9611 10907 6097 11179 2618 1375 10428
7561 2709 10394 10645 2904 8154 3444 11684 7126 12162 3604 6727 9135 3712 5660 2407 4478 9611 0 3294 4492 3566 11951 10708 2815
8857 4005 11690 11941 1560 9450 4740 12980 8422 13458 4900 8023 10431 716 6956 2639 5774 10907 3294 0 5788 914 13247 12004 1597
4047 3737 6880 7131 5398 4640 3036 8170 3612 8648 1394 3213 5621 6206 2146 4901 1148 6097 4492 5788 0 6060 8437 7194 5309
9129 4277 11962 12213 1832 9722 5012 13252 8694 13730 5172 8295 10703 1332 7228 2911 6046 11179 3566 914 6060 0 13519 12276 1869
4972 11196 2625 2302 12857 4443 10495 1955 5927 1033 8853 7006 4098 13665 7705 12360 8607 2618 11951 13247 8437 13519 0 2003 12768
3729 9953 1382 1059 11614 3200 9252 1736 4684 2214 7610 5763 2855 12422 6462 11117 7364 1375 10708 12004 7194 12276 2003 0 11525
8378 3526 11211 11462 1207 8971 4261 12501 7943 12979 4421 7544 9952 2015 6477 2160 5295 10428 2815 1597 5309 1869 12768 11525 0
'''

sInput3 = '''
24
9
0 1059 2462 7081 3275 4944 6321 2906 4447 5463 1029 4033 1257 1643 2954 6308 6793 529 3084 2312 5791 5826 2858 1987
1059 0 1517 8020 4214 5883 7260 1961 5386 6402 1968 4972 498 698 2009 7247 7732 852 4023 3251 6730 6765 1913 1042
2462 1517 0 9423 5617 7286 8663 710 6789 7805 3371 6375 1901 1079 1414 8650 9135 2255 5426 4654 8133 8168 662 945
7081 8020 9423 0 4972 2415 2154 9867 4330 2590 6840 3266 8218 8604 9915 2423 1232 7490 5327 6189 2332 1355 9819 8948
3275 4214 5617 4972 0 2835 4212 6061 2338 3354 3034 1924 4412 4798 6109 4199 4684 3684 1521 2383 3682 3717 6013 5142
4944 5883 7286 2415 2835 0 1655 7730 2193 797 4703 1129 6081 6467 7778 1642 2127 5353 3190 4052 1125 1160 7682 6811
6321 7260 8663 2154 4212 1655 0 9107 3570 1830 6080 2506 7458 7844 9155 1663 1866 6730 4567 5429 1572 899 9059 8188
2906 1961 710 9867 6061 7730 9107 0 7233 8249 3815 6819 2345 1523 1858 9094 9579 2699 5870 5098 8577 8612 920 1389
4447 5386 6789 4330 2338 2193 3570 7233 0 2712 4206 1282 5584 5970 7281 3557 4042 4856 2693 3555 3040 3075 7185 6314
5463 6402 7805 2590 3354 797 1830 8249 2712 0 5222 1648 6600 6986 8297 1817 2302 5872 3709 4571 1300 1335 8201 7330
1029 1968 3371 6840 3034 4703 6080 3815 4206 5222 0 3792 2166 2552 3863 6067 6552 1438 2843 2071 5550 5585 3767 2896
4033 4972 6375 3266 1924 1129 2506 6819 1282 1648 3792 0 5170 5556 6867 2493 2978 4442 2279 3141 1976 2011 6771 5900
1257 498 1901 8218 4412 6081 7458 2345 5584 6600 2166 5170 0 1082 2393 7445 7930 1050 4221 3449 6928 6963 2297 1426
1643 698 1079 8604 4798 6467 7844 1523 5970 6986 2552 5556 1082 0 1571 7831 8316 1436 4607 3835 7314 7349 1475 604
2954 2009 1414 9915 6109 7778 9155 1858 7281 8297 3863 6867 2393 1571 0 9142 9627 2747 5918 5146 8625 8660 1810 1437
6308 7247 8650 2423 4199 1642 1663 9094 3557 1817 6067 2493 7445 7831 9142 0 2135 6717 4554 5416 1559 1168 9046 8175
6793 7732 9135 1232 4684 2127 1866 9579 4042 2302 6552 2978 7930 8316 9627 2135 0 7202 5039 5901 2044 1067 9531 8660
529 852 2255 7490 3684 5353 6730 2699 4856 5872 1438 4442 1050 1436 2747 6717 7202 0 3493 2721 6200 6235 2651 1780
3084 4023 5426 5327 1521 3190 4567 5870 2693 3709 2843 2279 4221 4607 5918 4554 5039 3493 0 2192 4037 4072 5822 4951
2312 3251 4654 6189 2383 4052 5429 5098 3555 4571 2071 3141 3449 3835 5146 5416 5901 2721 2192 0 4899 4934 5050 4179
5791 6730 8133 2332 3682 1125 1572 8577 3040 1300 5550 1976 6928 7314 8625 1559 2044 6200 4037 4899 0 1077 8529 7658
5826 6765 8168 1355 3717 1160 899 8612 3075 1335 5585 2011 6963 7349 8660 1168 1067 6235 4072 4934 1077 0 8564 7693
2858 1913 662 9819 6013 7682 9059 920 7185 8201 3767 6771 2297 1475 1810 9046 9531 2651 5822 5050 8529 8564 0 1341
1987 1042 945 8948 5142 6811 8188 1389 6314 7330 2896 5900 1426 604 1437 8175 8660 1780 4951 4179 7658 7693 1341 0
'''

sInput = sInput3

def PRINT_MATRIX(mat):
    for l in mat:
        print('\t'.join([str(i) for i in l]))

def MATRIX_TO_FILE(mat):
    temp = ['']
    for l in mat:
        temp.append('\t'.join([str(i) for i in l]))
    temp.append('')

    sOutput = '\n'.join(temp)
    with open('221011/221011_Q1_output.txt', 'w') as f:
        f.write(sOutput)

def PARSE(sInput):
    lines = sInput.strip().split('\n')
    n = int(lines[0])
    j = int(lines[1])

    matDist = []
    for l in lines[2:]:
        matDist.append([int(x) for x in l.split(' ') if x != ''])

    return n, j, matDist

def LIMBLENGTH(i):
    global n, matDist
    lstDist = matDist[i]

    temp = []
    for j in range(n):
        if j == i: continue
        for k in range(j, n):
            if k == i: continue
            dist = lstDist[j] + lstDist[k] - matDist[j][k]
            temp.append(int(dist/2))
    
    print(min(temp))

n, j, matDist = PARSE(sInput)
LIMBLENGTH(j)