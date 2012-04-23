package com.freizl.dbunit;

import static org.junit.Assert.assertEquals;

import org.dbunit.database.QueryDataSet;
import org.dbunit.dataset.DefaultDataSet;
import org.dbunit.dataset.ITable;
import org.dbunit.operation.DatabaseOperation;
import org.dbunit.operation.DeleteOperation;
import org.junit.Test;

public class SampleTest extends AbstractDBUnitTest {

    @Test
    public void testView() throws Exception {

        QueryDataSet qds = new QueryDataSet(getDatabaseTester().getConnection());

        String testTable = "EMPLOYEE";
        qds
                .addTable(testTable,
                        "select first_name from EMPLOYEE where employee_id >= 2 and employee_id <= 4");
        assertEquals(3, qds.getTable(testTable).getRowCount());
        assertEquals("Drew", qds.getTable(testTable).getValue(0, "First_Name"));

    }

    @Test
    public void testDelete() throws Exception {

        String testTable = "EMPLOYEE";
        String deleteTarget = "select * from EMPLOYEE where employee_id >= 2 and employee_id <= 4";

        // another way to create dataset
        ITable table = this.getDatabaseTester().getConnection()
                .createQueryTable(testTable, deleteTarget);
        DefaultDataSet set = new DefaultDataSet(table);
        DeleteOperation.DELETE.execute(
                this.getDatabaseTester().getConnection(), set);

        DatabaseOperation.DELETE.execute(getDatabaseTester().getConnection(),
                set);

        QueryDataSet expectedDS = new QueryDataSet(this.getDatabaseTester()
                .getConnection());
        expectedDS.addTable(testTable, deleteTarget);
        assertEquals(0, expectedDS.getTable(testTable).getRowCount());

    }

    @Override
    protected void customSetup() throws Exception {
        // TODO Auto-generated method stub

    }

    @Override
    protected void customTeardown() throws Exception {
        // TODO Auto-generated method stub

    }
}