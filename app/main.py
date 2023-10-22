from pipeline.extract import extract_from_excel
from pipeline.transform import concatenate
from pipeline.load import load_excel

if __name__ == '__main__':
    df_list = extract_from_excel('data/input')
    df = concatenate(df_list)
    load_excel(df, "data/output", "output")