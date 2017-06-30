package com.inheritance;

/**
 * Created by deepa on 6/23/2017.
 */
public class Cars extends Vehicles {
    private String carType;
    private int numGears;
    private int steering;
    //private int startGear;
    private int currentGear;


    public Cars(int numSeats, String carType, int numGears, int steering) {
        super("Cars", 4);
        this.carType = carType;
        this.numGears = numGears;
        this.steering = steering;
        this.currentGear=0;
    }
    public void changeGear(int gearNum){
        if (gearNum>this.numGears || gearNum<0){
            System.out.println("Sorry you can't change any more gears. You can still move at higher/lower speeds though");
        }
        else {
            System.out.println("Gear changed to " + gearNum);
            this.currentGear = gearNum;
        }
    }

    @Override
    public void move(int speed) {
        System.out.println("Cars.move() called");

        if (speed>getCurrentSpeed()) {
            changeGear(this.currentGear + 1);
        }
        else if(speed==getCurrentSpeed()){
            System.out.println("No cnage in gear");
        }
        else{
            changeGear(this.currentGear - 1);
        }
        super.move(speed);
    }

    @Override
    public void stop() {
        this.changeGear(0);
        super.stop();
    }
}
