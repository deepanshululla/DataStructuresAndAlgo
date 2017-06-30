package com.LinkedLists;

/**
 * Created by deepa on 6/29/2017.
 */

class Customer{
    private String name;
    private Double currentBalance;

    public Customer(String name, Double currentBalance) {
        this.name = name;
        this.currentBalance = currentBalance;
    }

    public Double getCurrentBalance() {
        return currentBalance;
    }

    public void setCurrentBalance(Double currentBalance) {
        this.currentBalance = currentBalance;
    }
}


public class Main {
    public static void main(String[] args){
       Customer c1 =new Customer("tim", 500.0);
       Customer c2;
       c2=c1;
       c2.setCurrentBalance(100.0);
        System.out.println(" the balance of c1 is "+ c1.getCurrentBalance());
        //changing c2's balance changed c1's balance
        // this is because assignment in java is done by reference.
        //c2 =c1 doesn't create a new object
        //c2 is just referenced to c1

    }

    public void lltest(){
        LinkedListClass ll =new LinkedListClass();
        ll.add(5);
        ll.add(6.5);
        ll.add("hello world");
        ll.printList();
    }



}
