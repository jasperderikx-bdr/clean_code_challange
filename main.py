import pandas as pd
from sklearn.linear_model import LinearRegression, RidgeCV
from datetime import time, datetime

supplies = ["pan", "rasp", "kom"]


def clean(text):
    str_list = text.split()
    str_list = [''.join(e for e in str if e.isalnum()) for str in str_list]
    str_list = [str.lower() for str in str_list]
    return str_list


def parse_recipes():
    df = pd.read_csv("data/lunch_recipes.csv")
    for word in supplies:
        df[f"{word}"] = df.recipe.apply(lambda text: clean(text).count(word) > 0)
    df = df.drop(['dish', 'url', "servings", "recipe"], axis=1)
    return df


def parse_attendance_sheet():
    df = pd.read_csv("data/key_tag_logs.csv")
    df['timestamp'] = df.timestamp.apply(lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
    df['date'] = df.timestamp.apply(lambda x: x.date())
    df['time'] = df.timestamp.apply(lambda x: x.time())
    import numpy as np
    result = pd.DataFrame(np.array(df.date), columns=['date']).drop_duplicates()

    # print(df.name.unique())
    for name in df.name.unique():
        df2 = df[df.name == name]

        df_check_in = df2[df2.event == "check in"]
        df_check_in = df_check_in[df_check_in.time < time(12, 0, 0)]

        df_check_out = df2[df2.event == "check out"]
        df_check_out = df_check_out[df_check_out.time > time(12, 0, 0)]
        lunch_dates = df_check_in.merge(df_check_out, on="date", how="inner").date
        result[f"{name}"] = result.date.apply(lambda x: 1 if x in list(lunch_dates) else 0)

    result['date'] = result['date'].apply(str)
    return result


def train_model():
    recipes = parse_recipes()
    attendance = parse_attendance_sheet()
    df = recipes.merge(attendance, on="date", how="outer").merge(pd.read_csv("data/dishwasher_log.csv")).fillna(0)
    reg = LinearRegression().fit(df.drop(["dishwashers", "date"], axis=1), df["dishwashers"])
    return dict(zip(reg.feature_names_in_,
                    [round(c, 3) for c in reg.coef_]))


if __name__ == "__main__":
    print(train_model())
