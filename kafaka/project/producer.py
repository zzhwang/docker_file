from confluent_kafka import Producer
import requests

#producer配置，dict格式
p = Producer({'bootstrap.servers':'192.168.1.88:19092,192.168.1.88:29092,192.168.1.88:39092'})

#回调函数
def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

##发送
for data in [i for i in range(30)]:
    p.produce('test', str(data),partition=1,callback=delivery_report)

p.poll(10)  ##等待返回结果最大时常，单位秒
p.flush()




