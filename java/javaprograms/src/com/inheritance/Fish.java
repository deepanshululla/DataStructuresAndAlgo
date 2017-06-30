package com.inheritance;

/**
 * Created by deepa on 6/23/2017.
 */
public class Fish extends Animal {
    private int gills;
    private int eyes;
    private int fins;

    public Fish(String name, int brain, int body, double size, double weight, int gills, int eyes, int fins) {
        super(name, 1, 1, size, weight);
        this.gills = gills;
        this.eyes = eyes;
        this.fins = fins;
    }

    private void rest(){

    }

    private void moveMuscles(){

    }

    private void moveBackFin(){

    }

    public void swim(int speed){
        moveMuscles();
        moveBackFin();
        super.move(speed);


    }

}
