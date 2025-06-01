import org.junit.Test;
import static org.junit.Assert.*;

public class SampleApplicationTest {

    @Test
    public void testGreet() {
        SampleApplication app = new SampleApplication();
        app.greet();
    }

    @Test
    public void testCalculate() {
        SampleApplication app = new SampleApplication();
        
        // Test with valid input
        assertEquals(20, app.calculate(5));
        
        // Test with invalid input
        try {
            app.calculate(0);
            fail("Expected ArithmeticException not thrown");
        } catch (ArithmeticException e) {
            // Expected exception
        }
    }
}
