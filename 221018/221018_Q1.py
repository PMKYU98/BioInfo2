sInput1 = '''
4
0   23  27  20
23  0   30  28
27  30  0   30
20  28  30  0
'''

sInput2 = '''
4
0   13  21  22
13  0   12  13
21  12  0   13
22  13  13  0
'''

sInput3 = '''
32
0	1930	1458	1837	1593	1764	1705	1372	1332	1343	1556	1476	1907	1233	1128	1464	1088	1420	1469	1275	1658	1975	1444	1454	1617	1543	1228	1691	1987	1991	1282	1423	
1930	0	1219	1107	1426	1196	1571	1272	1240	1610	1696	1763	1505	1898	1116	1623	1903	1283	1447	1184	1958	1998	1899	1582	1269	1641	1595	1955	1836	1830	1913	1804	
1458	1219	0	1416	1653	1629	2044	1321	1365	1256	1391	1667	1938	1455	1942	1123	1084	1358	1574	1300	1718	1474	1101	1964	1480	1778	1926	1134	1135	1894	1694	1536	
1837	1107	1416	0	1515	1211	1788	1720	1550	2040	1083	1484	1954	1349	1333	1665	1549	1758	1448	1523	1098	2004	1747	1594	1436	1959	1676	1031	1686	1168	1929	1943	
1593	1426	1653	1515	0	1266	1967	1433	1786	1534	1607	1320	1915	1806	1336	1417	1951	1466	1381	1475	1901	1277	2022	1852	1933	1503	1752	1214	1331	1265	1164	1077	
1764	1196	1629	1211	1266	0	1554	1626	1638	1329	1790	1525	1684	1305	1562	1746	1892	1688	1376	1200	1533	1851	1198	1452	1621	1271	1177	1940	1648	1728	1528	1697	
1705	1571	2044	1788	1967	1554	0	1048	1565	1109	2003	1039	1904	1176	2031	1190	1661	1312	1295	1043	1287	1612	1960	1234	1882	1306	1844	1434	1636	1888	1113	1375	
1372	1272	1321	1720	1433	1626	1048	0	1726	2008	1100	1508	1405	1496	1509	1545	1849	1827	1820	1948	1056	1927	1701	1784	1274	1599	1910	1692	1156	1858	1140	1541	
1332	1240	1365	1550	1786	1638	1565	1726	0	1587	1213	1873	2047	1247	1671	1566	1052	1682	1346	1547	1611	1383	1835	1360	1976	1759	1966	1385	1121	1624	1568	2019	
1343	1610	1256	2040	1534	1329	1109	2008	1587	0	1657	1702	1431	1397	1925	1524	1643	1456	1355	1816	1600	1094	1148	1115	1297	1344	1570	1218	1585	1354	1330	1042	
1556	1696	1391	1083	1607	1790	2003	1100	1213	1657	0	1932	1870	1303	1352	1032	1035	1049	1057	1451	1051	1950	1874	1338	1153	1639	2011	1324	1732	1495	1486	1159	
1476	1763	1667	1484	1320	1525	1039	1508	1873	1702	1932	0	1313	1596	1561	1407	1709	1117	1322	1744	2045	1154	1779	1477	1443	2026	1250	1166	1995	2009	1555	1792	
1907	1505	1938	1954	1915	1684	1904	1405	2047	1431	1870	1313	0	1504	1440	1082	1529	1169	1745	1608	1603	1677	1414	1814	1192	1712	1138	1210	1622	1406	1182	1055	
1233	1898	1455	1349	1806	1305	1176	1496	1247	1397	1303	1596	1504	0	1370	1457	2024	1489	1908	1774	1471	1877	1511	1730	1203	1103	1646	1902	1175	1650	1085	1862	
1128	1116	1942	1333	1336	1562	2031	1509	1671	1925	1352	1561	1440	1370	0	1936	1581	1822	1027	1290	2001	1531	1649	1299	1689	1866	1659	1317	1669	1063	1311	1386	
1464	1623	1123	1665	1417	1746	1190	1545	1566	1524	1032	1407	1082	1457	1936	0	1105	1782	1450	1108	1558	1353	1618	1293	1187	1281	1359	1351	2013	1507	1761	1403	
1088	1903	1084	1549	1951	1892	1661	1849	1052	1643	1035	1709	1529	2024	1581	1105	0	1188	2014	1435	1348	1922	1409	1846	1770	1937	1204	1399	1411	2029	1833	1432	
1420	1283	1358	1758	1466	1688	1312	1827	1682	1456	1049	1117	1169	1489	1822	1782	1188	0	1734	1754	1729	1132	1286	1342	1651	1374	1700	1973	1992	1445	1046	1845	
1469	1447	1574	1448	1381	1376	1295	1820	1346	1355	1057	1322	1745	1908	1027	1450	2014	1734	0	1828	1685	1291	1579	2028	1811	1334	1743	1997	1206	2018	1777	1205	
1275	1184	1300	1523	1475	1200	1043	1948	1547	1816	1451	1744	1608	1774	1290	1108	1435	1754	1828	0	1337	2023	1127	1988	1248	1773	1740	1393	1631	1229	1891	1167	
1658	1958	1718	1098	1901	1533	1287	1056	1611	1600	1051	2045	1603	1471	2001	1558	1348	1729	1685	1337	0	1981	1106	1514	1934	1080	1453	1742	2002	1225	1171	2006	
1975	1998	1474	2004	1277	1851	1612	1927	1383	1094	1950	1154	1677	1877	1531	1353	1922	1132	1291	2023	1981	0	1341	1517	1071	1296	1914	1681	1893	1912	1551	1577	
1444	1899	1101	1747	2022	1198	1960	1701	1835	1148	1874	1779	1414	1511	1649	1618	1409	1286	1579	1127	1106	1341	0	1751	1878	1427	1222	1246	1867	1821	1335	1253	
1454	1582	1964	1594	1852	1452	1234	1784	1360	1115	1338	1477	1814	1730	1299	1293	1846	1342	2028	1988	1514	1517	1751	0	1724	1900	2048	2042	2046	1970	1267	1288	
1617	1269	1480	1436	1933	1621	1882	1274	1976	1297	1153	1443	1192	1203	1689	1187	1770	1651	1811	1248	1934	1071	1878	1724	0	1230	1076	1189	2017	1544	1227	1371	
1543	1641	1778	1959	1503	1271	1306	1599	1759	1344	1639	2026	1712	1103	1866	1281	1937	1374	1334	1773	1080	1296	1427	1900	1230	0	1124	1482	1803	1237	2005	1478	
1228	1595	1926	1676	1752	1177	1844	1910	1966	1570	2011	1250	1138	1646	1659	1359	1204	1700	1743	1740	1453	1914	1222	2048	1076	1124	0	1860	1548	1382	1739	1033	
1691	1955	1134	1031	1214	1940	1434	1692	1385	1218	1324	1166	1210	1902	1317	1351	1399	1973	1997	1393	1742	1681	1246	2042	1189	1482	1860	0	1276	1028	1616	1818	
1987	1836	1135	1686	1331	1648	1636	1156	1121	1585	1732	1995	1622	1175	1669	2013	1411	1992	1206	1631	2002	1893	1867	2046	2017	1803	1548	1276	0	1813	1815	1119	
1991	1830	1894	1168	1265	1728	1888	1858	1624	1354	1495	2009	1406	1650	1063	1507	2029	1445	2018	1229	1225	1912	1821	1970	1544	1237	1382	1028	1813	0	2007	1418	
1282	1913	1694	1929	1164	1528	1113	1140	1568	1330	1486	1555	1182	1085	1311	1761	1833	1046	1777	1891	1171	1551	1335	1267	1227	2005	1739	1616	1815	2007	0	1802	
1423	1804	1536	1943	1077	1697	1375	1541	2019	1042	1159	1792	1055	1862	1386	1403	1432	1845	1205	1167	2006	1577	1253	1288	1371	1478	1033	1818	1119	1418	1802	0	
'''

