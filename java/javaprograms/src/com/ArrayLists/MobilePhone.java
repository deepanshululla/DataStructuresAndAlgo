package com.ArrayLists;


/**
 * Created by deepa on 6/28/2017.
 */
public class MobilePhone {
    private static ContactsList contactsList = new ContactsList();


    public void addContactPhone(String name,String number){
        Contact c= new Contact(name,number);
        contactsList.addContact(c);
    }
    public void addContact(Contact c){
        contactsList.addContact(c);
    }
    public void removeContact(Contact c){
        contactsList.removeContact(c);
    }
    public void removeContact(String name){
        contactsList.removeContact(name);
    }
    public void updateContact(Contact oldContact, Contact newContact){
        contactsList.updateContact(oldContact,newContact);
    }
    public Contact getContactByName(String name){
        int position = contactsList.findIndexOf(name);
        if(position>=0){
            return contactsList.getContact(position);
        }
        else{
            return  null;
        }
    }
    public void printContacts(){
        contactsList.printContacts();
    }



}
