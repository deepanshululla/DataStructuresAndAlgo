package com.helloworld2;

public class Main {

    public static void main(String[] args) {
        // essentially any data type with size x ranges from -2^(x-1) to (2^x)-1
        // that is because zero is same in all
        //int has a width of 32 bits
        int maxValue=2147483647;
        // this is 2^31-1 if you see
        int minValue= -2147483648;
        int newIntVal=minValue/2;
        System.out.println("New integer value is " + newIntVal);

        //byte has a width of 8
        byte maxval=127;
        byte minval=-128;
        //byte newByte=minval/2; //is wrong because every time we try to do arithmetic it converts to integer
        byte newByte=(byte)(minval/2); //this is correct We need to do casting
        System.out.println("New byte value is "+ newByte);

        // short has a width of 16
        short maxvalShort=32767;
        short minvalShort=-32768;
        //2^15

        //long has a width of 64 bits
        long maxLongVal=9223372036854775807L;
        long minLongVal=-9223372036854775808l;
        long newLong=minLongVal/2; // this is correct
        System.out.println("new long is " + newLong);

        long newLong2 = 50000 + 10*newByte + newIntVal + minvalShort;
        System.out.println(newLong2);

        // all long types must followed by a capital or small L


    }
}
