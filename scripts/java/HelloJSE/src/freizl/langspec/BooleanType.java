package freizl.langspec;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

/**
 * JLS §4.2.5
 */
public class BooleanType {

	@Test
	public void test1() {
		boolean x = true;
		boolean y = true;
		boolean z = false;

		assertTrue(x & y);
		assertTrue(x | z);
		assertTrue(z ^ y);
	}

	@Test
	public void test2() {
		/**
		 * && operator is like & (§15.22.2), but evaluates its right-hand
		 * operand only if the value of its left-hand operand is true.
		 */
		assertFalse(getXValue() && getYValue());
		assertTrue(getXValue() || getZValue());
	}

	private boolean getXValue() {
		System.out.println("about to get x value.");
		return false;
	}

	private boolean getYValue() {
		System.out.println("about to get y value.");
		return true;
	}

	private boolean getZValue() {
		System.out.println("about to get z value.");
		return true;
	}

}
