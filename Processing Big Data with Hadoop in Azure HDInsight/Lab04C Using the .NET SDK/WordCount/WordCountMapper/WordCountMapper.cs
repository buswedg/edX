using System;
using System.IO;

namespace WordCountMapper
{
    class WordCountMapper
    {
        static void Main(string[] args)
        {
            if (args.Length > 0)
            {
                Console.SetIn(new StreamReader(args[0]));
            }

            string line;
            string[] words;

            // Get input via Streaming interface
            while ((line = Console.ReadLine()) != null)
            {
                // split string into individual words based on space delimiter
                words = line.Split(' ');

                foreach (string word in words)
                    if (word.Trim().Length > 0)
                    {
                        // write word key to Streaming interface
                        Console.WriteLine(word.ToLower());
                    }
                    
            }
        }
    }
}
