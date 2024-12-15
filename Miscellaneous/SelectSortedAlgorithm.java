package selectSortedAlgorithm;

public class SelectSortedAlgorithm {
	public static void main(String[] args) {
	int[] Array = {54, 77, 45, 56, 68};
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
	for (int k=0; k<Array.length; k++) {
		System.out.println(Array[k]);
	}
}
}