sInput = sInput3

def PRINT_TREE(tree):
    for edge in sorted(tree):
        print('%d->%d:%.3f' % (edge[0], edge[1], edge[2]))

def DELETE_EDGE(tree, st, ed):
    for i in range(len(tree)):
        if st == tree[i][0] and ed == tree[i][1]:
            del tree[i]
            break

    for i in range(len(tree)):
        if st == tree[i][1] and ed == tree[i][0]:
            del tree[i]
            break

def ADD_EDGE(tree, st, ed, dist):
    tree.append((st, ed, dist))
    tree.append((ed, st, dist))
    global maxnode

def PRINT_MATRIX(mat, newline=False):
    if newline: print('')
    for l in mat:
        print('\t'.join([str(i) for i in l]))

def PARSE(sInput, delimiter=' '):
    lines = sInput.strip().split('\n')
    n = int(lines[0])

    matD = []
    for l in lines[1:]:
        matD.append([int(x) for x in l.split(delimiter) if x != ''])

    return n, matD

def TOTAL_DISTANCE(i, matD):
    return sum(matD[i])

def NEIGHBOR_MATRIX(n, matD):
    matDstar = []
    for i in range(len(matD)):
        totalDistance_i = TOTAL_DISTANCE(i, matD)
        newRow = []
        for j in range(len(matD[i])):
            if i == j: newRow.append(0)
            else: 
                totalDistance_j = TOTAL_DISTANCE(j, matD)
                newRow.append((n - 2) * matD[i][j] - totalDistance_i - totalDistance_j)
        matDstar.append(newRow)

    return matDstar

