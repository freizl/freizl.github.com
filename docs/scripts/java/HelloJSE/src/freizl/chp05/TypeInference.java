package freizl.chp05;

import static org.junit.Assert.*;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.junit.Test;

public class TypeInference {
	
	@Test
	public void test1() {
		// Parameterized type instance creation with static factory
		Map<String, List<String>> anagrams = newHashMap();
		assertNotNull(anagrams);
	}

	/**
	 * Generic static factory method Another example at Item27.union function.
	 */
	public static <K, V> HashMap<K, V> newHashMap() {
		return new HashMap<K, V>();
	}

}
