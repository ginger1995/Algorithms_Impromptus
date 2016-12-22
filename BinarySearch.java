import java.util.Arrays;

public class BinarySearch {

    public static int rank(int key, int[] a){
        int lo = 0;
        int hi = a.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (a[mid] > key) hi = mid - 1;
            else if (a[mid] < key) lo = mid + 1;
            else return mid;
        }
        return -1;
    }

    public static void main(String[] args){
        //bsh = new BinarySearch();
        int a[] = {1,2,3,4,5,6,7,8,9};
        System.out.println(BinarySearch.rank(7, a));
    }
}
