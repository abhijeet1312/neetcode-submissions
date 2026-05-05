class Solution {
public:
    bool isPalindrome(string s) {
    string str="";
    for(auto ch:s)
    {
        if(isalnum(ch))
        {
            str+=tolower(ch);
        }
    }
     
    int left=0;
    int right=str.size()-1;
    cout<<(str);
    while(left<=right)
    {
        if(str[left]!=str[right])
        {
               return false;
        }
        left++;
        right--;
    }
    return true;
    }
};
