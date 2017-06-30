package com.inheritance;

/**
 * Created by deepa on 6/23/2017.
 */
public class Ferrari extends Cars {
    private String model;
    private String color;

    public Ferrari(String model, String color) {
        super(2,"Ferrari", 6, 1);
        this.model = model;
        this.color = color;
    }
    @Override
    public void move(int speed){
        super.move(speed);

    }


}
