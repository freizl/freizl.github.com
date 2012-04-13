package com.freizl.dbunit;

import static org.junit.Assert.assertEquals;

import java.io.FileInputStream;
import java.io.FileOutputStream;

import org.dbunit.database.QueryDataSet;
import org.dbunit.dataset.xml.FlatXmlDataSet;
import org.dbunit.operation.DatabaseOperation;
import org.junit.Test;

/**
 * Backup and Restore
 * 
 */
public class BackupTableTest extends AbstractDBUnitTest {

    private static final String ADDRESS_TABLE = "ADDRESS";
    private static final String EMPLOYEE_TABLE = "EMPLOYEE";
    private static final String EMPLOYEE_BACKUP = "employee-backup.xml";

    @Test
    public void testView() throws Exception {

        QueryDataSet qds = new QueryDataSet(getDatabaseTester().getConnection());

        qds
                .addTable(EMPLOYEE_TABLE,
                        "select first_name from EMPLOYEE where employee_id >= 2 and employee_id <= 4");
        qds.addTable(ADDRESS_TABLE);

        assertEquals(3, qds.getTable(EMPLOYEE_TABLE).getRowCount());
        assertEquals("Drew", qds.getTable(EMPLOYEE_TABLE).getValue(0,
                "First_Name"));
        assertEquals(1, qds.getTable(ADDRESS_TABLE).getRowCount());
        assertEquals(310050, qds.getTable(ADDRESS_TABLE).getValue(0,
                "post_code"));
    }

    @Override
    protected void customSetup() throws Exception {
        getDatabaseTester().setSetUpOperation(DatabaseOperation.CLEAN_INSERT);

        QueryDataSet backupDS = new QueryDataSet(this.getDatabaseTester()
                .getConnection());
        backupDS.addTable(EMPLOYEE_TABLE);
        backupDS.addTable(ADDRESS_TABLE);
        FlatXmlDataSet.write(backupDS, new FileOutputStream(EMPLOYEE_BACKUP));
    }

    @Override
    protected void customTeardown() throws Exception {
        getDatabaseTester()
                .setTearDownOperation(DatabaseOperation.CLEAN_INSERT);
        getDatabaseTester().setDataSet(
                new FlatXmlDataSet(new FileInputStream(EMPLOYEE_BACKUP)));
    }
}