package com.njuics.kafka;

import java.util.*;
import org.apache.kafka.clients.consumer.*;
import java.time.Duration;

public class Consumer {
    private KafkaConsumer<String, String> consumer;

    public Consumer(){
        Properties props = new Properties();
        props.put("bootstrap.servers", "114.212.189.141:9092");
        props.put("group.id", "hiveconsumer");
        props.put("enable.auto.commit", "true");
        props.put("auto.commit.interval.ms", "1000");
        props.put("session.timeout.ms", "30000");
        props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        consumer = new KafkaConsumer<String, String>(props);
        consumer.subscribe(Arrays.asList("topic1"));
    }
    public ConsumerRecords<String, String> poll(Duration d){
        return consumer.poll(d);
    }

    public void close(){
        consumer.close();
    }
}