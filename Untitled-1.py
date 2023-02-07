# %%
from sklearn.metrics import accuracy_score, precision_score
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
import seaborn as sns
import matplotlib.pyplot as pyt
import pandas as pd

# %%
matches = pd.read_csv("matches.csv", index_col=0)

# %%
matches.head()

# %%
matches.shape

# %%
matches.isnull().sum()

# %%
matches["team"].value_counts()

# %%
matches["round"].value_counts()

# %%
matches.dtypes

# %%
matches["date"] = pd.to_datetime(matches["date"])

# %%
matches

# %%
matches.dtypes

# %%
matches["venue_code"] = matches["venue"].astype("category").cat.codes

# %% [markdown]
# 0 - Away 1 - Home

# %%
matches["team_code"] = matches["team"].astype("category").cat.codes
matches["opp_code"] = matches["opponent"].astype("category").cat.codes

# %%
matches[["team", "team_code"]].drop_duplicates()
# matches[["opponent","opp_code"]].drop_duplicates()
# matches["team"].unique()

# %%
matches["hour"] = matches["time"].str.replace(
    ":.+", "", regex=True).astype("int")

# %%
matches["day_code"] = matches["day"].astype("category").cat.codes

# %% [markdown]
# 0 - Thu
# 1 - Fri
# 2 - Sat
# 3 - Sun
# 4 - Mon
# 5 - Tue
# 6 - Wed
#

# %%
matches["target"] = (matches["result"] == 'W').astype("int")

# %% [markdown]
# 0 - Draw/Lose
#

# %% [markdown]
# 1 - Win
#

# %%
matches["hour"].unique()

# %%
team = matches.loc[matches.team == "Manchester City"]
cor = team.corr().round(2)
cor

# %%
pyt.figure(figsize=(25, 20))
plot = sns.heatmap(matches.corr(), annot=True, fmt=".2f")

# %%
model = LogisticRegression(random_state=16)

# %%
train = matches[matches["date"] < '2022-1-1']
test = matches[matches["date"] > '2022-1-1']

# %%
predictors = ["venue_code", "team_code", "opp_code",
              "hour", "day_code", "xg", "xga", "gf"]

# %%
x = model.fit(train[predictors].values, train["target"])

# %%
preds = model.predict(test[predictors].values)

# %%
accuracy_score(test["target"], preds)

# %%
precision_score(test["target"], preds)

# %%
file = "Final.pkl"
pickle.dump(model, open(file, 'wb'))

# %%
load = pickle.load(open(file, 'rb'))

# %%
arr = np.array([0, 18, 16, 3, 1.9, 1.3, 0, 1.5])
result = load.predict(arr.reshape(1, -1))

# %%
if result[0] == 1:
    print("Win")
else:
    print("Lose/Draw")
