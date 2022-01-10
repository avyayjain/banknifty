import pandas as pd

data = pd.read_csv(r'C:\Users\avyay\Downloads\2020\2020\Yearly Consolidated\CSV 2020\BANKNIFTY.csv')


df = pd.DataFrame(data)


data_opening = df[(df["time"] == "09:30")]
new_data = df[(df["time"] == "15:15")]

data_opening['difference'] = data_opening['open'] - data_opening['close']
data_opening["percentage %"] = data_opening["difference"] / 100


new_data['difference'] = new_data['open'] - new_data['close']
new_data["percentage %"] = new_data["difference"] / 100


data_opening = data_opening[data_opening["difference"] > 0]

data_ok = pd.DataFrame()
i = 0
for data in new_data.values:
    for new in data_opening.values:
        if data[1] == new[1]:
            data_ok.append(data_opening[i])
        else:
            data_ok.append(new_data[i])
        i = i + 1


