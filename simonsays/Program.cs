using System.Security.Cryptography;

namespace Program
{
  class Program
  {
    static void Main(string[] args)
    {
      Dictionary<string, ConsoleKey> actions = new()
      {
        {"Hands on head", ConsoleKey.H},
        {"Hands on ears", ConsoleKey.E},
        {"Right hand up", ConsoleKey.R},
        {"Left hand up", ConsoleKey.L},
        {"Hands on shoulders", ConsoleKey.S}
      };
      string[] intros = new string[] { "Simon says ", "" };
      // gen random action and intro
      Random rnd = new();
      // repeat the below 10 times
      for (int i = 0; i < 10; i++)
      {
        // gen random action and intro
        int actionIndex = rnd.Next(0, actions.Keys.Count);
        int introIndex = rnd.Next(0, intros.Length);
        // get the instruction (key)
        string instruction = actions.Keys.ElementAt(actionIndex);
        // get action key
        ConsoleKey actionKey = actions.Values.ElementAt(actionIndex);
        // print action and intro
        Console.WriteLine(@"{0}{1}", intros[introIndex], actions.Keys.ElementAt(actionIndex));
        ConsoleKeyInfo info = Console.ReadKey();
        // if the key pressed is not the action key
        if (info.Key != actionKey)
        {
          Console.WriteLine("You lose!");
          // exit
          return;
      } else {
          Console.Clear();
        }
      }
    }
  }
}