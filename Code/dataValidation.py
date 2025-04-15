import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_data(df):
    validation_report = []

    # Check for NaNs
    nan_counts = df.isna().sum()
    if nan_counts.any():
        logging.warning(f"Columns with NaN values: {nan_counts[nan_counts > 0]}")
        validation_report.append("Data contains missing values")

    # Check for duplicate entries
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        logging.warning(f"Number of duplicate rows: {duplicates}")
        validation_report.append("Data contains duplicates")

    # Check for negative values in non-negative columns like 'Volume', 'Close', 'High', 'Low', 'Open'
    non_negative_cols = ['Volume', 'Close', 'High', 'Low', 'Open']
    for col in non_negative_cols:
        if col in df.columns:
            if (df[col] < 0).any():
                logging.warning(f"Negative values found in column {col}")
                validation_report.append(f"Column {col} contains negative values")

    # Check if 'Date' is in correct datetime format
    if 'Date' in df.columns:
        try:
            pd.to_datetime(df['Date'])
        except ValueError:
            logging.error("Date column does not match expected datetime format")
            validation_report.append("Date column format issue")

    # Check for correct data types
    expected_types = {
    'Open': float, 'High': float, 'Low': float, 'Close': float, 
    'Volume': int, 'company_name': object, 'Date': 'datetime64[ns]'
    }
    for col, expected_type in expected_types.items():
        if col in df.columns:
            if df[col].dtype != expected_type:
                if col == 'company_name' and df[col].dtype == object:
                    continue  # Skip this check for 'company_name' if it's of type 'object'
                logging.warning(f"Column {col} has unexpected type {df[col].dtype}, expected {expected_type}")
                validation_report.append(f"Column {col} type mismatch")

    # Check for sufficient data for analysis (example: at least 5 years per company)
    min_entries = 5 * 300  # Assuming roughly 365 trading days per year
    if 'company_name' in df.columns:
        for company in df['company_name'].unique():
            company_data = df[df['company_name'] == company]
            if len(company_data) < min_entries:
                logging.warning(f"Insufficient data for {company}: {len(company_data)} entries")
                validation_report.append(f"Insufficient data for {company}")

    if validation_report:
        raise ValueError(f"Data validation failed: {'; '.join(validation_report)}")
    else:
        logging.info("Data validation passed successfully")

    return df
