package com.composition;

/**
 * Created by deepa on 6/23/2017.
 */
public class PC {
    private Case theCase;//case is a reserverd keyword
    private Monitor monitor;
    private Motherboard motherboard;
    //PC has the above 3 CLasses in each instance we create

    public PC(Case theCase, Monitor monitor, Motherboard motherboard) {
        this.theCase = theCase;
        this.monitor = monitor;
        this.motherboard = motherboard;
    }

    public void powerUp(){
        getTheCase().pressPowerButton();
        drawLogo();
    }
    public void drawLogo(){
        //draw some fancy logo
        getMonitor().drawPixelAt(1200,500,"Blue");
    }

    private Case getTheCase() {
        return theCase;
    }

    private Monitor getMonitor() {
        return monitor;
    }

    private Motherboard getMotherboard() {
        return motherboard;
    }
}
