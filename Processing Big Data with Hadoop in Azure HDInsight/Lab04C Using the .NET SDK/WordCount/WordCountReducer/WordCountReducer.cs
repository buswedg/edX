using System;
using System.IO;

namespace WordCountReducer
{
    class WordCountReducer
    {
        static void Main(string[] args)
        {
            string word, lastWord = null;
            int count = 0;

            // Get inout from Streaming interface
            if (args.Length > 0)
            {
                Console.SetIn(new StreamReader(args[0]));
            }

            // count values for each word key
            while ((word = Console.ReadLine()) != null)
            {
                if (word != lastWord)
                {
                    // write word and final count to streaming interface
                    if (lastWord != null)
                        Console.WriteLine("{0}{1}", lastWord, count);

                    count = 1;
                    lastWord = word;
                }
                else
                {
                    count += 1;
                }
            }
            Console.WriteLine(count);

        }
    }
}
