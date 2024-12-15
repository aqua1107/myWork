package practice;

public class Addr {
    private String name;
    private String phone;
    private String email;
    private String address;
    private String group;

    public Addr(String name, String phone, String email, String address, String group) {
        this.name = name;
        this.phone = phone;
        this.email = email;
        this.address = address;
        this.group = group;
    }

    public String getName() {
        return this.name;
    }
    public String getPhone() {
        return this.phone;
    }
    public String getEmail() {
        return this.email;
    }
    public String getAddress() {
        return this.address;
    }
    public String getGroup() {
        return this.group;
    }

    public void setName(String name) {
        this.name = name;
    }
    public void setPhone(String phone) {
        this.phone = phone;
    }
    public void setEmail(String email) {
        this.email = email;
    }
    public void setAddress(String address) {
        this.address = address;
    }
    public void setGroup(String group) {
        if (group.equals("친구")) {
            this.group = group;
        } else {
            this.group = "가족";
        }
    }

    public void printInfo() {
        System.out.println("이름: " + name);
        System.out.println("전화번호: " + phone);
        System.out.println("이메일: " + email);
        System.out.println("주소: " + address);
        System.out.println("그룹: " + group);
    }
}
