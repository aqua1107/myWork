package practice;

import java.util.Scanner;
public class SmartPhoneMain {
	public void printMenu() {
        System.out.println("------------------");
        System.out.println("1. 연락처 등록");
        System.out.println("2. 모든 연락처 출력");
        System.out.println("3. 연락처 검색");
        System.out.println("4. 연락처 삭제");
        System.out.println("5. 연락처 수정");
        System.out.println("6. 시스템 종료");
        System.out.println("------------------");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);  
        SmartPhone sp = new SmartPhone();
        
        while (true) {
        	SmartPhoneMain spm = new SmartPhoneMain();
            spm.printMenu();
            System.out.print(">>> ");
            int choice = sc.nextInt();
            sc.nextLine();
            
            switch (choice) {
            case 1:
                sp.inputAddrData();
                sp.addAddr();
                break;
            case 2:
                sp.printAllAddr();
                break;
            case 3:
                sp.searchAddr();
                break;
            case 4:
                sp.deleteAddr();
                break;
            case 5:
                sp.editAddr();
                break;
            case 6:
                System.out.println("시스템을 종료합니다.");
                System.exit(0);
                break;
            default:
                System.out.println("잘못된 입력입니다. 다시 시도하세요.");
        }
    }
    }
}