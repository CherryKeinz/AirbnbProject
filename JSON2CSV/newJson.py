# -*-coding:utf-8-*-
import csv
import json
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def trans(path):
    model = []
    with codecs.open(path + '.json', 'r', 'utf-8') as jsonData:
        load_dict = json.loads(jsonData.read())
        for i, item in enumerate(load_dict):
            per = {}
            per['home'] = dict([(k,item[k]) for k in item if k=="hometype" or k== "city"
                                or k== "guest" or k== "bedroom" or k== "bathroom" or k== "bed"or k== "price" or k== "review"])
            
            per['host'] = dict([(k, item[k]) for k in item if k == "hostname" or k == "hostcountry"
                                or k== "jointime" or
                                k== "hostcity" or k== "hoststate"])
            per['location'] = dict([(k, item[k]) for k in item if k == "city" or k == "state"
                                or k== "country"])
            per['website'] = dict([(k, item[k]) for k in item if k == 'website'])
            model.append(per)
    with codecs.open(path + 'new.json', 'wb','utf-8') as newJSONfile:
        json.dump(model, newJSONfile)


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
    path = 'D:\MyCode\Python\sihuo\JSON2CSV\demo'
    print (path)
    trans(path)
