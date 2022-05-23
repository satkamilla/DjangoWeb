namespace ProjectStack
{
    public class MyStack
    {  
        public const int StackSize = 100;
        public const int Empty = -1;

        private static string[] arrStack = new string[StackSize];
        private static int top = Empty;

        public bool Push(string s)
        {
            if (top >= StackSize - 1)
                return false;
            else
            {
                arrStack[++top] = s;
                return true;
            }
        }

        public bool Pop(out string s)
        {
            s = "";

            if (top == Empty)
                return false;
            else
            {
                s = arrStack[top--];
                return true;
            }
        }
        public bool Pop() // without input info
        {
            if (top == Empty)
                return false;
            else
            {
                top--;
                return true;
            }
        }
        public bool Peek(out string s)
        {
            s = "";

            if (top == StackSize)
                return false;
            else
            {
                s = arrStack[top];
                return true;
            }
        }
    }
    
}
