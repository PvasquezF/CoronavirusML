from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy
import matplotlib.pyplot 
import json

def pinta(ax,ay,sec, graph):
    matplotlib.pyplot.figure()
    matplotlib.pyplot.scatter(ax, ay)
    matplotlib.pyplot.plot(sec, graph.predict(sec), color="red")
    matplotlib.pyplot.title("Regresion Polinomial")
    matplotlib.pyplot.savefig('Muertes en el departamento de Guatemala por Covid19')
    matplotlib.pyplot.show()

def analisis(municipio):
    municipio.insert(0, 0)
    y = numpy.array(municipio)
    x = numpy.array(range(len(municipio)))
    sec = numpy.linspace(x.min(), x.max(), len(municipio)).reshape(-1, 1)
    value=9
    graph=make_pipeline(PolynomialFeatures(value), LinearRegression())
    graph.fit(x[:, numpy.newaxis], y)
    pinta(x,y,sec, graph)
    
def sumalista(listaNumeros):
    laSuma = 0
    for i in listaNumeros:
        laSuma = laSuma + i
    return laSuma

fechas =["2020-02-13","2020-02-14","2020-02-15","2020-02-16","2020-02-17","2020-02-18","2020-02-19","2020-02-20","2020-02-21","2020-02-22","2020-02-23","2020-02-24","2020-02-25","2020-02-26","2020-02-27","2020-02-28","2020-02-29","2020-03-01","2020-03-02","2020-03-03","2020-03-04","2020-03-05","2020-03-06","2020-03-07","2020-03-08","2020-03-09","2020-03-10","2020-03-11","2020-03-12","2020-03-13","2020-03-14","2020-03-15","2020-03-16","2020-03-17","2020-03-18","2020-03-19","2020-03-20","2020-03-21","2020-03-22","2020-03-23","2020-03-24","2020-03-25","2020-03-26","2020-03-27","2020-03-28","2020-03-29","2020-03-30","2020-03-31","2020-04-01","2020-04-02","2020-04-03","2020-04-04","2020-04-05","2020-04-06","2020-04-07","2020-04-08","2020-04-09","2020-04-10","2020-04-11","2020-04-12","2020-04-13","2020-04-14","2020-04-15","2020-04-16","2020-04-17","2020-04-18","2020-04-19","2020-04-20","2020-04-21","2020-04-22","2020-04-23","2020-04-24","2020-04-25","2020-04-26","2020-04-27","2020-04-28","2020-04-29","2020-04-30","2020-05-01","2020-05-02","2020-05-03","2020-05-04","2020-05-05","2020-05-06","2020-05-07","2020-05-08","2020-05-09","2020-05-10","2020-05-11","2020-05-12","2020-05-13","2020-05-14","2020-05-15","2020-05-16","2020-05-17","2020-05-18","2020-05-19","2020-05-20","2020-05-21","2020-05-22","2020-05-23","2020-05-24","2020-05-25","2020-05-26","2020-05-27","2020-05-28","2020-05-29","2020-05-30","2020-05-31","2020-06-01","2020-06-02","2020-06-03","2020-06-04","2020-06-05","2020-06-06","2020-06-07","2020-06-08","2020-06-09","2020-06-10","2020-06-11","2020-06-12","2020-06-13","2020-06-14","2020-06-15","2020-06-16","2020-06-17","2020-06-18","2020-06-19","2020-06-20","2020-06-21","2020-06-22","2020-06-23","2020-06-24","2020-06-25","2020-06-26","2020-06-27","2020-06-28","2020-06-29","2020-06-30","2020-07-01","2020-07-02","2020-07-03","2020-07-04","2020-07-05","2020-07-06","2020-07-07","2020-07-08","2020-07-09","2020-07-10","2020-07-11","2020-07-12","2020-07-13","2020-07-14","2020-07-15","2020-07-16","2020-07-17","2020-07-18","2020-07-19","2020-07-20","2020-07-21","2020-07-22","2020-07-23","2020-07-24","2020-07-25","2020-07-26","2020-07-27","2020-07-28","2020-07-29","2020-07-30","2020-07-31","2020-08-01","2020-08-02","2020-08-03","2020-08-04","2020-08-05","2020-08-06","2020-08-07","2020-08-08","2020-08-09","2020-08-10","2020-08-11","2020-08-12","2020-08-13","2020-08-14","2020-08-15","2020-08-16","2020-08-17","2020-08-18","2020-08-19","2020-08-20","2020-08-21","2020-08-22","2020-08-23","2020-08-24","2020-08-25","2020-08-26","2020-08-27","2020-08-28","2020-08-29","2020-08-30","2020-08-31","2020-09-01","2020-09-02","2020-09-03","2020-09-04","2020-09-05","2020-09-06","2020-09-07","2020-09-08","2020-09-09","2020-09-10","2020-09-11","2020-09-12","2020-09-13","2020-09-14","2020-09-15","2020-09-16","2020-09-17","2020-09-18","2020-09-19","2020-09-20","2020-09-21","2020-09-22","2020-09-23","2020-09-24","2020-09-25","2020-09-26","2020-09-27","2020-09-28","2020-09-29","2020-09-30","2020-10-01","2020-10-02","2020-10-03","2020-10-04","2020-10-05","2020-10-06","2020-10-07","2020-10-08","2020-10-09","2020-10-10","2020-10-11","2020-10-12","2020-10-13","2020-10-14","2020-10-15","2020-10-16","2020-10-17","2020-10-18","2020-10-19","2020-10-20","2020-10-21","2020-10-22","2020-10-23","2020-10-24","2020-10-25","2020-10-26","2020-10-27","2020-10-28","2020-10-29","2020-10-30","2020-10-31","2020-11-01","2020-11-02","2020-11-03","2020-11-04","2020-11-05","2020-11-06","2020-11-07","2020-11-08"]
alta_vera=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,2,0,0,0,0,0,1,0,0,1,0,1,1,0,1,0,1,2,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,0,0,0,1,0,0,2,1,1,0,0,0,0,0,0,0,0,1,0,0,0,3,2,0,0,2,0,0,1,1,0,0,0,1,0,2,0,0,1,0,3,0,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,2,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,2,0,0,0,0,0,0,0,0,1,0,0]
baja_vera=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,1,0,1,0,0,1,1,1,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,2,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
chimalten=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,2,0,1,3,0,0,0,0,0,1,1,0,0,0,1,2,1,1,1,0,0,1,0,0,1,0,1,0,0,0,0,3,1,1,1,3,3,1,0,0,1,1,3,1,2,0,0,1,0,1,0,2,3,3,1,3,2,0,1,3,0,0,2,0,0,4,0,0,0,3,1,2,1,1,1,1,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,2,0,0,0,0,1,1,0,1,1,0,0,0,0,3,0,0,0,1,2,2,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,1,0,0,0,1,0,0,0,0]
chiquimul=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0,0,0,0,1,1,0,0,1,1,2,1,3,0,0,0,1,0,0,2,1,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0]
el_progre=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,1,0,0,1,0,2,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,3,1,0,0,1,1,2,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,2,0,1,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
escuintla=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,2,1,0,1,0,0,1,2,1,1,0,2,1,1,2,0,4,1,1,1,3,4,2,2,1,3,4,5,5,1,5,9,5,7,5,9,3,4,6,7,5,5,4,5,3,4,6,6,5,7,3,3,3,5,2,3,1,6,0,3,2,1,2,2,2,5,1,2,2,2,2,0,2,2,2,0,1,2,2,1,3,0,0,0,0,3,0,0,0,1,2,0,1,0,0,2,0,0,1,1,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,1,1,0,1,0,0,0,2,0,0,0,1,0,0,0,0,0,2,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,1,0,0]
guatemala=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,5,5,5,5,5,5,6,6,6,6,6,6,7,7,8,8,8,9,9,9,10,11,12,13,14,14,14,15,15,15,17,19,21,23,24,25,30,34,37,43,48,55,60,73,80,88,93,102,117,126,137,147,156,177,187,202,220,231,250,267,288,312,330,349,367,390,413,430,458,474,488,510,526,545,567,588,614,640,669,699,720,743,766,788,810,836,875,899,930,961,998,1034,1065,1109,1131,1152,1179,1200,1232,1251,1282,1299,1328,1342,1362,1383,1404,1424,1434,1458,1473,1482,1495,1510,1523,1534,1548,1557,1571,1577,1588,1604,1612,1619,1630,1640,1646,1655,1663,1681,1689,1701,1711,1711,1715,1724,1733,1739,1741,1744,1750,1753,1761,1765,1769,1780,1782,1788,1793,1798,1800,1806,1810,1816,1820,1824,1829,1829,1832,1833,1834,1841,1845,1851,1852,1856,1859,1860,1865,1867,1869,1871,1876,1881,1884,1886,1889,1889,1896,1898,1899,1904,1909,1911,1916,1919,1920,1923,1926,1929,1932,1935,1935,1941,1943,1944,1946,1948,1954,1956,1959,1960,1964,1968,1973,1975,1976,1977,1978,1980,1981,1981]
huehueten=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,2,0,1,0,0,0,0,0,1,1,0,2,0,2,0,0,0,0,0,1,0,0,3,0,1,0,0,1,0,0,0,1,0,0,0,1,1,1,1,1,2,0,2,0,1,0,2,0,1,1,0,0,1,1,0,1,2,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,1,1,1,0,0,2,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0]
izabal=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,2,2,2,1,0,1,3,5,1,0,0,0,2,1,0,2,1,1,2,0,0,1,5,2,0,1,2,2,1,1,1,5,4,1,6,3,1,4,2,1,1,2,1,1,2,0,2,2,1,2,3,3,0,1,2,0,0,1,4,1,1,0,3,3,2,3,1,1,0,1,0,1,0,1,0,0,2,1,1,1,1,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,2,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,1,0,0,0,2,0,0,1,0,0,0,0,0,0,0,0,0]
jalapa=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
jutiapa=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,2,1,0,0,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,1,0,0,0,1,2,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
peten=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,2,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,2,4,5,1,0,0,1,0,2,0,0,0,0,4,3,0,2,2,1,0,0,1,0,2,1,1,0,1,2,2,0,1,0,1,3,0,1,0,1,1,1,1,2,0,2,1,0,0,1,0,0,0,0,2,0,0,1,1,2,2,0,0,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0]
quetzalte=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,1,1,1,0,0,0,0,2,0,0,1,0,2,2,3,2,1,0,0,4,0,4,0,3,2,1,2,2,0,1,0,3,0,5,2,0,7,2,4,1,2,1,3,2,2,5,7,1,2,1,1,4,3,3,1,8,2,0,5,4,1,4,0,4,4,2,1,4,5,2,2,4,2,5,5,4,0,2,1,5,3,2,1,4,0,5,1,2,2,0,1,4,1,0,1,4,1,3,1,0,0,1,2,2,0,2,4,4,1,2,0,3,3,1,1,1,0,0,1,1,0,1,0,1,1,1,1,1,0,0,0,2,0,0,0,0,0,2,0,1,2,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0]
quiche=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,2,0,1,1,1,1,0,0,0,2,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,1,0,0,0,3,1,1,1,1,0,0,0,0,0,1,0,0,2,0,0,0,0,0,0,1,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
rethauleu=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,2,0,0,0,0,0,0,0,2,2,3,0,1,0,3,0,0,0,1,0,0,1,0,0,0,0,2,0,0,1,3,0,2,1,2,1,1,1,0,1,0,1,1,1,2,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
sacatepeq=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,2,0,0,0,2,0,0,1,1,0,1,2,0,0,1,0,1,0,0,0,1,0,1,0,0,0,2,0,0,0,1,2,2,2,1,2,0,0,2,0,2,1,1,1,3,0,3,3,1,2,2,0,2,5,0,1,2,3,1,3,0,3,1,4,0,3,3,3,1,1,1,1,1,2,2,0,0,0,0,2,3,3,1,0,0,1,2,2,1,0,0,0,2,1,1,1,2,1,1,0,1,0,0,1,1,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,1,1,1,0,1,0,0,1,2,0,0,1,0,2,1,0,0,1,2,1,1,0,0,0,0,0,0,0,2,0,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,0]
sanmarcos=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,2,0,2,0,0,0,0,0,1,1,2,0,0,0,1,2,0,0,1,1,0,2,1,3,0,0,0,2,1,0,1,0,0,2,3,0,4,0,1,1,1,0,0,1,1,2,0,2,0,0,2,1,3,2,1,2,0,2,2,1,1,0,0,1,0,1,2,2,2,2,0,0,0,0,1,1,0,0,1,1,1,1,4,1,2,0,2,1,0,0,1,2,0,1,1,0,1,0,0,2,1,1,0,2,0,0,1,0,1,2,1,0,1,1,0,1,0,1,2,1,0,1,2,2,0,0,0,0,1,1,0,0,2,2,2,3,0,1,1,0,0,0,0,0,1,1,0,0,1,0,0,1,1,0,1,0,0,1,1,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0]
santarosa=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,2,0,1,0,0,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,0,0,1,0,0,0,0,2,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
sin_datos=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
solola=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,2,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,2,0,0,0,2,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3,0,1,0,1,0,0,0,0,1,0,0,1,1,1,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0]
suchitepe=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,2,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,3,0,1,0,0,1,1,4,2,0,2,2,3,2,2,1,1,2,4,1,1,1,3,3,1,0,1,1,0,1,4,2,3,1,1,5,2,1,1,0,3,3,1,1,4,0,3,1,0,0,0,3,2,0,1,0,0,2,0,3,0,1,1,0,0,1,1,0,0,1,0,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,2,1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
totonicap=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,4,5,5,5,6,6,6,6,6,7,8,9,9,9,9,9,9,12,12,12,12,12,13,13,15,15,17,18,18,19,20,21,21,21,21,21,21,21,21,22,23,23,23,23,23,23,25,26,26,28,29,29,29,34,35,36,39,40,41,44,44,45,46,49,49,49,51,52,53,54,54,54,54,57,60,60,65,65,66,66,66,66,66,66,67,68,68,68,68,68,68,68,69,70,70,70,70,71,71,71,71,72,72,73,73,73,75,76,76,76,77,77,79,79,79,81,83,83,83,83,83,83,83,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86]
zacapa=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,2,2,2,4,4,5,5,5,5,5,5,5,7,7,7,7,7,8,9,9,12,12,14,14,14,15,15,17,17,17,19,21,25,26,26,27,29,31,31,32,32,33,35,37,37,37,37,41,41,41,42,42,43,43,43,43,43,43,43,44,44,44,44,44,44,44,44,44,44,44,47,47,47,47,47,47,47,47,47,47,47,47,48,49,49,49,49,49,49,49,50,52,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,55,55,55,55,55,55,55,56,56,56,56,57,57,57,57,57,58,58,58,59,59,59,59,60,60,61,61,61,61,61,61,61,62,62,62,63,63,63]

