package com.composition;

/**
 * Created by deepa on 6/23/2017.
 */
public class Dimensions {
    private int width;
    private int height;
    private int depth;

    public Dimensions(int width, int height, int depth) {
        this.width = width;
        this.height = height;
        this.depth = depth;
    }

    public Dimensions(int width, int height) {
        this.width = width;
        this.height = height;
        this.depth=0;
    }
}
