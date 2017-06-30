package com.charboolean;

/**
 * Created by deepa on 6/18/2017.
 */
public class Main {
    public static void main(String[] args){
        char myChar = 'A';
        //can only store one character
        //we can also enter unicode characters
        char myChar2= '\u00A9';
        //https://unicode-table.com/en/#control-character
        System.out.println(myChar);
        System.out.println("unicode value= "+ myChar2);
        boolean myBool = true;
        boolean myBool2 = false;
        System.out.println("it is "+ myBool);
    }
}
