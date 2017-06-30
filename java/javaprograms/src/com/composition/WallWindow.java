package com.composition;



/**
 * Created by deepa on 6/24/2017.
 */
public class WallWindow {
    private Dimensions dimension;
    private String color;
    private int numWindows;

    public WallWindow(Dimensions dimension, String color, int numWindows) {
        this.dimension = dimension;
        this.color = color;
        this.numWindows = numWindows;
    }

    public int getNumWindows() {
        return numWindows;
    }

    public Dimensions getDimension() {
        return dimension;
    }

    public String getColor() {
        return color;
    }
}
