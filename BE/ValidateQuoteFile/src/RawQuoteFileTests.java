import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.regex.Pattern;

import org.testng.Assert;
import org.testng.SkipException;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;

public class RawQuoteFileTests {	
	
	Pattern rawQuoteIdRegex = Pattern.compile("\\x00\\x2b(\\d*)");

	Pattern datetimeRegex = Pattern.compile("\\d{4}-\\d{2}-\\d{2}-\\d{2}\\.\\d{2}\\.\\d{2}\\.\\d{6}");
	DateTimeFormatter datetimeFormatter = DateTimeFormatter.ofPattern("YYYY-MM-DD-HH.mm.ss.SSSSSS");

	Pattern dateRegex = Pattern.compile("\\d{2}\\/\\d{2}\\/\\d{4}");
	DateTimeFormatter dateFormatter = DateTimeFormatter.ofPattern("MM/DD/YYYY");

	Pattern endOfRecordsRegex = Pattern.compile("\\x1a");
	static final String endOfRecordsLine = new String(new byte[] {0x1a});

	@DataProvider
	public static Object[][] RawQuoteFilename() {
		String rawquotefilename = System.getProperty("rawquotefile");
		if (rawquotefilename == null) {
			throw new SkipException("Property 'rawquotefile' not specified");
		}
		System.out.println("rawquotefile:" + rawquotefilename);
		return new Object[][] {
			new Object[] { rawquotefilename }
		};
	}
	
//	@Test
//	public void manualTestRawQuoteFile() throws IOException {
//		testRawQuoteFile("transfertest77 (1).txt");
//	}
	
	@Test(dataProvider="RawQuoteFilename")
	public void testRawQuoteFile(String rawquotefilename) throws IOException {
		File f = new File(rawquotefilename);
		Assert.assertTrue(f.exists(), "File does not exist");
		Assert.assertTrue(f.isFile(), "Is not a file");
		Assert.assertTrue(f.canRead(), "File is not readable");
		Assert.assertTrue(f.length() != 0, "File is empty");

		InputStream is = new FileInputStream(rawquotefilename); 
		BufferedReader buf = new BufferedReader(new InputStreamReader(is)); 
		int count = 0;
		String line;
		while((line = buf.readLine()) != null) {
			if (line.equals(endOfRecordsLine)) {
				break;
			}
			count++;
			ArrayList<String> parts = new ArrayList<String>(Arrays.asList(line.split("\\s+")));
			Assert.assertEquals(parts.size(), 5, "Incorrect number of columns");
			/* column 0 */
			Assert.assertTrue(
					(rawQuoteIdRegex.matcher(parts.get(0))).matches(), "QuoteId entry is incorrect"
					);

			/* column 1 - datetime */
			Assert.assertTrue(
					(datetimeRegex.matcher(parts.get(1))).matches(), "CreateDatetime is incorrect"
					);

			/* column 2 - datetime */
			Assert.assertTrue(
					(datetimeRegex.matcher(parts.get(2))).matches(), "UpdatedDatetime is incorrect"
					);

			/* column 3 */
			/* TODO: Assert Column String value? */

			/* column 4 - date */
			Assert.assertTrue(
					(dateRegex.matcher(parts.get(4))).matches(), "Last Column Date entry is incorrect"
					);
		}
		buf.close();
		System.out.println("record count:" + count);
	}
}