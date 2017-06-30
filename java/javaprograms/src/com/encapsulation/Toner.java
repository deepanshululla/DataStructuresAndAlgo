package com.encapsulation;

/**
 * Created by deepa on 6/24/2017.
 */
public class Toner {
    private double currentLevel;
    private boolean isColored;
    private int numPagesTotal;
    private int numPagesLeft;
    private double numLevelPerPages;

    public Toner(boolean isColored, int numPagesTotal) {
        this.isColored = isColored;
        this.numPagesTotal = numPagesTotal;
        this.numLevelPerPages = 100.0/numPagesTotal;
        this.numPagesLeft =numPagesTotal;
        this.currentLevel=100.0;
    }

    public void decreaseLevel(double numPages){
        //System.out.println(numLevelPerPages);
        this.numPagesLeft-=numPages;
        this.currentLevel-=numPages* numLevelPerPages;

    }
    public void refillToner(){
        this.currentLevel=100.0;
        this.numPagesLeft=this.numPagesTotal;
    }

    public double getCurrentLevel() {
        return currentLevel;
    }

    public boolean isColored() {
        return isColored;
    }

    public int getNumPagesTotal() {
        return numPagesTotal;
    }

    public int getNumPagesLeft() {
        return numPagesLeft;
    }

    public double getNumLevelPerPages() {
        return numLevelPerPages;
    }
}
