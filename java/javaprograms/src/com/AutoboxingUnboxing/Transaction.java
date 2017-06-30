package com.AutoboxingUnboxing;

/**
 * Created by deepa on 6/29/2017.
 */
public class Transaction {
    private String transactionType;
    private Double amount;

    public Transaction(String transactionType, Double amount) {
        this.transactionType = transactionType;
        this.amount = amount;
    }

    public Double getAmount() {
        return amount;
    }

    @Override
    public String toString() {
        return transactionType+":"+amount.toString();
    }
}
