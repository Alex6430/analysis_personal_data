import sklearn
import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn import datasets
from sklearn.decomposition import PCA
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
import pylab as pl

df1 = pd.read_excel("Ankety-despatched-1.xlsx", skiprows=3, header=1)
df2 = pd.read_excel("Ankety-despatched-2.xlsx", skiprows=3, header=1)

data_frames = [df1, df2]
df = pd.concat(data_frames, sort=False)
df.drop_duplicates(keep='last', inplace=True)
df = df.dropna()  # Удаляет те записи, в которых есть пропуски

df = df.rename(columns={"Дата рождения": "Birthday",
                        "Пол": "Sex",
                        "Когда Вы видите, слышите или представляете какую-либо букву или цифру, то это вызывает у Вас ощущение цвета, вкуса, фактуры и т.д. ": "Question 1",
                        "Названия дней недели (понедельник, вторник и т.д.) или месяцев (январь, февраль и т.д.) вызывают ли у Вас ощущение цвета?": "Question 2",
                        "Числа, буквы и/или названия интервалов времени, такие как дни недели и месяцы, мысленно представляются ли Вам в виде последовательности, располагающейся в трехмерном пространстве? ": "Question 3",
                        "Звучание отдельных звуков, аккордов или мелодий, сыгранных на определенном музыкальном инструменте, вызывают ли у Вас ощущения цвета? ": "Question 4",
                        "Числа, буквы и/или названия интервалов времени, такие как дни недели и месяцы, мысленно представляются ли Вам в виде отдельных качеств человека (добродушный, щедрый и т.д.) или в виде целой личности (веселый лысый старик, стремительная женщина и т.д.)?": "Question 5",
                        "Испытывая боль (например, головную), эмоции (сожаление или печаль) или оргазм, Вы переживаете ощущение цвета, вкуса или аромата? ": "Question 6",
                        "При непосредственном взгляде на человека или при мысли о нем Вы ощущаете определенный цвет или целую гамму разных оттенков? ": "Question 7",
                        "Прикосновение разного характера к различным частям Вашего тела сопровождается для Вас ощущением цвета. Например, при прикосновении к холодной или теплой воде Вы испытываете ощущение различной цветовой гаммы?": "Question 8",
                        "Определенный звук вызывает у Вас отчетливое ощущение вкуса, запаха или прикосновения. Например, при звуке тикающих часов у Вас во рту возникает кисловатый привкус или при звуке пролетающего самолета у Вас возникает отчетливое ощущение прикосновения?": "Question 9",
                        "При взгляде на картину, обстановку или определенное расположение предметов у Вас возникает отчетливое ощущение вкуса во рту, запаха или звука?": "Question 10"})

# mas_name = {"Birthday": "Дата рождения",
#             "Sex": "Пол",
#             "Question 1": "Когда Вы видите, слышите или представляете какую-либо букву или цифру, то это вызывает у Вас ощущение цвета, вкуса, фактуры и т.д. ",
#             "Question 2": "Названия дней недели (понедельник, вторник и т.д.) или месяцев (январь, февраль и т.д.) вызывают ли у Вас ощущение цвета?",
#             "Question 3": "Числа, буквы и/или названия интервалов времени, такие как дни недели и месяцы, мысленно представляются ли Вам в виде последовательности, располагающейся в трехмерном пространстве? ",
#             "Question 4": "Звучание отдельных звуков, аккордов или мелодий, сыгранных на определенном музыкальном инструменте, вызывают ли у Вас ощущения цвета? ",
#             "Question 5": "Числа, буквы и/или названия интервалов времени, такие как дни недели и месяцы, мысленно представляются ли Вам в виде отдельных качеств человека (добродушный, щедрый и т.д.) или в виде целой личности (веселый лысый старик, стремительная женщина и т.д.)?",
#             "Question 6": "Испытывая боль (например, головную), эмоции (сожаление или печаль) или оргазм, Вы переживаете ощущение цвета, вкуса или аромата? ",
#             "Question 7": "При непосредственном взгляде на человека или при мысли о нем Вы ощущаете определенный цвет или целую гамму разных оттенков? ",
#             "Question 8": "Прикосновение разного характера к различным частям Вашего тела сопровождается для Вас ощущением цвета. Например, при прикосновении к холодной или теплой воде Вы испытываете ощущение различной цветовой гаммы?",
#             "Question 9": "Определенный звук вызывает у Вас отчетливое ощущение вкуса, запаха или прикосновения. Например, при звуке тикающих часов у Вас во рту возникает кисловатый привкус или при звуке пролетающего самолета у Вас возникает отчетливое ощущение прикосновения?",
#             "Question 10": "При взгляде на картину, обстановку или определенное расположение предметов у Вас возникает отчетливое ощущение вкуса во рту, запаха или звука?"}

