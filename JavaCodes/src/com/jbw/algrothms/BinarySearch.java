package com.jbw.algrothms;

import edu.princeton.cs.algs4.StdIn;

public class BinarySearch {
	public static int rank(int key, int[] a) {
		int lo = 0;
		int hi = a.length - 1;
		while (lo <= hi) {
			int mid = lo + (hi - lo) / 2;
			if (a[mid] > key)
				hi = mid - 1;
			else if (a[mid] < key)
				lo = mid + 1;
			else
				return mid;
		}
		return -1;
	}
	
	public static void main(String[] args) {
		int a[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
		System.out.println("Please enter a number:");
		int key = StdIn.readInt();
		System.out.println(BinarySearch.rank(key, a));
	}
}
