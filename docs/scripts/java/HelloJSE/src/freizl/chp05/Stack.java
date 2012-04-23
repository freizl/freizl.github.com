package freizl.chp05;

import java.util.ArrayList;
import java.util.List;

public class Stack<E> {
	private List<E> stack = new ArrayList<E>();

	public void pushAll_1(List<E> src) {
		for (E x : src) {
			push(x);
		}
	}

	public void pushAll_2(List<? extends E> src) {
		for (E x : src) {
			push(x);
		}
	}

	public void popAll_1(List<E> dest) {
		while (!isEmpty()) {
			dest.add(pop());
		}
	}

	public void popAll_2(List<? super E> dest) {
		while (!isEmpty()) {
			dest.add(pop());
		}
	}

	public void push(E x) {
		stack.add(x);
	}

	public E pop() {
		return stack.remove(stack.size() - 1);
	}

	public boolean isEmpty() {
		return stack.size() == 0;
	}
}
