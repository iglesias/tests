import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.util.Scanner;

class IPv4Validator {

    private Pattern ipv4Pattern;

    private static final String IPv4_REGEXP = "((\\d|[1-9]\\d|1[\\d][\\d]|2[0-4]\\d|25[0-5])\\.(\\d|[1-9]\\d|1[\\d][\\d]|2[0-4]\\d|25[0-5])\\.(\\d|[1-9]\\d|1[\\d][\\d]|2[0-4]\\d|25[0-5])\\.(\\d|[1-9]\\d|1[\\d][\\d]|2[0-4]\\d|25[0-5]))";

    public IPv4Validator() {
        ipv4Pattern = Pattern.compile(IPv4_REGEXP);
    }

    public String isIPv4Valid(String str) {
        Matcher m = ipv4Pattern.matcher(str);
        if (m.matches())
            return m.group(1);
        else
            return null;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        IPv4Validator validator = new IPv4Validator();
        while (true) {
            String str = validator.isIPv4Valid(input.nextLine());
            if (str != null)
                System.out.println("Valid IPv4 address: " + str);
        }
    }

}
