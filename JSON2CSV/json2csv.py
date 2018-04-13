#-*-coding:utf-8-*-
import csv
import json
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def trans(path):
    with codecs.open(path+'.json', 'r', 'utf-8') as jsonData:
        load_dict = json.loads(jsonData.read())
        keySet = set('')
        keys = []
        for i,item in enumerate(load_dict):
            for k in item:
##                if k=="hasSelect":
##                    item.pop(k)
                if k not in keySet:
                    keys.append(k)
                    keySet.add(k)
    
    # with open(path+'.csv', 'wb') as csvfile:
        # dict类型写入
        # writer = csv.DictWriter(csvfile, fieldnames=keys)
        # writer.writeheader()
        # writer.writerows(load_dict)

    with open(path + '.csv', 'wb') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['website', 'hometype', 'price', 'city', 'state', 'country', 'bedroom', 'bed', 'guest'
                                    , 'bathroom', 'review', 'review_date', 'hostname', 'jointime'])
        csvwriter.writerow([22])
        csvwriter.writerow([33])

            
##            if i==0:
##                print item
##                keys = []
##                for k in item:
##                    keys.append(k)
##                writer.writerow(k)
##            value = []
##            for k in item:
##                value.append(item[k])
##            print value
##            writer.writerow(item[k])
    
        


if __name__ == '__main__':
##    # path=str(sys.argv[1]) # 获取path参数
    path = 'D:\MyCode\Python\sihuo\JSON2CSV\demonew'
    print (path)
    trans(path)
