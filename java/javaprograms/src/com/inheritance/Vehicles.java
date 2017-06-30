package com.inheritance;

/**
 * Created by deepa on 6/23/2017.
 */
public class Vehicles {
    private String vehicleType;
    private int numSeats;
    private int currentSpeed;

    public Vehicles(String vehicleType, int numSeats) {
        this.vehicleType = vehicleType;
        this.numSeats = numSeats;
        this.currentSpeed=0;
    }

    public void setNumSeats(int numSeats) {
        this.numSeats = numSeats;
    }

    public int getCurrentSpeed() {
        return currentSpeed;
    }

    public void move(int speed){
        if (speed<0 || speed>1000){
            System.out.println("sorry can't go at this speed");
        }
        else {
            this.currentSpeed = speed;
            System.out.println("Vehicle.speed() called");
            System.out.println("Vehicle is moving at " + speed);
        }
    }
    public void stop(){
        this.currentSpeed=0;
    }
}
