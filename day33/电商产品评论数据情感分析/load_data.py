# 电商产品评论数据情感分析/load_data.py
import pandas as pd

def csv2txt():
    '''
    提取评论并保存为txt
    :return:
    '''
    inputfile = 'data/huizong.csv'  # 评论汇总文件
    outputfile = 'data/output/meidi_jd.txt'  # 评论提取后保存路径
    data = pd.read_csv(inputfile, encoding='utf-8')
    data = data[[u'评论']][data[u'品牌'] == u'海尔']
    data.to_csv(outputfile, index=False, header=False, encoding='utf-8')

if __name__ == '__main__':
    csv2txt()