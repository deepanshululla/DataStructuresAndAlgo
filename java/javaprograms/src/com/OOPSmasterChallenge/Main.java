package com.OOPSmasterChallenge;

/**
 * Created by deepa on 6/27/2017.
 */
public class Main {
    public static void main(String[] args){
        AddOnItem tomato = new AddOnItem("tomato", 1.0);
        AddOnItem lettuce = new AddOnItem("lettuce",2.0);
        AddOnItem carrot =new AddOnItem("carrot",1);
        AddOnItem mayonaise= new AddOnItem("mayo",0.5);
        AddOnItem spinach = new AddOnItem("spinach",1);
        AddOnItem none=new AddOnItem();

        Hamburger hm =new Hamburger("bread","chicken",5);
        System.out.println("The total cost is "+ hm.itemizeBurger(tomato,carrot,mayonaise,spinach));
        System.out.println("The total cost is "+ hm.itemizeBurger(tomato,carrot));
        PopularHamburger1 hm2=new PopularHamburger1();
        System.out.println("The total cost is "+ hm2.itemizeBurger(tomato,carrot,mayonaise,spinach));
        System.out.println("The total cost is "+ hm2.itemizeBurger(tomato,carrot));

    }
}
