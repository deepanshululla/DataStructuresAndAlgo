package com.ArrayLists;

import java.util.ArrayList;

/**
 * Created by deepa on 6/27/2017.
 */
public class GroceryList{
    private ArrayList<String> groceryList=new ArrayList<String>();
    //arraylist is a class
    public void addGroceryItem(String item){
        groceryList.add(item);
    }
    public void printGroceryList(){
        System.out.println("You have "+ groceryList.size() +" items");
        for(int i=0;i<groceryList.size();i++){
            System.out.println("Item "+ (i+1)+ ": "+ groceryList.get(i));
        }
    }
    public void modifyGroceryItem(String olditem,String newItem){
        int position=getIndex(olditem);
        if(position>=0){
            modifyGroceryItem(position,newItem);
        }
    }

    public ArrayList<String> getGroceryList() {
        return groceryList;
    }

    private void modifyGroceryItem(int position, String newItem){
        groceryList.set(position,newItem);
    }

    public void removeGroceryItem(String item){
        int position=getIndex(item);
        if(position>=0){
            removeGroceryItem(position);
        }
    }

    private void removeGroceryItem(int position){
        String item= groceryList.get(position);
        groceryList.remove(position);
    }
    public boolean itemExists(String item){
        return groceryList.contains(item);
    }
    public int getIndex(String item){

        int position= groceryList.indexOf(item);
        //returns -1 if item doesn't exist
        return position;
    }
    public String findItem(String searchItem) {
//        boolean exists = groceryList.contains(searchItem);

        int position = groceryList.indexOf(searchItem);
        if(position >=0) {
            return groceryList.get(position);
        }

        return null;
    }
    public boolean onFile(String searchItem){
        int position = getIndex(searchItem);
        if(position>=0){
            return true;
        }
        else {
            return false;
        }
    }

}