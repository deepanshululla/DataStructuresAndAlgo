package com.classes;

/**
 * Created by deepa on 6/21/2017.
 */
public class BankAccount {
    private String accountNumber;
    private String customerName;
    private String email;
    private long phoneNumber;
    private double balance;

    public String getCustomerName() {
        return customerName;
    }

    public BankAccount() {
        this("56789","default name","default email", 0000000,0 );
        System.out.println("empty constructor");
    }

    public BankAccount(String accountNumber, String customerName, double balance) {
        this(accountNumber,customerName,"Default email",0000000,balance);
//        this.accountNumber = accountNumber;
//        this.customerName = customerName;
//        this.balance = balance;
    }

    public BankAccount(String accountNumber, String customerName, String email, long phoneNumber) {
          this(accountNumber,customerName,email,phoneNumber,0);
//        this.accountNumber = accountNumber;
//        this.customerName = customerName;
//        this.email = email;
//        this.phoneNumber = phoneNumber;
    }

    public BankAccount(String accountNumber, String customerName, String email, long phoneNumber, double balance) {
        //notice Constructor doesn't have any return type
        this.accountNumber = accountNumber;
        this.customerName = customerName;
        this.email = email;
        this.phoneNumber = phoneNumber;
        this.balance = balance;

    }

    public void setCustomerName(String customerName) {
        this.customerName = customerName;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public long getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(long phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public void setAccountNumber(String accountNumber){
        this.accountNumber=accountNumber;
    }
    public String getAccountNumber(){
        return this.accountNumber;
    }
    public void setBalance(double newBalance){
        this.balance=newBalance;
    }
    public double getBalance(){
        return this.balance;
    }
    public void depositMoney(double amountDeposited){
        if (amountDeposited>0)
            this.balance+=amountDeposited;
        else{
            System.out.println("Please enter valid amount");
        }
    }
    public void withdrawMoney(double amountWithdrawn){
        if (amountWithdrawn>0 && amountWithdrawn<this.balance)
            this.balance-=amountWithdrawn;
        else{
            System.out.println("Please enter valid amount");
        }
    }


}
