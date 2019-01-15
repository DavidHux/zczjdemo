package com.njuics.hive;

import java.sql.SQLException;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.DriverManager;

public class HiveJdbcClient {
    // private static String driverName = "org.apache.hadoop.hive.jdbc.HiveDriver";
    private static String driverName = "org.apache.hive.jdbc.HiveDriver";
    private String connectionName = "jdbc:hive2://114.212.189.141:30973/default";
    private String user = "root";
    private String pswd = "";
    public Statement stmt;

    public HiveJdbcClient() {
        init();
    }
    private void init(){
        try {
            Class.forName(driverName);
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
            System.exit(1);
        }
        try {
            Connection con = DriverManager.getConnection(connectionName, user, pswd);
            stmt = con.createStatement();
        } catch (SQLException e) {
            e.printStackTrace();
            System.exit(1);
        }
    }

    public HiveJdbcClient(String connectionName) {
        this.connectionName = connectionName;
        init();
    }

    public void execute(String cmd) throws SQLException {
        stmt.execute(cmd);
    }

    public ResultSet executeQuery(String sql) throws SQLException {
        return stmt.executeQuery(sql);
    }

    public void close() {
        try {
            stmt.close();
        } catch (Exception e) {
            System.out.println("close jdbc client error");
            e.printStackTrace();
        }
    }

    /**
     * @param args
     * @throws SQLException
     **/
    public static void main(String[] args) throws SQLException {
        try {
            Class.forName(driverName);
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
            System.exit(1);
        }
        Connection con = DriverManager.getConnection("jdbc:hive2://114.212.189.141:30973/default", "root", "");
        Statement stmt = con.createStatement();
        String tableName = "pokes2";
        stmt.execute("drop table " + tableName);
        Boolean res1 = stmt.execute("create table " + tableName + " (key int, value string)");
        if (!res1) {
            System.out.println("create table failed");
        }
        // show tables
        String sql = "show tables '" + tableName + "'";
        System.out.println("Running: " + sql);
        ResultSet res = stmt.executeQuery(sql);
        if (res.next()) {
            System.out.println(res.getString(1));
        }
        // describe table
        sql = "describe " + tableName;
        System.out.println("Running: " + sql);
        res = stmt.executeQuery(sql);
        while (res.next()) {
            System.out.println(res.getString(1) + "\t" + res.getString(2));
        }
        // load data into table
        // NOTE: filepath has to be local to the hive server
        // NOTE: /tmp/test_hive_server.txt is a ctrl-A separated file with two fields
        // per line
        String filepath = "/root/pokes.txt";
        sql = "load data local inpath '" + filepath + "' into table " + tableName;
        System.out.println("Running: " + sql);
        stmt.execute(sql);
        // select * query
        sql = "select * from " + tableName;
        System.out.println("Running: " + sql);
        res = stmt.executeQuery(sql);
        while (res.next()) {
            System.out.println(String.valueOf(res.getInt(1)) + "\t" + res.getString(2));
        }
        // regular hive query
        sql = "select count(1) from " + tableName;
        System.out.println("Running: " + sql);
        res = stmt.executeQuery(sql);
        while (res.next()) {
            System.out.println(res.getString(1));
        }
    }
}