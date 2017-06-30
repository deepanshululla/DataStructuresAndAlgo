package com.inheritance;


/**
 * Created by deepa on 6/23/2017.
 */
public class Main {
    public static void main(String[] args){
        vehicleFunction();
        //animalFunction();
    }
    public static void animalFunction(){
        Animal animal =new Animal("Animal", 1,1,5,50);

        //Dog dog= new Dog("Browny",2,30,2,4,1,20,"silky");

        //dog.feed();//feed function was defined in animal class. Since feed was public dog inherited the function
        //dog.walk();
        //dog.run();
        Fish fish= new Fish("fishy",1,1,1,4,1,2,4);
        fish.swim(5);
    }

    public static void vehicleFunction(){
        Ferrari ferrari= new Ferrari("Ferrari 458 Italia ","red");
        ferrari.move(100);
        ferrari.move(200);
        ferrari.move(150);
        ferrari.move(100);
        ferrari.move(50);
        ferrari.move(25);
        ferrari.stop();



    }
}
