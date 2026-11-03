class Solution {
    public int addDigits(int num) {
        int sum=0;
        while(Integer.toString(num).length()>=2){
            

            for (int i=0;i<=Integer.toString(num).length();i++){
                int a = num%10 ;

                num=num/10 ;
                sum+=a;

            }
            num=sum;
            sum=0;

        
        }
        return num;
        
    }
}

