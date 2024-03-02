
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> triplet = new ArrayList();

        Arrays.sort(nums);

        for(int i=0; i<nums.length-2; i++){
            if(i>0 && nums[i]==nums[i-1])
                continue;
            
            int left = i+1;
            int rigth = nums.length-1;
            while(left<rigth){
                int sum = nums[i]+nums[left]+nums[rigth];
                if(sum == 0){
                    List<Integer> list = Arrays.asList(nums[i],nums[left],nums[rigth]);
                    triplet.add(list);
                
                while(left<rigth && nums[rigth]==nums[rigth-1]){
                    rigth--;
                }
                while(left<rigth && nums[left]==nums[left+1]){
                    left++;
                }
                
                }
                if(sum>0){
                  rigth--;  
                }else left++;
            }



        }
    return triplet;
    }
}