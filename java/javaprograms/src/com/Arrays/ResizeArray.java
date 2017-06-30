package com.Arrays;

import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by deepa on 6/27/2017.
 */
public class ResizeArray {
    private static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args){
        int[] tryArr={2,3,5,6,1};
        printArray(tryArr);
        int[] newArr =resizeArray(tryArr,tryArr.length+2);
        newArr[5]=4;
        newArr[6]=89;
        printArray(newArr);
    }

    public static int[] resizeArray(int[] array, int newlength){
        int[] newArr;
        if (newlength<=array.length){
            newArr= Arrays.copyOf(array,newlength);
            //copies only first newlength elements
        }
        else{
            newArr =new int[newlength];
            for(int i=0;i<array.length;i++){
                newArr[i]=array[i];
            }
            //for(int i=array.length;i<newlength;i++){
            //    newArr[i]=-1;
            //}
        }

        return newArr;
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
