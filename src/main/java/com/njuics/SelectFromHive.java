package com.njuics;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.sql.ResultSet;

import com.njuics.hive.HiveJdbcClient;

public class SelectFromHive {

    public static void main(String[] args) {
        String tablename = "checkeddata";
        String outfilename = "data/selectedDataFromHive.csv";

        // int[] ckpa = { 1, 50, 25, 26, 31, 23, 12, 13, 33, 32, 38 };
        // String[] keys = { "ID", "BUSLICENO", "MODEL", "PRODUCTTYPE", "BATCHNUM", "ISREFUSE", "REGION", "SCALE",
                // "WORKERNUM", "SALESVOLUME", "LABELISPASS" };
        String[] keys = {"ORGANID", "CERTNO", "PRODUCTTYPE", "PRODUCTTYPECODE", "SALESVOLUME", "PRODNAME", "SCALE", "SCALECONTENT", "YEARTOTALOUTPUT", "WORKERNUM", "ISPASS"};

        HiveJdbcClient hc = new HiveJdbcClient();
        String sql = "SELECT KAFKAKEY";
        for (String a : keys) {
            sql += ", " + a;
        }
        sql += " FROM " + tablename;
        System.out.println(sql);
        try {
            ResultSet rs = hc.executeQuery(sql);
            BufferedWriter writer = new BufferedWriter(new FileWriter(outfilename));
            while (rs.next()) {
                String str = rs.getString(1);
                for (int s = 2; s < 13; s++) {
                    str += ", " + rs.getString(s);
                }
                writer.write(str + "\n");
            }
            writer.close();
        } catch (Exception e) {
            System.out.println("select form hive error");
            e.printStackTrace();
        }
        hc.close();
    }
}