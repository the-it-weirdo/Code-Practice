/**
 * Challenge:
 * There was a teacher in a small town who loves coding and
 * he wants to create a program which prints out the whole
 * multiplication table of an entered number for his students.
 * Write a program to help him do this.
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


class Day1 {

    public static void main(String[] args) {
    
        Day1 program = new Day1();
        Integer number = program.getInput();
        if (number != null) {
            program.printMultiplicationTable(number);
        }
    }

    private Integer getInput() {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        Integer number = null;
        try {
            System.out.print("Please enter a number for table: ");
            number = Integer.parseInt(reader.readLine());
            reader.close();
        } catch(IOException e) {
            System.out.println("Unexpected IO exception");
        } catch(Exception e) {
            System.out.println("Please enter a valid integer.");
        }
        return number;
    }

    private void printMultiplicationTable(int number) {
        for(int i = 0; i <= 20; i++) {
            System.out.printf("%4d * %2d = %6d\n", number, i, number*i);
        }
    }
}