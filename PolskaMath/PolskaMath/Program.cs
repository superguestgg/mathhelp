using System;

namespace PolskaMath;

public class PolskaMath
{
    static Stack<char> operationsStack = new Stack<char>();
    static Queue<char> queue = new Queue<char>();
    static Dictionary<char,int> operations
        = new Dictionary<char,int>{ {'+', 0}, {'-', 0}, {'*', 1}, {'/', 1} };

    public static void Main()
    {
        while (true)
        {
            var s = Console.ReadLine();
            Console.WriteLine(new string(ToPolska(s)));
            Console.WriteLine("");
        }
    }

    public static char[] ToPolska(string stringEquation)
    { 
        var arrayEquation = stringEquation.ToCharArray();
        foreach (var element in arrayEquation)
        {
            if (element == ')')
            {
                var prevElement = operationsStack.Pop();
                while (prevElement != '(')
                {
                    queue.Enqueue(prevElement);
                    prevElement = operationsStack.Pop();                    
                }  
            }
            else if (element == '(')
            {
                operationsStack.Push(element);
            }
            else if (operations.ContainsKey(element))
            {
                while (operationsStack.Count > 0)
                {
                    var previousOperation = operationsStack.Peek();
                    if (!operations.ContainsKey(previousOperation))
                        break;
                    if (operations[previousOperation] >= operations[element])
                    {
                        operationsStack.Pop();
                        queue.Enqueue(previousOperation);
                    }
                    else
                    {
                        break;
                    }
                }
                operationsStack.Push(element);
            }
            else
            {
                queue.Enqueue(element);
            }
        }
        while (operationsStack.Count > 0)
        {
            Console.WriteLine(operationsStack.Peek());
            queue.Enqueue(operationsStack.Pop());
        }
        return queue.ToArray();
    }

    static void PolskaMathBySlava(string line)
    {
        Stack<char> resultStack = new Stack<char>();
        Stack<char> operationsStack = new Stack<char>();
        for (var i = 0; i < line.Length; i++)
        {
            var lineChar = line[i];
            if (lineChar == '+')
            {
                operationsStack.Push(lineChar);
            }
            else if (lineChar == '-')
            {
                operationsStack.Push(lineChar);
            }
            else if (lineChar == '*')
            {
                operationsStack.Push(lineChar);
            }
            else if (lineChar == '/')
            {
                operationsStack.Push(lineChar);
            }
            else if (lineChar == ')' || operationsStack.Peek() == '*')
            {
                resultStack.Push(operationsStack.Pop());
            }
            else if (lineChar != '(')
            {
                resultStack.Push(lineChar);
            }        
        }
        while (operationsStack.Count > 0)
        {
            resultStack.Push(operationsStack.Pop());
        }
        Console.WriteLine("Hello World");
        Console.WriteLine(new string(resultStack.ToArray()));
    }
}
