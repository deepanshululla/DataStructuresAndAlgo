/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package sortingalgorithmsPackage;

import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author deepa
 */
public class SortingAlgorithmsClassTest {
    
    public SortingAlgorithmsClassTest() {
    }
    
    @BeforeClass
    public static void setUpClass() {
    }
    
    @AfterClass
    public static void tearDownClass() {
    }

    /**
     * Test of main method, of class SortingAlgorithmsClass.
     */
    @Test
    public void testMain() {
        System.out.println("main");
        String[] args = null;
        SortingAlgorithmsClass.main(args);
        //testBubbleSort();
        //testCountingSort();
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }
     @Test
    public void testBubbleSort(){
        System.out.println("Bubble sort");
        Integer[] arr={4,5,5,1,3,1,6,6,7,7,7,4,3,2};
        arr = BubbleSort.sort(arr);
        Integer[] sortedArr={1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7};
        assertArrayEquals("Mathing with sorted array",arr,sortedArr);
        
    }
    @Test
    public void testCountingSort(){
        System.out.println("Count sort");
        int[] arr={4,5,5,1,3,1,6,6,7,7,7,4,3,2};
        arr = CountingSort.sort(arr);
        int[] sortedArr={1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7};
        assertArrayEquals("Mathing with sorted array",arr,sortedArr);
        
    }
   
    @Test
    public void testMergeSort(){
        System.out.println("merge sort");
        int[] arr={4,5,5,1,3,1,6,6,7,7,7,4,3,2};
        MergeSort m=new MergeSort();
        m.sort(arr);
        int[] sortedArr={1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7};
        assertArrayEquals("Mathing with sorted array",arr,sortedArr);
        
    }
    @Test
    public void testQuickSort(){
        System.out.println("Quick sort");
        int[] arr={4,5,5,1,3,1,6,6,7,7,7,4,3,2};
        QuickSort m=new QuickSort();
        m.sort(arr);
        int[] sortedArr={1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 7};
        assertArrayEquals("Mathing with sorted array",arr,sortedArr);
        
    }
}
