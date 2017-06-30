package com.operators;

/**
 * Created by deepa on 6/18/2017.
 */
public class Main {
    public static void main(String[] args){

        int res=1+2;
        int myScore =100;
        boolean bool=true;
        char ctest= 'c';
        String strTest= "lorem ipsum";
        if ((myScore==100) && (bool==true)){
            System.out.println("hell yeah");
        }
        if ((myScore==100) || (bool==false)) System.out.println("yeah");
        if ((ctest=='c') && (strTest=="lorem ipsum")) System.out.println("it matches both strings and characters");
        //if myScore=100{}
        // the error was using only one equal to sign
        if (bool=false) System.out.println(" how come this is not an error");
        bool=false;
        if (bool=true) System.out.println(" The above one didn't print. will this one?");
        bool =true;
        boolean bool2= bool ? true: false;
        //ternary operator
        // so it is saying return true if bool is true else return false
        System.out.println("the result is "+ bool2);


    }
}
