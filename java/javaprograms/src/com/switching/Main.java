package com.switching;

/**
 * Created by deepa on 6/20/2017.
 */
public class Main {
    public static void main(String[] args){
        int value=1;
        int switchValue=9;
        //break is very important in switch statements.
        //it tells to exit the switch statements
        /*switch (switchValue){
            case 1: {
                //is equivalent to if swicthValue==1
                System.out.println("switch value=" + switchValue);
                break;
            }
            case 2:{
                System.out.println("switch avlue=" + switchValue);
                break;
            }
            case 3:case 4:case 5:{
                System.out.println("switch avlue=" + switchValue);
                break;
            }
            default:{
                //more like else the case which is not covered
                System.out.println("It is not 1,2,3,4 or 5");
                break;// this break is not necessary
            }
        }*/
        String month="January";
        switch(month.toLowerCase()){
            case "january":
                System.out.println(month);
                break;
            case "february":
                System.out.println(month);
                break;
            case "march":case "april":case "may":case "june":case "july":
                System.out.println(month);
                break;
            case "august":case "september":case "October":case "Novermber":case "December":
                System.out.println(month);
                break;
            default:
                System.out.println("Unknown");
        }

    }
}
