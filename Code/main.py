import logging
import os
import pickle
from dataDownloading import downloadDataFromYahooServer
from dataVisualization import visualize_data # type: ignore
from dataValidation import validate_data # type: ignore

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    pickle_path = "./../Data/stock_data.pkl"
    if os.path.exists(pickle_path):
        logging.info("Pickle file found! Loading downloaded dataset...")
        with open(pickle_path, 'rb') as pkl_file:
            df = pickle.load(pkl_file)
    else:
        logging.info("Downloading the data !!!")
        try:
            pickle_path = downloadDataFromYahooServer()
        except Exception as e:
            logging.error(f"Error downloading data: {e}")
            return

    logging.info("Data downloaded successfully!")

    try:
        df = validate_data(df)
    except ValueError as e:
        logging.error(f"Data validation failed: {e}")
        return

    logging.info("Data validation completed successfully!")

    try:
        visualize_data(df)
    except Exception as e:
        logging.error(f"Error visualizing data: {e}")
        return

    logging.info("Data visualization completed!")

if __name__ == "__main__":
    main()