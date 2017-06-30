package com.Strings;

/**
 * Created by deepa on 6/18/2017.
 */
public class Main {
    public static void main(String[] args){
        String myString = "string is always in double quotes";
        System.out.println("here is a string: "+ myString);
        String newString = "concat:" + myString;
        System.out.println("another:"+ newString);
        String string2= newString + "\u00A9 2017";
        System.out.println("another:"+ string2);
        String string3= newString + "25.78";
        System.out.println("another:"+ string3);
        String string4= newString + 50;
        System.out.println("another:"+ string4);

    }
}
