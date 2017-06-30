package com.composition;

/**
 * Created by deepa on 6/23/2017.
 */
public class Main {
    public static void main(String[] args){
        houseMethod();

    }
    public static void houseMethod(){
        Dimensions windowDimension= new Dimensions(5,8);
        Dimensions doorDimensions= new Dimensions(10,20);

        Door door=new Door(doorDimensions,"yellow",6);
        WallWindow window= new WallWindow(windowDimension,"white",10);
        Furniture furniture=new Furniture(40,"wooden",true);

        House house= new House(4,3,furniture,door,window);
        System.out.println("the no. of doors in the house are "+ house.getDoor().getNumDoors());


    }
    public static void PCmethod(){
        Dimensions dimensions=new Dimensions(20,20,5);
        Case theCase= new Case("220B","Apple","240",dimensions);

        Monitor theMonitor=new Monitor("MAC","Apple", 27, new Resolution(2540,1440));
        //we created a new Resolution object without name it.

        Motherboard motherboard=new Motherboard("Mac","Apple",2,2,"Unix");
        PC thePC = new PC(theCase,theMonitor,motherboard);
        thePC.powerUp();
        //thePC.getMonitor().drawPixelAt(200,200,"red");
        //thePC.getMotherboard().loadProgram("MacOS");
        //thePC.getTheCase().pressPowerButton();
    }

}
