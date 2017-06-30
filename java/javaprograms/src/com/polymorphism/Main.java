package com.polymorphism;

/**
 * Created by deepa on 6/27/2017.
 */


class Car{
    private int cylinders;
    private String name;
    private boolean engine;
    private int wheels;

    public Car(int cylinders, String name) {
        this.cylinders = cylinders;
        this.name = name;
        this.wheels=4;
        this.engine=true;
    }
    public void startEngine(){
        System.out.println("Car.startEngine() called");
    }
    public void accelerate(){
        System.out.println("Car.accelerate() called");
    }
    public void brake(){
        System.out.println("Car.brake() called");
    }

    public int getCylinders() {
        return cylinders;
    }

    public String getName() {
        return name;
    }

    public boolean isEngine() {
        return engine;
    }

    public int getWheels() {
        return wheels;
    }
}
class Ferrari extends Car{
    public Ferrari() {
        super(4, "Ferrari");
    }

    @Override
    public void startEngine() {
        //super.startEngine();
        System.out.println("Ferrari.startEngine() called");
    }

    @Override
    public void accelerate() {
        System.out.println("Ferrari.accelerate() called");
    }

    @Override
    public void brake() {
        System.out.println("Ferrari.brake() called");
    }
}

class SomeCar extends Car{
    public SomeCar() {
        super(1,"SomeCar");
    }
}

public class Main {
    public static void main(String[] args){
        for(int i=0;i<10;i++){
            Car car=randomCar();
            car.startEngine();
            car.accelerate();
            car.brake();
            System.out.println("\n");
        }


    }
    public static Car randomCar(){
        int randomCar= (int) (Math.random()*2)+1;
        switch (randomCar){
            case 1:
                return new Ferrari();
            case 2:
                return new SomeCar();
            default:
                return null;
        }
    }
}