# mas_name = {"Birthday": "Дата рождения",
#             "Sex": "Пол",
#             "Question 1": "q1",
#             "Question 2": "q2",
#             "Question 3": "q3",
#             "Question 4": "q4",
#             "Question 5": "q5",
#             "Question 6": "q6",
#             "Question 7": "q7",
#             "Question 8": "q8",
#             "Question 9": "q9",
#             "Question 10": "q10"}


df['Birthday'] = df['Birthday'].dt.year
df.to_excel("data.xlsx")

# # визуализация
# gp = df.groupby(['Birthday', 'Sex']).size().unstack().plot(kind='bar',
#                                                            cmap=matplotlib.colors.ListedColormap(
#                                                                ['b', 'gold']))
# gp.set_yscale('log')
# gp.get_figure().savefig('визуализация sex')
#
#
# # вопрос 1
# q1_sex = df.groupby(['Sex', 'Question 1']).size().unstack().plot(kind='bar',
#                                                                  cmap=matplotlib.colors.ListedColormap(
#                                                                      ['r', 'g']))
# q1_year = df.groupby(['Birthday', 'Question 1']).size().unstack().plot(kind='bar')
# q1_year.set_yscale('log')
# q1_sex.get_figure().savefig('вопрос 1 sex')
# q1_year.get_figure().savefig('вопрос 1 year')
#
# # #вопрос 2
# q2_sex = df.groupby(['Sex', 'Question 2']).size().unstack().plot(kind='bar', cmap=matplotlib.colors.ListedColormap(['r', 'g']))
# q2_year = df.groupby(['Birthday', 'Question 2']).size().unstack().plot(kind='bar')
# q2_year.set_yscale('log')
# q2_sex.get_figure().savefig('вопрос 2 sex')
# q2_year.get_figure().savefig('вопрос 2 year')
#
# # вопрос 3
# q3_sex = df.groupby(['Sex', 'Question 3']).size().unstack().plot(kind='bar', cmap=matplotlib.colors.ListedColormap(['r', 'g']))
# q3_year = df.groupby(['Birthday', 'Question 3']).size().unstack().plot(kind='bar')
# q3_year.set_yscale('log')
# q3_sex.get_figure().savefig('вопрос 3 sex')
# q3_year.get_figure().savefig('вопрос 3 year')
#
# # вопрос 4
# q4_sex = df.groupby(['Sex', 'Question 4']).size().unstack().plot(kind='bar', cmap=matplotlib.colors.ListedColormap(['r', 'g']))
# q4_year = df.groupby(['Birthday', 'Question 4']).size().unstack().plot(kind='bar')
# q4_year.set_yscale('log')
# q4_sex.get_figure().savefig('вопрос 4 sex')
# q4_year.get_figure().savefig('вопрос 4 year')
#
# # вопрос 5
# q5_sex = df.groupby(['Sex', 'Question 5']).size().unstack().plot(kind='bar', cmap=matplotlib.colors.ListedColormap(['r', 'g']))
# q5_year = df.groupby(['Birthday', 'Question 5']).size().unstack().plot(kind='bar')
# q5_year.set_yscale('log')
# q5_sex.get_figure().savefig('вопрос 5 sex')
# q5_year.get_figure().savefig('вопрос 5 year')
#
# # вопрос 6
# q6_sex = df.groupby(['Sex', 'Question 6']).size().unstack().plot(kind='bar', cmap=matplotlib.colors.ListedColormap(['r', 'g']))
# q6_year = df.groupby(['Birthday', 'Question 6']).size().unstack().plot(kind='bar')
# q6_year.set_yscale('log')
# q6_sex.get_figure().savefig('вопрос 6 sex')
# q6_year.get_figure().savefig('вопрос 6 year')
#
# # вопрос 7
# q7_sex = df.groupby(['Sex', 'Question 7']).size().unstack().plot(kind='bar', cmap=matplotlib.colors.ListedColormap(['r', 'g']))
# q7_year = df.groupby(['Birthday', 'Question 7']).size().unstack().plot(kind='bar')
# q7_year.set_yscale('log')
# q7_sex.get_figure().savefig('вопрос 7 sex')
# q7_year.get_figure().savefig('вопрос 7 year')
#
# # вопрос 8
# q8_sex = df.groupby(['Sex', 'Question 8']).size().unstack().plot(kind='bar', cmap=matplotlib.colors.ListedColormap(['r', 'g']))
# q8_year = df.groupby(['Birthday', 'Question 8']).size().unstack().plot(kind='bar')
# q8_year.set_yscale('log')
# q8_sex.get_figure().savefig('вопрос 8 sex')
# q8_year.get_figure().savefig('вопрос 8 year')
#
# # вопрос 9
# q9_sex = df.groupby(['Sex', 'Question 9']).size().unstack().plot(kind='bar', cmap=matplotlib.colors.ListedColormap(['r', 'g']))
# q9_year = df.groupby(['Birthday', 'Question 9']).size().unstack().plot(kind='bar')
# q9_year.set_yscale('log')
# q9_sex.get_figure().savefig('вопрос 9 sex')
# q9_year.get_figure().savefig('вопрос 9 year')
#
# # вопрос 10
# q10_sex = df.groupby(['Sex', 'Question 10']).size().unstack().plot(kind='bar', cmap=matplotlib.colors.ListedColormap(['r', 'g']))
# q10_year = df.groupby(['Birthday', 'Question 10']).size().unstack().plot(kind='bar')
# q10_year.set_yscale('log')
# q10_sex.get_figure().savefig('вопрос 10 sex')
# q10_year.get_figure().savefig('вопрос 10 year')


