package com.encapsulation;

/**
 * Created by deepa on 6/24/2017.
 */
public class Player {
    public String name;
    public int health;
    public String weapon;

    public void loseHealth(int damage){
        this.health-=damage;
        if (this.health<=0){
            System.out.println("player knocked out");
        }
    }

    public int healthRemaining(){
        return this.health;
    }
}
