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

public class ProcessedQuoteFileTests {
	
	Pattern idRegex = Pattern.compile("\\d+");

	Pattern dateRegex = Pattern.compile("\\d{2}\\/\\d{2}\\/\\d{4}");
	DateTimeFormatter dateFormatter = DateTimeFormatter.ofPattern("MM/DD/YYYY");

	@DataProvider
	public static Object[][] ProcessedQuoteFilename() {
		String processedquotefilename = System.getProperty("processedquotefile");
		if (processedquotefilename == null) {
			throw new SkipException("Property 'processedquotefile' not specified");
		}
		System.out.println("processedquotefile:" + processedquotefilename);
		return new Object[][] {
			new Object[] { processedquotefilename }
		};
	}
	
//	@Test
//	public void manualTestRawQuoteFile() throws IOException {
//		testProcessedQuoteFile("quote-20180504.txt");
//	}

	@Test(dataProvider="ProcessedQuoteFilename")
	public void testProcessedQuoteFile(String processedquotefilename) throws IOException {
		File f = new File(processedquotefilename);
		Assert.assertTrue(f.exists(), "File does not exist");
		Assert.assertTrue(f.isFile(), "Is not a file");
		Assert.assertTrue(f.canRead(), "File is not readable");
		Assert.assertTrue(f.length() != 0, "File is empty");

		InputStream is = new FileInputStream(processedquotefilename); 
		BufferedReader buf = new BufferedReader(new InputStreamReader(is)); 

		String line;
		line = buf.readLine();
		Assert.assertNotNull(line);
		String expectedHeaderLine = "QuoteID CreateDate";
		Assert.assertEquals(line, expectedHeaderLine, "Expected header is incorrect");
		
		int count = 0;
		while((line = buf.readLine()) != null) {
			count++;
			ArrayList<String> parts = new ArrayList<String>(Arrays.asList(line.split(" ")));
			Assert.assertEquals(parts.size(), 2);
			/* column 0 */
			/* TODO: Assert Column QuoteID value */
			Assert.assertTrue(
					(idRegex.matcher(parts.get(0))).matches(), "QuoteID entry is not valid integer"
					);

			Assert.assertTrue(
					(dateRegex.matcher(parts.get(1))).matches(), "CreateDate entry is not valid date"
					);
		}
		buf.close();
		System.out.println("record count:" + count);
	}
}
