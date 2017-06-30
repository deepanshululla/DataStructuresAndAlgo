package com.whileloops;

/**
 * Created by deepa on 6/20/2017.
 */
public class Main2 {
    public static void main(String[] args){
        int num1=5;
        int finish=15;
        int count=0;
        while (num1<finish){
            if(!isEven(num1)){
                num1++;
                continue;
            }
            count++;
            if(count>5){
                break;
            }
            System.out.println("Even number "+count+" is "+ num1);
            num1++;
        }
        System.out.println("total even numbers found="+count);
    }
    public static boolean isEven(int num){
        if(num%2==0){
            return true;
        }
        return false;
    }
}
