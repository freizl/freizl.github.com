package freizl.langspec;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class CopyRightTest {

	@Before
	public void setUp() throws Exception {
	}

	@After
	public void tearDown() throws Exception {
	}

	@Test
	public void testValue() {
		getValue();
	}

	@CopyRight(value = "copy right")
	@Deprecated
	private String getValue() {
		return "Copy Right";
	}
}
