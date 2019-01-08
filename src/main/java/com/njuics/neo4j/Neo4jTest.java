package com.njuics.neo4j;

import org.neo4j.driver.v1.AuthTokens;
import org.neo4j.driver.v1.Driver;
import org.neo4j.driver.v1.GraphDatabase;
import org.neo4j.driver.v1.Session;
import org.neo4j.driver.v1.StatementResult;
import org.neo4j.driver.v1.Transaction;
import org.neo4j.driver.v1.TransactionWork;

import static org.neo4j.driver.v1.Values.parameters;

/**
 * Neo4jTest
 */
public class Neo4jTest implements AutoCloseable {
    private final Driver driver;

    public Neo4jTest( String uri, String user, String password )
    {
        driver = GraphDatabase.driver( uri, AuthTokens.basic( user, password ) );
    }

    @Override
    public void close() throws Exception {
        driver.close();
    }

    public void printGreeting(final String message) {
        try (Session session = driver.session()) {
            String greeting = session.writeTransaction(new TransactionWork<String>() {
                @Override
                public String execute(Transaction tx) {
                    StatementResult result = tx.run("CREATE (a:Greeting) " + "SET a.message = $message "
                            + "RETURN a.message + ', from node ' + id(a)", parameters("message", message));
                    return result.single().get(0).asString();
                }
            });
            String readsql = session.readTransaction(new TransactionWork<String>(){

                @Override
                public String execute(Transaction tx) {
                    StatementResult rs = tx.run("MATCH (n:Company) RETURN n LIMIT 25");
                    return rs.next().get("n").toString();
                }

            });
            System.out.println(greeting);
            System.out.println(readsql);
        }
    }

    public static void main(String... args) throws Exception {
        try (Neo4jTest greeter = new Neo4jTest("bolt://localhost:8687", "neo4j", "")) {
            greeter.printGreeting("hello, world");
        }
    }
}
