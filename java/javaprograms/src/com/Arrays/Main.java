package com.Arrays;

/**
 * Created by deepa on 6/27/2017.
 */
public class Main {
    public static void main(String[] args){
        int[] myArray;
        myArray= new int[10];//declaration
        //or
        int[] myArray2=new int[10];//declaration

        //10 is no. of elements in array
        //or
        int[] myArray3={1,2,3,4,56,6,6,7,8,8,9};//declaration with initialization
        myArray[5]=50;

        //or
        int[] myArray4=new int[10];//declaration
        //another way to initializae is to use loops
        for(int i=0;i<myArray4.length;i++){
            myArray4[i]=i;
        }
        printArray(myArray4);
        int elem = myArray[5];
        System.out.println(elem);
        System.out.println(myArray[5]);
        elem=60;//
        System.out.println(myArray[5]);
        System.out.println(elem);
        //arrays index start from 0 to length of array -1
        String[] myStringArray= new String[5];
        myStringArray[0]="hello world";
        System.out.println(myStringArray[0]);


    }
    public static void printArray(int[] myArray4){
        for(int i=0;i<myArray4.length;i++){
            System.out.println(myArray4[i]);
        }
    }

}
