import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd

# Loop Through the dictionary
favorite_languages = {
    'Jen': ['python', 'c', 'ruby'],
    'Sarah': ['c', 'Java', 'JavaScript'],
    'David': ['c++', 'Ruby', 'JavaScript'],
    'Robert': ['Spring', 'Java', 'React']
}

for key, value in favorite_languages.items():
    for v in value:
        print("Favorite language of student " + key + " is " + v)
    print(".................................")

# check if the user is privileged

Users = ['Andrew', 'David', 'John', 'Klark', 'Alice']
Privileged_Users = ['Andrew', 'Carolina', 'David', 'George']

for u in Users:
    if u in Privileged_Users:
        print(u + " is privileged")

# Task 3
CopyOf_Privileged_Users = []
for u in Users:
    if u in Privileged_Users:
        CopyOf_Privileged_Users.append(u)

print(CopyOf_Privileged_Users)



# Task 4
X = np.array([[185, 72], [170, 56], [168, 60], [179, 68], [182, 72], [188, 77], [177, 67]])
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
print(kmeans.cluster_centers_)

# Task 5
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color='black')
plt.show()

# Task 6

Students = {
    'StudName': ['Alan', 'Vivian'],
    'StudAge': [21, 22]
}
s_df = pd.DataFrame(Students, index=['S1', 'S2'])
print(s_df)

New_Students = {
    'StudName': ['John', 'Martin'],
    'StudAge': [23, 24],
}

s_df_2 = pd.DataFrame(New_Students, index=['S3', 'S4'])
result = pd.concat([s_df, s_df_2])
print(result)

select = result.loc[(result['StudAge'] >= 20) & (result['StudName'] == 'John')]
print(select)
