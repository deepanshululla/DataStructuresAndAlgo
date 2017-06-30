package com.floatsanddoubles;

/**
 * Created by deepa on 6/18/2017.
 */
public class Main {
    public static void main(String[] args){
        int myInt=5/3;
        double myDouble=5D/3D;
        // good practice to put d or D in the end for floats
        float myFloat=5F/3F;
        // good practice to put f or F in the end for floats

        // When you enter a decimal number java assumes a double number
        double myDouble2=4.35;
        //float myFloat2= 3.4; This is incorrect as java assumes no. with decimals are doubles
        float myFloat2= (float) 3.4;
        System.out.println(myInt);
        System.out.println(myDouble);
        System.out.println(myFloat);
        System.out.println(myDouble2);
        System.out.println(myFloat2);
    }

}
