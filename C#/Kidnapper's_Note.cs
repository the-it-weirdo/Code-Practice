/** **** Question ****

Harold is a kidnapper who wrote a ransom note, 
but now he is worried it will be traced back to 
him through his handwriting. He found a magazine 
and wants to know if he can cut out whole words from
it and use them to create an untraceable replica 
of his ransom note. The words in his note are case-sensitive 
and he must use only whole words available in the magazine. 
He cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, 
print Yes if he can replicate his ransom note exactly 
using whole words from the magazine; otherwise, print No.

For example, the note is "Attack at dawn". The magazine 
contains only "attack at dawn". The magazine has all the 
right words, but there's a case mismatch. The answer is No.

**** Function Description ****

Complete the checkMagazine function. 
It must print "Yes" if the note can be formed using the magazine, or "No".

checkMagazine has the following parameters:

magazine: an array of strings, each a word in the magazine
note: an array of strings, each a word in the ransom note


*/

using System.Collections.Generic;
using System.Collections;
using System.Linq;
using System;

class Solution {

    // Complete the checkMagazine function below.
    static string checkMagazine(string[] magazine, string[] note) {
        var magazineWords = magazine.GroupBy(x => x)
                            .Select(g => new { Word=g.Key, Count=g.Count() })
                            .ToDictionary(x => x.Word, x=>x.Count);
        
        var noteWords = note.GroupBy(x => x)
                            .Select(g => new { Word=g.Key, Count=g.Count()})
                            .ToDictionary(x=>x.Word, x=>x.Count);
        
        
        bool isPossible = true;
        foreach(var wordInfo in noteWords) {
            int countInMagazine;
            if(magazineWords.TryGetValue(wordInfo.Key, out countInMagazine))
            {
                if (countInMagazine < wordInfo.Value)
                {
                    isPossible = false;
                    break;
                }
            }
            else 
            {
                isPossible = false;
                break;
            }
        }
        
        return isPossible ? "Yes": "No";
    }

    public struct Question
    {
        public string[] magazine;
        public string[] note;
        public string answer;
    }

    static void Main(string[] args) {

        var queAndAnswers = new List<Question>();

        queAndAnswers.Add(new Question{magazine = "give me one grand today night".Split(' '), 
                                       note = "give one grand today".Split(' '), 
                                       answer = "Yes"});

        queAndAnswers.Add(new Question{magazine = "two times three is not four".Split(' '), 
                                       note = "two times two is four".Split(' '), 
                                       answer = "No"});

        queAndAnswers.Add(new Question{magazine = "ive got a lovely bunch of coconuts".Split(' '), 
                                       note = "ive got some coconuts".Split(' '), 
                                       answer = "No"});

        foreach(var elem in queAndAnswers)
        {
            string actual = checkMagazine(elem.magazine, elem.note);
            if(!actual.Equals(elem.answer))
            {
                Console.WriteLine($"Test case failed. Expected: {elem.answer}. Actual: {actual}");
                return;
            }
        }
        Console.WriteLine("Test Complete. All cases passed.");
    }
}
