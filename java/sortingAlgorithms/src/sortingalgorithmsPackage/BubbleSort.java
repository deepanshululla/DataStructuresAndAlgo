/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sortingalgorithmsPackage;

import java.util.Arrays;

/**
 *
 * @author deepa
 * @param <T>
 */
public class BubbleSort <T extends Comparable<T>>  {
    public static <T extends Comparable<T>> T[] sort(T[] input) {
        //inplace verion of bubble sort
        System.out.println("before sorting "+Arrays.toString(input));
        for(int i=0;i<input.length;i++){
            for(int j=i;j<input.length;j++){
                if (input[i].compareTo(input[j])>0){
                   T temp=input[i];
                   input[i]=input[j];
                   input[j]=temp;

                }

            }
        }
        System.out.println("before sorting "+Arrays.toString(input));
        return input;
        
    }
}
