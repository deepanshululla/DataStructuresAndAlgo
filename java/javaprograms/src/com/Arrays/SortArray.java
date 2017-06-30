package com.Arrays;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;


/**
 * Created by deepa on 6/27/2017.
 */
public class SortArray {
    private static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args){
        int[] tryArr={2,3,5,6,1};
        printArray(sortArray(tryArr));
    }

    public static int[] sortArray(int[] array){

        int[] sortedArr= Arrays.copyOf(array,array.length);
        boolean flag=true;
        int temp;
        while(flag){
            flag=false;
            // element 0 :160
            //elemnt 1 :40
            //elemnt 2 :50
            for(int i=0;i<array.length-1;i++){
                if(sortedArr[i]<sortedArr[i+1]){
                    temp=sortedArr[i];
                    sortedArr[i]=sortedArr[i+1];
                    sortedArr[i+1]=temp;
                    flag=true;
                }
            }
        }

        return sortedArr;
    }
    public static int[] scanArray(int num){
        System.out.println("Enter "+num+" values:");
        int[] values= new int[num];

        for(int i=0;i<values.length;i++){
            values[i]=scanner.nextInt();
        }
        return values;
    }
    public static void printArray(int[] myArray4){
        for(int i=0;i<myArray4.length;i++){
            System.out.println("Element "+i+" is "+myArray4[i]);
        }
    }
}
