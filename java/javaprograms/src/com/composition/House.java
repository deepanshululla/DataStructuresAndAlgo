package com.composition;

/**
 * Created by deepa on 6/24/2017.
 */
public class House {
    private int numBedRooms;
    private int numBathrooms;
    private Furniture furniture;
    private Door door;
    private WallWindow window;


    public House(int numBedRooms, int numBathrooms, Furniture furniture, Door door, WallWindow window) {
        this.numBedRooms = numBedRooms;
        this.numBathrooms = numBathrooms;
        this.furniture = furniture;
        this.door = door;
        this.window = window;
    }

    public void changeNumBedRooms(int newNum){
        this.numBedRooms=newNum;
    }
    public void changeNumBathRooms(int newNum){
        this.numBathrooms=newNum;
    }

    public Furniture getFurniture() {
        return furniture;
    }

    public Door getDoor() {
        return door;
    }

    public WallWindow getWindow() {
        return window;
    }


    public int getNumBathrooms() {
        return numBathrooms;
    }

    public int getNumBedRooms() {
        return numBedRooms;
    }
}
