package com.AutoboxingUnboxing;

/**
 * Created by deepa on 6/29/2017.
 */
public class Challenge {
    public static void main(String[] args){
        Customer c1 = new Customer("Tom",Double.valueOf(100.0));
        Customer c2 = new Customer("tom",Double.valueOf(100.0));
        //autoboxing
        Branches b1 = new Branches("Boston Branch");
        Bank bank1= new Bank("SBI");
        b1.addCustomer(c1);
        b1.addCustomer(c1);
        b1.addCustomer(c2);
        bank1.addBranch(b1);
        c1.depositMoney(200.0);
        //bank1.getBranchesArrayList().get(0).getCustomerArrayList().get(0).checkBalance();
        System.out.println(bank1.getBranchesArrayList());
        //System.out.println(bank1.getBranchByName("Boston common branch").getCustomerbyName("jim"));
        Branches b3 =bank1.getBranchByName("Boston Branch");
        if(b3!=null){
            Customer c3=b3.getCustomerbyName("tom");
            if(c3!=null){
                System.out.println(c3);
            }
        }



    }
}
