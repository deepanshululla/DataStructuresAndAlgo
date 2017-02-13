/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sortingalgorithmsPackage;

import java.util.Arrays;

/**
 *
 * @author deepanshu
 */
public class MergeSort{
   
    private int[] helper;
    private int lengthArray;
    private int[] numbers;
    
    public void sort(int[] input){
        //this.inp=input;
        System.out.println("before sorting "+Arrays.toString(input));
        lengthArray=input.length;
        this.numbers=input;
        this.helper=new int[lengthArray];
        
        mergeSortHelper(0,lengthArray-1);
        System.out.println("After sorting "+Arrays.toString(input));
    }
    
    public void mergeSortHelper(int start_index,int end_index){
        //System.out.println("Splitting "+Arrays.toString(inp));
        if (start_index<end_index){
            int midPoint=(start_index+end_index)/2;
            mergeSortHelper(start_index,midPoint);
            mergeSortHelper(midPoint+1,end_index);
            merge(start_index,midPoint,end_index);
            
        }
    }    

    public void merge(int start_index,int midPoint,int end_index){
         
            int i=start_index,j=midPoint+1,k=start_index;
            for(int p = start_index; p <= end_index; p++) {
                helper[p] = numbers[p];
            }
            while(i<=midPoint && j<=end_index){
                if (helper[i]<=helper[j]){
                    numbers[k]=helper[i];
                    i++;
                }
                else{
                    numbers[k]=helper[j];
                    j++;
                }
                k++;
            }
            while (i<=midPoint){
                numbers[k]=helper[i];
                i++;
                k++;
            }
            
       
    }
    
   /* 
    public static void main(String[] args){
        int[] arr={6,1,3,2,6,5,7};
        MergeSort m=new MergeSort();
        m.sort(arr);
        //Integer[] arr2 = sort(arr);
        System.out.println("Sorted "+Arrays.toString(arr));
        //Integer[] sortedArr={1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7};
    }
*/
}
