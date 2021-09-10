package freizl.langspec;


public enum OperationEnum {
	PLUS {
		double eval(final double x, final double y) {
			return x + y;
		}
	},
	MINUS {
		double eval(final double x, final double y) {
			return x - y;
		}
	},
	TIMES {
		double eval(final double x, final double y) {
			return x * y;
		}
	},
	DIVIDED_BY {
		double eval(final double x, final double y) {
			return x / y;
		}
	};

	// Perform the arithmetic operation represented by this constant
	abstract double eval(double x, double y);

	public static void main(String args[]) {
		double x = 2.0;
		double y = 4.0;

		for (OperationEnum op : OperationEnum.values())
			System.out.println(x + " " + op + " " + y + " = " + op.eval(x, y));
	}

}