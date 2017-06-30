package com.LinkedLists;

/**
 * Created by deepa on 6/29/2017.
 */

class Node{
    private String value;
    private Node nextNode;

    public Node(String value, Node nextNode) {
        this.value = value;
        this.nextNode = nextNode;
    }

    public Node(String value) {
        this.value = value;
        this.nextNode=null;
    }

    public Node() {
        this.value=null;
        this.nextNode=null;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public Node getNextNode() {
        return nextNode;
    }

    public void setNextNode(Node nextNode) {
        this.nextNode = nextNode;
    }
}
public class LinkedListClass {
    private Node headNode;
    private Node currentNode;
    private int listLength;

    public LinkedListClass() {
        this.headNode=new Node();
        this.currentNode=headNode;
        this.listLength=0;
    }

    public void add(Node n){
        if (n==null){
            System.out.println("Null node detected.Can't add this");
            return;
        }
        if (headNode.getValue()==null){
            headNode=n;
            currentNode=headNode;
        }else{
            currentNode.setNextNode(n);
            currentNode=n;
        }
        this.listLength+=1;
    }

    public void add(Integer num){

        if (headNode.getValue()==null){
            headNode.setValue(num.toString());
            currentNode=headNode;
        }
        else {
            currentNode.setNextNode(new Node(num.toString()));
            currentNode = currentNode.getNextNode();
        }
        this.listLength+=1;
    }

    public void add(String num){

        if (headNode.getValue()==null){
            headNode.setValue(num);
            currentNode=headNode;
        }
        else {
            currentNode.setNextNode(new Node(num));
            currentNode = currentNode.getNextNode();
        }
        this.listLength+=1;
    }

    public void add(Double num){

        if (headNode.getValue()==null){
            headNode.setValue(num.toString());
            currentNode=headNode;
        }
        else {
            currentNode.setNextNode(new Node(num.toString()));
            currentNode = currentNode.getNextNode();
        }
        this.listLength+=1;
    }



    public void printList(){
        Node currNode= headNode;
        while(currNode!=null){
            System.out.println(currNode.getValue());
            currNode=currNode.getNextNode();
        }
    }
}
