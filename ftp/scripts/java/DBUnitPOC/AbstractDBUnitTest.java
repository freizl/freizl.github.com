package com.freizl.dbunit;

import org.dbunit.IDatabaseTester;
import org.dbunit.JdbcDatabaseTester;
import org.dbunit.database.DatabaseConfig;
import org.dbunit.dataset.IDataSet;
import org.dbunit.dataset.xml.FlatXmlDataSet;
import org.dbunit.ext.oracle.OracleDataTypeFactory;
import org.dbunit.operation.DatabaseOperation;
import org.junit.After;
import org.junit.Before;

public abstract class AbstractDBUnitTest {

    private IDatabaseTester databaseTester;

    protected IDatabaseTester getDatabaseTester() {
        return databaseTester;
    }

    @Before
    public void setUp() throws Exception {
        System.out.println("I am before methods");
        initJdbcDatabaseTester();
        customSetup();
        databaseTester.setDataSet(getDataSet());
        databaseTester.onSetup();
    }

    private void initJdbcDatabaseTester() throws Exception {
        if (databaseTester == null) {
            databaseTester = new JdbcDatabaseTester(
                    "oracle.jdbc.driver.OracleDriver",
                    "jdbc:oracle:thin:@localhost:1521:orcl", "weblogic",
                    "weblogic", "WEBLOGIC");

            databaseTester.getConnection().getConfig().setProperty(
                    DatabaseConfig.PROPERTY_DATATYPE_FACTORY,
                    new OracleDataTypeFactory());

            databaseTester.setSetUpOperation(DatabaseOperation.REFRESH);
            databaseTester.setTearDownOperation(DatabaseOperation.NONE);

        }
    }

    protected IDataSet getDataSet() throws Exception {
        final FlatXmlDataSet dataset = new FlatXmlDataSet(Thread
                .currentThread().getContextClassLoader().getResourceAsStream(
                        "hr-seed.xml"));
        return dataset;
    }

    protected abstract void customSetup() throws Exception;

    @After
    public void tearDown() throws Exception {
        System.out.println("I am after methods");
        customTeardown();
        databaseTester.onTearDown();
    }

    protected abstract void customTeardown() throws Exception;

}