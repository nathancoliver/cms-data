from pathlib import Path
from typing import Dict, List

# from numpy import nan
from pandas import DataFrame, read_csv  # type: ignore

from cms_data import MONTHS

data_file_path = Path("data", "beneficiary_2025.csv")

df = read_csv(data_file_path, sep="|")

df["BENE_ID"] = abs(df["BENE_ID"])
df.set_index("BENE_ID", inplace=True)

month_columns = [
    "CST_SHR_GRP_CD",
    "DUAL_STUS_CD",
    "HMO_IND",
    "MDCR_ENTLMT_BUYIN_IND",
    "MDCR_STATUS_CODE",
    "PTC_CNTRCT_ID",
    "PTC_PBP_ID",
    "PTC_PLAN_TYPE_CD",
    "PTD_CNTRCT_ID",
    "PTD_SGMT_ID",
    "RDS_IND",
    "STATE_CNTY_FIPS_CD",
]


month_data_storage: Dict[str, List[str | int]] = {"beneficiary_id": [], "month": [], "type": [], "data": []}

for month_column in month_columns:
    for month in MONTHS:
        column = f"{month_column}_{str(month).zfill(2)}"

        month_data = df[~df[column].isna()]
        month_data_length = len(month_data)
        month_data_storage["beneficiary_id"].extend(month_data.index.tolist())
        month_data_storage["month"].extend([month] * month_data_length)
        month_data_storage["type"].extend([month_column] * month_data_length)
        month_data_storage["data"].extend(month_data[column].tolist())

month_df = DataFrame(month_data_storage).set_index("beneficiary_id")

print()
