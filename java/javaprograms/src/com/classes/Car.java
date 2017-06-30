package com.classes;

public class Car {
    //class name Car should be in capital
    private int doors; //member variable
    //member variables or fields are state components of car
    //they represent how the car is
    //these are usaully marked as private so MV can't be accessed out side the class.
    private int wheels;
    private String model;
    private String engine;
    private String color;
    //we are creating methods to access private variables outside of our classe
    public void setModel(String modelName){
        String validModel = modelName.toLowerCase();
        if(validModel.equals("carrera") || validModel.equals("commodore")){
            this.model = modelName;
        }
        else{
            this.model="Unknown";
        }
    }
    public String getModel(){
        return this.model;
    }

}
