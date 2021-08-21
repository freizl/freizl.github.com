package com.perficient;

import java.util.ArrayList;
import java.util.List;

import org.junit.Test;

public class Item23 {

	@Test
	public void testRawTypeRuntiemError() {
		List<String> strings = new ArrayList<String>();
		unsafeAdd(strings, new Integer(42));
		String s = strings.get(0);
	}

	private void unsafeAdd(List list, Object o) {
		list.add(o);
	}

	@Test
	public void testRawTypeCompileError() {
		List<String> strings = new ArrayList<String>();
		safeAdd(strings, new Integer(42));
		String s = strings.get(0);
	}

	private void safeAdd(List<Object> list, Object o) {
		list.add(o);
	}

	@Test
	public void testAddSomethingToWildcastTypeList() {
		List<?> impossibleList = new ArrayList<?>();
		List<?> results = null;
		wildcastAdd(results, null);
	}

	private void wildcastAdd(List<?> list, Object o) {
		// can not add anything to wildcast type list, other than null
		list.add(o);
		list.add(null);
	}
}