package com.classes;

/**
 * Created by deepa on 6/21/2017.
 */
public class VIPCustomer {
    String name;
    double creditLimit;
    String emailAddress;

    @Override
    public String toString() {
        return "VIPCustomer{" +
                "name='" + name + '\'' +
                ", creditLimit=" + creditLimit +
                ", emailAddress='" + emailAddress + '\'' +
                '}';
    }

    public VIPCustomer(String name, String emailAddress) {
        this(name,100_000, emailAddress);
    }

    public VIPCustomer() {
        this("DefaultName",100_000 ,"DefaultEmail");
    }

    public String getName() {
        return name;
    }

    public double getCreditLimit() {
        return creditLimit;
    }

    public String getEmailAddress() {
        return emailAddress;
    }

    public VIPCustomer(String name, double creditLimit, String emailAddress) {

        this.name = name;
        this.creditLimit = creditLimit;
        this.emailAddress = emailAddress;
    }
}
