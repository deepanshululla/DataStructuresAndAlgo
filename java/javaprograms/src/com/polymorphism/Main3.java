package com.polymorphism;

/**
 * Created by deepa on 6/27/2017.
 */

class Movie{
    private String name;

    public Movie(String name){
        this.name=name;
    }
    public String plot(){
        return "No Plot here";
    }

    public String getName() {
        return name;
    }
}

class Jaws extends Movie{
    public Jaws() {
        super("Jaws");
    }
    @Override
    public String plot(){
        return "A shark eats lots of people";
    }
}
class IndependenceDay extends Movie{
    public IndependenceDay() {
        super("Independence Day");
    }

    @Override
    public String plot() {
        return "Aliens attempt to take over the planet earth";
    }
}

class MazeRunner extends Movie{
    public MazeRunner() {
        super("MazeRunner");
    }

    @Override
    public String plot() {
        return "Kids try and escape a maze";
    }
}

class StarWars extends Movie{
    public StarWars() {
        super("Starwars");
    }

    @Override
    public String plot() {
        return "Imperial forces try to take over the Universe";
    }
}

class Forgettable extends Movie{
    public Forgettable() {
        super("Forgettable");
    }
    //no plot method
}
public class Main3 {
    public static void main(String[] args){
        for(int i=1;i<11;i++){
            Movie movie=randomMovie();
            System.out.println("Movie # "+ i+
                    ": "+ movie.getName()+ "\n" +
                    "Plot: " + movie.plot() +"\n");
        }

    }
    public static Movie randomMovie(){
        //returns a random movie
        int randomNumber=(int) (Math.random()*5) +1;
        //math.random generates a random number between 0.0 and 1.0
        System.out.println("Random Number generated is "+ randomNumber);
        switch (randomNumber){
            case 1:
                return new Jaws();
            case 2:
                return new IndependenceDay();
            case 3:
                return new MazeRunner();
            case 4:
                return new StarWars();
            case 5:
                return new Forgettable();
        }
        return null;
    }
}
