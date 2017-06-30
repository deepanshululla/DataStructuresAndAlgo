package com.methodOverloading;

/**
 * Created by deepa on 6/20/2017.
 */
public class Main {
    public static void main(String[] args){
//        int newScore= calculateScore("Hugo", 100);
//        //System.out.println();
//        int newScore2= calculateScore(500);
//        calculateScore();
//        calculateScore("Sherlock",400.5);

        calcFeetAndInchestoCentimeters(5,3);
        calcFeetAndInchestoCentimeters(63);
        calcFeetAndInchestoCentimeters(6,0);
        calcFeetAndInchestoCentimeters(-120);
    }
    public static double calcFeetAndInchestoCentimeters(int feet, int inches){
        if(feet>=0 && inches<=12 && inches>=0){
            //1 ft=12 inches and 1 inch =2.54 centimeter
            double totalinches=feet*12+inches;
            double centimeters=totalinches*2.54;
            System.out.println(" The height in centimeter is "+centimeters);
            return centimeters;
        }
        else{
            System.out.println("Invalid parameters");
        }
        return -1;
    }
    public static double calcFeetAndInchestoCentimeters(int inches){
        if (inches>=0){
            int feet=inches/12;
            int newFeet=inches%12;
            return calcFeetAndInchestoCentimeters(feet,newFeet);
        }
        else{
            System.out.println("Invalid parameters");
        }
        return -1;
    }
    public static int calculateScore(String name, int score){
        System.out.println("Player "+ name+ " has scored "+ score);
        return score*1000;
    }
    public static int calculateScore(int score){
        System.out.println("Anonymous Player "+ "has scored "+ score);
        return score*1000;
    }
    public static void calculateScore(){
        System.out.println("No information available");
        //return 0;
    }
    public static int calculateScore(String name, double score){
        System.out.println("Player "+ name+ " has scored "+ score);
        return (int)score*1000;
    }

}
