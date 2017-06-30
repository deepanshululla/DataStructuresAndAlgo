package com.LinkedLists;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.Scanner;

/**
 * Created by deepa on 6/29/2017.
 */
public class Demo {
    public static void main(String[] args) {
        //iteratorMethod();
        listIteratorMethod();

    }

    private static void printList(LinkedList<String> linkedList){
        Iterator<String> i=linkedList.iterator();
        while(i.hasNext()){
            System.out.println("Now visiting "+i.next());
        }
        System.out.println("========================");

    }
    private static void iteratorMethod(){
        LinkedList<String> placesToVisit= new LinkedList<String>();
        placesToVisit.add("Sydney");
        placesToVisit.add("Melbourne");
        placesToVisit.add("Brisbane");
        placesToVisit.add("Perth");
        placesToVisit.add("Adelaide");

        printList(placesToVisit);
        placesToVisit.add(1,"Alice Springs");// insert Alice sprigs between Sydney and Melbourne
        printList(placesToVisit);
        placesToVisit.remove(4);//removes perth
        printList(placesToVisit);
    }
    private static void listIteratorMethod(){
        LinkedList<String> placesToVisit= new LinkedList<String>();
        addInOrder(placesToVisit,"Sydney");
        addInOrder(placesToVisit,"melbourne");
        addInOrder(placesToVisit,"london");
        addInOrder(placesToVisit,"mumbai");
        addInOrder(placesToVisit,"melbourne");
        printList(placesToVisit);
        visit(placesToVisit);

    }

    private static boolean addInOrder(LinkedList<String> linkedList,String newCity){
        //trying to add items in alphabetical order
        ListIterator<String> stringListIterator= linkedList.listIterator();
        // the difference between listiterator and iterator is
        // 1) listiterator allows us to go back to previous value unlike the iterator
        // 2) An iterator points to the first item while a listiterator.next() will point to the first value in linkedlist

        while(stringListIterator.hasNext()){
            int comparison = stringListIterator.next().compareTo(newCity);
            // if 0 we have the same city already there,
            //if >0 then newcity must come before the item and insertion has to be made
            if (comparison==0){
                //equal do not add this city as it already there
                System.out.println("City "+ newCity+" is already added");
                return false;
            }else if(comparison>0){
                //we need to insert newCity here
                //Brisbane-> Adelaide
                stringListIterator.previous();
                stringListIterator.add(newCity.toLowerCase());
                return true;

            } else if(comparison<0){
                //move on to next city
                //continue;
            }
        }
        // we traversed the whole list. we could not find a position for it,so we are addiing it to very end
        stringListIterator.add(newCity.toLowerCase());
        return true;
    }

    private static void visit(LinkedList<String> cities){
        Scanner scanner = new Scanner(System.in);
        boolean quit = false;
        // Java implemented double liked list but doing this caused a problem
        // the problem is java has implemented only netx and previous function
        // and not for the current one
        // so if  iterator. next ="mumbai" then after this iterator.previous="mumbai"
        // whereas it should have been the next value is mumbai but the previous value is melbourne
        //For correcting this we keep track of linked list direction
        boolean goingForward=true;
        ListIterator<String> stringListIterator =cities.listIterator();
        if(cities.isEmpty()){
            System.out.println("No cities in this list");
        } else{
            System.out.println(" now visiting "+ stringListIterator.next());
            printMenu();
        }
        while(!quit){
            int action = scanner.nextInt();
            scanner.nextLine();
            switch (action){
                case 0:
                    System.out.println("Holiday vacation over");
                    quit=true;
                    break;
                case 1:
                    if(!goingForward){
                        //if some one called to move backward last time
                        // we can set the current value to be next of it
                        if(stringListIterator.hasNext()){
                            stringListIterator.next();
                        }
                        goingForward=true;
                    }
                    if (stringListIterator.hasNext()){
                        System.out.println("Now visiting "+ stringListIterator.next());
                    }else{
                        System.out.println("Reached end of list");
                        goingForward=false;
                    }
                    break;
                case 2:
                    if(goingForward){
                        if(stringListIterator.hasPrevious()){
                            stringListIterator.previous();
                        }
                        goingForward=false;
                    }
                    if (stringListIterator.hasPrevious()){
                        System.out.println("Now visiting "+ stringListIterator.previous());
                    }else{
                        System.out.println("Reached starting of list");
                        goingForward=true;
                    }
                    break;
                case 3:
                    printMenu();
                    break;



            }


        }

    }
    private static void printMenu(){
        System.out.println("Available actions.\n Press");
        System.out.println("0 - to quit\n"+
        "1 to goto next city \n"+
        "2 to goto previous menu \n"+
        "3 to goto menu option");
    }
}
