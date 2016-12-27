package com.jbw.algrothms;

import edu.princeton.cs.algs4.StdIn;

public class MyStack_LkLst<Item> {// The Stack data structure implemented by a
									// linked list.

	private class Node {
		Item item;
		Node next;
	}

	private Node first;
	private int N;

	public boolean isEmpty() {
		return first == null;
	}

	public int size() {
		return N;
	}

	public Item push(Item item) {
		Node oldfirst = first;
		first = new Node();
		first.item = item;
		first.next = oldfirst;
		N++;
		return item;
	}

	public Item pop() {
		Item item = first.item;
		first = first.next;
		N--;
		return item;
	}

	public static void main(String[] args) {
		MyStack_LkLst<String> s = new MyStack_LkLst<>();
		while (true) {
			String item = StdIn.readString();
			if ((!item.equals("-")) && (!item.equals("exit"))) {
				System.out.println(s.push(item) + " is pushed in!");
			} else if (item.equals("exit")) {
				System.out.println("(Here the " + s.size() + " item(s) still left on stack!)");
				return;
			} else if (!s.isEmpty()) {
				System.out.println(s.pop() + " is popped out!");
			} else {
				System.out.println("(" + s.size() + " item left on stack,can not pop anymore!)");
			}
		}
	}

}
