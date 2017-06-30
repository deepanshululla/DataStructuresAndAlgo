package com.Arrays;

import java.util.Scanner;

/**
 * Created by deepa on 6/27/2017.
 */
public class AverageArray {
    private static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args){
        int[] myArray = scanArray(5);
        printArray(myArray);
        System.out.println(" the average is "+ getAverage(myArray));
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
            System.out.println("Element "+i+":"+myArray4[i]);
        }
    }
    public static double getAverage(int[] myArray){
        double averageVal=0;
        int sum=0;
        for(int i=0;i<myArray.length;i++){
            sum+=myArray[i];
        }
        averageVal=(double) sum/(double) myArray.length;
        return averageVal;
    }
}
