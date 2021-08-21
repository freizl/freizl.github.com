
import javax.jms.JMSException;
import javax.jms.QueueConnection;
import javax.jms.QueueConnectionFactory;
import oracle.jms.AQjmsFactory;
import org.apache.log4j.Logger;

public class OracleAQFactory implements QueueConnectionFactory {

	private Logger logger = Logger.getLogger(getClass());

	/** AQ Server Connection */
	private String userName = "";
	private String password = "";
	private String hostName = "";
	private String sid = "";
	private int port = 1521;
	private String connectType = "thin";

	private static QueueConnectionFactory qcf = null;

	// -------------------------------------------------------------------
	// Implementation of interface QueueConnectionFactory
	// -------------------------------------------------------------------

	public OracleAQFactory() throws JMSException {
		if (logger.isDebugEnabled()) {
			logger.debug("OracleAQFactory Constructor.");
			logger.debug(this.connectType + ":" + this.hostName + ":"
					+ this.port + ":" + this.sid);
		}
	}

	private void initConnectFactory() throws JMSException {
		if (logger.isDebugEnabled()) {
			logger.debug("initConnectFactory:");
			logger.debug(this.connectType + ":" + this.hostName + ":"
					+ this.port + ":" + this.sid);
			logger.debug("this.qcf: " + qcf);
		}
		if (qcf == null) {
			qcf = AQjmsFactory.getQueueConnectionFactory(this.hostName,
					this.sid, this.port, this.connectType);
		}
	}

	public QueueConnection createQueueConnection() throws JMSException {
		return this.createQueueConnection(this.userName, this.password);
	}

	public QueueConnection createQueueConnection(String userName,
			String password) throws JMSException {
		initConnectFactory();
		return qcf.createQueueConnection(userName, password);
	}

	public QueueConnection createConnection() throws JMSException {
		// return qcf.createConnection();
		return this.createConnection(this.userName, this.password);
	}

	public QueueConnection createConnection(String userNameArg,
			String passwordArg) throws JMSException {

		this.initConnectFactory();
		if (logger.isDebugEnabled()) {
			logger.debug("------- " + userNameArg + ":" + passwordArg);
			logger.debug("this.connectFactory:" + qcf);
		}
		return qcf.createQueueConnection(userNameArg, passwordArg);
	}

	// -------------------------------------------------------------------
	// Getter and Setter
	// -------------------------------------------------------------------

	/** IGNORED */

}