package com.composition;

/**
 * Created by deepa on 6/24/2017.
 */
public class Door {
    private Dimensions dimension;
    private String color;
    private int numDoors;

    public int getNumDoors() {
        return numDoors;
    }

    public Door(Dimensions dimension, String color, int numDoors) {

        this.dimension = dimension;
        this.color = color;
        this.numDoors = numDoors;
    }

    public Door(Dimensions dimension, String color) {
        this.dimension = dimension;
        this.color = color;
    }

    public Dimensions getDimension() {
        return dimension;
    }

    public String getColor() {
        return color;
    }
}
