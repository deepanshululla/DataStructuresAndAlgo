package com.composition;

/**
 * Created by deepa on 6/23/2017.
 */
public class Monitor {
    private String model;
    private String manufatcturer;
    private int size;
    private Resolution nativeResolution;//Resolution is a part of monitor. A monitor "has" resolution.

    public Monitor(String model, String manufatcturer, int size, Resolution nativeResolution) {
        this.model = model;
        this.manufatcturer = manufatcturer;
        this.size = size;
        this.nativeResolution = nativeResolution;
    }
    public void drawPixelAt(int x,int y, String color){
        System.out.println("Drawing pixel at "+x + ", "+ y +" in color"+ color);
    }

    public String getModel() {
        return model;
    }

    public String getManufatcturer() {
        return manufatcturer;
    }

    public int getSize() {
        return size;
    }

    public Resolution getNativeResolution() {
        return nativeResolution;
    }
}