# Замена анкетных ответов да и нет на 0 и 1
yes_no_dict = {'Да': 1, 'Нет': 0}
for column in df.columns[2:]:
    df[column] = df[column].replace(yes_no_dict)
data = df.iloc[:, 2:].copy()

# цветовое отображение данных
colors = ['tomato', 'forestgreen', 'navy', 'gold', 'k', 'r', 'b', 'c', 'm', 'y']

# кластеризация
# метод главных компонент
pca_3 = PCA(n_components=10)
data_3d = pca_3.fit_transform(data)
pca_3.explained_variance_ratio_

kmeans = KMeans(n_clusters=3, n_init=10)
target_3d = kmeans.fit_predict(data)  # разбиваем данные на классы

# print(data[:,"Когда Вы видите, слышите или представляете какую-либо букву или цифру, то это вызывает у Вас ощущение цвета, вкуса, фактуры и т.д. "])
for number_class in range(3):
    mass = data.iloc[np.where(target_3d == number_class)[0], :]
    mass.to_excel("class "+str(number_class)+".xlsx")
    dict_question = {}
    for number_question in range(0, mass.shape[1]):
        lst = mass._get_values[:, number_question]
        dct = {1: 0, 0: 0}
        for i in lst:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1

        dct[1], dct[0] = float('{:.3f}'.format(dct[1] / (dct[1] + dct[0]))), float(
            '{:.3f}'.format(dct[0] / (dct[1] + dct[0])))
        # print(dct[1])
        dict_question[number_question] = dct
    print(dict_question)
    with open('dict_question '+str(number_class)+'.txt', 'w') as out:
        for key, val in dict_question.items():
            out.write('{}:{}\n'.format(key, val))

# отображение кластеризации
fig = plt.figure(figsize=(15, 11))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data_3d[:, 0], data_3d[:, 1], data_3d[:, 2],
           c=target_3d,
           cmap=matplotlib.colors.ListedColormap(colors))
fig.savefig('кластеризация')

# классификация
# метод К ближайших соседей
model = KNeighborsClassifier(n_neighbors=3)
model.fit(data[:1000], target_3d[:1000])
print(model)
# make predictions
expected = target_3d[1001:]  # ожидаемое
predicted = model.predict(data[1001:])  # предсказанное
error = 0

for item in range(0, len(expected)):
    if expected[item] != predicted[item]:
        error += 1

print("error for classificator = " + str(error / len(expected)))

# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))

# отрисовка классификации
fig = plt.figure(figsize=(15, 11))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data_3d[:, 0][:1680], data_3d[:, 1][:1680], data_3d[:, 2][:1680],
           c=predicted,
           cmap=matplotlib.colors.ListedColormap(colors))
# ax.scatter(data_3d[:, 0][:1680], data_3d[:, 1][:1680], data_3d[:, 2][:1680],
#            c=expected,
#            cmap='Reds')

fig.savefig('классификация')

# fig = plt.figure()
# plt.scatter(range(0,len(expected)),expected,c='red' )
# plt.scatter(range(0,len(predicted)),predicted,c='blue' )
# plt.grid(True)
plt.show()
