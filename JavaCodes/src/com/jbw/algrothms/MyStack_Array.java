package com.jbw.algrothms;

import java.util.Iterator;

import edu.princeton.cs.algs4.StdIn;

public class MyStack_Array<Item> implements Iterable<Item> {//The Stack data structure implemented by an Array.

	private Item[] a;
	private int N;

	public MyStack_Array(int cap) {
		a = (Item[]) new Object[cap];
	}

	public boolean isEmpty() {
		return N == 0;
	}

	public int size() {
		return N;
	}

	public Item push(Item item) {
		if (N == a.length)
			resizeStack(2 * a.length);
		a[N++] = item;
		return item;
	}

	public Item pop() {
		Item item = a[--N];
		a[N] = null;// 避免对象游离
		if (N <= (a.length / 4) && N > 0)
			resizeStack(a.length / 2);
		return item;
	}

	private void resizeStack(int max) {
		Item[] temp = (Item[]) new Object[max];
		for (int i = 0; i < N; i++) {
			temp[i] = a[i];
		}
		a = temp;
		System.out.println("The max size of stack now is adjusted to: " + a.length);
	}

	public class ReverseArrayIterator implements Iterator<Item> {

		private int i = N;

		@Override
		public boolean hasNext() {
			return i > 0;
		}

		@Override
		public Item next() {
			return a[--i];
		}

		@Override
		public void remove() {
		}

	}

	@Override
	public Iterator<Item> iterator() {
		return new ReverseArrayIterator();
	}

	private void print_all_left() {
		for (Item item : a) {
			if (item != null) {
				System.out.println(item);
			}
		}
	}

	// main function
	public static void main(String[] args) {
		MyStack_Array<String> s = new MyStack_Array<String>(1);
		while (true) {
			String item = StdIn.readString();
			if ((!item.equals("-")) && (!item.equals("exit"))) {
				System.out.println(s.push(item) + " is pushed in!");
			} else if (item.equals("exit")) {
				// ((Object[]) (s.a)).length is very important!
				System.out.println("The max size of stack now is: " + ((Object[]) (s.a)).length);
				System.out.println("(Here the " + s.size() + " item(s) still left on stack!)");
				s.print_all_left();
				return;
			} else if (!s.isEmpty()) {
				System.out.println(s.pop() + " is popped out!");
			} else {
				System.out.println("(" + s.size() + " item left on stack,can not pop anymore!)");
			}
		}
	}
}
