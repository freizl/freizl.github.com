package com.poc.spring;

import static org.junit.Assert.assertEquals;

import java.util.List;
import java.util.Map;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class EmployeeDaoImplTest {

    private static ApplicationContext act;
    private static EmployeeDaoImpl employeeDaoImpl;

    @BeforeClass
    public static void beforeClass() {
        act = new ClassPathXmlApplicationContext("daoApplicationContext.xml");
        employeeDaoImpl = (EmployeeDaoImpl) act.getBean("employeeDaoImpl");
    }

    @AfterClass
    public static void afterClass() {
        employeeDaoImpl = null;
        act = null;
    }

    @Before
    public void setUp() {

    }

    @After
    public void tearDown() {

    }

    @Test
    public void testQuery() {
        String[] names = { "Jose", "HellFire", "simon" };
        List<Map<String, Object>> result = employeeDaoImpl.query();
        for (int i = 0; i < result.size(); i++) {
            assertEquals(names[i], result.get(i).get("FIRST_NAME"));
        }

        assertEquals(3, result.size());
    }

}
