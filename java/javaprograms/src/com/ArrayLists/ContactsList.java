package com.ArrayLists;

import java.util.ArrayList;

/**
 * Created by deepa on 6/28/2017.
 */
public class ContactsList {
    ArrayList<Contact> contactsList = new ArrayList<Contact>();

    public void addContact(Contact c){
        if (contactExists(c)){
            System.out.println("Contact already exists");
        }else{
            contactsList.add(c);
            System.out.println("Contact "+ c +" is  added successfully");
        }
    }

    public void updateContact(Contact oldContact,Contact newContact){
        if(contactExists(newContact)){
            System.out.println("Contact already exists");
        }
        else {
            int position = findIndexOf(oldContact);
            contactsList.set(position,newContact);
        }
    }
    public void removeContact(String name){
        int position = findIndexOf(name);
        if(position>=0){
            contactsList.remove(position);
        }else{
            System.out.println("Contact not found");
        }
    }
    public void removeContact(Contact c){
        int position = findIndexOf(c);
        if(position>=0){
            contactsList.remove(position);
        }else{
            System.out.println("Contact not found");
        }

    }


    public void printContacts(){
        for(int i=0;i< contactsList.size();i++){
            System.out.println(""+contactsList.get(i));
        }
    }


    public boolean contactExists(Contact c){
        int position = findIndexOf(c);
        //System.out.println(position);
        if (position>=0){
            return true;
        }
        return false;
    }
    public Contact getContact(int i){
        if (i>=0){
            return contactsList.get(i);
        }
        return null;
    }

    private int findIndexOf(Contact c){
        int position= contactsList.indexOf(c);

        if (position>=0){
            return position;
        }
        else {
            position=findIndexOf(c.getName());
            if(position>=0){
                return position;
            }
            return -1;
        }
    }
    public int findIndexOf(String name){
        for(int i=0;i<contactsList.size();i++){
            if(contactsList.get(i).getName().equals(name)){
                return i;
            }
        }
        return -1;
    }

}
