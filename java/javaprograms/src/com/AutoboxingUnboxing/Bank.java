package com.AutoboxingUnboxing;

import java.util.ArrayList;

/**
 * Created by deepa on 6/29/2017.
 */
public class Bank {
    private String bankName;
    private ArrayList<Branches> branchesArrayList=new ArrayList<Branches>();

    public Bank(String bankName) {
        this.bankName = bankName.toLowerCase();
    }

    public String getBankName() {
        return this.bankName.toLowerCase();
    }


    @Override
    public String toString() {
        return String.format("%s%s", this.getBankName(), this.getBranchesArrayList().toString());
    }
    public Branches getBranchByName(String branchName){
        if (findIndexOf(branchName)>=0){
        return this.getBranchesArrayList().get(this.findIndexOf(branchName.toLowerCase()));
    }
    return null;
    }

    public ArrayList<Branches> getBranchesArrayList() {
        return branchesArrayList;
    }

    public void addBranch(Branches b){
        if (ifExists(b)){
            System.out.println(" We already have a branch with this name");
        }
        else {
            branchesArrayList.add(b);
        }
    }
    public void removeBranch(Branches b){
        if (!(ifExists(b))){
            System.out.println(" We don't have a branch with this name");
        }
        else {
            branchesArrayList.remove(b);
        }
    }

    public int findIndexOf(String branchName){
        for(int i=0;i<branchesArrayList.size();i++){
            if (branchesArrayList.get(i).getBranchName().equals(branchName.toLowerCase())){
                return i;
            }
        }
        return -1;
    }

    public int findIndexOf(Branches b){
        return this.branchesArrayList.indexOf(b);
    }

    public boolean ifExists(Branches b){
        int position= findIndexOf(b);
        String branchName= b.getBranchName().toLowerCase();
        if (position>=0){
            return true;
        }
        else {
            position=findIndexOf(branchName);
            if(position>=0){
                return true;
            }
            else {
                return false;
            }
        }
    }
}
