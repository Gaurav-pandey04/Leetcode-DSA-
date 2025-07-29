public class Second{
    public static void main(String[] args) {
        int[] arr = {12, 45, 67, 20, 90 };      
        int largest_num = 0, secondLargest_num = 0;

        for(int num : arr){
            if(largest_num < num){
                secondLargest_num = largest_num;
                largest_num = num;
            }
        }

        System.out.println(secondLargest_num);
    }
}