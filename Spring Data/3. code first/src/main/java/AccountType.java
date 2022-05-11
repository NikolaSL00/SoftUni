
public enum AccountType {
    FREE("FREE"),
    TRAIL("TRAIL"),
    GOLD("GOLD"),
    PLATINUM("PLATINUM");

    private final String value;

    AccountType(String value){
        this.value = value;
    }

    public String getValue() {
        return value;
    }
}
