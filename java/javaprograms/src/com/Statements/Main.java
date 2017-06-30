package com.Statements;

/**
 * Created by deepa on 6/18/2017.
 */
public class Main {
    public static void main(String[] args) {
        // all variable types names can't be used as variable names
        int myvar = 50;//this is the whole statement myvar=50 is an expression
        myvar++;//is also a statement
        System.out.println("this is a statement");
        System.out.println("This " +
                "is " + "another " +
                "statement "
        );// Even on multiple lines java thinks since semicolon is not there,the steament is not ended
        int var2 = 50;double var3 = 4;
        //multiple statements seperated bys semicolon is fine

    }
}
