import time,json,requests,random,datetime
from campus import CampusCard

def main():
    #定义变量
    success,failure=[],[]
    #sectets字段录入
    phone, password, sckey = [], [], []
    #多人循环录入
    while True:  
        try:
            users = input()
            info = users.split(',')
            phone.append(info[0])
            password.append(info[1])
            sckey.append(info[2])
        except:
            break

    #提交打卡
    for index,value in enumerate(phone):
        print("开始尝试为用户%s打卡"%(value[-4:]))
        count = 0
        while (count <= 3):
            try:
                campus = CampusCard(phone[index], password[index])
                token = campus.user_info["sessionId"]
                userInfo=getUserInfo(token)
                response = checkIn(userInfo,token)
                strTime = getNowTime()
                if response.json()["msg"] == '成功':
                    success.append(value[-4:])
                    print(response.text)
                    msg = strTime + value[-4:]+"打卡成功"
                    if index == 0:
                        result=response
                    break
                else:
                    failure.append(value[-4:])
                    print(response.text)
                    msg =  strTime + value[-4:] + "打卡异常"
                    count = count + 1
                    if index == 0:
                        result=response
                    if count<=3:
                        print('%s打卡失败，开始第%d次重试...'%(value[-4:],count))
                    time.sleep(5)
            except Exception as e:
                print(e.__class__)
                failure.append(value[-4:])
                print(response.text)
                msg = strTime + value[-4:] +"出现错误"
                count = count + 1
                if index == 0:
                    result=response
                if count<=3:
                    print('%s打卡出错，开始第%d次重试...'%(value[-4:],count))
                time.sleep(5)
        print(msg)
        print("-----------------------")
    fail = sorted(set(failure),key=failure.index)
    title = "成功: %s 人,失败: %s 人"%(len(success),len(fail))
    try:
        print('主用户开始微信推送...')
        wechatPush(title,sckey[0],success,fail,result)
    except:
        print("微信推送出错！")

#时间函数
def getNowTime():
    cstTime = (datetime.datetime.utcnow() + datetime.timedelta(hours=8))
    strTime = cstTime.strftime("%H:%M:%S ")
    return strTime

#打卡参数配置函数
def getUserJson(userInfo,token):
    #随机温度(36.2~36.8)
    a=random.uniform(36.2,36.8)
    temperature = round(a, 1)
    return  {
        "businessType": "epmpics",
        "method": ""submitUpInfo",
        "jsonData": {
        "deptStr": {
             "deptid": 216094,
             "text": "人工智能与大数据学院-软件工程-软件1701"
        },
        #如果你来自其他学校，请自行打卡抓包修改地址字段
        "areaStr": "{\"streetNumber\":\"7号\",\"street\":\"经八路\",\"district\":\"金水区\",\"city\":\"郑州市\",\"province\":\"河南省\",\"town\":\"\",\"pois\":\"经八路三社区-3号楼\",\"lng\":113.67636200000192,\"lat\":34.780110968927,\"address\":\"金水区经八路7号经八路三社区-3号楼\",\"text\":\"河南省-郑州市\",\"code\":\"\"}", 
        "reportdate": round(time.time()*1000),
        "customerid": userInfo['customerId'],
        "deptid": userInfo['classId'],
        "source": "app",
        "templateid": "pneumonia",
        "stuNo": userInfo['stuNo'],
        "username": userInfo['username'],
        "userid": round(time.time()),
        "updatainfo": [  
                  {
                    "propertyname": "isGoWarningAdress",
                    "value": "女"
                  },
                  {
                    "propertyname": "jtdz",
                    "value": "河南省郑州市金水区"
                  },
                  {
                    "propertyname": "personNO",
                    "value": "412801199711041722"
                  },
                  {
                    "propertyname": "langtineadress",
                    "value": "河南省郑州市金水区七号院三号楼一单元10号"
                  },
                  {
                    "propertyname": "ownPhone",
                    "value": "13253616952"
                  },
                  {
                    "propertyname": "emergencyContact",
                    "value": "13592506675"
                  },
                  {
                    "propertyname": "tradeNum",
                    "value": "D01S204"
                  },
                  {
                    "propertyname": "temperature",
                    "value": "36.4"
                  },
                  {
                    "propertyname": "symptom",
                    "value": "均无"
                  },
                  {
                    "propertyname": "isContactpatient",
                    "value": "均无"
                  },
                  {
                    "propertyname": "istouchcb",
                    "value": "否"
                  },
                  {
                    "propertyname": "isTransitProvince",
                    "value": "否"
                  },
                  {
                    "propertyname": "isTouch",
                    "value": "否"
                  },
                  {
                    "propertyname": "backadress",
                    "value": ""
                  },
                  {
                    "propertyname": "isContactFriendIn14",
                    "value": "否"
                  },
                  {
                    "propertyname": "sxaddress",
                    "value": ""
                  },
                  {
                    "propertyname": "medicalObservation",
                    "value": "否"
                  },
                  {
                    "propertyname": "sxss",
                    "value": ""
                  },
                  {
                    "propertyname": "isConfirmed",
                    "value": "否"
                  },
                  {
                    "propertyname": "assistRemark",
                    "value": ""
                  },
                  {
                    "propertyname": "gyfh",
                    "value": "否"
                  },
                  {
                    "propertyname": "FamilyIsolate",
                    "value": ""
                  },
                  {
                    "propertyname": "ishborwh",
                    "value": "否"
                  },
                  {
                    "propertyname": "IsHospitaltxt",
                    "value": ""
                  },
                  {
                    "propertyname": "fhhb",
                    "value": "否"
                  },
                  {
                    "propertyname": "isname",
                    "value": ""
                  },
                  {
                    "propertyname": "other1",
                    "value": ""
                  },
                  {
                    "propertyname": "isFFHasSymptom",
                    "value": "是"
                  }
        ],
        "gpsType": 1,
        "token": "8bc37c38-a030-4ade-9821-fcd30215ddcd"
      }
    }    

#信息获取函数
def getUserInfo(token):
    token={'token':token}
    sign_url = "https://reportedh5.17wanxiao.com/api/clock/school/getUserInfo"
    #提交打卡
    response = requests.post(sign_url, data=token)
    return response.json()['userInfo']

#打卡提交函数
def checkIn(userInfo,token):
    sign_url = "https://reportedh5.17wanxiao.com/sass/api/epmpics"
    jsons=getUserJson(userInfo,token)
    #提交打卡
    response = requests.post(sign_url, json=jsons)
    return response

#微信通知
def wechatPush(title,sckey,success,fail,result):    
    strTime = getNowTime()
    page = json.dumps(result.json(), sort_keys=True, indent=4, separators=(',', ': '),ensure_ascii=False)
    content = f"""
`{strTime}` 
#### 打卡成功用户：
`{success}` 
#### 打卡失败用户:
`{fail}`
#### 主用户打卡信息:
```
{page}
```
### 😀[收藏此项目](https://github.com/YooKing/HAUT_autoCheck)

        """
    data = {
            "text":title,
            "desp":content
    }
    scurl='https://sc.ftqq.com/'+sckey+'.send'
    try:
        req = requests.post(scurl,data = data)
        if req.json()["errmsg"] == 'success':
            print("Server酱推送服务成功")
        else:
            print("Server酱推送服务失败")
    except:
        print("微信推送参数错误")

if __name__ == '__main__':
    main()
