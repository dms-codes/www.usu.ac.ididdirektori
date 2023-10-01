# Faculty and Docent Data Retrieval Script

The `faculty_and_docent_data_retrieval.py` script is a Python script for retrieving faculty and docent data from a university website using Selenium. It includes functions to extract faculty names and docent profiles, as well as a multithreading approach to fetch data for multiple faculty-docent pairs.

## Prerequisites

Before using this script, make sure you have the following prerequisites installed:

- Python 3.x
- Selenium
- Chrome WebDriver

You can install Selenium using pip:

```bash
pip install selenium
```

Make sure to download the appropriate Chrome WebDriver for your Chrome browser version.

## Usage

1. Clone or download the script to your local machine.

2. Install the required Python libraries mentioned in the "Prerequisites" section.

3. Configure the script by specifying the `BASE_URL` variable and other parameters according to your university website structure.

4. Create an input CSV file (`input.csv`) with two columns: "Faculty" and "Docent." Add the faculty and docent pairs you want to retrieve data for.

5. Run the script:

```bash
python faculty_and_docent_data_retrieval.py
```

The script will retrieve data for the specified faculty and docent pairs, and the results will be saved in an output CSV file (`output.csv`).

## Functions

### `get_faculties(driver)`

This function retrieves the list of faculty names available on the university website.

### `get_driver()`

This function initializes a Chrome WebDriver for web scraping.

### `get_docents(driver, select, faculties)`

This function retrieves docent data for each faculty specified in the `faculties` list.

### `select_data(faculty, docent, writer, csvfile)`

This function navigates to the docent's profile page and extracts relevant data, including name, NIP, NIDN, email, expertises, bio, and profile URL.

## Multithreading

The script employs multithreading to improve data retrieval efficiency. It processes multiple faculty-docent pairs concurrently.

## Example

```bash
python faculty_and_docent_data_retrieval.py
```

This command will execute the script, retrieve data for the specified faculty-docent pairs in `input.csv`, and store the results in `output.csv`.

Feel free to customize the script to suit your university website's structure and data retrieval needs.
```

You can customize this README by replacing `faculty_and_docent_data_retrieval.py` with the actual name of your script and providing additional information or examples as needed.
