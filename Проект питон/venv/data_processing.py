import pandas as pd

def finde_all(filename: str) -> pd.DataFrame:
    df = pd.read_csv(filename, sep = '\t', header = 0, names = ['index'])
    return df.head()


#попытка написать алгоритмы
count = 0
filtSignal = 0.0
#фильтр среднее арифметическое. Однократная выборка
b = 30

def oneSample(filename:str):
    sum = 0
    tweets = list(finde_all(f'./data/{filename}.txt').to_dict().values())
    for tweet in tweets:
        sum = sum + tweet
        return (sum/b)



#верный код 
if __name__ == '__main__':
    df = pd.read_csv('./data/pulse.txt', sep = '\t', header = 0, names = ['index'])
    print(df.head())
    oneSample(pulse)
    
