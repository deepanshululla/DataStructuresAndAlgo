package com.whileloops;

/**
 * Created by deepa on 6/20/2017.
 */
public class Main {
    public static void main(String[] args){
        int count=10;
        while(count<=5){
            System.out.println("count value is "+ count);
            count++;
        }
        System.out.println("******************");
        count=10;
        while(true){

            if(count >5){
                break;
            }
            System.out.println("count value is "+ count);
            count++;
        }
        System.out.println("******************");
        count=10;
        do{
            System.out.println("count value is "+ count);
            count++;
        }while(count<=5);
    }
}
