def leaps(year_1: int, year_2: int) -> int:
    assert year_1 <= year_2, 'second argument must be greater or equal to the first'

    y1_4rounded = (year_1 + ((year_1%4!=0) * (4 - year_1%4)))
    y2_4rounded = (year_2 + ((year_2%4!=0) * (4 - year_2%4)))
    dividing_by4 = (y2_4rounded - y1_4rounded) // 4

    y1_100rounded = (year_1 + ((year_1%100!=0) * (100 - year_1%100)))
    y2_100rounded = (year_2 + ((year_2%100!=0) * (100 - year_2%100)))
    dividing_by100 = (y2_100rounded - y1_100rounded) // 100

    y1_200 = year_1 - 200
    y2_200 = year_2 - 200
    y1_600 = year_1 - 600
    y2_600 = year_2 - 600
    y1_900_200_rounded = (y1_200 + ((y1_200%900!=0) * (900 - y1_200%900)))
    y2_900_200_rounded = (y2_200 + ((y2_200%900!=0) * (900 - y2_200%900)))
    y1_900_600_rounded = (y1_600 + ((y1_600%900!=0) * (900 - y1_600%900)))
    y2_900_600_rounded = (y2_600 + ((y2_600%900!=0) * (900 - y2_600%900)))
    dividing_by900_200 = (y2_900_200_rounded - y1_900_200_rounded) // 900
    dividing_by900_600 = (y2_900_600_rounded - y1_900_600_rounded) // 900

    return dividing_by4 - dividing_by100 + dividing_by900_200 + dividing_by900_600

import time

print(leaps(2016, 2017))# => 1
print(leaps(2019, 2020))# => 0
print(leaps(1900, 1901))# => 0
print(leaps(2000, 2001))# => 1
print(leaps(2800, 2801))# => 0
print(leaps(123456, 123456))# => 0
print(leaps(1234, 5678))# => 1077
print(leaps(123456, 7891011))# => 1881475

start = time.time()
l = leaps(123456789101112, 1314151617181920)# => 288412747246240
calc_time = time.time() - start
print(l)
print('{0:.6f}s'.format(calc_time))