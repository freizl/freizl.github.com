package com.freizl.dbunit;

import static org.junit.Assert.assertEquals;

import org.dbunit.database.QueryDataSet;
import org.dbunit.dataset.Column;
import org.dbunit.dataset.DefaultDataSet;
import org.dbunit.dataset.DefaultTable;
import org.dbunit.dataset.IDataSet;
import org.dbunit.dataset.datatype.DataType;
import org.junit.Test;

/**
 * Construct Dataset manually with DefaultDataSet and DefaultTable.
 * 
 */
public class DefaultDatasetTest extends AbstractDBUnitTest {

    private String testTable = "EMPLOYEE";

    @Test
    public void testView() throws Exception {

        QueryDataSet qds = new QueryDataSet(getDatabaseTester().getConnection());

        qds
                .addTable(testTable,
                        "select * from EMPLOYEE where employee_id >= 2 and employee_id <= 4");
        assertEquals(3, qds.getTable(testTable).getRowCount());
        assertEquals("Drew", qds.getTable(testTable).getValue(0, "First_Name"));

    }

    protected IDataSet getDataSet() throws Exception {
        Column[] employeeColumns = initTableColumns();

        String[] employeeRowOne = { "2", "Dreww", "Smith", "000-29-2030" };
        String[] employeeRowTwo = { "3", "Nickk", "Marquiss", "000-90-0000" };
        String[] employeeRowThree = { "4", "Josee", "Whitson", "000-67-0000" };

        DefaultTable table = new DefaultTable(testTable, employeeColumns);
        table.addRow(employeeRowOne);
        table.addRow(employeeRowTwo);
        table.addRow(employeeRowThree);

        DefaultDataSet set = new DefaultDataSet(table);
        return set;
    }

    private Column[] initTableColumns() {
        Column employeeId = new Column("EMPLOYEE_ID", DataType.NUMERIC,
                Column.NO_NULLS);
        Column firstName = new Column("FIRST_NAME", DataType.VARCHAR);
        Column lastName = new Column("LAST_NAME", DataType.VARCHAR);
        Column ssn = new Column("SSN", DataType.VARCHAR);

        return new Column[] { employeeId, firstName, lastName, ssn };
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