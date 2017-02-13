/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sortingalgorithmsPackage;

/**
 *
 * @author deepa
 */
public class RadixSort {
    public static int findMaxDigits(Integer[] arr,int base){
        int max=Integer.MIN_VALUE;
        int temp;
        for(int num: arr){
            temp = (int) Math.log(num)/(int)Math.log(base);
            if (temp>max){
                max=temp;
            }
        }
        return max;
    }
    public static Integer[] sort(Integer[] arr,int base){
        int numBuckets=base;//creating buckets=base
        int maxNumDigits=0;
        
        maxNumDigits=findMaxDigits(arr,base);
        //System.out.println(maxNumDigits);
        Integer[] curentDigit=new Integer[arr.length];
        int divisor=1;
        
        return arr;
    }
}
