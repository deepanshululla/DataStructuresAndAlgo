package com.AutoboxingUnboxing;

import java.util.ArrayList;

/**
 * Created by deepa on 6/29/2017.
 */
public class Customer {
    private String customerName;
    private Double currentBalance;
    private ArrayList<Transaction> transactionsList = new ArrayList<Transaction>();


    public Customer(String customerName, Double currentBalance) {
        this.customerName = customerName.toLowerCase();
        this.currentBalance = currentBalance;
    }

    @Override
    public String toString() {
        return "customerName: "+ this.getCustomerName() +"\t current balance:"+ this.getCurrentBalance();
    }

    public void depositMoney(Double amount){
        if (amount>0){
            this.currentBalance+=amount;
            this.transactionsList.add(new Transaction("Deposit",amount));
        }
        else{
            System.out.println("Invalid amount");
        }
    }
    public void withdrawMoney(Double amount){
        if (amount>0 && amount<=this.currentBalance){
            this.currentBalance-=amount;
            this.transactionsList.add(new Transaction("Withdraw",amount));
        }
        else{
            System.out.println("Invalid amount");
        }
    }
    public Double checkBalance(){
        Transaction t1 = new Transaction("Checkedbalance",this.currentBalance);
        this.transactionsList.add(t1);
        System.out.println(t1);
        return this.currentBalance;
    }
    public ArrayList<Transaction> getTransactionsList(){
        return this.transactionsList;
    }

    public String getCustomerName() {
        return customerName.toLowerCase();
    }

    public Double getCurrentBalance() {
        return currentBalance;
    }
}
