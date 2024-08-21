bool isPalindrome(char* s) 
{
    int length = strlen(s);
    char duplicate[length];
    char *temp = s;
    int count = 0;

    while(*temp)
    {
        if(isalnum(*temp))
        {
            duplicate[count] = tolower(*temp);
            count++;
        }

        temp++;
    }

    char first = ' ';
    char last = ' ';
    count--;

    for(int i = 0; i < count; i++)
    {
        first = duplicate[i];
        last = duplicate[count - i];

        if(first != last)
        {
            return false;
        }

        if(i >= (count - i))
        {
            break;
        }
    }

    return true;
}