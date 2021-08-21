package freizl.chp05;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.junit.Test;

/**
 * Generic Methods.
 * 
 */
public class Item28 {

	@Test
	@SuppressWarnings("unused")
	public void testPushAll_1() {
		Stack<Number> numberStack = new Stack<Number>();
		List<Integer> integers = new ArrayList<Integer>(Arrays.asList(1, 2, 3));

		// compile error
		// numberStack.pushAll_1(integers);

	}

	@Test
	public void testPushAll_2() {
		Stack<Number> numberStack = new Stack<Number>();
		List<Integer> integers = new ArrayList<Integer>(Arrays.asList(1, 2, 3));

		numberStack.pushAll_2(integers);

	}

	@Test
	@SuppressWarnings("unused")
	public void testPopAll_1() {
		Stack<Number> numberStack = new Stack<Number>();
		List<Object> integers = new ArrayList<Object>();

		// compile error
		// numberStack.popAll_1(integers);

	}

	@Test
	public void testPopAll_2() {
		Stack<Number> numberStack = new Stack<Number>();
		List<Object> integers = new ArrayList<Object>();

		// compile error
		numberStack.popAll_2(integers);

	}

}
