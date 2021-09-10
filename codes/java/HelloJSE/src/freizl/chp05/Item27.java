package freizl.chp05;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Set;

import org.junit.Test;

/**
 * Generic Methods.
 * 
 */
public class Item27 {

	@Test
	public void test1() {
		Set<String> guys = new HashSet<String>(Arrays.asList("Tom", "Dick",
				"Harry"));
		Set<String> stooges = new HashSet<String>(Arrays.asList("Larry", "Moe",
				"Curly"));

		/**
		 * In the case , the compiler sees that both arguments to union are of
		 * type Set<String>, so it knows that the type parameter E must be
		 * String. This process is called type inference.
		 */
		Set<String> aflCio = union(guys, stooges);

		System.out.println(aflCio);

	}

	// generic type method
	private static <E> Set<E> union(Set<E> s1, Set<E> s2) {
		Set<E> result = new HashSet<E>(s1);
		result.addAll(s2);
		return result;
	}

	@Test
	public void test2() {
		List<String> list = new ArrayList<String>(Arrays.asList("Tom", "Dick",
				"Harry"));
		System.out.println(max(list));
	}

	// Using a recursive type bound to express mutual comparability
	private static <T extends Comparable<T>> T max(List<T> list) {
		Iterator<T> i = list.iterator();
		T result = i.next();
		while (i.hasNext()) {
			T t = i.next();
			if (t.compareTo(result) > 0)
				result = t;
		}
		return result;

	}

}
