/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sortingalgorithmsPackage;
import java.util.Arrays;
/**
 *
 * @author deepa
 */
public class QuickSort {
    private int[] array;
    public void sort(int[] arr){
        //QuickSort q=QuickSort();
        System.out.println("before sorting "+Arrays.toString(arr));
        array=arr;
        quickSortHelper(0,arr.length-1);
        System.out.println("After sorting "+Arrays.toString(array));
    }
    public void quickSortHelper(int start,int end){
        if (start<end){
            int split=partition(start,end);
            quickSortHelper(start,split-1);
            quickSortHelper(split+1,end);
        }
    }
    public int partition(int start,int end){
        int split;
        int i=start-1;
        int val=array[end];//choosing the last value as the pivot
        //System.out.printf("Pivot=%d\n",val);
        for(int j=start;j<end;j++){
            if (array[j]<val){
                i++;
                if (array[i]!=array[j]){
                    int temp=array[j];
                    array[j]=array[i];
                    array[i]=temp;
                }
            }
        }    
        if (array[i+1]!=array[end]){
                int temp2=array[i+1];
                array[i+1]=array[end];
                array[end]=temp2;
        }
        
        //System.out.println("intermediate sorting "+Arrays.toString(array));
        split=i+1;
        //System.out.printf("Splitpoint=index number %d\n ",split);
        return split;
    }
    /*
    public static void main(String[] args){
        int[] arr={6,1,3,2,5,7,7,4};
        QuickSort q=new QuickSort();
        q.sort(arr);
    }
*/
}
