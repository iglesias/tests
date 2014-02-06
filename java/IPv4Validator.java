import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.util.Scanner;

/* IPv4 regular expression wrapper. */
class IPv4Validator {

    /* Attribute used to compile the regular expression once, and use it many times. */
    private Pattern ipv4Pattern;

    /* Very ugly regular expression, but it becomes handy for the IPMerger. */
    private static final String IPv4_REGEXP = "((\\d|[1-9]\\d|1[\\d][\\d]|2[0-4]\\d|25[0-5])\\.(\\d|[1-9]\\d|1[\\d][\\d]|2[0-4]\\d|25[0-5])\\.(\\d|[1-9]\\d|1[\\d][\\d]|2[0-4]\\d|25[0-5])\\.(\\d|[1-9]\\d|1[\\d][\\d]|2[0-4]\\d|25[0-5]))";

    /* Default constructor. */
    public IPv4Validator() {
        ipv4Pattern = Pattern.compile(IPv4_REGEXP);
    }

    /* Check whether the given string matches the IPv4 regular expression. */
    public boolean isIPv4Valid(String str) {
        Matcher m = ipv4Pattern.matcher(str);
        return m.matches();
    }

    /* Simple tester to count valid IP address within a range of positive numbers. The range is
     * defined by a lower bound (lb) and an upper bound (ub). */
    private void TestRangeIPs(int lb, int ub) {
        if (lb < 0 || ub < 0) return;
        if (ub < lb) return;

        int numValidIPs = 0;
        for (int i = lb; i <= ub; i++) {
            String ip1 = Integer.toString((i >> 24) & 0xff);
            String ip2 = Integer.toString((i >> 16) & 0xff);
            String ip3 = Integer.toString((i >>  8) & 0xff);
            String ip4 = Integer.toString((i      ) & 0xff);

            StringBuilder sb = new StringBuilder();
            sb.append(ip1).append(".").append(ip2).append(".").append(ip3).append(".").append(ip4);
            numValidIPs += (isIPv4Valid(sb.toString()) ? 1 : 0);

            if (i == lb)
                System.out.print("Tried IP addresses from " + sb.toString());

            if (i == ub)
                System.out.println(" to " + sb.toString() + " and obtained a total of " + numValidIPs + " valid IP addresses.");
        }

        assert numValidIPs == ub-lb+1;
    }

    private void TestIncorrectIPs() {
       assert !isIPv4Valid("000.1.2.3");    // no zeros to the left accepted
       assert !isIPv4Valid("0001.1.2.3");   // similar to the one above
       assert !isIPv4Valid("1.2.3");        // too short
       assert !isIPv4Valid("1.2.3.4.5");    // too long
       assert !isIPv4Valid("256.0.0.0");    // out of bounds in different positions, here and below
       assert !isIPv4Valid("0.256.0.0");
       assert !isIPv4Valid("0.0.256.0");
       assert !isIPv4Valid("0.0.0.256");
       assert !isIPv4Valid("-1.0.0.0");     // negative numbers
       assert !isIPv4Valid("a.b.5.6");      // only numbers
    }

    public static void main(String[] args) {
        IPv4Validator validator = new IPv4Validator();
        int lb = 0;
        int ub = 1000000;
        if (args.length == 2) {
            try {
                lb = Integer.parseInt(args[0]);
                ub = Integer.parseInt(args[1]);
            } catch (NumberFormatException e) {
                System.err.println("Usage: java IPv4Validator [lower bound] [upper bound].");
            }
        }
        validator.TestRangeIPs(lb, ub);
        validator.TestIncorrectIPs();
    }

}
