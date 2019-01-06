package com.njuics.kafka;

import java.util.*;
import org.apache.kafka.clients.consumer.*;
import org.apache.kafka.common.PartitionInfo;

public class TestTopics {
    public static void main(String[] args){
        Properties props = new Properties();
        props.put("bootstrap.servers", "114.212.189.141:9092");
        props.put("group.id", "te");
        props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        KafkaConsumer<String, String> simpleConsumer = new KafkaConsumer<String, String>(props);
        Map<String, List<PartitionInfo>> m = simpleConsumer.listTopics();
        m.forEach((k, v) -> System.out.println("key: " + k + ",value: " + v));
        simpleConsumer.close();
    }
}