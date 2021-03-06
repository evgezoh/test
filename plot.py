from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler
import pandas as pd
import plotly
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_excel("pic.xlsx").drop(['ID'], 1)

scaler = StandardScaler()
scaler = MinMaxScaler()
scaler = MaxAbsScaler()
X_scaled = scaler.fit_transform(data)

tsne = TSNE(n_components=2)
tsne_representation = tsne.fit_transform(X_scaled)

print(tsne_representation)
print(tsne_representation[:, 0])
print(tsne_representation[:, 1])

#plt.show(pd.DataFrame(tsne_representation.plot()))
# plt.scatter(tsne_representation[:, 0], tsne_representation[:, 1])
# plt.show()


# df = pd.read_excel('video_games_sales.xlsx')
# df = df.dropna()
# print(df.shape)


# sales_df = df[[x for x in df.columns if 'Sales' in x] + ['Year_of_Release']]
# print(sales_df.groupby('Year_of_Release').sum()    )
#
# plt.show(sales_df.groupby('Year_of_Release').sum().plot())
# plt.show(sales_df.groupby('Year_of_Release').sum().plot(kind='bar', rot=45))
#
#
# cols = ['Global_Sales', 'Critic_Score', 'Critic_Count', 'User_Score', 'User_Count']
# sns_plot = sns.pairplot(df[cols])
# plt.show(sns_plot)
# sns_plot.savefig('pairplot.png')
#
# plt.show(sns.distplot(df.Critic_Score))


# top_platforms = df.Platform.value_counts().sort_values(ascending = False).head(5).index.values
# df['User_Score'] = df['User_Score'].astype(int)
# plt.show(sns.boxplot(y="Platform", x="User_Score", data=df[df.Platform.isin(top_platforms)], orient="h"))
# plt.show(sns.boxplot(y="Platform", x="Critic_Score", data=df[df.Platform.isin(top_platforms)], orient="h"))


data = pd.read_excel('data.xlsx', sheet_name=0)
print(data)

data = data.groupby('square').mean()
#data.set_index('square', inplace=True)
#data = pd.DataFrame(data['opsum'])
plt.show(data.plot())
