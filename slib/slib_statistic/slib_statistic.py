import numpy as np
from scipy import stats

def test():
    print('OK')

def data_analysis(src, info=True):
    
    # 期待値
    average = np.mean(src)

    # 中央値
    median = np.median(src)

    # 標本分散
    variance = np.var(src)
    
    # 標準偏差
    standard_deviation = variance ** (1/2)

    # 不偏分散
    unbiased_variance = np.var(src, ddof=1)

    # 歪度
    skew = stats.skew(src)

    # 尖度
    kurtosis = stats.kurtosis(src)
    
    # 最頻値
    mode = np.argmax(np.bincount(src.astype(int)))
    
    # 最大値と最大値の索引
    max_value, max_index = np.max(src), np.argmax(src)

    if info:
        print('average(期待値): ', '%.3f' % average)
        print('median(中央値): ', '%.3f' % median)
        print('variance(標本分散): ', '%.3f' % variance)
        print('standard_deviation(標準偏差): ', '%.3f' % standard_deviation)
        print('unbiased_variance(不偏分散): ', '%.3f' % unbiased_variance)
        print('skew(歪度): ', '%.3f' % skew)
        print('kurtosis(尖度): ', '%.3f' % kurtosis)
        print('mode(最頻値): ', mode)

    return {'average': average, 
            'median': median, 
            'variance': variance, 
            'standard_deviation': standard_deviation, 
            'unbiased_variance': unbiased_variance, 
            'skew': skew, 
            'kurtosis': kurtosis, 
            'mode': mode, 
            'max_value': max_value, 
            'max_index': max_index}

def list_calculata(list1: list, list2: list, d: str) -> list:

    # listの間の計算

    if len(list1) != len(list2):
        print('sou: The lengths of the two lists are not the same!')
        
    re = []
        
    for i in range(len(list2)):
        
        if d == '+':
            if list1[i] == None or list2[i] == None: re.append(None)
            else: re.append(list1[i]+list2[i])
                
        if d == '-':
            if list1[i] == None or list2[i] == None: re.append(None)
            else: re.append(list1[i]-list2[i])
                
        if d == '*':
            if list1[i] == None or list2[i] == None: re.append(None)
            else: re.append(list1[i]*list2[i])
                
        if d == '/':
            if list1[i] == None or list2[i] == None: re.append(None)
            else: re.append(list1[i]/list2[i])
            
    return re