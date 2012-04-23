import java.util.Calendar;
/**
 * 
 */
public class StaticFinalClass {

    private static Calendar today = null;

    static {
        System.out.println("I am static init blcok");
    }

    private StaticFinalClass() {
        System.out.println("I am the private constructor");
        today = Calendar.getInstance();
    }

    public static void todayInString() {
        System.out.println("I am the static method : todayInString");
        System.out.println(today);
    }

    public static void main(String[] args) {
        StaticFinalClass.todayInString();
        // output
        // I am static init blcok
        // I am the static method : todayInString
        // null
    }
}
