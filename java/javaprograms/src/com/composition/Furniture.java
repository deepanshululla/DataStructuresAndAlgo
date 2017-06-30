package com.composition;

/**
 * Created by deepa on 6/24/2017.
 */
public class Furniture {
    private int numPieces;
    private String furnitureType;
    private boolean isFurnished;

    public Furniture(int numPieces, String furnitureType, boolean isFurnished) {

        this.numPieces = numPieces;
        this.furnitureType = furnitureType;
        this.isFurnished = isFurnished;
    }

    public int getNumPieces() {
        return numPieces;
    }

    public String getFurnitureType() {
        return furnitureType;
    }
    public boolean isFurnished() {
        return isFurnished;
    }
}
