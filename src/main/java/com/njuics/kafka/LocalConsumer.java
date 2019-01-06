package com.njuics.kafka;

import java.util.*;
import org.apache.kafka.clients.consumer.*;
import java.time.Duration;

public class LocalConsumer {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put("bootstrap.servers", "114.212.189.141:9092");
        props.put("group.id", "testlocalconsumer");
        props.put("enable.auto.commit", "true");
        props.put("auto.commit.interval.ms", "1000");
        props.put("session.timeout.ms", "30000");
        props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
        KafkaConsumer<String, String> consumer = new KafkaConsumer<String, String>(props);
        consumer.subscribe(Arrays.asList("topic1", "global22"));
        long t = new Date().getTime();
        while (new Date().getTime() < t + 60 * 1000) {
            // System.out.printf("fsdf\n");
            Duration d = Duration.ofMillis(100);
            ConsumerRecords<String, String> records = consumer.poll(d);
            for (ConsumerRecord<String, String> record : records)
                System.out.printf("offset = %d, key = %s, value = %s\n", record.offset(), record.key(), record.value());
        }
        consumer.close();
    }
}