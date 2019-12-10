from confluent_kafka import Consumer, KafkaError,TopicPartition

c = Consumer({
    'bootstrap.servers': '192.168.1.88:29092',
    'group.id': 'group2',
    'default.topic.config': {
        'auto.offset.reset': 'largest' # largest # smallest
 }
})

# 1 选取topic提取
# c.subscribe(['test'])

# 2 分区偏移 从第几个分区第几个数据开始
tp = TopicPartition('test',1,0)
c.assign([tp])
c.seek(tp)

while True:
    msg = c.poll()
    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(msg.error())
            break

    print('Received message: {},{},{}'.format(msg.value().decode('utf-8'),msg.topic(),msg.partition()))

c.close()
