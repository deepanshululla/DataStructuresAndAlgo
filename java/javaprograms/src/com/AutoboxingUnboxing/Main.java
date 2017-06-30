package com.AutoboxingUnboxing;

import java.util.ArrayList;

/**
 * Created by deepa on 6/29/2017.
 */
class IntClass{
    // this is a wrapper for an integer primitive data type
    private int value;

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public IntClass(int value) {

        this.value = value;
    }
}
public class Main {
    public static void main(String[] args){
        String[] strArray = new String[10];
        int[] intArray =new int[10];

        ArrayList<String> stringArrayList= new ArrayList<String>();
        stringArrayList.add("hello world");

        //ArrayList<int> intArrayList =new ArrayList<int>();
        // this gives an error because we can't use primitive types in array lists. We need to have a class
        ArrayList<Integer> integerArrayList = new ArrayList<Integer>();
        integerArrayList.add(54);
        //or
        //define our own class
        ArrayList<IntClass> intClassArrayList = new ArrayList<IntClass>();
        intClassArrayList.add(new IntClass(54));
        Integer myIntval2 =new Integer(54);
        Double myDouble= new Double(5.5);
        for(int i=0;i<10;i++){
            integerArrayList.add(i*10);
            //or
            integerArrayList.add(Integer.valueOf(i));
            //This is autoboxing which is typecasting int to Integer although java does it for us.
        }
        for(int i=0;i<integerArrayList.size();i++){
            System.out.println(i +" --> "+ integerArrayList.get(i).intValue());
            // This is unboxing where we get the value back of our primitive int type
            // unboxing is converting back to primitive type
        }
        System.out.println(integerArrayList);
        Integer myIntval= 45;
        // how is this working Integer is a class and we always to have to
        // initialize our classes like Integer myIntval =new Integer(54);
        int myInt = myIntval.intValue(); //this is what essentially the


    }
}
