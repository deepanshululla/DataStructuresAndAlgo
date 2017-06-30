package com.com.conditionals;

/**
 * Created by deepa on 6/20/2017.
 */
public class Main {
    public static void main(String[] args){
        int score = 50;
        boolean gameOver=true;
        if (score==50)//conditions hold always be wroiteen withing ()
            System.out.println("u can put single line without code blocks");
        if (score==50) {
            System.out.println("u can't put double line without code blocks");
            System.out.println("touche");
        }
        if (score<=50){
            System.out.println("yeah");
        } else if (score>100){
            System.out.println("lorem");
        } else{
            System.out.println("ipsum");
        } //block comments in intellij by cntrl+shift+/
        //you can comment single line comments in intellij with cntrl+/
        if (gameOver==true){
            int finalScore =score+ 1000;
            System.out.println("your final score is "+ finalScore);
            // scope of finalScoreis withing this code block. It can't be
            // accessed from outside
        }


    }
}
