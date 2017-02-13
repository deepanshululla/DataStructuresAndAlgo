/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sortingalgorithmsPackage;

import java.util.Arrays;

/**
 *only sorts positive integers,in place but uses O(k) space where k is maximum range for elements
 * Time=O(n+k)
 * @author deepa
 */
public class CountingSort {
    public static int findMax(int[] arr){
        int max=Integer.MIN_VALUE;
        for (int arr1 : arr) {
            if (arr1 > max) {
                max = arr1;
            }
        }
        return max;
    }
    public static void createCountArray(int[] count,int[] input){
        for(int i:input){
            count[i]++;
        }
        
    }
     public static void cumulateCountArray(int[] count){
        for(int i=1;i<count.length;i++){
            count[i]=count[i-1]+count[i];
        }
       
         
    }
    public static int[] arrange(int[] input,int[] counts){
        
        int[] out=new int[input.length+1];
        System.out.println("before sorting "+Arrays.toString(input));
        
        for (int i =input.length-1;i>=0;i--) {
           out[counts[input[i]]]=input[i];
           counts[input[i]]--; 
        }
      
        int[] out2=new int[input.length];
        out2=Arrays.copyOfRange(out,1,out.length);
        System.out.println("after sorting "+Arrays.toString(out2));
        return out2;
       
    }
    public static int[] sort(int[] input){
        int m=findMax(input);
        int[] out2=new int[input.length];
        int[] countArray=new int[m+1];//By default all arrays in java with int type are initalized to 0
        createCountArray(countArray,input);
        
        cumulateCountArray(countArray);
        //System.out.println("cumulative count array "+Arrays.toString(countArray));
        out2=arrange(input,countArray);
        return out2;
        
    }
    
   
}
