package com.njuics;

import java.io.File;
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Date;

import com.njuics.kafka.*;

public class Check2Kafka {

    // private long maxDelayMsecs = 6 * 1000;
    // private long watermarkDelayMSecs = 600;
    long sleeptime = 1000;
    boolean display = true;

    public static void main(String[] args) {
        System.out.println(args.length);
        File file = new File(args[0]);
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            Check2Kafka w = new Check2Kafka();
            w.generateOrderedStream(br);
        } catch (Exception e) {
            System.out.println("error occured");
            System.out.println(e.getMessage());
        }
    }

    private void generateOrderedStream(BufferedReader br) {

        String line;
        String wasteid = new Date().toString();
        Producer prod = new Producer("114.212.189.141:9092", "topic1");
        int count = 0;
        
        try {
            while ((line = br.readLine()) != null) {
                if (this.display)
                    System.out.println(line);

                prod.send(wasteid+count, line);
                Thread.sleep(sleeptime);
                count ++;
            }
        } catch (Exception e) {
            System.out.println("produce data error occured");
            System.out.println(e.getMessage());
        }
        prod.close();
    }

}
