package com.methods;

/**
 * Created by deepa on 6/20/2017.
 */
public class Main {
    //methods should be withing class
    public static void main(String[] args){
        int finalScore1=calculateScore(true,800,5);
        //System.out.println("your final score is "+ finalScore);
        int finalScore2=calculateScore(false,100,1);
        //System.out.println("your final score is "+ finalScore);
        int finalScore3=calculateScore(true,150,1);
        int finalScore4=calculateScore(true,900,15);
        displayHighScorePosition("John",calculateHighScorePosition(finalScore1));
        displayHighScorePosition("Cena",calculateHighScorePosition(finalScore2));
        displayHighScorePosition("Jon",calculateHighScorePosition(finalScore3));
        displayHighScorePosition("Snow",calculateHighScorePosition(finalScore4));
    }

    public static int calculateScore(boolean gameOver, int score, int levelCompleted){
        int finalScore=-1;
        if(gameOver){
            finalScore = score +(levelCompleted * 10);
        }
        return finalScore;
    }
    public static void displayHighScorePosition(String name, int position){
        System.out.println(name +" has got position number " +position);
    }
    public static int calculateHighScorePosition(int score){
        if (score>1000){
            return 1;
        } else if (score<=1000 && score >500){
            return 2;
        } else if (score<=500 && score >100) {
            return 3;
        } else{
            return 4;
        }
    }
}
