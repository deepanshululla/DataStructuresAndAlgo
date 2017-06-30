package com.inheritance;

/**
 * Created by deepa on 6/23/2017.
 */
public class Dog extends Animal{
    // for extending or inheriting it needs to call the constructor of parent class

    private int eyes;
    private int legs;
    private int tail;
    private int teeth;
    private String coat;

    public Dog(String name, double size, double weight, int eyes, int legs, int tail, int teeth, String coat) {
        super(name, 1, 1, size, weight);
        //super class constructor of parent class
        this.eyes=eyes;
        this.legs=legs;
        this.tail=tail;
        this.teeth=teeth;
        this.coat=coat;
    }

    private void chew(){
        System.out.println("Dog.chew() called");
        System.out.println("chew chew.. The food is tasty");
    }

    public void walk(){
        System.out.println("dog.walk() called");
        super.move(5);
        //or..The later is more preffered as if we decide to overload move function later
        move(5);
    }
    public void run(){
        System.out.println("dog.run() called");
        move(10);
    }
    public void moveLegs(){
        System.out.println("Dogs.moveLegs() called");
    }
    @Override
    public void move(int speed){
        System.out.println("Dog.move() called");
        moveLegs();
        super.move(speed);
    }


    @Override
    public void feed() {
        System.out.println("Dog.feed() called");
        System.out.println("So much food..Wow Wow");
        chew();
        super.feed();
    }
}
