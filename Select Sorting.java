package sortingAlgorithm;

public class Project1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] Array = {4, 77, 45, 56, 68};
		int temp;
		for(int i = 0; i < Array.length; i++) {
				for(int j = 0; j < Array.length - i - 1; j++) {
					if(Array[j] > Array[j+1]) {
		                temp = Array[j];
		                Array[j] = Array[j+1];
		                Array[j+1] = temp;
}
		}
				}
		for (int i=0; i<Array.length; i++) {
			System.out.println(Array[i]);
		}
}
}