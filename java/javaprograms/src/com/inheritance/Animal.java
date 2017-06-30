package com.inheritance;

/**
 * Created by deepa on 6/23/2017.
 */
public class Animal {
    private String name;
    private int brain;
    private int body;
    private double size;
    private double weight;

    public Animal(String name, int brain, int body, double size, double weight) {
        this.name = name;
        this.brain = brain;
        this.body = body;
        this.size = size;
        this.weight = weight;
    }

    public void eat(){
        System.out.println("animal.eat() called");
    }

    public void feed(){
        System.out.println("Animal.feed() called");
        System.out.println("Thanks for feeding me");
    }

    public void move(int speed){
        System.out.println("Animal is moving at "+speed);
    }
    public String getName() {
        return name;
    }

    public int getBrain() {
        return brain;
    }

    public int getBody() {
        return body;
    }

    public double getSize() {
        return size;
    }

    public double getWeight() {
        return weight;
    }
}
