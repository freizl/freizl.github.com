package com.poc.spring;

import java.util.List;
import java.util.Map;

import org.springframework.jdbc.core.support.JdbcDaoSupport;

public class EmployeeDaoImpl extends JdbcDaoSupport {

    public EmployeeDaoImpl() {
        super();
    }

    /**
     * Search for all employees.
     * 
     */
    @SuppressWarnings("unchecked")
    public List<Map<String, Object>> query() {
        return getJdbcTemplate().queryForList(
                "select * from employee order by employee_id");
    }

}
