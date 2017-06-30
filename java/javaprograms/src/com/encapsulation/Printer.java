package com.encapsulation;

/**
 * Created by deepa on 6/24/2017.
 */
public class Printer {
    private Toner toner;
    private int totalPrinted;
    private int numPagesPrinted;
    private boolean isDuplexPrinter;
    //private double currentlevel;
    public Printer(Toner toner, boolean isDuplexPrinter) {
        this.toner = toner;
        this.numPagesPrinted = 0;
        this.totalPrinted=0;
        this.isDuplexPrinter = isDuplexPrinter;
        //this.currentlevel=toner.getCurrentLevel();
    }

    public void printPage(String contents){
        double currentlevel=toner.getCurrentLevel();
        if (currentlevel>-1 && currentlevel>this.toner.getNumLevelPerPages()){
        System.out.println("Contents of page are \n"+ contents);
        this.toner.decreaseLevel(1);
        if (this.isDuplexPrinter){
            if(this.totalPrinted%2==0){
                this.numPagesPrinted+=1;
                this.totalPrinted+=1;
            }else{
                this.numPagesPrinted+=1;
            }

        }
        else{
            this.numPagesPrinted+=1;
            this.totalPrinted+=1;
        }
        }else{
            System.out.println("Sorry you can't put any more pages. Please refill the toner.");
        }

    }
    public void printNPages(int n){
        double currentlevel=this.toner.getCurrentLevel();
        System.out.println("Printing "+ n +" pages");
        if (currentlevel>=(n-1)*this.toner.getNumLevelPerPages()) {
            this.toner.decreaseLevel(n);
        }else{
            System.out.println("Not enough ink to print pages. Please refill before or decrease amount of pages.");
        }

    }
    public void refillPrinterInk(){
        this.toner.refillToner();
    }

    public Toner getToner() {
        return toner;
    }

    public int getNumPagesPrinted() {
        return numPagesPrinted;
    }

    public boolean isDuplexPrinter() {
        return isDuplexPrinter;
    }
}
