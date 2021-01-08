/* ****** Question ******
HackerLand Enterprise is adopting a new viral advertising strategy. When they launch a new product, 
they advertise it to exactly 5 people on social media.

On the first day, half of those  people (i.e., floor(5/2) = 2) like the advertisement and each shares it with 3 of their friends.
At the beginning of the second day,  (2*3)=6 people receive the advertisement.

Each day, floor(recipients/2) of the recipients like the advertisement and will share it with  friends on the following day. 
Assuming nobody receives the advertisement twice, determine how many people have liked the ad by the end of a given day, 
beginning with launch day as day .

****** X ******
*/

/* ****** Approach ******

For n = 5,

Day Shared Liked Cumulative
1      5     2       2
2      6     3       5
3      9     4       9
4     12     6      15
5     18     9      24

****** X ******
*/

import java.util.*;

public class ViralAdvertisement {

    // Complete the viralAdvertising function below.
    static int viralAdvertising(int n) {

        int shared = 5, cumulative = 0, liked;
        
        for(int i = 1; i <= n; i++) {
            liked = (int) Math.floor(shared/2);
            cumulative+=liked;
            shared = liked * 3;
        }
        
        return cumulative;
    }

    public static void main(String[] args) {
        int[] testCases = new int[] {3, 4, 5};
        int[] results = new int[] {9, 15, 24};

        for(int i = 0; i < testCases.length; i++) {
        	int expected = results[i];
        	int actual = viralAdvertising(testCases[i]);

        	if(expected != actual) {
        		System.out.println("Wrong Answer for " + testCases[i] + ". Expected: " + expected + ". Actual: " + actual);
        	}
        }
        System.out.println("Run complete.");
    }
}
