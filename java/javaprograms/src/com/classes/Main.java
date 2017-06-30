package com.classes;

/**
 * Created by deepa on 6/21/2017.
 */
public class Main {
    public static void main(String[] args){
        //BankAccount ba1= new BankAccount("573843784378","bob",1000);
//        BankAccount ba1= new BankAccount();
//        System.out.println("Current balance is "+ ba1.getBalance());
//        ba1.depositMoney(200);
//        System.out.println("Current balance is "+ ba1.getBalance());
//        ba1.depositMoney(-26);
//        System.out.println("Current balance is "+ ba1.getBalance());
//        ba1.withdrawMoney(500);
//        System.out.println("Current balance is "+ ba1.getBalance());
//        ba1.withdrawMoney(900);
//        System.out.println("Current balance is "+ ba1.getBalance());
//        BankAccount ba2= new BankAccount();
        VIPCustomer cust1= new VIPCustomer("Bob","bob@email.com");
        System.out.println("Customer details are "+ cust1.toString());
    }
}
