import java.io.IOException;
import java.util.Properties;

public class PropertiesUtil {

    private final Properties props = new Properties();

    private final String PROPERTIES_FILE = "target.properties";

    private static PropertiesUtil theInstance;

    private PropertiesUtil() {
        super();
        try {
            props.load(getClass().getClassLoader().getResourceAsStream(
                    PROPERTIES_FILE));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static PropertiesUtil getInstance() {
        if (theInstance == null) {
            theInstance = new PropertiesUtil();
        }
        return theInstance;
    }

    public Properties getProps() {
        return props;
    }
}
