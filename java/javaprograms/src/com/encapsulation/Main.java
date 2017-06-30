package com.encapsulation;

/**
 * Created by deepa on 6/24/2017.
 */
  public class Main {
    public static void main(String[] args){
        //playerMethodWithoutEncaps();
        //playerMothodEncaps();
        printerClassMethod();

    }
    public static void printerClassMethod(){
        Toner toner = new Toner(false,500);
        Printer printer =new Printer(toner,true);
        printer.printPage("New page1");
        System.out.println("Pages left are "+printer.getToner().getNumPagesLeft());
        System.out.println("Toner level left is "+printer.getToner().getCurrentLevel());
        printer.printNPages(100);
        System.out.println("Pages left are "+printer.getToner().getNumPagesLeft());
        System.out.println("Toner level left is "+printer.getToner().getCurrentLevel());
        printer.printNPages(500);
        System.out.println("Pages left are "+printer.getToner().getNumPagesLeft());
        System.out.println("Toner level left is "+printer.getToner().getCurrentLevel());
        printer.printNPages(399);
        System.out.println("Pages left are "+printer.getToner().getNumPagesLeft());
        System.out.println("Toner level left is "+printer.getToner().getCurrentLevel());
        printer.refillPrinterInk();
        printer.printPage("New page1");
        System.out.println("Pages left are "+printer.getToner().getNumPagesLeft());
        System.out.println("Toner level left is "+printer.getToner().getCurrentLevel());
        printer.printNPages(100);
        System.out.println("Pages left are "+printer.getToner().getNumPagesLeft());
        System.out.println("Toner level left is "+printer.getToner().getCurrentLevel());


    }
    public static void playerMothodEncaps(){
        EnhancedPlayer player=new EnhancedPlayer("Tim", 50, "sword");
        System.out.println("Remaining health ="+ player.getHealth());
        int damage=10;
        player.loseHealth(damage);
        System.out.println("Remaining health = "+ player.getHealth());

    }
    public static void playerMethodWithoutEncaps(){
        Player player =new Player();
        player.name="WreakHavoC";
        player.health=20;
        player.weapon="FireSword";

        int damage=10;
        player.loseHealth(damage);
        System.out.println("Remaining health = "+ player.healthRemaining());


    }


}
