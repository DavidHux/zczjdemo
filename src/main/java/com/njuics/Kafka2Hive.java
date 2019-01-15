package com.njuics;

import java.time.Duration;
import java.util.Date;
import org.apache.kafka.clients.consumer.*;

import com.njuics.hive.HiveJdbcClient;
import com.njuics.kafka.Consumer;

public class Kafka2Hive {
    private static String tablename = "checkeddata";

    public static void main(String[] args) {
        Consumer cons = new Consumer();
        System.out.println("kafka2hive begin:");
        long t = new Date().getTime();
        HiveJdbcClient hc = new HiveJdbcClient();
        while (new Date().getTime() < t + 60 * 1000) {
            // System.out.printf("fsdf\n");
            Duration d = Duration.ofMillis(100);
            ConsumerRecords<String, String> records = cons.poll(d);
            if(records.isEmpty()){
                continue;
            }
            // INSERT INTO TABLE students
            // VALUES ('fred flintstone', 35, 1.28), ('barney rubble', 32, 2.32);
            String sql = "INSERT INTO TABLE " + tablename + " VALUES ";
            String dele = "";
            for (ConsumerRecord<String, String> record : records) {
                // System.out.printf("offset = %d, key = %s, value = %s\n", record.offset(),
                // record.key(), record.value());
                String[] ls = record.value().split("\",\"");
                if (ls.length != 104) {
                    System.out.println("kafka record length error, not 104");
                    System.out.printf(record.key(), record.value());
                }
                sql += dele;
                dele = " ,";
                sql += "('" + record.key() + "'";
                for (String str : ls) {
                    sql += ", '" + str.replace("\"", "") + "'";
                }
                sql += ")";
            }
            try {
                hc.execute(sql);
                System.out.println("record inserted");
            } catch (Exception e) {
                System.out.println("insert data to hive error");
                e.printStackTrace();
            }
        }
        cons.close();
    }
}