package com.jbw.algrothms;

import edu.princeton.cs.algs4.StdIn;

public class Queue_LkLst<Item> {
	private static class Node<Item> {
		Item item;
		Node<Item> next;
	}

	private Node<Item> first;
	private Node<Item> last;
	private int N;

	public Queue_LkLst() {
		first = null;
		last = null;
		N = 0;
	}

	public boolean isEmpty() {
		return first == null;
	}

	public int size() {
		return N;
	}

	public Item enqueue(Item item) {
		Node<Item> oldlast = last;
		last = new Node<Item>();
		last.item = item;
		last.next = null;
		if (isEmpty()) {
			first = last;
		} else {
			oldlast.next = last;
		}
		N++;
		return item;
	}

	public Item dequeue() {
		if (!isEmpty()) {
			Item item = first.item;
			first = first.next;
			N--;
			return item;
		} else {
			return null;
		}
	}

	public static void main(String[] args) {
		Queue_LkLst<String> q = new Queue_LkLst<>();
		while (true) {
			String item = StdIn.readString();
			if (!item.equals("-")) {
				System.out.println(q.enqueue(item) + " is appended to the queue.");
			} else {
				if (q.isEmpty()) {
					System.out.println("the queue is empty!");
				} else {
					System.out.println(q.dequeue() + " is removed from the queue.");
				}
			}
		}
	}
}
