package practice;
import java.util.Scanner;
public class SmartPhone {
    Scanner sc = new Scanner(System.in);
    public static final Addr[] addressBook = new Addr[10]; // 배열 이름 변경
    private String name, phone, email, address, group;
    int count = 0;

    public void inputAddrData() {
        System.out.println("이름을 입력하세요: ");
        name = sc.nextLine();
        System.out.println("전화번호를 입력하세요: ");
        phone = sc.nextLine();
        System.out.println("이메일을 입력하세요: ");
        email = sc.nextLine();
        System.out.println("주소를 입력하세요: ");
        address = sc.nextLine();
        System.out.println("그룹을 입력하세요(친구/가족): ");
        group = sc.nextLine();
    }

    public void addAddr() {
        Addr addr = new Addr(name, phone, email, address, group);
        if (count < addressBook.length) {
            addressBook[count] = addr;
            count++;
            System.out.println("연락처에 추가했습니다.");
        } else {
	            System.out.println("연락처가 가득 찼습니다.");
	        }
	    }
	
	    public void printAllAddr() {
        for (int i = 0; i < count; i++) {
            addressBook[i].printInfo();
        }
    }

    public void searchAddr() {
        System.out.print("이름을 입력하세요: ");
        String name = sc.nextLine();
        boolean found = false;
        for (int i = 0; i < count; i++) {
            if (addressBook[i].getName().equals(name)) {
                addressBook[i].printInfo();
                found = true;
                break;
            }
        }
        if (!found) {
            System.out.println("주소를 찾을 수 없습니다.");
        }
    }

    public void deleteAddr() {
        System.out.print("삭제할 이름을 입력하세요: ");
        String name = sc.nextLine();
        boolean found = false;
        for (int i = 0; i < count; i++) {
            if (addressBook[i].getName().equals(name)) {
                for (int j = i; j < count - 1; j++) {
                    addressBook[j] = addressBook[j + 1];
                }
                addressBook[count - 1] = null;
                count--;
                System.out.println("연락처가 삭제되었습니다.");
                found = true;
                break;
            }
        }
        if (!found) {
            System.out.println("삭제할 연락처를 찾을 수 없습니다.");
        }
    }

    public void editAddr() {
        System.out.print("수정할 이름을 입력하세요: ");
        String name = sc.nextLine();
        boolean found = false;
        for (int i = 0; i < count; i++) {
            if (addressBook[i].getName().equals(name)) {
                System.out.println("수정할 항목을 선택하세요: ");
                System.out.println("1. 이륾");
                System.out.println("2. 전화번호");
                System.out.println("3. 이메일");
                System.out.println("4. 주소");
                System.out.println("5. 그룹");
                int choice = sc.nextInt();
                sc.nextLine();

                switch (choice) {
                	case 1: 
                		System.out.println("새 이름을 입력하세요: ");
                		addressBook[i].setName(sc.nextLine());
                		break;
                    case 2:
                        System.out.println("새 전화번호를 입력하세요: ");
                        addressBook[i].setPhone(sc.nextLine());
                        break;
                    case 3:
                        System.out.println("새 이메일을 입력하세요: ");
                        addressBook[i].setEmail(sc.nextLine());
                        break;
                    case 4:
                        System.out.println("새 주소를 입력하세요: ");
                        addressBook[i].setAddress(sc.nextLine());
                        break;
                    case 5:
                        System.out.println("새 그룹을 입력하세요: ");
                        addressBook[i].setGroup(sc.nextLine());
                        break;
                    default:
                        System.out.println("잘못된 선택입니다.");
                }
                System.out.println("연락처가 수정되었습니다.");
                found = true;
                break;
            }
        }
        if (!found) {
            System.out.println("수정할 연락처를 찾을 수 없습니다.");
        }
    }
}