def FIND_MINPOS(mat):
    minValue, minY, minX = 0, 0, 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] < minValue:
                minValue, minY, minX = mat[i][j], i, j

    return minY, minX

def MERGE_IJ(i, j, matD):
    global lstClstrs, dirChildren

    matDnew = []
    for y in range(len(matD)):
        if y == i or y == j: continue
        else:
            newRow = [matD[y][x] for x in range(len(matD[y])) if x != i and x != j]
            newRow.append((matD[y][i] + matD[y][j] - matD[i][j]) / 2)
            matDnew.append(newRow)
    
    newRow = [matDnew[y][-1] for y in range(len(matDnew))] + [0]
    matDnew.append(newRow)
        
    new = max(lstClstrs) + 1
    temp = []
    for idx in range(len(lstClstrs)):
        if idx == i or idx == j: continue
        else: temp.append(lstClstrs[idx])
    temp.append(new)

    dirChildren[new] = (lstClstrs[i], lstClstrs[j])
    lstClstrs = temp

    return new, matDnew

def INITIALIZE(n):
    lstClstrs = [i for i in range(n)]
    dirChildren = {}
    dirLimb = {}
    return lstClstrs, dirChildren, dirLimb

def NEIGHBOR_JOINING(n, matD):
    global lstClstrs
    tree = []

    while len(lstClstrs) > 1:
        if len(lstClstrs) == 2:
            ADD_EDGE(tree, lstClstrs[0], lstClstrs[1], matD[0][1])
            return tree

        matDstar = NEIGHBOR_MATRIX(n, matD)
        minY, minX = FIND_MINPOS(matDstar)
        
        delta = (TOTAL_DISTANCE(minY, matD) - TOTAL_DISTANCE(minX, matD)) / (n - 2)
        i, j = lstClstrs[minY], lstClstrs[minX]
        limb_i = (matD[minY][minX] + delta) / 2
        limb_j = (matD[minY][minX] - delta) / 2

        newnode, matD = MERGE_IJ(minY, minX, matD)
        ADD_EDGE(tree, newnode, i, limb_i)
        ADD_EDGE(tree, newnode, j, limb_j)
        n -= 1

    return tree

      
n, matD = PARSE(sInput, delimiter='\t')
lstClstrs, dirChildren, dirLimb = INITIALIZE(n)
Tree = NEIGHBOR_JOINING(n, matD)
PRINT_TREE(Tree)