from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler, MinMaxScaler, MaxAbsScaler
import pandas as pd
import numpy as np
import plotly
import matplotlib.pyplot as plt
import seaborn as sns


# data = pd.read_excel("pic.xlsx").drop(['ID'], 1)
#
# scaler = StandardScaler()
# scaler = MinMaxScaler()
# scaler = MaxAbsScaler()
# X_scaled = scaler.fit_transform(data)
#
# tsne = TSNE(n_components=2)
# tsne_representation = tsne.fit_transform(X_scaled)
#
# print(tsne_representation)
# print(tsne_representation[:, 0])
# print(tsne_representation[:, 1])



# scatter
# plt.show(pd.DataFrame(tsne_representation.plot()))
# plt.scatter(tsne_representation[:, 0], tsne_representation[:, 1])
# plt.show()




# df = pd.read_excel('video_games_sales.xlsx')
# df = df.dropna()
# print(df.shape)


# plot
# sales_df = df[[x for x in df.columns if 'Sales' in x] + ['Year_of_Release']]
# print(sales_df.groupby('Year_of_Release').sum())
# plt.show(sales_df.groupby('Year_of_Release').sum().plot(rot=45))
# plt.show(sales_df.groupby('Year_of_Release').sum().plot(kind='bar', rot=45))


# distplot save
# cols = ['Global_Sales', 'Critic_Score', 'Critic_Count', 'User_Score', 'User_Count']
# sns_plot = sns.pairplot(df[cols])
# plt.show(sns_plot)
# sns_plot.savefig('pairplot.png')

# plt.show(sns.distplot(df.Critic_Score))





# subplot
# mix = mixture.GaussianMixture(n_components=2, max_iter=10000)
# mix.fit(data)
#
# list = mix.predict(data)
# plt.subplot(320 + i)
# plt.scatter(x, y, c=list)
# plt.show()




# boxplot
# top_platforms = df.Platform.value_counts().sort_values(ascending = False).head(5).index.values
# df['User_Score'] = df['User_Score'].astype(int)
# plt.show(sns.boxplot(y="Platform", x="User_Score", data=df[df.Platform.isin(top_platforms)], orient="h"))
# plt.show(sns.boxplot(y="Platform", x="Critic_Score", data=df[df.Platform.isin(top_platforms)], orient="h"))



# plot
# data = pd.read_excel('data.xlsx', sheet_name=0)
# print(data)
#
# data = data.groupby('square').mean()
# plt.show(data.plot())


#############################################################################
# x = np.linspace(-10, 10, 100)
# plt.figure()
# plt.subplot(1, 2, 1)
# plt.plot(x, np.sin(x), 'p', color='g', label='sin(x)', linestyle='solid', markerfacecolor='white', markeredgecolor='pink')
# plt.plot(x, np.cos(x))
# plt.legend()
# plt.title('SIN')
# # plt.xlim(-10, 10)
# # plt.ylim(-2, 2)
# # plt.axis('tight')
# # plt.axis('equal')
# # plt.axis([-10, 10, -2, 2])
# plt.show()
#############################################################################

# rnd = np.random.RandomState(0)
# x = rnd.rand(100)
# y = rnd.rand(100)
#
# colors = rnd.rand(100)
# size = rnd.rand(100) * 1000
#
# plt.scatter(x, y, c=colors, s=size, alpha=0.3, cmap='viridis')
# plt.colorbar()
# plt.show()

#############################################################################

# rnd = np.random.RandomState(0)
# x = rnd.rand(100)
# y = rnd.rand(100)
#
# plt.errorbar(x, y, yerr=0.1, fmt='.')
# plt.show()

#############################################################################