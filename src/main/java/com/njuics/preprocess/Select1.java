package com.njuics.preprocess;

// import java.beans.Statement;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.sql.ResultSet;

import com.njuics.hive.HiveJdbcClient;

/**
 * Select1
 */
public class Select1 {

    public static void main(String[] args) {
        String outfilename = "mlmodel/python/data/lgpc/checkedP3.csv";
        HiveJdbcClient hjc = new HiveJdbcClient("jdbc:hive2://114.212.189.141:30973/zhijian");
        String sql = "select * from checkedproduct";
        System.out.println("Running: " + sql);
        try {
            ResultSet res = hjc.executeQuery(sql);
            // res.next();
            // while (res.next()) {
            //     System.out.println(res.getString(1) + "\t" + res.getString(2));
            // }
            BufferedWriter writer = new BufferedWriter(new FileWriter(outfilename));
            while (res.next()) {
                String str = res.getString(1);
                for (int s = 2; s < 13; s++) {
                    str += "," + res.getString(s);
                }
                writer.write(str + "\n");
            }
            writer.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
        System.out.println("End.");
    }
}