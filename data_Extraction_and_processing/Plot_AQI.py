import pandas as pd
import matplotlib.pyplot as plt

def avg_data_2013():
    temp_i = 0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2013.csv', chunksize=24):
        add_var = 0
        avg = 0.0
        df = pd.DataFrame(rows)
        data = df['PM2.5'].tolist()
        for i in data:
            if isinstance(i, (float, int)):
                add_var += i
            elif isinstance(i, str):
                if i not in ('NoData', 'PwrFail', '---', 'InVld'):
                    add_var += float(i)
        avg = add_var / 24
        temp_i += 1
        average.append(avg)
    return average

def avg_data_2014():
    temp_i = 0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2014.csv', chunksize=24):
        add_var = 0
        avg = 0.0
        df = pd.DataFrame(rows)
        data = df['PM2.5'].tolist()
        for i in data:
            if isinstance(i, (float, int)):
                add_var += i
            elif isinstance(i, str):
                if i not in ('NoData', 'PwrFail', '---', 'InVld'):
                    add_var += float(i)
        avg = add_var / 24
        temp_i += 1
        average.append(avg)
    return average

def avg_data_2015():
    temp_i = 0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2015.csv', chunksize=24):
        add_var = 0
        avg = 0.0
        df = pd.DataFrame(rows)
        data = df['PM2.5'].tolist()
        for i in data:
            if isinstance(i, (float, int)):
                add_var += i
            elif isinstance(i, str):
                if i not in ('NoData', 'PwrFail', '---', 'InVld'):
                    add_var += float(i)
        avg = add_var / 24
        temp_i += 1
        average.append(avg)
    return average

def avg_data_2016():
    temp_i = 0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2016.csv', chunksize=24):
        add_var = 0
        avg = 0.0
        df = pd.DataFrame(rows)
        data = df['PM2.5'].tolist()
        for i in data:
            if isinstance(i, (float, int)):
                add_var += i
            elif isinstance(i, str):
                if i not in ('NoData', 'PwrFail', '---', 'InVld'):
                    add_var += float(i)
        avg = add_var / 24
        temp_i += 1
        average.append(avg)
    return average

def avg_data_2017():
    temp_i = 0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2017.csv', chunksize=24):
        add_var = 0
        avg = 0.0
        df = pd.DataFrame(rows)
        data = df['PM2.5'].tolist()
        for i in data:
            if isinstance(i, (float, int)):
                add_var += i
            elif isinstance(i, str):
                if i not in ('NoData', 'PwrFail', '---', 'InVld'):
                    add_var += float(i)
        avg = add_var / 24
        temp_i += 1
        average.append(avg)
    return average

def avg_data_2018():
    temp_i = 0
    average = []
    for rows in pd.read_csv('Data/AQI/aqi2018.csv', chunksize=24):
        add_var = 0
        avg = 0.0
        df = pd.DataFrame(rows)
        data = df['PM2.5'].tolist()
        for i in data:
            if isinstance(i, (float, int)):
                add_var += i
            elif isinstance(i, str):
                if i not in ('NoData', 'PwrFail', '---', 'InVld'):
                    add_var += float(i)
        avg = add_var / 24
        temp_i += 1
        average.append(avg)
    return average

if __name__ == "__main__":
    lst2013 = avg_data_2013()
    lst2014 = avg_data_2014()
    lst2015 = avg_data_2015()
    lst2016 = avg_data_2016()
    lst2017 = avg_data_2017()
    lst2018 = avg_data_2018()

    plt.plot(range(len(lst2013)), lst2013, label="2013 data")
    plt.plot(range(len(lst2014)), lst2014, label="2014 data")
    plt.plot(range(len(lst2015)), lst2015, label="2015 data")
    plt.plot(range(len(lst2016)), lst2016, label="2016 data")
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()
