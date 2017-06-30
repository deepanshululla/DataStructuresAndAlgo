package com.OOPSmasterChallenge;

/**
 * Created by deepa on 6/27/2017.
 */
public class AddOnItem {
    private String name;
    private double price;

    public AddOnItem(String name, double price) {
        this.name = name;
        this.price = price;
    }

    public AddOnItem() {
        this.name=null;
        this.price=0;
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }
}
