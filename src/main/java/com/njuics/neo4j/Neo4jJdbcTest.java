package com.njuics.neo4j;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

/**
 * Neo4jJdbcTest
 */
public class Neo4jJdbcTest {

    public static void main(String[] args) throws SQLException {
        Connection con = DriverManager.getConnection("jdbc:neo4j:bolt://localhost:8687");

        // Querying
        try (Statement stmt = con.createStatement()) {
            ResultSet rs = stmt.executeQuery("MATCH (n:Company) RETURN n LIMIT 25");
            while (rs.next()) {
                System.out.println(rs.getString("n"));
            }
        }
        con.close();

    }
}