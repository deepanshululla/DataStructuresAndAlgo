package com.AutoboxingUnboxing;

import java.util.ArrayList;

/**
 * Created by deepa on 6/29/2017.
 */
public class Branches {
    private String branchName;
    private ArrayList<Customer> customerArrayList= new ArrayList<Customer>();

    public Branches(String branchName) {
        this.branchName = branchName.toLowerCase();
    }

    public String getBranchName() {
        return branchName;
    }

    @Override
    public String toString() {
        return this.getBranchName()+this.getCustomerArrayList();
    }

    public Customer getCustomerbyName(String customerName){
        if (findIndexOf(customerName)>=0) {
            return this.getCustomerArrayList().get(findIndexOf(customerName.toLowerCase()));
        }
        return null;
    }


    public ArrayList<Customer> getCustomerArrayList() {
        return this.customerArrayList;
    }

    public void addCustomer(Customer c){
        //System.out.println(ifExists(c));
        if (ifExists(c)){
            System.out.println("We already have a customer with this name"+ c.getCustomerName());

        }else{
            this.customerArrayList.add(c);
            System.out.println("Cusomer "+c+ " is added");
        }

    }

    public void removeCustomer(Customer c){
        if (!(ifExists(c))){
            System.out.println("We don't have a customer with this name");

        }else{
            this.customerArrayList.remove(c);
            System.out.println("Cusomer "+c+ " is removed");
        }

    }

    public int findIndexOf(String customerName){
        for(int i=0;i<this.customerArrayList.size();i++){
            if (this.customerArrayList.get(i).getCustomerName().equals(customerName.toLowerCase())){
                return i;
            }
        }
        return -1;
    }

    public int findIndexOf(Customer c){
        return this.customerArrayList.indexOf(c);
    }

    public boolean ifExists(Customer c){
        int position= findIndexOf(c);
        //System.out.println(position);
        if(position>=0){
            return true;
        }

        int position2=findIndexOf(c.getCustomerName().toLowerCase());
        if (position2>=0){
            return true;
        }
        return false;
    }

}
