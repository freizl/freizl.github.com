package freizl.chp05;

import java.util.ArrayList;
import java.util.List;

import org.junit.Test;

public class Item23 {

	@Test
	public void test1() {
		List<Object> objectTypes = new ArrayList<Object>();
		objectTypes.add("aa");

		/**
		 * List<String> is a subtype of the raw type List, but not of the
		 * parameterized type List<Object> (Item 25).
		 */
		// compile error
		// objectTypeAdd(new ArrayList<String>(), "bb");
	}

	@SuppressWarnings("unused")
	private void objectTypeAdd(List<Object> a, Object value) {
		a.add(value);
	}

	@SuppressWarnings("unused")
	private void wildcardTypesAdd(List<?> a, String value) {
		a.add(null);
		/** you can’t put any element (other than null) into a Collection<?> */
		// compile error
		// a.add(value);
	}

}
