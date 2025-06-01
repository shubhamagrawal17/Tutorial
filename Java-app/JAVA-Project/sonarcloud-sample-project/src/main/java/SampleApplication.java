
// SampleApplication.java
public class SampleApplication {

    public static void main(String[] args) {
        SampleApplication app = new SampleApplication();
        app.greet();
        int result = app.calculate(5);
        System.out.println("Calculation result: " + result);
    }

    // This method has an intentional code smell: unused variable
    public void greet() {
        String greeting = "Hello, World!";  // Unused variable
        System.out.println("Hello from the Sample Application");
    }

    // This method has an intentional bug: division by zero for input 0
    public int calculate(int number) {
        if (number == 0) {
            return 100 / 0;  // This will throw an ArithmeticException
        }
        return 100 / number;
    }
}
