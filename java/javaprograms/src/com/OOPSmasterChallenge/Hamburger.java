package com.OOPSmasterChallenge;

/**
 * Created by deepa on 6/27/2017.
 */

class PopularHamburger1 extends Hamburger{
    public PopularHamburger1() {
        super("BreadWhite", "Crispy Chicken", 4);
    }
}
class PopularHamburger2 extends Hamburger{
    public PopularHamburger2() {
        super("Wheat Bread", "Soya",4.5 );
    }
}

public class Hamburger {
    private String rollType;
    private String meatType;
    private double basePrice;

    public Hamburger(String rollType, String meatType, double basePrice) {
        this.rollType = rollType;
        this.meatType = meatType;
        this.basePrice = basePrice;
    }

    public double itemizeBurger(AddOnItem item1, AddOnItem item2, AddOnItem item3, AddOnItem item4){
        double totalCost=this.basePrice;
        if (item1.getName()!=null){
            totalCost+=item1.getPrice();
        }
        if (item2.getName()!=null){
            totalCost+=item2.getPrice();
        }
        if (item3.getName()!=null){
            totalCost+=item3.getPrice();
        }
        if (item4.getName()!=null){
            totalCost+=item4.getPrice();
        }
        return totalCost;
    }

    public double itemizeBurger(AddOnItem item1, AddOnItem item2, AddOnItem item3){
        double totalCost=this.basePrice;
        if (item1.getName()!=null){
            totalCost+=item1.getPrice();
        }
        if (item2.getName()!=null){
            totalCost+=item2.getPrice();
        }
        if (item3.getName()!=null){
            totalCost+=item3.getPrice();
        }

        return totalCost;
    }
    public double itemizeBurger(AddOnItem item1, AddOnItem item2){
        double totalCost=this.basePrice;
        if (item1.getName()!=null){
            totalCost+=item1.getPrice();
        }
        if (item2.getName()!=null){
            totalCost+=item2.getPrice();
        }

        return totalCost;
    }
    public double itemizeBurger(AddOnItem item1){
        double totalCost=this.basePrice;
        if (item1.getName()!=null){
            totalCost+=item1.getPrice();
        }

        return totalCost;
    }
    public double itemizeBurger(){


        return this.basePrice;
    }

}
