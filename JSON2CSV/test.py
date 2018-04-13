#输出数据写入CSV文件
import csv
data = [
{'Petal.Length': '1.4', 'Sepal.Length': '5.1', 'Petal.Width': '0.2', 'Sepal.Width': '3.5', 'Species': 'setosa'},
{'Petal.Length': '1.4', 'Sepal.Length': '4.9', 'Petal.Width': '0.2', 'Sepal.Width': '3', 'Species': 'setosa'},
{'Petal.Length': '1.3', 'Sepal.Length': '4.7', 'Sepal.Width': '3.2', 'Species': 'setosa'},
{'Petal.Length': '1.5', 'Sepal.Length': '4.6', 'Petal.Width': '0.2', 'Sepal.Width': '3.1'}
]
header = ['Petal.Length', 'Sepal.Length', 'Petal.Width', 'Sepal.Width', 'Species']
#Python3.4以后的新方式，解决空行问题
with open('11.csv', 'wb') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()    #   写入表头
    writer.writerows(data)  # 批量写入
