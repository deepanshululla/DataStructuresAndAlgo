package com.forLoops;

/**
 * Created by deepa on 6/20/2017.
 */
public class Main {
    public static void main(String[] args){
        double amount =10000;
        double interestRate=2;
        int primeNumCount=0;
        /*for (interestRate=0;interestRate<9;interestRate++){
            System.out.println("Intertest with interest rate "+interestRate+"% is =" +
                    ""+String.format("%.2f",calculateInterest(amount,interestRate)));
        }*/
        System.out.println("**************");
        for(int i=13;i>=2;i--){
            if (isPrime(i)){
                primeNumCount+=1;
                System.out.println(i);
            }
            if(primeNumCount>=3){
                break;
            }
        }
    }

    public static double calculateInterest(double amount, double interestRate){
        return (amount*(interestRate/100));
    }

    public static boolean isPrime(int num){
        if (num==1){
            return false;
        }
        //for(int i=2;i<num;i++){ This is not efficient enough
        // more optimized could be num/2
        // way mroe could be square root
        for(int i=2;i<=(long)Math.sqrt(num);i++){
                if (num%i==0){
                    return false;
                }
            }
        return true;
    }
}
