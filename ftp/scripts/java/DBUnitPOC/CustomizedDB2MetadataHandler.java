package com.freizl.dbunit.custom;

import java.sql.ResultSet;
import java.sql.SQLException;

import org.dbunit.database.DefaultMetadataHandler;
import org.dbunit.util.SQLHelper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Customized MetadataHandler for DB2 as match Columns failed with a
 * RuntimeException warning. {@link DBUnit Bug 2838922}.
 * 
 */
public class CustomizedDB2MetadataHandler extends DefaultMetadataHandler {

    public CustomizedDB2MetadataHandler() {
        super();
    }

    private static final Logger logger = LoggerFactory
            .getLogger(DefaultMetadataHandler.class);

    public boolean matches(ResultSet columnsResultSet, String catalog,
            String schema, String table, String column, boolean caseSensitive)
            throws SQLException {
        if (logger.isTraceEnabled())
            logger.trace("matches(columnsResultSet={}, catalog={}, schema={},"
                    + " table={}, column={}, caseSensitive={}) - start",
                    new Object[] { columnsResultSet, catalog, schema, table,
                            column, Boolean.valueOf(caseSensitive) });

        String catalogName = columnsResultSet.getString(1);
        String schemaName = columnsResultSet.getString(2);
        String tableName = columnsResultSet.getString(3);
        String columnName = columnsResultSet.getString(4);

        if (logger.isDebugEnabled()) {
            logger
                    .debug(
                            "Comparing the following values using caseSensitive={} (searched<=>actual): "
                                    + "catalog: {}<=>{} schema: {}<=>{} table: {}<=>{} column: {}<=>{}",
                            new Object[] { Boolean.valueOf(caseSensitive),
                                    catalog, catalogName, schema, schemaName,
                                    table, tableName, column, columnName });
        }

        boolean areEqual = areEqualIgnoreBothNull(catalog, catalogName,
                caseSensitive)
                && areEqualIgnoreNull(schema, schemaName, caseSensitive)
                && areEqualIgnoreNull(table, tableName, caseSensitive)
                && areEqualIgnoreNull(column, columnName, caseSensitive);
        return areEqual;
    }

    private boolean areEqualIgnoreBothNull(String value1, String value2,
            boolean caseSensitive) {
        boolean areEqual = true;
        if (value1 != null && value2 != null) {
            if (value1.equals("") && value2.equals("")) {
                if (caseSensitive) {
                    areEqual = value1.equals(value2);
                } else {
                    areEqual = value1.equalsIgnoreCase(value2);
                }
            }
        }
        return areEqual;
    }

    private boolean areEqualIgnoreNull(String value1, String value2,
            boolean caseSensitive) {
        return SQLHelper.areEqualIgnoreNull(value1, value2, caseSensitive);
    }

}
