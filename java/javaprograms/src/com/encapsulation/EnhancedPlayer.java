package com.encapsulation;

/**
 * Created by deepa on 6/24/2017.
 */
public class EnhancedPlayer {
    private String name;
    private int hitPoints;
    private String weapon;

    public EnhancedPlayer(String name, int hitPoints, String weapon) {
        this.name = name;
        if (hitPoints >0 || hitPoints >200)
        {
            this.hitPoints = hitPoints;
        }
        this.weapon = weapon;
    }

    public void loseHealth(int damage){
        this.hitPoints -=damage;
        if (this.hitPoints <=0){
            System.out.println("player knocked out");
        }
    }

    public int getHealth() {
        return hitPoints;
    }
}
