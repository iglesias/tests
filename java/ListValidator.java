import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.util.Scanner;

/* Comma-separated list of integers regular expression wrapper. */
class ListValidator {

    /* Attribute used to store the state of the regular expression once compiled (compile once, used
     * many times). */
    private Pattern listPattern;

    /* Simple regular expression to match comma-separated list of positive integers. Note that it
     * forces the list to have at least one element. In the task, this entails that if a valid IP
     * address appears, but the associated list does not have at least one number, this IP
     * address will not appear in the final result. */
    private static final String INTEGER_LIST_REGEXP = "((0,|[1-9]\\d*,)*(0|[1-9]\\d*))";

    /* Default constructor. */
    public ListValidator() {
        listPattern = Pattern.compile(INTEGER_LIST_REGEXP);
    }

    /* Check whether the given string matches the format of the list. */
    public boolean isListValid(String str) {
        Matcher m = listPattern.matcher(str);
        return m.matches();
    }

    /* In this case we propose an interactive test. In case a valid list is introduced by the user,
     * then the list is shown. Otherwise nothing is printed on return. */
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ListValidator validator = new ListValidator();
        while (true) {
            String str = input.nextLine();
            if (validator.isListValid(str)) {
                String[] integerList = str.split(",");
                System.out.print("Valid comma-separated list of integers: [");
                for (int i = 0; i < integerList.length; i++) {
                    if (i < integerList.length-1)
                        System.out.print(integerList[i] + ", ");
                    else
                        System.out.println(integerList[i] + "]");
                }
            }
        }
    }
}
