import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.util.Scanner;

class ListValidator {
    private Pattern listPattern;

    private static final String INTEGER_LIST_REGEXP = "((0,|[1-9]\\d*,)*(0|[1-9]\\d*))";

    public ListValidator() {
        listPattern = Pattern.compile(INTEGER_LIST_REGEXP);
    }

    public String isListValid(String str) {
        Matcher m = listPattern.matcher(str);
        if (m.matches())
            return m.group(1);
        else
            return null;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ListValidator validator = new ListValidator();
        while (true) {
            String str = validator.isListValid(input.nextLine());
            if (str != null) {
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