def main():
    #LEEMOS NUESTRO ARCHIVO DE INFORMACION y PROCESAMIENTO DE DATA
    #arch = open('data.json', 'r')
    #lista_casos = json.loads(arch.read())['COVID19']
    print("=========================================================================================")
    print("|                                   INFORMACION COVID 19                                |")
    print("=========================================================================================")
    print("Alta Verapaz: "+str(sumalista(alta_vera)))
    print("Baja Verapaz: "+str(sumalista(baja_vera)))
    print("Chimaltenango: "+str(sumalista(chimalten)))
    print("Chiquimula: "+str(sumalista(chiquimul)))
    print("El Progreso: "+str(sumalista(el_progre)))
    print("Escuintla: "+str(sumalista(escuintla)))
    print("Huehuetenango: "+str(sumalista(huehueten)))
    print("Izabal: "+str(sumalista(izabal)))
    print("Jalapa: "+str(sumalista(jalapa)))
    print("Jutiapa: "+str(sumalista(jutiapa)))
    print("Petén: "+str(sumalista(peten)))
    print("Quetzaltenango: "+str(sumalista(quetzalte)))
    print("Quiche: "+str(sumalista(quiche)))
    print("Rethauleu: "+str(sumalista(rethauleu)))
    print("Sacatepequez: "+str(sumalista(sacatepeq)))
    print("San Marcos: "+str(sumalista(sanmarcos)))
    print("Santa Rosa: "+str(sumalista(santarosa)))
    print("Sin datos: "+str(sumalista(sin_datos)))
    print("Solola: "+str(sumalista(solola)))
    print("Suchitepequez: "+str(sumalista(suchitepe)))
    print("Totonicapan: "+str(totonicap[len(totonicap)-1]))
    print("Zacapa: "+str(zacapa[len(zacapa)-1]))
    #arch.close()
    analisis(guatemala)

main()