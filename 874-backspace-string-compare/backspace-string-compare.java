class Solution {
    public boolean backspaceCompare(String s, String t) {
        if(org(s).equals(org(t))){
            return true;
        }
        else{
            return false;
        }
        
    }
    public String org(String s){
        Stack<Character> st = new Stack<>();

        for(char ch : s.toCharArray()){
            if( ch != '#'){
                st.push(ch);
            }
            else if(!st.isEmpty()){
                st.pop();
            }
        }
        StringBuilder sb = new StringBuilder();
        for(char c : st){
            sb.append(c);
        }
        return sb.toString();

    }
    
}